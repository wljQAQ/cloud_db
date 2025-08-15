import { BaseFramework } from '@cloud_db/components';

import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <BaseFramework />
    </>
  );
}

export default App;
