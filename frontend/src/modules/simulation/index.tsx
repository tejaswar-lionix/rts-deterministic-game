import React, {useState} from 'react';
export const SimulationView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>SIMULATION - Simulation - deterministic lockstep, fix</h2><p>lockstep</p></div>
};
export default SimulationView;
