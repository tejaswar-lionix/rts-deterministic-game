import React, {useState} from 'react';
export const EconomyView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>ECONOMY - Economy - resources, gathering, trade</h2><p>resources</p></div>
};
export default EconomyView;
