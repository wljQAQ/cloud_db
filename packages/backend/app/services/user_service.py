from core.exception_handler import BusinessException
from schemas.user_schema import UserSchema

# --- 模拟数据库层 ---
# 在真实应用中，这里会被替换为数据库会话和ORM查询
_fake_users_db: dict[int, UserSchema] = {
    1: UserSchema(id=1, username="Rick"),
    2: UserSchema(id=2, username="Morty"),
}


# --- 服务函数 ---


def get_all_users() -> list[UserSchema]:
    """获取所有用户的业务逻辑"""
    return list(_fake_users_db.values())


def get_user_by_id(user_id: int) -> UserSchema:
    """
    根据ID获取单个用户的业务逻辑。
    如果找不到，则抛出业务异常。
    """
    user = _fake_users_db.get(user_id)
    if not user:
        raise BusinessException(code=1001, msg=f"用户ID '{user_id}' 不存在.")
    return user
