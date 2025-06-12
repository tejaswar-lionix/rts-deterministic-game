import React, {useState} from 'react';
export const FrontendView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>FRONTEND - Frontend - canvas, minimap, HUD, replay </h2><p>canvas</p></div>
};
export default FrontendView;
