;; 基本思想:将子树map后映射为一个整数，该整数为该子树中的叶子
;;   结点个数，再通过累积所有的根节点的子树中的叶子结点的个数即可。

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (count-leaves tree)
  (accumulate +
              0
              (map (lambda (sub-tree)
                     (if (pair? sub-tree)
                         (count-leaves sub-tree)
                         1))
                   tree)))

; testing
(count-leaves (list 1 2 (list 3) (list 4 (list 5 6)) 7 8))