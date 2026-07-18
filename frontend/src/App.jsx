import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import InstructorDashboard from './pages/InstructorDashboard'
import InstructorProfile from './pages/InstructorProfile'
import FeedbackForm from './pages/FeedbackForm'
import AdminDashboard from './pages/AdminDashboard'
import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout><Home /></Layout>} />
        <Route path="/feedback/:qrCode" element={<FeedbackForm />} />
        <Route path="/instructor/:id" element={<Layout><InstructorProfile /></Layout>} />
        <Route path="/dashboard" element={<Layout><InstructorDashboard /></Layout>} />
        <Route path="/admin" element={<Layout><AdminDashboard /></Layout>} />
      </Routes>
    </Router>
  )
}

export default App
