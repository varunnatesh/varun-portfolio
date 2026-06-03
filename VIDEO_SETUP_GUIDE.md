# 🎥 Adding Your Introduction Video

## ✨ Video Integration is Ready!

Your portfolio now supports a professional intro video in the hero section!

---

## 🎯 Two Ways to Add Your Video

### **Option 1: Upload Video File (Recommended)**

#### Step 1: Prepare Your Video
- **Format:** MP4 (recommended for best compatibility)
- **Duration:** 30-60 seconds ideal
- **Resolution:** 1920x1080 (Full HD) or 1280x720 (HD)
- **File Size:** Under 50MB for fast loading
- **Content:** Your introduction script:
  > "Hi, I'm Varun. AI researcher, IEEE published developer, and someone who builds things that actually work. Welcome to my portfolio — let me show you what I mean."

#### Step 2: Upload via Admin Panel
1. Go to **http://localhost:8000/admin**
2. Login with your credentials
3. Click **Site Configuration**
4. Scroll to **Hero Section**
5. Click **"Choose File"** next to **"Hero video file"**
6. Select your MP4 video
7. Click **Save**

#### Step 3: Check Your Homepage
- Visit **http://localhost:8000**
- Your video will appear on the left side of the hero section
- Video will autoplay (muted) on page load
- Users can click play/pause button overlay

---

### **Option 2: Use External Video URL**

If your video is hosted elsewhere (YouTube, Vimeo, cloud storage):

#### For Direct Video URLs:
1. Go to **Admin Panel** → **Site Configuration**
2. In **"Hero video URL"** field, paste your video URL
3. Example: `https://yourdomain.com/intro-video.mp4`
4. Click **Save**

#### Note on YouTube/Vimeo:
- If using YouTube/Vimeo, you'll need to use the embed code instead
- The current setup works best with direct MP4 URLs
- For YouTube embeds, let me know and I can modify the template

---

## 🎨 How It Looks

### **With Video (Two Column Layout):**
```
┌─────────────────────────────────────────┐
│           Hero Section                  │
├──────────────────┬──────────────────────┤
│                  │                      │
│   [Your Video]   │   Your Name          │
│   with controls  │   Typing Effect      │
│   & play button  │   Description        │
│                  │   CTA Buttons        │
│                  │   Stats Counter      │
│                  │                      │
└──────────────────┴──────────────────────┘
```

### **Without Video (Centered Layout):**
```
┌─────────────────────────────────────────┐
│           Hero Section                  │
├─────────────────────────────────────────┤
│                                         │
│          Your Name (centered)           │
│          Typing Effect                  │
│          Description                    │
│          CTA Buttons                    │
│          Stats Counter                  │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🎬 Video Features

✅ **Autoplay** - Video starts automatically (muted)  
✅ **Loop** - Video repeats continuously  
✅ **Controls** - Users can play/pause, seek, adjust volume  
✅ **Play/Pause Overlay** - Elegant button appears on hover  
✅ **Responsive** - Adapts to mobile/tablet screens  
✅ **Modern Design** - Rounded corners, shadow effects  
✅ **Caption** - Shows "Varun K N - Introduction"  

---

## 📱 Mobile Experience

On mobile devices:
- Video moves above the text content
- Maintains proper sizing
- Touch-friendly controls
- Optimized for mobile data

---

## 🎥 Video Recording Tips

### **Equipment:**
- Use your phone camera (modern phones are great!)
- Or laptop webcam
- Or professional camera if available

### **Setting:**
- Good lighting (face a window or use soft lighting)
- Clean background (professional space)
- Minimal noise (quiet room)

### **Recording:**
- Look at the camera
- Speak clearly and confidently
- Smile naturally
- Keep it under 60 seconds
- Practice your script a few times

### **Editing (Optional):**
- Use free tools: DaVinci Resolve, iMovie, CapCut
- Add subtle background music (low volume)
- Add your name/title overlay
- Export as MP4, H.264 codec

---

## 🔧 Technical Details

### **Supported Formats:**
- ✅ **MP4** (H.264) - Best compatibility
- ✅ **WebM** - Good for web
- ✅ **OGG** - Alternative format

### **Recommended Settings:**
- **Resolution:** 1920x1080 or 1280x720
- **Bitrate:** 3-5 Mbps for HD
- **Frame Rate:** 30fps or 60fps
- **Audio:** AAC codec, 128kbps
- **File Size:** Under 50MB

### **Optimization:**
```bash
# Using ffmpeg to compress video:
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4
```

---

## 🎯 Current Video Path

If you upload via admin, your video will be saved to:
```
media/videos/your-video-name.mp4
```

You can also manually place your video in this folder and reference it.

---

## 🚀 Quick Start Steps

**5-Minute Setup:**

1. ✅ Record your 30-second intro
2. ✅ Convert/compress to MP4 (if needed)
3. ✅ Login to admin panel
4. ✅ Upload video in Site Configuration
5. ✅ Refresh homepage - Done!

---

## 🎨 Customization Options

### **Remove Autoplay:**
Edit `templates/portfolio/home.html`:
- Remove `autoplay` attribute from `<video>` tag

### **Remove Loop:**
- Remove `loop` attribute from `<video>` tag

### **Add Poster Image:**
```html
<video poster="path/to/thumbnail.jpg" ...>
```

### **Change Video Size:**
Edit `static/css/style.css`:
```css
.video-wrapper {
    max-width: 600px; /* Adjust size */
}
```

---

## 📋 Checklist

Before uploading your video:
- [ ] Video is in MP4 format
- [ ] Duration is under 60 seconds
- [ ] File size is under 50MB
- [ ] Content is professional
- [ ] Audio is clear
- [ ] Lighting is good
- [ ] Background is clean

After uploading:
- [ ] Video displays on homepage
- [ ] Video autoplays (muted)
- [ ] Play/pause button works
- [ ] Video loops smoothly
- [ ] Mobile view works
- [ ] Audio plays when unmuted

---

## 🎭 Alternative: Text-Only Hero

If you prefer not to use video, the portfolio works perfectly without it!

Simply don't upload a video, and you'll get:
- Centered hero content
- Full-width design
- All other features intact

---

## 💡 Pro Tips

1. **Keep it Short** - 30-45 seconds is ideal
2. **Be Authentic** - Natural is better than perfect
3. **Show Personality** - Let your passion for AI shine
4. **Add Captions** - For accessibility (optional)
5. **Test on Mobile** - Ensure it looks good everywhere
6. **Compress Well** - Balance quality and file size

---

## 🔥 Your Script Reference

Based on what you mentioned:

> "Hi, I'm Varun. AI researcher, IEEE published developer, and someone who builds things that actually work. Welcome to my portfolio — let me show you what I mean."

**Extended version (45 seconds):**

> "Hi, I'm Varun K N, an AI researcher and machine learning engineer. I've published research in IEEE on deep learning-based object detection and built production ML systems with over 90% accuracy. From rental intelligence platforms to forest fire detection, I create AI solutions that actually work in the real world. Welcome to my portfolio — let's build something amazing together."

---

## 🆘 Troubleshooting

### **Video not showing:**
- Check file uploaded in Admin → Site Configuration
- Verify video format is MP4
- Check browser console for errors

### **Video too large to upload:**
- Compress using online tools (CloudConvert, HandBrake)
- Or use external hosting (Vimeo, Dropbox)

### **Video not playing:**
- Try different browser (Chrome recommended)
- Check video codec (H.264 required)
- Verify file isn't corrupted

### **Layout looks wrong:**
- Clear browser cache
- Check browser width (responsive design)
- Verify CSS loaded properly

---

## 📞 Need Help?

If you need assistance:
1. Check video file format and size
2. Try uploading a different video
3. Check browser console for errors
4. Test in different browsers

---

## 🎉 You're All Set!

Your portfolio is now ready for a professional video introduction!

**Next Steps:**
1. Record your intro video
2. Upload via admin panel
3. Test on homepage
4. Show it to the world!

Your video will make your portfolio stand out and create an immediate personal connection with visitors! 🚀

---

**Current Status:** Video integration ✅ Complete!

**Upload Location:** Admin Panel → Site Configuration → Hero Section

**Video Display:** Homepage Hero Section (Left Side)
