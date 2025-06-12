import React, {useState} from 'react';
export const CommandsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>COMMANDS - Commands - input queue, command buffer, </h2><p>input queue</p></div>
};
export default CommandsView;
