document.addEventListener('DOMContentLoaded', () => {
  
  // Helper to fetch blogs data
  async function fetchBlogs() {
    try {
      // Assuming blogs.json is in the same directory
      const response = await fetch('./blogs.json');
      if (!response.ok) {
        throw new Error('Failed to load blog data.');
      }
      return await response.json();
    } catch (error) {
      console.error(error);
      return [];
    }
  }

  // --- Render Blog List (for blogs.html) ---
  const blogListContainer = document.getElementById('blog-list-container');
  
  if (blogListContainer) {
    fetchBlogs().then(blogs => {
      blogListContainer.innerHTML = ''; // clear loading text
      
      if (blogs.length === 0) {
        blogListContainer.innerHTML = '<p style="color: var(--grey); text-align: center; width: 100%;">No posts found.</p>';
        return;
      }
      
      blogs.forEach(blog => {
        const card = document.createElement('a');
        card.href = `post.html?id=${blog.id}`;
        card.className = 'blog-card';
        
        card.innerHTML = `
          <div class="blog-card-category">${blog.category || 'Insight'}</div>
          <h3 class="blog-card-title">${blog.title}</h3>
          <p class="blog-card-excerpt">${blog.excerpt}</p>
          <div class="blog-card-footer">
            <span class="blog-card-date">${blog.date}</span>
            <span class="blog-card-readmore">Read more →</span>
          </div>
        `;
        
        blogListContainer.appendChild(card);
      });
    });
  }

  // --- Render Individual Blog Post (for post.html) ---
  const postContainer = document.getElementById('post-container');
  
  if (postContainer) {
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get('id');
    
    if (!postId) {
      postContainer.innerHTML = `
        <div style="text-align: center; padding: 40px 0;">
          <h2>Post Not Found</h2>
          <p style="color: var(--grey); margin-top: 10px;">The requested article could not be located.</p>
        </div>
      `;
      return;
    }
    
    fetchBlogs().then(blogs => {
      const blog = blogs.find(b => b.id == postId);
      
      if (!blog) {
        postContainer.innerHTML = `
          <div style="text-align: center; padding: 40px 0;">
            <h2>Post Not Found</h2>
            <p style="color: var(--grey); margin-top: 10px;">The requested article does not exist.</p>
          </div>
        `;
        return;
      }

      // Update page title
      document.title = `${blog.title} - Blazrs`;
      
      // Render content
      postContainer.innerHTML = `
        <div class="post-header">
          <div class="post-meta">
            <span class="post-category">${blog.category || 'Insight'}</span>
            <span class="post-date">${blog.date}</span>
          </div>
          <h1 class="post-title">${blog.title}</h1>
        </div>
        <div class="post-content">
          ${blog.content}
        </div>
      `;

      if (window.mermaid) {
        window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
      }
    });
  }
  
});
