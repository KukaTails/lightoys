(define (tree-map proc tree)
  (map (lambda (sub-tree)
         (if (not (pair? sub-tree))
             (proc sub-tree)
             (tree-map proc sub-tree)))
       tree))

; definition for square-tree
(define (square x) (* x x))
(define (square-tree tree) (tree-map square tree))

; testing for square-tree
(display (square-tree (list 1
                            (list 2 (list 3 4) 5)
                            (list 6 7))))