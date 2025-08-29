import '../../style/globals.css';

import { Calendar, Home, Inbox, Search, Settings } from 'lucide-react';
import * as React from 'react';
import { ImperativePanelHandle } from 'react-resizable-panels';

import { DataTable } from '../..';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarTrigger,
  useSidebar
} from '../../ui';

const items = [
  {
    title: 'Home',
    url: '#',
    icon: Home
  },
  {
    title: 'Inbox',
    url: '#',
    icon: Inbox
  },
  {
    title: 'Calendar',
    url: '#',
    icon: Calendar
  },
  {
    title: 'Search',
    url: '#',
    icon: Search
  },
  {
    title: 'Settings',
    url: '#',
    icon: Settings
  }
];

export function AppSidebar() {
  return (
    <Sidebar className="w-full" collapsible="none">
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map(item => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
}

const ResizableLayout = ({ sider, content }: { sider: React.ReactNode; content: React.ReactNode }) => {
  const { setOpen } = useSidebar();
  const panelRef = React.useRef<ImperativePanelHandle>(null);

  const handleToggle = () => {
    const panel = panelRef.current;
    if (panel) {
      if (panel.isCollapsed()) {
        panel.expand();
      } else {
        panel.collapse();
      }
    }
  };

  return (
    <ResizablePanelGroup direction="horizontal">
      <ResizablePanel
        ref={panelRef}
        collapsible
        defaultSize={16}
        minSize={10}
        collapsedSize={0} // 3.75rem * 16px/rem = 60px
        onCollapse={() => setOpen(false)}
        onExpand={() => setOpen(true)}
        className="!overflow-auto"
      >
        {sider}
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel>
        <div className="relative h-full w-full">
          <div className="absolute left-2 top-2 z-10">
            <SidebarTrigger onClick={handleToggle} />
          </div>
          {content}
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
};

export const BiLayout = () => {
  return (
    <div className="h-[100vh] w-[100vw]">
      <SidebarProvider className="block h-full w-full">
        <ResizableLayout
          sider={<AppSidebar />}
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
                ]}
              ></DataTable>
            </div>
          }
        ></ResizableLayout>
      </SidebarProvider>
    </div>
  );
};
