import React, {useState} from 'react';
export const CombatView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>COMBAT - Combat - damage, armor, range, projectil</h2><p>damage</p></div>
};
export default CombatView;
