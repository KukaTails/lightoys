;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1.04|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #t () #f)))
; the result of (if (> b 0) + -) will be + or - operator,
; which will be appied to the operands.
(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

; test
a-plus-abs
(a-plus-abs-b 1 -2)