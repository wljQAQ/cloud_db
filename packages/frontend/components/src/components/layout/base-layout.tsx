import { ReactNode } from 'react';

import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '../../ui/resizable';

interface Props {
  header: ReactNode;
  sider: ReactNode;
  content: ReactNode;
}

export const BaseLayout = (props: Props) => {
  return (
    <>
      <div className="flex h-full w-full flex-col">
        <header className="h-16 border-b">{props.header}</header>

        {/* 内容区域 */}
        <ResizablePanelGroup direction="horizontal" className="flex-1">
          <ResizablePanel defaultSize={20}>{props.sider}</ResizablePanel>
          <ResizableHandle />
          <ResizablePanel defaultSize={80}>{props.content}</ResizablePanel>
        </ResizablePanelGroup>
      </div>
    </>
  );
};
