(define (square-tree tree)
  (define nil '())
  (define (square x) (* x x))
  (cond ((null? tree) nil)
        ((not (pair? tree)) (square tree))
        (else (cons (square-tree (car tree))
                    (square-tree (cdr tree))))))

(define (square-tree-map tree)
  (define (square x) (* x x))
  (map (lambda (sub-tree)
         (if (not (pair? sub-tree))
             (square sub-tree)
             (square-tree-map sub-tree)))
       tree))

; testing
(define tree (list (list 1 2) (list 2 3 6)))

(display (square-tree tree))
(newline)
(display (square-tree-map tree))
(newline)
(display (square-tree-map (list 1
                                (list 2 (list 3 4) 5)
                                (list 6 7))))