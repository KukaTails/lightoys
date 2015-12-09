(define (square-list items) 
  (define (iter things answer) 
    (if (null? things) 
        answer 
        (iter (cdr things) 
              (cons (square (car things)) answer)))) 
  (iter items nil)) 

(square-list (list 1 2 3 4))

; (cons (square (car things)) answer)
; the car of things should not be the front of (cons (square (car things)) answer)

(define (square-list items) 
  (define (iter things answer) 
    (if (null? things) 
        answer 
        (iter (cdr things) 
              (cons answer (square (car things)))))) 
  (iter items nil))

; answer is a list