# SNMP MIB module (IANA-MAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\IANA-MAU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:34 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaMauMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 154)
)
if mibBuilder.loadTexts:
    ianaMauMIB.setRevisions(
        ("2010-02-23 00:00",
         "2007-04-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAifMauTypeListBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bOther", 0),
          ("bAUI", 1),
          ("b10base5", 2),
          ("bFoirl", 3),
          ("b10base2", 4),
          ("b10baseT", 5),
          ("b10baseFP", 6),
          ("b10baseFB", 7),
          ("b10baseFL", 8),
          ("b10broad36", 9),
          ("b10baseTHD", 10),
          ("b10baseTFD", 11),
          ("b10baseFLHD", 12),
          ("b10baseFLFD", 13),
          ("b100baseT4", 14),
          ("b100baseTXHD", 15),
          ("b100baseTXFD", 16),
          ("b100baseFXHD", 17),
          ("b100baseFXFD", 18),
          ("b100baseT2HD", 19),
          ("b100baseT2FD", 20),
          ("b1000baseXHD", 21),
          ("b1000baseXFD", 22),
          ("b1000baseLXHD", 23),
          ("b1000baseLXFD", 24),
          ("b1000baseSXHD", 25),
          ("b1000baseSXFD", 26),
          ("b1000baseCXHD", 27),
          ("b1000baseCXFD", 28),
          ("b1000baseTHD", 29),
          ("b1000baseTFD", 30),
          ("b10GbaseX", 31),
          ("b10GbaseLX4", 32),
          ("b10GbaseR", 33),
          ("b10GbaseER", 34),
          ("b10GbaseLR", 35),
          ("b10GbaseSR", 36),
          ("b10GbaseW", 37),
          ("b10GbaseEW", 38),
          ("b10GbaseLW", 39),
          ("b10GbaseSW", 40),
          ("b10GbaseCX4", 41),
          ("b2BaseTL", 42),
          ("b10PassTS", 43),
          ("b100BaseBX10D", 44),
          ("b100BaseBX10U", 45),
          ("b100BaseLX10", 46),
          ("b1000BaseBX10D", 47),
          ("b1000BaseBX10U", 48),
          ("b1000BaseLX10", 49),
          ("b1000BasePX10D", 50),
          ("b1000BasePX10U", 51),
          ("b1000BasePX20D", 52),
          ("b1000BasePX20U", 53),
          ("b10GbaseT", 54),
          ("b10GbaseLRM", 55),
          ("b1000baseKX", 56),
          ("b10GbaseKX4", 57),
          ("b10GbaseKR", 58),
          ("b10G1GbasePRXD1", 59),
          ("b10G1GbasePRXD2", 60),
          ("b10G1GbasePRXD3", 61),
          ("b10G1GbasePRXU1", 62),
          ("b10G1GbasePRXU2", 63),
          ("b10G1GbasePRXU3", 64),
          ("b10GbasePRD1", 65),
          ("b10GbasePRD2", 66),
          ("b10GbasePRD3", 67),
          ("b10GbasePRU1", 68),
          ("b10GbasePRU3", 69))
    )


class IANAifMauMediaAvailable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("available", 3),
          ("notAvailable", 4),
          ("remoteFault", 5),
          ("invalidSignal", 6),
          ("remoteJabber", 7),
          ("remoteLinkLoss", 8),
          ("remoteTest", 9),
          ("offline", 10),
          ("autoNegError", 11),
          ("pmdLinkFault", 12),
          ("wisFrameLoss", 13),
          ("wisSignalLoss", 14),
          ("pcsLinkFault", 15),
          ("excessiveBER", 16),
          ("dxsLinkFault", 17),
          ("pxsLinkFault", 18),
          ("availableReduced", 19),
          ("ready", 20))
    )



class IANAifMauAutoNegCapBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bOther", 0),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("bFdxPause", 8),
          ("bFdxAPause", 9),
          ("bFdxSPause", 10),
          ("bFdxBPause", 11),
          ("b1000baseX", 12),
          ("b1000baseXFD", 13),
          ("b1000baseT", 14),
          ("b1000baseTFD", 15),
          ("b10GbaseT", 16),
          ("b1000baseKX", 17),
          ("b10GbaseKX4", 18),
          ("b10GbaseKR", 19))
    )


class IANAifJackType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rj45", 2),
          ("rj45S", 3),
          ("db9", 4),
          ("bnc", 5),
          ("fAUI", 6),
          ("mAUI", 7),
          ("fiberSC", 8),
          ("fiberMIC", 9),
          ("fiberST", 10),
          ("telco", 11),
          ("mtrj", 12),
          ("hssdc", 13),
          ("fiberLC", 14),
          ("cx4", 15))
    )



# MIB Managed Objects in the order of their OIDs

_Dot3MauType_ObjectIdentity = ObjectIdentity
dot3MauType = _Dot3MauType_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4)
)
_Dot3MauTypeAUI_ObjectIdentity = ObjectIdentity
dot3MauTypeAUI = _Dot3MauTypeAUI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 1)
)
if mibBuilder.loadTexts:
    dot3MauTypeAUI.setStatus("current")
_Dot3MauType10Base5_ObjectIdentity = ObjectIdentity
dot3MauType10Base5 = _Dot3MauType10Base5_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 2)
)
if mibBuilder.loadTexts:
    dot3MauType10Base5.setStatus("current")
_Dot3MauTypeFoirl_ObjectIdentity = ObjectIdentity
dot3MauTypeFoirl = _Dot3MauTypeFoirl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 3)
)
if mibBuilder.loadTexts:
    dot3MauTypeFoirl.setStatus("current")
_Dot3MauType10Base2_ObjectIdentity = ObjectIdentity
dot3MauType10Base2 = _Dot3MauType10Base2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 4)
)
if mibBuilder.loadTexts:
    dot3MauType10Base2.setStatus("current")
_Dot3MauType10BaseT_ObjectIdentity = ObjectIdentity
dot3MauType10BaseT = _Dot3MauType10BaseT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 5)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseT.setStatus("current")
_Dot3MauType10BaseFP_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFP = _Dot3MauType10BaseFP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 6)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseFP.setStatus("current")
_Dot3MauType10BaseFB_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFB = _Dot3MauType10BaseFB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 7)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseFB.setStatus("current")
_Dot3MauType10BaseFL_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFL = _Dot3MauType10BaseFL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 8)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseFL.setStatus("current")
_Dot3MauType10Broad36_ObjectIdentity = ObjectIdentity
dot3MauType10Broad36 = _Dot3MauType10Broad36_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 9)
)
if mibBuilder.loadTexts:
    dot3MauType10Broad36.setStatus("current")
_Dot3MauType10BaseTHD_ObjectIdentity = ObjectIdentity
dot3MauType10BaseTHD = _Dot3MauType10BaseTHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 10)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseTHD.setStatus("current")
_Dot3MauType10BaseTFD_ObjectIdentity = ObjectIdentity
dot3MauType10BaseTFD = _Dot3MauType10BaseTFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 11)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseTFD.setStatus("current")
_Dot3MauType10BaseFLHD_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFLHD = _Dot3MauType10BaseFLHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 12)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseFLHD.setStatus("current")
_Dot3MauType10BaseFLFD_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFLFD = _Dot3MauType10BaseFLFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 13)
)
if mibBuilder.loadTexts:
    dot3MauType10BaseFLFD.setStatus("current")
_Dot3MauType100BaseT4_ObjectIdentity = ObjectIdentity
dot3MauType100BaseT4 = _Dot3MauType100BaseT4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 14)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseT4.setStatus("current")
_Dot3MauType100BaseTXHD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseTXHD = _Dot3MauType100BaseTXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 15)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseTXHD.setStatus("current")
_Dot3MauType100BaseTXFD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseTXFD = _Dot3MauType100BaseTXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 16)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseTXFD.setStatus("current")
_Dot3MauType100BaseFXHD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseFXHD = _Dot3MauType100BaseFXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 17)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseFXHD.setStatus("current")
_Dot3MauType100BaseFXFD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseFXFD = _Dot3MauType100BaseFXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 18)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseFXFD.setStatus("current")
_Dot3MauType100BaseT2HD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseT2HD = _Dot3MauType100BaseT2HD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 19)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseT2HD.setStatus("current")
_Dot3MauType100BaseT2FD_ObjectIdentity = ObjectIdentity
dot3MauType100BaseT2FD = _Dot3MauType100BaseT2FD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 20)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseT2FD.setStatus("current")
_Dot3MauType1000BaseXHD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseXHD = _Dot3MauType1000BaseXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 21)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseXHD.setStatus("current")
_Dot3MauType1000BaseXFD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseXFD = _Dot3MauType1000BaseXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 22)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseXFD.setStatus("current")
_Dot3MauType1000BaseLXHD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseLXHD = _Dot3MauType1000BaseLXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 23)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseLXHD.setStatus("current")
_Dot3MauType1000BaseLXFD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseLXFD = _Dot3MauType1000BaseLXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 24)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseLXFD.setStatus("current")
_Dot3MauType1000BaseSXHD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseSXHD = _Dot3MauType1000BaseSXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 25)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseSXHD.setStatus("current")
_Dot3MauType1000BaseSXFD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseSXFD = _Dot3MauType1000BaseSXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 26)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseSXFD.setStatus("current")
_Dot3MauType1000BaseCXHD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseCXHD = _Dot3MauType1000BaseCXHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 27)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseCXHD.setStatus("current")
_Dot3MauType1000BaseCXFD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseCXFD = _Dot3MauType1000BaseCXFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 28)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseCXFD.setStatus("current")
_Dot3MauType1000BaseTHD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseTHD = _Dot3MauType1000BaseTHD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 29)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseTHD.setStatus("current")
_Dot3MauType1000BaseTFD_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseTFD = _Dot3MauType1000BaseTFD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 30)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseTFD.setStatus("current")
_Dot3MauType10GigBaseX_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseX = _Dot3MauType10GigBaseX_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 31)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseX.setStatus("current")
_Dot3MauType10GigBaseLX4_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseLX4 = _Dot3MauType10GigBaseLX4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 32)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseLX4.setStatus("current")
_Dot3MauType10GigBaseR_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseR = _Dot3MauType10GigBaseR_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 33)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseR.setStatus("current")
_Dot3MauType10GigBaseER_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseER = _Dot3MauType10GigBaseER_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 34)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseER.setStatus("current")
_Dot3MauType10GigBaseLR_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseLR = _Dot3MauType10GigBaseLR_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 35)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseLR.setStatus("current")
_Dot3MauType10GigBaseSR_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseSR = _Dot3MauType10GigBaseSR_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 36)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseSR.setStatus("current")
_Dot3MauType10GigBaseW_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseW = _Dot3MauType10GigBaseW_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 37)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseW.setStatus("current")
_Dot3MauType10GigBaseEW_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseEW = _Dot3MauType10GigBaseEW_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 38)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseEW.setStatus("current")
_Dot3MauType10GigBaseLW_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseLW = _Dot3MauType10GigBaseLW_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 39)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseLW.setStatus("current")
_Dot3MauType10GigBaseSW_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseSW = _Dot3MauType10GigBaseSW_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 40)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseSW.setStatus("current")
_Dot3MauType10GigBaseCX4_ObjectIdentity = ObjectIdentity
dot3MauType10GigBaseCX4 = _Dot3MauType10GigBaseCX4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 41)
)
if mibBuilder.loadTexts:
    dot3MauType10GigBaseCX4.setStatus("current")
_Dot3MauType2BaseTL_ObjectIdentity = ObjectIdentity
dot3MauType2BaseTL = _Dot3MauType2BaseTL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 42)
)
if mibBuilder.loadTexts:
    dot3MauType2BaseTL.setStatus("current")
_Dot3MauType10PassTS_ObjectIdentity = ObjectIdentity
dot3MauType10PassTS = _Dot3MauType10PassTS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 43)
)
if mibBuilder.loadTexts:
    dot3MauType10PassTS.setStatus("current")
_Dot3MauType100BaseBX10D_ObjectIdentity = ObjectIdentity
dot3MauType100BaseBX10D = _Dot3MauType100BaseBX10D_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 44)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseBX10D.setStatus("current")
_Dot3MauType100BaseBX10U_ObjectIdentity = ObjectIdentity
dot3MauType100BaseBX10U = _Dot3MauType100BaseBX10U_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 45)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseBX10U.setStatus("current")
_Dot3MauType100BaseLX10_ObjectIdentity = ObjectIdentity
dot3MauType100BaseLX10 = _Dot3MauType100BaseLX10_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 46)
)
if mibBuilder.loadTexts:
    dot3MauType100BaseLX10.setStatus("current")
_Dot3MauType1000BaseBX10D_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseBX10D = _Dot3MauType1000BaseBX10D_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 47)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseBX10D.setStatus("current")
_Dot3MauType1000BaseBX10U_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseBX10U = _Dot3MauType1000BaseBX10U_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 48)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseBX10U.setStatus("current")
_Dot3MauType1000BaseLX10_ObjectIdentity = ObjectIdentity
dot3MauType1000BaseLX10 = _Dot3MauType1000BaseLX10_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 49)
)
if mibBuilder.loadTexts:
    dot3MauType1000BaseLX10.setStatus("current")
_Dot3MauType1000BasePX10D_ObjectIdentity = ObjectIdentity
dot3MauType1000BasePX10D = _Dot3MauType1000BasePX10D_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 50)
)
if mibBuilder.loadTexts:
    dot3MauType1000BasePX10D.setStatus("current")
_Dot3MauType1000BasePX10U_ObjectIdentity = ObjectIdentity
dot3MauType1000BasePX10U = _Dot3MauType1000BasePX10U_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 51)
)
if mibBuilder.loadTexts:
    dot3MauType1000BasePX10U.setStatus("current")
_Dot3MauType1000BasePX20D_ObjectIdentity = ObjectIdentity
dot3MauType1000BasePX20D = _Dot3MauType1000BasePX20D_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 52)
)
if mibBuilder.loadTexts:
    dot3MauType1000BasePX20D.setStatus("current")
_Dot3MauType1000BasePX20U_ObjectIdentity = ObjectIdentity
dot3MauType1000BasePX20U = _Dot3MauType1000BasePX20U_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 53)
)
if mibBuilder.loadTexts:
    dot3MauType1000BasePX20U.setStatus("current")
_Dot3MauType10GbaseT_ObjectIdentity = ObjectIdentity
dot3MauType10GbaseT = _Dot3MauType10GbaseT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 54)
)
if mibBuilder.loadTexts:
    dot3MauType10GbaseT.setStatus("current")
_Dot3MauType10GbaseLRM_ObjectIdentity = ObjectIdentity
dot3MauType10GbaseLRM = _Dot3MauType10GbaseLRM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 55)
)
if mibBuilder.loadTexts:
    dot3MauType10GbaseLRM.setStatus("current")
_Dot3MauType1000baseKX_ObjectIdentity = ObjectIdentity
dot3MauType1000baseKX = _Dot3MauType1000baseKX_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 56)
)
if mibBuilder.loadTexts:
    dot3MauType1000baseKX.setStatus("current")
_Dot3MauType10GbaseKX4_ObjectIdentity = ObjectIdentity
dot3MauType10GbaseKX4 = _Dot3MauType10GbaseKX4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 57)
)
if mibBuilder.loadTexts:
    dot3MauType10GbaseKX4.setStatus("current")
_Dot3MauType10GbaseKR_ObjectIdentity = ObjectIdentity
dot3MauType10GbaseKR = _Dot3MauType10GbaseKR_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 58)
)
if mibBuilder.loadTexts:
    dot3MauType10GbaseKR.setStatus("current")
_Dot3MauType10G1GbasePRXD1_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXD1 = _Dot3MauType10G1GbasePRXD1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 59)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXD1.setStatus("current")
_Dot3MauType10G1GbasePRXD2_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXD2 = _Dot3MauType10G1GbasePRXD2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 60)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXD2.setStatus("current")
_Dot3MauType10G1GbasePRXD3_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXD3 = _Dot3MauType10G1GbasePRXD3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 61)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXD3.setStatus("current")
_Dot3MauType10G1GbasePRXU1_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXU1 = _Dot3MauType10G1GbasePRXU1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 62)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXU1.setStatus("current")
_Dot3MauType10G1GbasePRXU2_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXU2 = _Dot3MauType10G1GbasePRXU2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 63)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXU2.setStatus("current")
_Dot3MauType10G1GbasePRXU3_ObjectIdentity = ObjectIdentity
dot3MauType10G1GbasePRXU3 = _Dot3MauType10G1GbasePRXU3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 64)
)
if mibBuilder.loadTexts:
    dot3MauType10G1GbasePRXU3.setStatus("current")
_Dot3MauType10GbasePRD1_ObjectIdentity = ObjectIdentity
dot3MauType10GbasePRD1 = _Dot3MauType10GbasePRD1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 65)
)
if mibBuilder.loadTexts:
    dot3MauType10GbasePRD1.setStatus("current")
_Dot3MauType10GbasePRD2_ObjectIdentity = ObjectIdentity
dot3MauType10GbasePRD2 = _Dot3MauType10GbasePRD2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 66)
)
if mibBuilder.loadTexts:
    dot3MauType10GbasePRD2.setStatus("current")
_Dot3MauType10GbasePRD3_ObjectIdentity = ObjectIdentity
dot3MauType10GbasePRD3 = _Dot3MauType10GbasePRD3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 67)
)
if mibBuilder.loadTexts:
    dot3MauType10GbasePRD3.setStatus("current")
_Dot3MauType10GbasePRU1_ObjectIdentity = ObjectIdentity
dot3MauType10GbasePRU1 = _Dot3MauType10GbasePRU1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 68)
)
if mibBuilder.loadTexts:
    dot3MauType10GbasePRU1.setStatus("current")
_Dot3MauType10GbasePRU3_ObjectIdentity = ObjectIdentity
dot3MauType10GbasePRU3 = _Dot3MauType10GbasePRU3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 69)
)
if mibBuilder.loadTexts:
    dot3MauType10GbasePRU3.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-MAU-MIB",
    **{"IANAifMauTypeListBits": IANAifMauTypeListBits,
       "IANAifMauMediaAvailable": IANAifMauMediaAvailable,
       "IANAifMauAutoNegCapBits": IANAifMauAutoNegCapBits,
       "IANAifJackType": IANAifJackType,
       "dot3MauType": dot3MauType,
       "dot3MauTypeAUI": dot3MauTypeAUI,
       "dot3MauType10Base5": dot3MauType10Base5,
       "dot3MauTypeFoirl": dot3MauTypeFoirl,
       "dot3MauType10Base2": dot3MauType10Base2,
       "dot3MauType10BaseT": dot3MauType10BaseT,
       "dot3MauType10BaseFP": dot3MauType10BaseFP,
       "dot3MauType10BaseFB": dot3MauType10BaseFB,
       "dot3MauType10BaseFL": dot3MauType10BaseFL,
       "dot3MauType10Broad36": dot3MauType10Broad36,
       "dot3MauType10BaseTHD": dot3MauType10BaseTHD,
       "dot3MauType10BaseTFD": dot3MauType10BaseTFD,
       "dot3MauType10BaseFLHD": dot3MauType10BaseFLHD,
       "dot3MauType10BaseFLFD": dot3MauType10BaseFLFD,
       "dot3MauType100BaseT4": dot3MauType100BaseT4,
       "dot3MauType100BaseTXHD": dot3MauType100BaseTXHD,
       "dot3MauType100BaseTXFD": dot3MauType100BaseTXFD,
       "dot3MauType100BaseFXHD": dot3MauType100BaseFXHD,
       "dot3MauType100BaseFXFD": dot3MauType100BaseFXFD,
       "dot3MauType100BaseT2HD": dot3MauType100BaseT2HD,
       "dot3MauType100BaseT2FD": dot3MauType100BaseT2FD,
       "dot3MauType1000BaseXHD": dot3MauType1000BaseXHD,
       "dot3MauType1000BaseXFD": dot3MauType1000BaseXFD,
       "dot3MauType1000BaseLXHD": dot3MauType1000BaseLXHD,
       "dot3MauType1000BaseLXFD": dot3MauType1000BaseLXFD,
       "dot3MauType1000BaseSXHD": dot3MauType1000BaseSXHD,
       "dot3MauType1000BaseSXFD": dot3MauType1000BaseSXFD,
       "dot3MauType1000BaseCXHD": dot3MauType1000BaseCXHD,
       "dot3MauType1000BaseCXFD": dot3MauType1000BaseCXFD,
       "dot3MauType1000BaseTHD": dot3MauType1000BaseTHD,
       "dot3MauType1000BaseTFD": dot3MauType1000BaseTFD,
       "dot3MauType10GigBaseX": dot3MauType10GigBaseX,
       "dot3MauType10GigBaseLX4": dot3MauType10GigBaseLX4,
       "dot3MauType10GigBaseR": dot3MauType10GigBaseR,
       "dot3MauType10GigBaseER": dot3MauType10GigBaseER,
       "dot3MauType10GigBaseLR": dot3MauType10GigBaseLR,
       "dot3MauType10GigBaseSR": dot3MauType10GigBaseSR,
       "dot3MauType10GigBaseW": dot3MauType10GigBaseW,
       "dot3MauType10GigBaseEW": dot3MauType10GigBaseEW,
       "dot3MauType10GigBaseLW": dot3MauType10GigBaseLW,
       "dot3MauType10GigBaseSW": dot3MauType10GigBaseSW,
       "dot3MauType10GigBaseCX4": dot3MauType10GigBaseCX4,
       "dot3MauType2BaseTL": dot3MauType2BaseTL,
       "dot3MauType10PassTS": dot3MauType10PassTS,
       "dot3MauType100BaseBX10D": dot3MauType100BaseBX10D,
       "dot3MauType100BaseBX10U": dot3MauType100BaseBX10U,
       "dot3MauType100BaseLX10": dot3MauType100BaseLX10,
       "dot3MauType1000BaseBX10D": dot3MauType1000BaseBX10D,
       "dot3MauType1000BaseBX10U": dot3MauType1000BaseBX10U,
       "dot3MauType1000BaseLX10": dot3MauType1000BaseLX10,
       "dot3MauType1000BasePX10D": dot3MauType1000BasePX10D,
       "dot3MauType1000BasePX10U": dot3MauType1000BasePX10U,
       "dot3MauType1000BasePX20D": dot3MauType1000BasePX20D,
       "dot3MauType1000BasePX20U": dot3MauType1000BasePX20U,
       "dot3MauType10GbaseT": dot3MauType10GbaseT,
       "dot3MauType10GbaseLRM": dot3MauType10GbaseLRM,
       "dot3MauType1000baseKX": dot3MauType1000baseKX,
       "dot3MauType10GbaseKX4": dot3MauType10GbaseKX4,
       "dot3MauType10GbaseKR": dot3MauType10GbaseKR,
       "dot3MauType10G1GbasePRXD1": dot3MauType10G1GbasePRXD1,
       "dot3MauType10G1GbasePRXD2": dot3MauType10G1GbasePRXD2,
       "dot3MauType10G1GbasePRXD3": dot3MauType10G1GbasePRXD3,
       "dot3MauType10G1GbasePRXU1": dot3MauType10G1GbasePRXU1,
       "dot3MauType10G1GbasePRXU2": dot3MauType10G1GbasePRXU2,
       "dot3MauType10G1GbasePRXU3": dot3MauType10G1GbasePRXU3,
       "dot3MauType10GbasePRD1": dot3MauType10GbasePRD1,
       "dot3MauType10GbasePRD2": dot3MauType10GbasePRD2,
       "dot3MauType10GbasePRD3": dot3MauType10GbasePRD3,
       "dot3MauType10GbasePRU1": dot3MauType10GbasePRU1,
       "dot3MauType10GbasePRU3": dot3MauType10GbasePRU3,
       "ianaMauMIB": ianaMauMIB}
)
