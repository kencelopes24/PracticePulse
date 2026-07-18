import { useState, useEffect } from 'react'

export default function AdminDashboard() {
  const [instructors, setInstructors] = useState([])
  const [feedback, setFeedback] = useState([])

  useEffect(() => {
    // TODO: Fetch admin data from API
  }, [])

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Admin Dashboard</h1>

      <div className="grid md:grid-cols-3 gap-6">
        <div className="card">
          <p className="text-gray-600">Total Instructors</p>
          <p className="text-3xl font-bold">28</p>
        </div>
        <div className="card">
          <p className="text-gray-600">Pending Approvals</p>
          <p className="text-3xl font-bold">5</p>
        </div>
        <div className="card">
          <p className="text-gray-600">Total Feedback</p>
          <p className="text-3xl font-bold">2,847</p>
        </div>
      </div>

      <div className="card">
        <h2 className="text-2xl font-bold mb-4">Pending Instructor Approvals</h2>
        <div className="space-y-4">
          <div className="p-4 bg-gray-50 rounded flex justify-between items-center">
            <div>
              <p className="font-bold">Instructor Name</p>
              <p className="text-sm text-gray-600">instructor@example.com</p>
            </div>
            <div className="space-x-2">
              <button className="btn-primary">Approve</button>
              <button className="btn-secondary">Reject</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
