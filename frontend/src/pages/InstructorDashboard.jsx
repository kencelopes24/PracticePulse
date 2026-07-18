import { useState, useEffect } from 'react'

export default function InstructorDashboard() {
  const [analytics, setAnalytics] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(false)
  }, [])

  if (loading) return <div>Loading...</div>

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Your Dashboard</h1>

      <div className="grid md:grid-cols-4 gap-6">
        <div className="card">
          <p className="text-gray-600">Average Rating</p>
          <p className="text-3xl font-bold">4.5</p>
          <p className="text-sm text-gray-500">Out of 5</p>
        </div>
        <div className="card">
          <p className="text-gray-600">Total Reviews</p>
          <p className="text-3xl font-bold">128</p>
          <p className="text-sm text-gray-500">This month</p>
        </div>
        <div className="card">
          <p className="text-gray-600">Recommendation Rate</p>
          <p className="text-3xl font-bold">92%</p>
          <p className="text-sm text-gray-500">Likely to recommend</p>
        </div>
        <div className="card">
          <p className="text-gray-600">Returning Students</p>
          <p className="text-3xl font-bold">73%</p>
          <p className="text-sm text-gray-500">Retention</p>
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-xl font-bold mb-4">Ratings Trend</h3>
          <p className="text-gray-500">Chart implementation here</p>
        </div>
        <div className="card">
          <h3 className="text-xl font-bold mb-4">Category Breakdown</h3>
          <p className="text-gray-500">Chart implementation here</p>
        </div>
      </div>

      <div className="card">
        <h3 className="text-xl font-bold mb-4">Recent Feedback</h3>
        <div className="space-y-4">
          <div className="p-4 bg-gray-50 rounded">
            <p className="font-semibold">⭐⭐⭐⭐⭐ Fantastic Class</p>
            <p className="text-gray-600">"Really felt welcomed and the pacing was perfect."</p>
            <p className="text-sm text-gray-500">2 days ago</p>
          </div>
        </div>
      </div>
    </div>
  )
}
