<h2><a href="https://leetcode.com/problems/1046-last-stone-weight">1046. Last Stone Weight</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr>
<p>You are given an array of integers <code> stones </code> where <code> stones [i]</code> is the weight of the <code> ith </code> stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If <code> x == y </code>, both stones are destroyed, and
If <code> x != y </code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return <code>0</code>. 

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
	<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
</ul>
