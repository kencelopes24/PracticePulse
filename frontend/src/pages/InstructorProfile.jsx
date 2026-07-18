import { useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'

export default function InstructorProfile() {
  const { id } = useParams()
  const [instructor, setInstructor] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(false)
  }, [id])

  if (loading) return <div>Loading...</div>

  return (
    <div className="space-y-8">
      <div className="grid md:grid-cols-3 gap-6">
        <div className="md:col-span-2 space-y-6">
          <div className="card">
            <h1 className="text-3xl font-bold mb-2">Instructor Name</h1>
            <div className="flex space-x-4 text-lg">
              <span>⭐ 4.5 (128 reviews)</span>
              <span>🔗 <a href="#" className="text-indigo-600">Website</a></span>
              <span>📷 <a href="#" className="text-indigo-600">Instagram</a></span>
            </div>
          </div>

          <div className="card">
            <h2 className="text-2xl font-bold mb-4">About</h2>
            <p className="text-gray-700 mb-4">Instructor bio goes here...</p>
            <div>
              <h3 className="font-bold mb-2">Certifications</h3>
              <ul className="list-disc list-inside text-gray-600">
                <li>RYT-200</li>
              </ul>
            </div>
          </div>

          <div className="card">
            <h2 className="text-2xl font-bold mb-4">Verified Testimonials</h2>
            <div className="space-y-4">
              <div className="p-4 bg-gray-50 rounded">
                <p className="font-semibold">⭐⭐⭐⭐⭐ Amazing Experience</p>
                <p className="text-gray-600">"This instructor really knows their craft."</p>
              </div>
            </div>
          </div>
        </div>

        <div className="card h-fit">
          <h3 className="text-xl font-bold mb-4">Specialties</h3>
          <div className="space-y-2">
            <span className="inline-block bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm">Vinyasa</span>
            <span className="inline-block bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm">Meditation</span>
          </div>
          <button className="mt-6 btn-primary w-full">Contact Instructor</button>
        </div>
      </div>
    </div>
  )
}
