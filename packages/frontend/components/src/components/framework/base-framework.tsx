import '../../style/globals.css';

import { BaseLayout, DataTable } from '../..';

export default function BaseFramework() {
  return (
    <div className="h-[100vh] w-[100vw]">
      <BaseLayout
        header={<div>header</div>}
        sider={<div>sider</div>}
        content={
          <div className="h-full w-full p-2">
            <DataTable
              columns={[
                {
                  accessorKey: 'status',
                  header: 'Status'
                },
                {
                  accessorKey: 'email',
                  header: 'Email'
                },
                {
                  accessorKey: 'amount',
                  header: 'Amount'
                }
              ]}
              data={[
                {
                  id: '728ed52f',
                  amount: 100,
                  status: 'pending',
                  email: 'm@example.com'
                },
                {
                  id: '489e1d42',
                  amount: 125,
                  status: 'processing',
                  email: 'example@gmail.com'
                }
                // ...
              ]}
            ></DataTable>
          </div>
        }
      ></BaseLayout>
    </div>
  );
}
