import React from 'react'
import Sidebar from './Sidebar'
import Display from './Display'
import {useParams} from 'react-router-dom';
function Dashboard() {
  const {netId} = useParams();
  return (
    <div>
      {/* <Sidebar/> */}
      <Display netId={netId}/>
    </div>
  )
}

export default Dashboard
