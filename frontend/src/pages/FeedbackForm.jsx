import { useParams, useState } from 'react'
import axios from 'axios'

export default function FeedbackForm() {
  const { qrCode } = useParams()
  const [formData, setFormData] = useState({
    overall_rating: 5,
    communication_rating: 5,
    pacing_rating: 5,
    welcomed_rating: 5,
    community_rating: 5,
    knowledge_rating: 5,
    recommend_rating: 5,
    favorite_aspect: '',
    suggestions: '',
    experience_level: '',
    is_returning_student: false,
  })
  const [submitted, setSubmitted] = useState(false)

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      setSubmitted(true)
    } catch (error) {
      console.error('Error submitting feedback:', error)
    }
  }

  if (submitted) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-indigo-600 to-pink-600">
        <div className="bg-white rounded-lg shadow-xl p-8 text-center">
          <h1 className="text-3xl font-bold mb-4">Thank You!</h1>
          <p className="text-gray-600 mb-6">Your feedback has been submitted and will help improve future classes.</p>
          <button className="btn-primary" onClick={() => window.close()}>Close</button>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-r from-indigo-600 to-pink-600 py-12">
      <div className="container mx-auto max-w-2xl">
        <div className="bg-white rounded-lg shadow-xl p-8">
          <h1 className="text-3xl font-bold mb-2">Class Feedback</h1>
          <p className="text-gray-600 mb-8">Your feedback is anonymous and helps instructors improve their classes.</p>

          <form onSubmit={handleSubmit} className="space-y-6">
            {[
              { name: 'overall_rating', label: 'Overall, how was this class?' },
              { name: 'communication_rating', label: 'How well did the instructor communicate?' },
              { name: 'pacing_rating', label: 'Was the pacing of the class right for you?' },
              { name: 'welcomed_rating', label: 'Did you feel welcomed?' },
              { name: 'community_rating', label: 'Did you feel a sense of community?' },
              { name: 'knowledge_rating', label: 'Was the instructor knowledgeable?' },
              { name: 'recommend_rating', label: 'How likely are you to recommend this class?' },
            ].map(q => (
              <div key={q.name}>
                <label className="block font-semibold mb-2">{q.label}</label>
                <div className="flex space-x-2">
                  {[1, 2, 3, 4, 5].map(rating => (
                    <button
                      key={rating}
                      type="button"
                      onClick={() => setFormData(prev => ({ ...prev, [q.name]: rating }))}
                      className={`px-4 py-2 rounded ${
                        formData[q.name] === rating
                          ? 'bg-indigo-600 text-white'
                          : 'bg-gray-200 text-gray-700'
                      }`}
                    >
                      {rating}
                    </button>
                  ))}
                </div>
              </div>
            ))}

            <div>
              <label className="block font-semibold mb-2">What was your favorite aspect of this class?</label>
              <textarea
                name="favorite_aspect"
                value={formData.favorite_aspect}
                onChange={handleChange}
                rows="3"
                className="w-full border rounded p-2"
              />
            </div>

            <div>
              <label className="block font-semibold mb-2">Do you have any suggestions for improvement?</label>
              <textarea
                name="suggestions"
                value={formData.suggestions}
                onChange={handleChange}
                rows="3"
                className="w-full border rounded p-2"
              />
            </div>

            <div>
              <label className="block font-semibold mb-2">Experience Level (optional)</label>
              <select name="experience_level" value={formData.experience_level} onChange={handleChange} className="w-full border rounded p-2">
                <option value="">Select...</option>
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
              </select>
            </div>

            <label className="flex items-center space-x-2">
              <input type="checkbox" name="is_returning_student" checked={formData.is_returning_student} onChange={handleChange} />
              <span>I am a returning student</span>
            </label>

            <button type="submit" className="btn-primary w-full">
              Submit Feedback
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}
