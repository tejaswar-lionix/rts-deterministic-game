import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for lobby, match, replay</h2><p>POST lobby</p></div>
};
export default ApiView;
