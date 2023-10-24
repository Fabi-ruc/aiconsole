import React from 'react';

import { useWebSocketStore } from '../store/useWebSocketStore';

export function SocketInitiator({ children }: { children: React.ReactNode }) {
  const { initWebSocket, disconnect } = useWebSocketStore();

  React.useEffect(() => {
    initWebSocket();
    return () => disconnect();
  }, [initWebSocket, disconnect]);

  return <>{children}</>;
}
