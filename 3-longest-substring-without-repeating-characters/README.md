<h2><a href="https://leetcode.com/problems/group-anagrams">3. Longest Substring Without Repeating Characters</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr>
<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring">substring</span>substring without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = [&quot;abcabcbb&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>

<p><strong>Explanation:</strong> <span class="example-io">[The answer is &quot;b&quot;, with the length of 1.]</span></p>
</div>
<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = [&quot;bbbbb&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>

<p><strong>Explanation:</strong> <span class="example-io">The answer is &quot;b&quot;, with the length of 1.</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = [&quot;pwwkew&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3]</span></p>

<p><strong>Explanation:</strong> <span class="example-io">The answer is &quot;wke&quot;, with the length of 3.</span></p>
<p></p><span class="example-io">Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>
