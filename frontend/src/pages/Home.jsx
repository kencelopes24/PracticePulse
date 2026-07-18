import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="space-y-12">
      <section className="text-center py-20 bg-gradient-to-r from-indigo-600 to-pink-600 text-white rounded-lg">
        <h1 className="text-5xl font-bold mb-4">Welcome to PracticePulse</h1>
        <p className="text-xl mb-8">Collect feedback. Analyze insights. Grow your wellness business.</p>
        <div className="space-x-4">
          <Link to="/dashboard" className="btn-primary">Get Started</Link>
          <a href="#features" className="btn-secondary">Learn More</a>
        </div>
      </section>

      <section id="features" className="grid md:grid-cols-3 gap-6">
        <div className="card">
          <h3 className="text-xl font-bold mb-4">📝 Collect Feedback</h3>
          <p>Students scan a QR code and provide anonymous feedback instantly after class.</p>
        </div>
        <div className="card">
          <h3 className="text-xl font-bold mb-4">📊 Analyze Trends</h3>
          <p>Monitor satisfaction, engagement, and retention with interactive dashboards.</p>
        </div>
        <div className="card">
          <h3 className="text-xl font-bold mb-4">⭐ Showcase Reviews</h3>
          <p>Display verified testimonials on your professional public profile.</p>
        </div>
      </section>
    </div>
  )
}
