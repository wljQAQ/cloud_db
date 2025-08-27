import logging

import asyncpg
from asyncpg.exceptions import (
    InvalidPasswordError,
    InvalidAuthorizationSpecificationError,
    CannotConnectNowError,
)

from core.exception_handler import BusinessException
from schemas.database_schema import DBConnect

# 配置一个简单的日志记录器
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class DatabaseService:
    """
    数据库相关业务逻辑服务
    """

    async def connect_test(self, connect_params: DBConnect) -> bool:
        """
        测试数据库连接。
        成功连接后会立即关闭连接，如果成功则返回 True，否则抛出 BusinessException。
        """
        try:
            conn = await asyncpg.connect(
                user=connect_params.username,
                password=connect_params.password,
                database=connect_params.database,
                host=connect_params.host,
                port=connect_params.port,
                timeout=5,  # 增加5秒连接超时
            )
            # 连接测试成功后，应立即关闭连接，释放资源
            await conn.close()
            log.info(f"数据库连接测试成功: {connect_params.host}")
            return True

        except (InvalidPasswordError, InvalidAuthorizationSpecificationError):
            log.warning(
                f"数据库认证失败: {connect_params.host}, user={connect_params.username}"
            )
            raise BusinessException(code=4001, msg="数据库认证失败，请检查用户名或密码")

        except (OSError, CannotConnectNowError):
            log.warning(
                f"无法连接到数据库: {connect_params.host}:{connect_params.port}"
            )
            raise BusinessException(
                code=5001, msg="无法连接到数据库，请检查主机、端口或网络设置"
            )

        except Exception as e:
            log.error(f"发生未知的数据库连接错误: {e}", exc_info=True)
            raise BusinessException(code=5000, msg=f"发生未知错误: {e}")

    async def get_tables(self, connect_params: DBConnect) -> list[str]:
        """
        获取指定数据库连接下的所有表名 (仅限 public schema)。
        """
        conn = None
        try:
            conn = await asyncpg.connect(
                user=connect_params.username,
                password=connect_params.password,
                database=connect_params.database,
                host=connect_params.host,
                port=connect_params.port,
                timeout=5,
            )
            # 查询 public schema 下的所有表，并按名称排序
            records = await conn.fetch(
                "SELECT * FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename"
            )

            table_names = [record["tablename"] for record in records]
            log.info(f"成功获取 {connect_params.host} 中的 {len(table_names)} 个表")
            return table_names

        except (InvalidPasswordError, InvalidAuthorizationSpecificationError):
            log.warning(
                f"数据库认证失败: {connect_params.host}, user={connect_params.username}"
            )
            raise BusinessException(code=4001, msg="数据库认证失败，请检查用户名或密码")

        except (OSError, CannotConnectNowError):
            log.warning(
                f"无法连接到数据库: {connect_params.host}:{connect_params.port}"
            )
            raise BusinessException(
                code=5001, msg="无法连接到数据库，请检查主机、端口或网络设置"
            )

        except Exception as e:
            log.error(f"获取表时发生未知错误: {e}", exc_info=True)
            raise BusinessException(code=5000, msg=f"获取表列表时发生未知错误: {e}")

        finally:
            if conn:
                await conn.close()
                log.info(f"数据库连接已关闭: {connect_params.host}")


database_service = DatabaseService()
