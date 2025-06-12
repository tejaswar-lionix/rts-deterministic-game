import React, {useState} from 'react';
export const UnitsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>UNITS - Units - infantry, archers, cavalry, AI, </h2><p>infantry</p></div>
};
export default UnitsView;
