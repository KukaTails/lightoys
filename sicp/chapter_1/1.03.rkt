;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1.03|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #t () #f)))
(define (sum-largest-two-of-three a b c)
  (if (>= a b)
      (+ a
         (if (>= b c) b c))
      (+ b
         (if (>= a c) a c))))

; test
(sum-largest-two-of-three -1 -1 2)
(sum-largest-two-of-three -1 0 2)
(sum-largest-two-of-three 100 -10 20)