# SNMP MIB module (SEH-PSRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\seh\SEH-PSRV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:21 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MailConnState(Integer32):
    """Custom type MailConnState based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("p3INIT", 1),
          ("p3DNSDONE", 2),
          ("p3CONNECT", 3),
          ("p3CONTACT", 4),
          ("p3LOGIN", 5),
          ("p3WORK", 6),
          ("p3CLOSED", 7),
          ("p3APOPLOGINFAIL", 8),
          ("p3APOPMD5FAIL", 9),
          ("p3CONNECTFAIL", 10),
          ("p3DATAFAIL", 11),
          ("p3DELFAIL", 12),
          ("p3DNSFAIL", 13),
          ("p3LISTFAIL", 14),
          ("p3LOGINFAIL", 15),
          ("p3MEMFAIL", 16),
          ("p3MFROMFAIL", 17),
          ("p3AUTHFAIL", 18),
          ("p3POPFAIL", 19),
          ("p3PWDFAIL", 20),
          ("p3RCPTFAIL", 21),
          ("p3RETRFAIL", 22),
          ("p3SCANFAIL", 23),
          ("p3SENTFAIL", 24),
          ("p3STATFAIL", 25),
          ("p3STATSCANFAIL", 26),
          ("p3USERFAIL", 27))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Seh_ObjectIdentity = ObjectIdentity
seh = _Seh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229)
)
_SehDevice_ObjectIdentity = ObjectIdentity
sehDevice = _SehDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 1)
)


class _SehDevInfo_Type(DisplayString):
    """Custom type sehDevInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SehDevInfo_Type.__name__ = "DisplayString"
_SehDevInfo_Object = MibScalar
sehDevInfo = _SehDevInfo_Object(
    (1, 3, 6, 1, 4, 1, 1229, 1, 1),
    _SehDevInfo_Type()
)
sehDevInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehDevInfo.setStatus("mandatory")
_SehPSrv_ObjectIdentity = ObjectIdentity
sehPSrv = _SehPSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2)
)
_SehGeneral_ObjectIdentity = ObjectIdentity
sehGeneral = _SehGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1)
)


class _SehSysInfo_Type(DisplayString):
    """Custom type sehSysInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SehSysInfo_Type.__name__ = "DisplayString"
_SehSysInfo_Object = MibScalar
sehSysInfo = _SehSysInfo_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 1),
    _SehSysInfo_Type()
)
sehSysInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSysInfo.setStatus("mandatory")


class _SehDefName_Type(DisplayString):
    """Custom type sehDefName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SehDefName_Type.__name__ = "DisplayString"
_SehDefName_Object = MibScalar
sehDefName = _SehDefName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 2),
    _SehDefName_Type()
)
sehDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehDefName.setStatus("mandatory")


class _SehPhysAddr_Type(PhysAddress):
    """Custom type sehPhysAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SehPhysAddr_Type.__name__ = "PhysAddress"
_SehPhysAddr_Object = MibScalar
sehPhysAddr = _SehPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 3),
    _SehPhysAddr_Type()
)
sehPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehPhysAddr.setStatus("mandatory")
_SehHwPn_Type = Integer32
_SehHwPn_Object = MibScalar
sehHwPn = _SehHwPn_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 4),
    _SehHwPn_Type()
)
sehHwPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehHwPn.setStatus("mandatory")


class _SehBiosId_Type(Integer32):
    """Custom type sehBiosId based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              107,
              108,
              109,
              110,
              111,
              112,
              113)
        )
    )
    namedValues = NamedValues(
        *(("ic53", 1),
          ("ic60", 2),
          ("ic55", 3),
          ("ic57", 4),
          ("ic59", 5),
          ("ic73", 6),
          ("ic53f", 7),
          ("ic77", 8),
          ("nc57", 9),
          ("nb53", 10),
          ("nb53f", 11),
          ("nb60", 12),
          ("ic56", 13),
          ("nc77", 14),
          ("nb73", 15),
          ("pm55", 16),
          ("ic69", 17),
          ("ic79", 18),
          ("ic59f", 19),
          ("nb59", 20),
          ("ic55f", 21),
          ("nb59f", 22),
          ("nb69", 23),
          ("nb79", 24),
          ("ic67", 25),
          ("nc67", 26),
          ("ic55t", 27),
          ("ic104", 51),
          ("ic105", 52),
          ("ic106", 53),
          ("ic107", 54),
          ("ic109", 55),
          ("ic126", 56),
          ("ic129", 57),
          ("ic99", 58),
          ("ic127", 59),
          ("ic146", 60),
          ("ic147", 61),
          ("ic149", 62),
          ("ic166", 63),
          ("ic167", 64),
          ("ic169", 65),
          ("sb109", 66),
          ("sb129", 67),
          ("sb149", 68),
          ("sb169", 69),
          ("ic124", 70),
          ("ic144", 71),
          ("pm102", 72),
          ("ic102", 73),
          ("ro102", 74),
          ("nc109", 75),
          ("ic175", 76),
          ("ic177", 77),
          ("ic179", 78),
          ("sb179", 79),
          ("ic189", 80),
          ("sb189", 81),
          ("xb105", 82),
          ("xb104", 83),
          ("xb124", 84),
          ("xb144", 85),
          ("ro105", 86),
          ("ic159", 87),
          ("ic154", 88),
          ("sb159", 89),
          ("ic156", 90),
          ("ic111", 91),
          ("ic190", 92),
          ("ic191", 93),
          ("ic134", 94),
          ("ic157", 95),
          ("ic178", 96),
          ("ic152", 97),
          ("wl105", 98),
          ("ic155", 99),
          ("pm152", 100),
          ("eb105", 101),
          ("ci102", 102),
          ("ci152", 103),
          ("ic125", 107),
          ("ic112", 108),
          ("cl105", 109),
          ("bl650", 110),
          ("wl109", 111),
          ("ic103", 112),
          ("wl154", 113))
    )


_SehBiosId_Type.__name__ = "Integer32"
_SehBiosId_Object = MibScalar
sehBiosId = _SehBiosId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 5),
    _SehBiosId_Type()
)
sehBiosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehBiosId.setStatus("mandatory")
_SehBiosVer_Type = Integer32
_SehBiosVer_Object = MibScalar
sehBiosVer = _SehBiosVer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 6),
    _SehBiosVer_Type()
)
sehBiosVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehBiosVer.setStatus("mandatory")


class _SehCmpId_Type(Integer32):
    """Custom type sehCmpId based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("kyocera", 1),
          ("epson", 2),
          ("pocket", 3),
          ("kyocera2", 4),
          ("hp", 5),
          ("box", 6),
          ("seh", 7),
          ("oki", 8))
    )


_SehCmpId_Type.__name__ = "Integer32"
_SehCmpId_Object = MibScalar
sehCmpId = _SehCmpId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 7),
    _SehCmpId_Type()
)
sehCmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehCmpId.setStatus("mandatory")
_SehCmplevel_Type = Integer32
_SehCmplevel_Object = MibScalar
sehCmplevel = _SehCmplevel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 8),
    _SehCmplevel_Type()
)
sehCmplevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehCmplevel.setStatus("mandatory")
_SehSerNum_Type = Integer32
_SehSerNum_Object = MibScalar
sehSerNum = _SehSerNum_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 9),
    _SehSerNum_Type()
)
sehSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSerNum.setStatus("mandatory")
_SehPrdYear_Type = Integer32
_SehPrdYear_Object = MibScalar
sehPrdYear = _SehPrdYear_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 10),
    _SehPrdYear_Type()
)
sehPrdYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehPrdYear.setStatus("mandatory")
_SehPrdMonth_Type = Integer32
_SehPrdMonth_Object = MibScalar
sehPrdMonth = _SehPrdMonth_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 11),
    _SehPrdMonth_Type()
)
sehPrdMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehPrdMonth.setStatus("mandatory")
_SehSwVer_Type = Integer32
_SehSwVer_Object = MibScalar
sehSwVer = _SehSwVer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 12),
    _SehSwVer_Type()
)
sehSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSwVer.setStatus("mandatory")
_SehSwRel_Type = Integer32
_SehSwRel_Object = MibScalar
sehSwRel = _SehSwRel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 13),
    _SehSwRel_Type()
)
sehSwRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSwRel.setStatus("mandatory")
_SehSwSub_Type = Integer32
_SehSwSub_Object = MibScalar
sehSwSub = _SehSwSub_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 14),
    _SehSwSub_Type()
)
sehSwSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSwSub.setStatus("mandatory")


class _SehSpMode_Type(Integer32):
    """Custom type sehSpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("postscript", 1),
          ("prescribe", 2),
          ("auto", 5),
          ("datamax", 6),
          ("zpl", 7),
          ("escpages3", 8),
          ("epl2", 9))
    )


_SehSpMode_Type.__name__ = "Integer32"
_SehSpMode_Object = MibScalar
sehSpMode = _SehSpMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 15),
    _SehSpMode_Type()
)
sehSpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehSpMode.setStatus("mandatory")
_SehHwMajor_Type = Integer32
_SehHwMajor_Object = MibScalar
sehHwMajor = _SehHwMajor_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 16),
    _SehHwMajor_Type()
)
sehHwMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehHwMajor.setStatus("mandatory")
_SehHwMinor_Type = Integer32
_SehHwMinor_Object = MibScalar
sehHwMinor = _SehHwMinor_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 17),
    _SehHwMinor_Type()
)
sehHwMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehHwMinor.setStatus("mandatory")


class _SehPassword_Type(DisplayString):
    """Custom type sehPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SehPassword_Type.__name__ = "DisplayString"
_SehPassword_Object = MibScalar
sehPassword = _SehPassword_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 18),
    _SehPassword_Type()
)
sehPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehPassword.setStatus("mandatory")


class _SehAccessControl_Type(Integer32):
    """Custom type sehAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SehAccessControl_Type.__name__ = "Integer32"
_SehAccessControl_Object = MibScalar
sehAccessControl = _SehAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 19),
    _SehAccessControl_Type()
)
sehAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehAccessControl.setStatus("mandatory")


class _SehDealer_Type(DisplayString):
    """Custom type sehDealer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SehDealer_Type.__name__ = "DisplayString"
_SehDealer_Object = MibScalar
sehDealer = _SehDealer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 20),
    _SehDealer_Type()
)
sehDealer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehDealer.setStatus("mandatory")


class _SehDealerURL_Type(DisplayString):
    """Custom type sehDealerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SehDealerURL_Type.__name__ = "DisplayString"
_SehDealerURL_Object = MibScalar
sehDealerURL = _SehDealerURL_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 21),
    _SehDealerURL_Type()
)
sehDealerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehDealerURL.setStatus("mandatory")


class _SehLocalisation_Type(DisplayString):
    """Custom type sehLocalisation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SehLocalisation_Type.__name__ = "DisplayString"
_SehLocalisation_Object = MibScalar
sehLocalisation = _SehLocalisation_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 22),
    _SehLocalisation_Type()
)
sehLocalisation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehLocalisation.setStatus("mandatory")


class _SehHpJetAdminCompatibility_Type(Integer32):
    """Custom type sehHpJetAdminCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SehHpJetAdminCompatibility_Type.__name__ = "Integer32"
_SehHpJetAdminCompatibility_Object = MibScalar
sehHpJetAdminCompatibility = _SehHpJetAdminCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 23),
    _SehHpJetAdminCompatibility_Type()
)
sehHpJetAdminCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehHpJetAdminCompatibility.setStatus("mandatory")


class _SehEnpcSupport_Type(Integer32):
    """Custom type sehEnpcSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("basic", 1),
          ("full", 2))
    )


_SehEnpcSupport_Type.__name__ = "Integer32"
_SehEnpcSupport_Object = MibScalar
sehEnpcSupport = _SehEnpcSupport_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 24),
    _SehEnpcSupport_Type()
)
sehEnpcSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehEnpcSupport.setStatus("mandatory")


class _SehAdminGroup_Type(DisplayString):
    """Custom type sehAdminGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SehAdminGroup_Type.__name__ = "DisplayString"
_SehAdminGroup_Object = MibScalar
sehAdminGroup = _SehAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 25),
    _SehAdminGroup_Type()
)
sehAdminGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehAdminGroup.setStatus("mandatory")


class _SehUpdateState_Type(Integer32):
    """Custom type sehUpdateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("active", 1),
          ("failed", 2))
    )


_SehUpdateState_Type.__name__ = "Integer32"
_SehUpdateState_Object = MibScalar
sehUpdateState = _SehUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 26),
    _SehUpdateState_Type()
)
sehUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehUpdateState.setStatus("mandatory")
_SehJobRecvTimeout_Type = Integer32
_SehJobRecvTimeout_Object = MibScalar
sehJobRecvTimeout = _SehJobRecvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 27),
    _SehJobRecvTimeout_Type()
)
sehJobRecvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehJobRecvTimeout.setStatus("mandatory")
_SehThinPrintPort_Type = Integer32
_SehThinPrintPort_Object = MibScalar
sehThinPrintPort = _SehThinPrintPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 29),
    _SehThinPrintPort_Type()
)
sehThinPrintPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehThinPrintPort.setStatus("mandatory")


class _SehHpHttpDaemon_Type(Integer32):
    """Custom type sehHpHttpDaemon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SehHpHttpDaemon_Type.__name__ = "Integer32"
_SehHpHttpDaemon_Object = MibScalar
sehHpHttpDaemon = _SehHpHttpDaemon_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 30),
    _SehHpHttpDaemon_Type()
)
sehHpHttpDaemon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehHpHttpDaemon.setStatus("mandatory")


class _SehBaseLine_Type(Integer32):
    """Custom type sehBaseLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SehBaseLine_Type.__name__ = "Integer32"
_SehBaseLine_Object = MibScalar
sehBaseLine = _SehBaseLine_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 31),
    _SehBaseLine_Type()
)
sehBaseLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehBaseLine.setStatus("mandatory")


class _SehEthernetConfig_Type(Integer32):
    """Custom type sehEthernetConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("tenbasehalf", 1),
          ("tenbasefull", 2),
          ("hundredbasehalf", 3),
          ("hundredbasefull", 4))
    )


_SehEthernetConfig_Type.__name__ = "Integer32"
_SehEthernetConfig_Object = MibScalar
sehEthernetConfig = _SehEthernetConfig_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 32),
    _SehEthernetConfig_Type()
)
sehEthernetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehEthernetConfig.setStatus("mandatory")


class _SehSwId_Type(Integer32):
    """Custom type sehSwId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("tpg", 2),
          ("vpn", 3),
          ("tni", 4),
          ("uds", 6))
    )


_SehSwId_Type.__name__ = "Integer32"
_SehSwId_Object = MibScalar
sehSwId = _SehSwId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 33),
    _SehSwId_Type()
)
sehSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSwId.setStatus("mandatory")


class _SehNetworkType_Type(Integer32):
    """Custom type sehNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ethernet10Mbit", 1),
          ("ethernet100MbitTx", 2),
          ("wireless54Mbit", 3),
          ("ethernet100MbitFx", 4),
          ("ethernet100MbitFxTx", 5),
          ("tokenring", 6),
          ("ethernetGbitTx", 7))
    )


_SehNetworkType_Type.__name__ = "Integer32"
_SehNetworkType_Object = MibScalar
sehNetworkType = _SehNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 34),
    _SehNetworkType_Type()
)
sehNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehNetworkType.setStatus("mandatory")
_SehUtnPort_Type = Integer32
_SehUtnPort_Object = MibScalar
sehUtnPort = _SehUtnPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 35),
    _SehUtnPort_Type()
)
sehUtnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehUtnPort.setStatus("mandatory")
_SehZebraPort_Type = Integer32
_SehZebraPort_Object = MibScalar
sehZebraPort = _SehZebraPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 36),
    _SehZebraPort_Type()
)
sehZebraPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehZebraPort.setStatus("mandatory")


class _SehServiceInfo_Type(DisplayString):
    """Custom type sehServiceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SehServiceInfo_Type.__name__ = "DisplayString"
_SehServiceInfo_Object = MibScalar
sehServiceInfo = _SehServiceInfo_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 37),
    _SehServiceInfo_Type()
)
sehServiceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehServiceInfo.setStatus("mandatory")
_SehButtonPressed_Type = Integer32
_SehButtonPressed_Object = MibScalar
sehButtonPressed = _SehButtonPressed_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 40),
    _SehButtonPressed_Type()
)
sehButtonPressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehButtonPressed.setStatus("mandatory")
_SehUtnSSLPort_Type = Integer32
_SehUtnSSLPort_Object = MibScalar
sehUtnSSLPort = _SehUtnSSLPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 45),
    _SehUtnSSLPort_Type()
)
sehUtnSSLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehUtnSSLPort.setStatus("mandatory")


class _SehUtnCiphert_Type(Integer32):
    """Custom type sehUtnCiphert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rc4MD5", 1),
          ("aes256SHA", 2))
    )


_SehUtnCiphert_Type.__name__ = "Integer32"
_SehUtnCiphert_Object = MibScalar
sehUtnCiphert = _SehUtnCiphert_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 46),
    _SehUtnCiphert_Type()
)
sehUtnCiphert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sehUtnCiphert.setStatus("mandatory")
_SehSwFeatures_Type = Integer32
_SehSwFeatures_Object = MibScalar
sehSwFeatures = _SehSwFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 1, 50),
    _SehSwFeatures_Type()
)
sehSwFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sehSwFeatures.setStatus("mandatory")
_SehPprinter_ObjectIdentity = ObjectIdentity
sehPprinter = _SehPprinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2)
)
_PprtNumber_Type = Integer32
_PprtNumber_Object = MibScalar
pprtNumber = _PprtNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 1),
    _PprtNumber_Type()
)
pprtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtNumber.setStatus("mandatory")
_PprtTable_Object = MibTable
pprtTable = _PprtTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pprtTable.setStatus("mandatory")
_PprtEntry_Object = MibTableRow
pprtEntry = _PprtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1)
)
pprtEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "pprtIndex"),
)
if mibBuilder.loadTexts:
    pprtEntry.setStatus("mandatory")


class _PprtIndex_Type(Integer32):
    """Custom type pprtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PprtIndex_Type.__name__ = "Integer32"
_PprtIndex_Object = MibTableColumn
pprtIndex = _PprtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 1),
    _PprtIndex_Type()
)
pprtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtIndex.setStatus("mandatory")
_PprtError_Type = Integer32
_PprtError_Object = MibTableColumn
pprtError = _PprtError_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 2),
    _PprtError_Type()
)
pprtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtError.setStatus("mandatory")


class _PprtType_Type(Integer32):
    """Custom type pprtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("parallel", 0),
          ("serial", 1),
          ("kyocera", 2),
          ("mio", 3),
          ("epson", 4),
          ("kuio", 5),
          ("eio", 6),
          ("usb", 7))
    )


_PprtType_Type.__name__ = "Integer32"
_PprtType_Object = MibTableColumn
pprtType = _PprtType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 3),
    _PprtType_Type()
)
pprtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtType.setStatus("mandatory")


class _PprtEcp_Type(Integer32):
    """Custom type pprtEcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtEcp_Type.__name__ = "Integer32"
_PprtEcp_Object = MibTableColumn
pprtEcp = _PprtEcp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 4),
    _PprtEcp_Type()
)
pprtEcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtEcp.setStatus("mandatory")


class _PprtPanel_Type(Integer32):
    """Custom type pprtPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtPanel_Type.__name__ = "Integer32"
_PprtPanel_Object = MibTableColumn
pprtPanel = _PprtPanel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 5),
    _PprtPanel_Type()
)
pprtPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtPanel.setStatus("mandatory")


class _PprtMailNotification1_Type(Integer32):
    """Custom type pprtMailNotification1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtMailNotification1_Type.__name__ = "Integer32"
_PprtMailNotification1_Object = MibTableColumn
pprtMailNotification1 = _PprtMailNotification1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 7),
    _PprtMailNotification1_Type()
)
pprtMailNotification1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailNotification1.setStatus("mandatory")


class _PprtMailAddress1_Type(DisplayString):
    """Custom type pprtMailAddress1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PprtMailAddress1_Type.__name__ = "DisplayString"
_PprtMailAddress1_Object = MibTableColumn
pprtMailAddress1 = _PprtMailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 8),
    _PprtMailAddress1_Type()
)
pprtMailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailAddress1.setStatus("mandatory")
_PprtMailServer1_Type = IpAddress
_PprtMailServer1_Object = MibTableColumn
pprtMailServer1 = _PprtMailServer1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 9),
    _PprtMailServer1_Type()
)
pprtMailServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailServer1.setStatus("mandatory")
_PprtMailMask1_Type = Integer32
_PprtMailMask1_Object = MibTableColumn
pprtMailMask1 = _PprtMailMask1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 10),
    _PprtMailMask1_Type()
)
pprtMailMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailMask1.setStatus("mandatory")


class _PprtMailNotification2_Type(Integer32):
    """Custom type pprtMailNotification2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtMailNotification2_Type.__name__ = "Integer32"
_PprtMailNotification2_Object = MibTableColumn
pprtMailNotification2 = _PprtMailNotification2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 11),
    _PprtMailNotification2_Type()
)
pprtMailNotification2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailNotification2.setStatus("mandatory")


class _PprtMailAddress2_Type(DisplayString):
    """Custom type pprtMailAddress2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PprtMailAddress2_Type.__name__ = "DisplayString"
_PprtMailAddress2_Object = MibTableColumn
pprtMailAddress2 = _PprtMailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 12),
    _PprtMailAddress2_Type()
)
pprtMailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailAddress2.setStatus("mandatory")
_PprtMailServer2_Type = IpAddress
_PprtMailServer2_Object = MibTableColumn
pprtMailServer2 = _PprtMailServer2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 13),
    _PprtMailServer2_Type()
)
pprtMailServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailServer2.setStatus("mandatory")
_PprtMailMask2_Type = Integer32
_PprtMailMask2_Object = MibTableColumn
pprtMailMask2 = _PprtMailMask2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 14),
    _PprtMailMask2_Type()
)
pprtMailMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtMailMask2.setStatus("mandatory")


class _PprtModel_Type(DisplayString):
    """Custom type pprtModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PprtModel_Type.__name__ = "DisplayString"
_PprtModel_Object = MibTableColumn
pprtModel = _PprtModel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 15),
    _PprtModel_Type()
)
pprtModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtModel.setStatus("mandatory")


class _PprtManufacturer_Type(DisplayString):
    """Custom type pprtManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PprtManufacturer_Type.__name__ = "DisplayString"
_PprtManufacturer_Object = MibTableColumn
pprtManufacturer = _PprtManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 16),
    _PprtManufacturer_Type()
)
pprtManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtManufacturer.setStatus("mandatory")


class _PprtEmulations_Type(DisplayString):
    """Custom type pprtEmulations based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PprtEmulations_Type.__name__ = "DisplayString"
_PprtEmulations_Object = MibTableColumn
pprtEmulations = _PprtEmulations_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 17),
    _PprtEmulations_Type()
)
pprtEmulations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtEmulations.setStatus("mandatory")


class _PprtFast_Type(Integer32):
    """Custom type pprtFast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtFast_Type.__name__ = "Integer32"
_PprtFast_Object = MibTableColumn
pprtFast = _PprtFast_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 18),
    _PprtFast_Type()
)
pprtFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtFast.setStatus("mandatory")
_PprtBaudrate_Type = Integer32
_PprtBaudrate_Object = MibTableColumn
pprtBaudrate = _PprtBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 19),
    _PprtBaudrate_Type()
)
pprtBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtBaudrate.setStatus("mandatory")


class _PprtParity_Type(DisplayString):
    """Custom type pprtParity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PprtParity_Type.__name__ = "DisplayString"
_PprtParity_Object = MibTableColumn
pprtParity = _PprtParity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 20),
    _PprtParity_Type()
)
pprtParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtParity.setStatus("mandatory")
_PprtDatabits_Type = Integer32
_PprtDatabits_Object = MibTableColumn
pprtDatabits = _PprtDatabits_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 21),
    _PprtDatabits_Type()
)
pprtDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDatabits.setStatus("mandatory")
_PprtStopbits_Type = Integer32
_PprtStopbits_Object = MibTableColumn
pprtStopbits = _PprtStopbits_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 22),
    _PprtStopbits_Type()
)
pprtStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtStopbits.setStatus("mandatory")


class _PprtFlowControl_Type(DisplayString):
    """Custom type pprtFlowControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PprtFlowControl_Type.__name__ = "DisplayString"
_PprtFlowControl_Object = MibTableColumn
pprtFlowControl = _PprtFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 23),
    _PprtFlowControl_Type()
)
pprtFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtFlowControl.setStatus("mandatory")


class _PprtDeviceID_Type(DisplayString):
    """Custom type pprtDeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PprtDeviceID_Type.__name__ = "DisplayString"
_PprtDeviceID_Object = MibTableColumn
pprtDeviceID = _PprtDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 24),
    _PprtDeviceID_Type()
)
pprtDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pprtDeviceID.setStatus("mandatory")


class _PprtDot4_Type(Integer32):
    """Custom type pprtDot4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtDot4_Type.__name__ = "Integer32"
_PprtDot4_Object = MibTableColumn
pprtDot4 = _PprtDot4_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 25),
    _PprtDot4_Type()
)
pprtDot4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDot4.setStatus("mandatory")


class _PprtPortMode_Type(Integer32):
    """Custom type pprtPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirectional", 1),
          ("kmptgdi", 2),
          ("utn", 3))
    )


_PprtPortMode_Type.__name__ = "Integer32"
_PprtPortMode_Object = MibTableColumn
pprtPortMode = _PprtPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 26),
    _PprtPortMode_Type()
)
pprtPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtPortMode.setStatus("mandatory")


class _PprtPjl_Type(Integer32):
    """Custom type pprtPjl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtPjl_Type.__name__ = "Integer32"
_PprtPjl_Object = MibTableColumn
pprtPjl = _PprtPjl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 2, 1, 27),
    _PprtPjl_Type()
)
pprtPjl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtPjl.setStatus("mandatory")


class _PprtDynUpdate_Type(Integer32):
    """Custom type pprtDynUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PprtDynUpdate_Type.__name__ = "Integer32"
_PprtDynUpdate_Object = MibScalar
pprtDynUpdate = _PprtDynUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 10),
    _PprtDynUpdate_Type()
)
pprtDynUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynUpdate.setStatus("mandatory")


class _PprtDynUpdateUrl_Type(DisplayString):
    """Custom type pprtDynUpdateUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PprtDynUpdateUrl_Type.__name__ = "DisplayString"
_PprtDynUpdateUrl_Object = MibScalar
pprtDynUpdateUrl = _PprtDynUpdateUrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 11),
    _PprtDynUpdateUrl_Type()
)
pprtDynUpdateUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynUpdateUrl.setStatus("mandatory")


class _PprtDynUpdateUsr_Type(DisplayString):
    """Custom type pprtDynUpdateUsr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PprtDynUpdateUsr_Type.__name__ = "DisplayString"
_PprtDynUpdateUsr_Object = MibScalar
pprtDynUpdateUsr = _PprtDynUpdateUsr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 12),
    _PprtDynUpdateUsr_Type()
)
pprtDynUpdateUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynUpdateUsr.setStatus("mandatory")


class _PprtDynUpdatePwd_Type(DisplayString):
    """Custom type pprtDynUpdatePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PprtDynUpdatePwd_Type.__name__ = "DisplayString"
_PprtDynUpdatePwd_Object = MibScalar
pprtDynUpdatePwd = _PprtDynUpdatePwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 13),
    _PprtDynUpdatePwd_Type()
)
pprtDynUpdatePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynUpdatePwd.setStatus("mandatory")


class _PprtDynStatusPath_Type(DisplayString):
    """Custom type pprtDynStatusPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PprtDynStatusPath_Type.__name__ = "DisplayString"
_PprtDynStatusPath_Object = MibScalar
pprtDynStatusPath = _PprtDynStatusPath_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 14),
    _PprtDynStatusPath_Type()
)
pprtDynStatusPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynStatusPath.setStatus("mandatory")


class _PprtDynUpdateHour_Type(Integer32):
    """Custom type pprtDynUpdateHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PprtDynUpdateHour_Type.__name__ = "Integer32"
_PprtDynUpdateHour_Object = MibScalar
pprtDynUpdateHour = _PprtDynUpdateHour_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 20),
    _PprtDynUpdateHour_Type()
)
pprtDynUpdateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynUpdateHour.setStatus("mandatory")


class _PprtDynReportMin_Type(Integer32):
    """Custom type pprtDynReportMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44640),
    )


_PprtDynReportMin_Type.__name__ = "Integer32"
_PprtDynReportMin_Object = MibScalar
pprtDynReportMin = _PprtDynReportMin_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 2, 21),
    _PprtDynReportMin_Type()
)
pprtDynReportMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pprtDynReportMin.setStatus("mandatory")
_SehLprinter_ObjectIdentity = ObjectIdentity
sehLprinter = _SehLprinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3)
)
_LprtNumber_Type = Integer32
_LprtNumber_Object = MibScalar
lprtNumber = _LprtNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 1),
    _LprtNumber_Type()
)
lprtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lprtNumber.setStatus("mandatory")
_LprtTable_Object = MibTable
lprtTable = _LprtTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lprtTable.setStatus("mandatory")
_LprtEntry_Object = MibTableRow
lprtEntry = _LprtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1)
)
lprtEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "lprtIndex"),
)
if mibBuilder.loadTexts:
    lprtEntry.setStatus("mandatory")


class _LprtIndex_Type(Integer32):
    """Custom type lprtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_LprtIndex_Type.__name__ = "Integer32"
_LprtIndex_Object = MibTableColumn
lprtIndex = _LprtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 1),
    _LprtIndex_Type()
)
lprtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lprtIndex.setStatus("mandatory")


class _LprtStart_Type(DisplayString):
    """Custom type lprtStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_LprtStart_Type.__name__ = "DisplayString"
_LprtStart_Object = MibTableColumn
lprtStart = _LprtStart_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 2),
    _LprtStart_Type()
)
lprtStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtStart.setStatus("mandatory")


class _LprtEnd_Type(DisplayString):
    """Custom type lprtEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_LprtEnd_Type.__name__ = "DisplayString"
_LprtEnd_Object = MibTableColumn
lprtEnd = _LprtEnd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 3),
    _LprtEnd_Type()
)
lprtEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtEnd.setStatus("mandatory")


class _LprtPhyPrt_Type(Integer32):
    """Custom type lprtPhyPrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4))
    )


_LprtPhyPrt_Type.__name__ = "Integer32"
_LprtPhyPrt_Object = MibTableColumn
lprtPhyPrt = _LprtPhyPrt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 4),
    _LprtPhyPrt_Type()
)
lprtPhyPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtPhyPrt.setStatus("mandatory")
_LprtTCPPort_Type = Integer32
_LprtTCPPort_Object = MibTableColumn
lprtTCPPort = _LprtTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 5),
    _LprtTCPPort_Type()
)
lprtTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtTCPPort.setStatus("mandatory")


class _LprtCRLF_Type(Integer32):
    """Custom type lprtCRLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtCRLF_Type.__name__ = "Integer32"
_LprtCRLF_Object = MibTableColumn
lprtCRLF = _LprtCRLF_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 6),
    _LprtCRLF_Type()
)
lprtCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtCRLF.setStatus("mandatory")


class _LprtHexDp_Type(Integer32):
    """Custom type lprtHexDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtHexDp_Type.__name__ = "Integer32"
_LprtHexDp_Object = MibTableColumn
lprtHexDp = _LprtHexDp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 7),
    _LprtHexDp_Type()
)
lprtHexDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtHexDp.setStatus("mandatory")


class _LprtBp_Type(Integer32):
    """Custom type lprtBp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtBp_Type.__name__ = "Integer32"
_LprtBp_Object = MibTableColumn
lprtBp = _LprtBp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 8),
    _LprtBp_Type()
)
lprtBp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtBp.setStatus("mandatory")


class _LprtAsPs_Type(Integer32):
    """Custom type lprtAsPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtAsPs_Type.__name__ = "Integer32"
_LprtAsPs_Object = MibTableColumn
lprtAsPs = _LprtAsPs_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 9),
    _LprtAsPs_Type()
)
lprtAsPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtAsPs.setStatus("mandatory")


class _LprtMode_Type(Integer32):
    """Custom type lprtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("postscript", 1))
    )


_LprtMode_Type.__name__ = "Integer32"
_LprtMode_Object = MibTableColumn
lprtMode = _LprtMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 10),
    _LprtMode_Type()
)
lprtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtMode.setStatus("mandatory")


class _LprtRsoSpool_Type(Integer32):
    """Custom type lprtRsoSpool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtRsoSpool_Type.__name__ = "Integer32"
_LprtRsoSpool_Object = MibTableColumn
lprtRsoSpool = _LprtRsoSpool_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 11),
    _LprtRsoSpool_Type()
)
lprtRsoSpool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtRsoSpool.setStatus("mandatory")


class _LprtSearch_Type(DisplayString):
    """Custom type lprtSearch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_LprtSearch_Type.__name__ = "DisplayString"
_LprtSearch_Object = MibTableColumn
lprtSearch = _LprtSearch_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 13),
    _LprtSearch_Type()
)
lprtSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtSearch.setStatus("mandatory")


class _LprtReplace_Type(DisplayString):
    """Custom type lprtReplace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_LprtReplace_Type.__name__ = "DisplayString"
_LprtReplace_Object = MibTableColumn
lprtReplace = _LprtReplace_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 14),
    _LprtReplace_Type()
)
lprtReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtReplace.setStatus("mandatory")


class _LprtBinaryPS_Type(Integer32):
    """Custom type lprtBinaryPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LprtBinaryPS_Type.__name__ = "Integer32"
_LprtBinaryPS_Object = MibTableColumn
lprtBinaryPS = _LprtBinaryPS_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 3, 2, 1, 15),
    _LprtBinaryPS_Type()
)
lprtBinaryPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lprtBinaryPS.setStatus("mandatory")
_SehIp_ObjectIdentity = ObjectIdentity
sehIp = _SehIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4)
)
_IpIpAddr_Type = IpAddress
_IpIpAddr_Object = MibScalar
ipIpAddr = _IpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 1),
    _IpIpAddr_Type()
)
ipIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIpAddr.setStatus("mandatory")
_IpNetMask_Type = IpAddress
_IpNetMask_Object = MibScalar
ipNetMask = _IpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 2),
    _IpNetMask_Type()
)
ipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetMask.setStatus("mandatory")
_IpDefGate_Type = IpAddress
_IpDefGate_Object = MibScalar
ipDefGate = _IpDefGate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 3),
    _IpDefGate_Type()
)
ipDefGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefGate.setStatus("mandatory")


class _IpBOOTP_Type(Integer32):
    """Custom type ipBOOTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpBOOTP_Type.__name__ = "Integer32"
_IpBOOTP_Object = MibScalar
ipBOOTP = _IpBOOTP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 4),
    _IpBOOTP_Type()
)
ipBOOTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBOOTP.setStatus("mandatory")


class _IpRARP_Type(Integer32):
    """Custom type ipRARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpRARP_Type.__name__ = "Integer32"
_IpRARP_Object = MibScalar
ipRARP = _IpRARP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 5),
    _IpRARP_Type()
)
ipRARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRARP.setStatus("mandatory")


class _IpAutoconf_Type(Integer32):
    """Custom type ipAutoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpAutoconf_Type.__name__ = "Integer32"
_IpAutoconf_Object = MibScalar
ipAutoconf = _IpAutoconf_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 6),
    _IpAutoconf_Type()
)
ipAutoconf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAutoconf.setStatus("mandatory")


class _IpDHCP_Type(Integer32):
    """Custom type ipDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpDHCP_Type.__name__ = "Integer32"
_IpDHCP_Object = MibScalar
ipDHCP = _IpDHCP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 7),
    _IpDHCP_Type()
)
ipDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDHCP.setStatus("mandatory")


class _IpZeroConf_Type(Integer32):
    """Custom type ipZeroConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpZeroConf_Type.__name__ = "Integer32"
_IpZeroConf_Object = MibScalar
ipZeroConf = _IpZeroConf_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 8),
    _IpZeroConf_Type()
)
ipZeroConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipZeroConf.setStatus("mandatory")


class _IpSetBy_Type(Integer32):
    """Custom type ipSetBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("snmp", 1),
          ("bootp", 2),
          ("dhcp", 3),
          ("arpping", 4),
          ("panel", 5),
          ("zeroconfig", 6),
          ("parameterfile", 7),
          ("rarp", 8),
          ("slp", 9),
          ("epsonenpc", 10),
          ("appleadm", 11),
          ("http", 12))
    )


_IpSetBy_Type.__name__ = "Integer32"
_IpSetBy_Object = MibScalar
ipSetBy = _IpSetBy_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 9),
    _IpSetBy_Type()
)
ipSetBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSetBy.setStatus("mandatory")
_IpWinsPrimarySrv_Type = IpAddress
_IpWinsPrimarySrv_Object = MibScalar
ipWinsPrimarySrv = _IpWinsPrimarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 10),
    _IpWinsPrimarySrv_Type()
)
ipWinsPrimarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipWinsPrimarySrv.setStatus("mandatory")
_IpWinsSecondarySrv_Type = IpAddress
_IpWinsSecondarySrv_Object = MibScalar
ipWinsSecondarySrv = _IpWinsSecondarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 11),
    _IpWinsSecondarySrv_Type()
)
ipWinsSecondarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipWinsSecondarySrv.setStatus("mandatory")


class _IpTCP_Type(Integer32):
    """Custom type ipTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpTCP_Type.__name__ = "Integer32"
_IpTCP_Object = MibScalar
ipTCP = _IpTCP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 12),
    _IpTCP_Type()
)
ipTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTCP.setStatus("mandatory")


class _IpDNS_Type(Integer32):
    """Custom type ipDNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpDNS_Type.__name__ = "Integer32"
_IpDNS_Object = MibScalar
ipDNS = _IpDNS_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 13),
    _IpDNS_Type()
)
ipDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDNS.setStatus("mandatory")


class _IpDomainName_Type(DisplayString):
    """Custom type ipDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_IpDomainName_Type.__name__ = "DisplayString"
_IpDomainName_Object = MibScalar
ipDomainName = _IpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 14),
    _IpDomainName_Type()
)
ipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDomainName.setStatus("mandatory")
_IpDnsPrimarySrv_Type = IpAddress
_IpDnsPrimarySrv_Object = MibScalar
ipDnsPrimarySrv = _IpDnsPrimarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 15),
    _IpDnsPrimarySrv_Type()
)
ipDnsPrimarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsPrimarySrv.setStatus("mandatory")
_IpDnsSecondarySrv_Type = IpAddress
_IpDnsSecondarySrv_Object = MibScalar
ipDnsSecondarySrv = _IpDnsSecondarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 16),
    _IpDnsSecondarySrv_Type()
)
ipDnsSecondarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsSecondarySrv.setStatus("mandatory")
_IpSenderNumber_Type = Integer32
_IpSenderNumber_Object = MibScalar
ipSenderNumber = _IpSenderNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 17),
    _IpSenderNumber_Type()
)
ipSenderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSenderNumber.setStatus("mandatory")
_IpSenderTable_Object = MibTable
ipSenderTable = _IpSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 18)
)
if mibBuilder.loadTexts:
    ipSenderTable.setStatus("mandatory")
_IpSenderEntry_Object = MibTableRow
ipSenderEntry = _IpSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 18, 1)
)
ipSenderEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipSenderIndex"),
)
if mibBuilder.loadTexts:
    ipSenderEntry.setStatus("mandatory")


class _IpSenderIndex_Type(Integer32):
    """Custom type ipSenderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpSenderIndex_Type.__name__ = "Integer32"
_IpSenderIndex_Object = MibTableColumn
ipSenderIndex = _IpSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 18, 1, 1),
    _IpSenderIndex_Type()
)
ipSenderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSenderIndex.setStatus("mandatory")


class _IpSender_Type(DisplayString):
    """Custom type ipSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_IpSender_Type.__name__ = "DisplayString"
_IpSender_Object = MibTableColumn
ipSender = _IpSender_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 18, 1, 2),
    _IpSender_Type()
)
ipSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSender.setStatus("mandatory")


class _IpAutoGate_Type(Integer32):
    """Custom type ipAutoGate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpAutoGate_Type.__name__ = "Integer32"
_IpAutoGate_Object = MibScalar
ipAutoGate = _IpAutoGate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 19),
    _IpAutoGate_Type()
)
ipAutoGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAutoGate.setStatus("mandatory")


class _IpZeroConfig_Type(Integer32):
    """Custom type ipZeroConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpZeroConfig_Type.__name__ = "Integer32"
_IpZeroConfig_Object = MibScalar
ipZeroConfig = _IpZeroConfig_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 20),
    _IpZeroConfig_Type()
)
ipZeroConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipZeroConfig.setStatus("mandatory")


class _IpHTTP_Type(Integer32):
    """Custom type ipHTTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpHTTP_Type.__name__ = "Integer32"
_IpHTTP_Object = MibScalar
ipHTTP = _IpHTTP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 21),
    _IpHTTP_Type()
)
ipHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHTTP.setStatus("mandatory")


class _IpIPv6_Type(Integer32):
    """Custom type ipIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpIPv6_Type.__name__ = "Integer32"
_IpIPv6_Object = MibScalar
ipIPv6 = _IpIPv6_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 22),
    _IpIPv6_Type()
)
ipIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPv6.setStatus("mandatory")


class _IpIPv6Addr_Type(DisplayString):
    """Custom type ipIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_IpIPv6Addr_Type.__name__ = "DisplayString"
_IpIPv6Addr_Object = MibScalar
ipIPv6Addr = _IpIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 23),
    _IpIPv6Addr_Type()
)
ipIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPv6Addr.setStatus("mandatory")


class _IpIPv6Plen_Type(Integer32):
    """Custom type ipIPv6Plen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpIPv6Plen_Type.__name__ = "Integer32"
_IpIPv6Plen_Object = MibScalar
ipIPv6Plen = _IpIPv6Plen_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 24),
    _IpIPv6Plen_Type()
)
ipIPv6Plen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPv6Plen.setStatus("mandatory")


class _IpIPv6Gate_Type(DisplayString):
    """Custom type ipIPv6Gate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_IpIPv6Gate_Type.__name__ = "DisplayString"
_IpIPv6Gate_Object = MibScalar
ipIPv6Gate = _IpIPv6Gate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 25),
    _IpIPv6Gate_Type()
)
ipIPv6Gate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPv6Gate.setStatus("mandatory")


class _IpIPv6Auto_Type(Integer32):
    """Custom type ipIPv6Auto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpIPv6Auto_Type.__name__ = "Integer32"
_IpIPv6Auto_Object = MibScalar
ipIPv6Auto = _IpIPv6Auto_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 26),
    _IpIPv6Auto_Type()
)
ipIPv6Auto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIPv6Auto.setStatus("mandatory")


class _IpFTP_Type(Integer32):
    """Custom type ipFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpFTP_Type.__name__ = "Integer32"
_IpFTP_Object = MibScalar
ipFTP = _IpFTP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 4, 30),
    _IpFTP_Type()
)
ipFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFTP.setStatus("mandatory")
_SehNovell_ObjectIdentity = ObjectIdentity
sehNovell = _SehNovell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5)
)


class _NwName_Type(DisplayString):
    """Custom type nwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_NwName_Type.__name__ = "DisplayString"
_NwName_Object = MibScalar
nwName = _NwName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 1),
    _NwName_Type()
)
nwName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwName.setStatus("mandatory")


class _NwNDS_Type(Integer32):
    """Custom type nwNDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwNDS_Type.__name__ = "Integer32"
_NwNDS_Object = MibScalar
nwNDS = _NwNDS_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 2),
    _NwNDS_Type()
)
nwNDS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDS.setStatus("mandatory")


class _NwBindery_Type(Integer32):
    """Custom type nwBindery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwBindery_Type.__name__ = "Integer32"
_NwBindery_Object = MibScalar
nwBindery = _NwBindery_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 3),
    _NwBindery_Type()
)
nwBindery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwBindery.setStatus("mandatory")


class _Nw8022_Type(Integer32):
    """Custom type nw8022 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Nw8022_Type.__name__ = "Integer32"
_Nw8022_Object = MibScalar
nw8022 = _Nw8022_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 4),
    _Nw8022_Type()
)
nw8022.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nw8022.setStatus("mandatory")


class _Nw8023_Type(Integer32):
    """Custom type nw8023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Nw8023_Type.__name__ = "Integer32"
_Nw8023_Object = MibScalar
nw8023 = _Nw8023_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 5),
    _Nw8023_Type()
)
nw8023.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nw8023.setStatus("mandatory")


class _NwEthII_Type(Integer32):
    """Custom type nwEthII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwEthII_Type.__name__ = "Integer32"
_NwEthII_Object = MibScalar
nwEthII = _NwEthII_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 6),
    _NwEthII_Type()
)
nwEthII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwEthII.setStatus("mandatory")


class _NwSNAP_Type(Integer32):
    """Custom type nwSNAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwSNAP_Type.__name__ = "Integer32"
_NwSNAP_Object = MibScalar
nwSNAP = _NwSNAP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 7),
    _NwSNAP_Type()
)
nwSNAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSNAP.setStatus("mandatory")


class _NwUpdate_Type(Integer32):
    """Custom type nwUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwUpdate_Type.__name__ = "Integer32"
_NwUpdate_Object = MibScalar
nwUpdate = _NwUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 8),
    _NwUpdate_Type()
)
nwUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwUpdate.setStatus("mandatory")
_NwUpdTime_Type = Integer32
_NwUpdTime_Object = MibScalar
nwUpdTime = _NwUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 9),
    _NwUpdTime_Type()
)
nwUpdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwUpdTime.setStatus("mandatory")
_NwPollTime_Type = Integer32
_NwPollTime_Object = MibScalar
nwPollTime = _NwPollTime_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 10),
    _NwPollTime_Type()
)
nwPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPollTime.setStatus("mandatory")


class _NwServer1_Type(DisplayString):
    """Custom type nwServer1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_NwServer1_Type.__name__ = "DisplayString"
_NwServer1_Object = MibScalar
nwServer1 = _NwServer1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 11),
    _NwServer1_Type()
)
nwServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwServer1.setStatus("mandatory")


class _NwServer2_Type(DisplayString):
    """Custom type nwServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_NwServer2_Type.__name__ = "DisplayString"
_NwServer2_Object = MibScalar
nwServer2 = _NwServer2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 12),
    _NwServer2_Type()
)
nwServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwServer2.setStatus("mandatory")


class _NwServer3_Type(DisplayString):
    """Custom type nwServer3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_NwServer3_Type.__name__ = "DisplayString"
_NwServer3_Object = MibScalar
nwServer3 = _NwServer3_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 13),
    _NwServer3_Type()
)
nwServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwServer3.setStatus("mandatory")


class _NwServer4_Type(DisplayString):
    """Custom type nwServer4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_NwServer4_Type.__name__ = "DisplayString"
_NwServer4_Object = MibScalar
nwServer4 = _NwServer4_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 14),
    _NwServer4_Type()
)
nwServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwServer4.setStatus("mandatory")


class _NwNDSCommonName_Type(DisplayString):
    """Custom type nwNDSCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_NwNDSCommonName_Type.__name__ = "DisplayString"
_NwNDSCommonName_Object = MibScalar
nwNDSCommonName = _NwNDSCommonName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 15),
    _NwNDSCommonName_Type()
)
nwNDSCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNDSCommonName.setStatus("mandatory")


class _NwNDSTreeFound_Type(DisplayString):
    """Custom type nwNDSTreeFound based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NwNDSTreeFound_Type.__name__ = "DisplayString"
_NwNDSTreeFound_Object = MibScalar
nwNDSTreeFound = _NwNDSTreeFound_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 16),
    _NwNDSTreeFound_Type()
)
nwNDSTreeFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNDSTreeFound.setStatus("mandatory")
_NwNDSFound_Type = Integer32
_NwNDSFound_Object = MibScalar
nwNDSFound = _NwNDSFound_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 17),
    _NwNDSFound_Type()
)
nwNDSFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNDSFound.setStatus("mandatory")
_NwConnNumber_Type = Integer32
_NwConnNumber_Object = MibScalar
nwConnNumber = _NwConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 18),
    _NwConnNumber_Type()
)
nwConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnNumber.setStatus("mandatory")
_NwConnTable_Object = MibTable
nwConnTable = _NwConnTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19)
)
if mibBuilder.loadTexts:
    nwConnTable.setStatus("mandatory")
_NwConnEntry_Object = MibTableRow
nwConnEntry = _NwConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1)
)
nwConnEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "nwConnIndex"),
)
if mibBuilder.loadTexts:
    nwConnEntry.setStatus("mandatory")


class _NwConnIndex_Type(Integer32):
    """Custom type nwConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NwConnIndex_Type.__name__ = "Integer32"
_NwConnIndex_Object = MibTableColumn
nwConnIndex = _NwConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 1),
    _NwConnIndex_Type()
)
nwConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnIndex.setStatus("mandatory")


class _NwConnServer_Type(DisplayString):
    """Custom type nwConnServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_NwConnServer_Type.__name__ = "DisplayString"
_NwConnServer_Object = MibTableColumn
nwConnServer = _NwConnServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 2),
    _NwConnServer_Type()
)
nwConnServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnServer.setStatus("mandatory")


class _NwConnState_Type(Integer32):
    """Custom type nwConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              17,
              32,
              48,
              64,
              160)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 0),
          ("binderyLogin", 2),
          ("binderyLoginSetPwd", 3),
          ("attached", 17),
          ("ndsLogin", 32),
          ("ndsAuthenticated", 48),
          ("ndsLocked", 64),
          ("ndsLoginSetPwd", 160))
    )


_NwConnState_Type.__name__ = "Integer32"
_NwConnState_Object = MibTableColumn
nwConnState = _NwConnState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 3),
    _NwConnState_Type()
)
nwConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnState.setStatus("mandatory")
_NwConnLastError_Type = Integer32
_NwConnLastError_Object = MibTableColumn
nwConnLastError = _NwConnLastError_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 4),
    _NwConnLastError_Type()
)
nwConnLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnLastError.setStatus("mandatory")


class _NwConnServerState_Type(Integer32):
    """Custom type nwConnServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("sleep", 1),
          ("busy", 2))
    )


_NwConnServerState_Type.__name__ = "Integer32"
_NwConnServerState_Object = MibTableColumn
nwConnServerState = _NwConnServerState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 5),
    _NwConnServerState_Type()
)
nwConnServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnServerState.setStatus("mandatory")


class _NwConnHeader_Type(Integer32):
    """Custom type nwConnHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802-3", 2),
          ("ieee802-2", 4),
          ("snap", 8),
          ("ieee802-5", 16))
    )


_NwConnHeader_Type.__name__ = "Integer32"
_NwConnHeader_Object = MibTableColumn
nwConnHeader = _NwConnHeader_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 6),
    _NwConnHeader_Type()
)
nwConnHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnHeader.setStatus("mandatory")
_NwConnNet_Type = Integer32
_NwConnNet_Object = MibTableColumn
nwConnNet = _NwConnNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 19, 1, 7),
    _NwConnNet_Type()
)
nwConnNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnNet.setStatus("mandatory")
_NwQueueNumber_Type = Integer32
_NwQueueNumber_Object = MibScalar
nwQueueNumber = _NwQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 20),
    _NwQueueNumber_Type()
)
nwQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueNumber.setStatus("mandatory")
_NwQueueTable_Object = MibTable
nwQueueTable = _NwQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21)
)
if mibBuilder.loadTexts:
    nwQueueTable.setStatus("mandatory")
_NwQueueEntry_Object = MibTableRow
nwQueueEntry = _NwQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1)
)
nwQueueEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "nwQueueIndex"),
)
if mibBuilder.loadTexts:
    nwQueueEntry.setStatus("mandatory")


class _NwQueueIndex_Type(Integer32):
    """Custom type nwQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NwQueueIndex_Type.__name__ = "Integer32"
_NwQueueIndex_Object = MibTableColumn
nwQueueIndex = _NwQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1, 1),
    _NwQueueIndex_Type()
)
nwQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueIndex.setStatus("mandatory")


class _NwQueueName_Type(DisplayString):
    """Custom type nwQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_NwQueueName_Type.__name__ = "DisplayString"
_NwQueueName_Object = MibTableColumn
nwQueueName = _NwQueueName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1, 2),
    _NwQueueName_Type()
)
nwQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueName.setStatus("mandatory")
_NwQueueConnId_Type = Integer32
_NwQueueConnId_Object = MibTableColumn
nwQueueConnId = _NwQueueConnId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1, 3),
    _NwQueueConnId_Type()
)
nwQueueConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueConnId.setStatus("mandatory")


class _NwQueuePort_Type(Integer32):
    """Custom type nwQueuePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("lp1", 1),
          ("lp2", 2),
          ("lp3", 4),
          ("lp4", 8),
          ("lp5", 16),
          ("lp6", 32),
          ("lp7", 64),
          ("lp8", 128))
    )


_NwQueuePort_Type.__name__ = "Integer32"
_NwQueuePort_Object = MibTableColumn
nwQueuePort = _NwQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1, 4),
    _NwQueuePort_Type()
)
nwQueuePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueuePort.setStatus("mandatory")


class _NwQueueState_Type(Integer32):
    """Custom type nwQueueState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              16,
              32,
              48,
              133,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("lost", 5),
          ("attachError", 16),
          ("printingError", 32),
          ("pollingError", 48),
          ("attached", 133),
          ("printing", 144),
          ("printingAbort", 160))
    )


_NwQueueState_Type.__name__ = "Integer32"
_NwQueueState_Object = MibTableColumn
nwQueueState = _NwQueueState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 21, 1, 5),
    _NwQueueState_Type()
)
nwQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueState.setStatus("mandatory")


class _NwRprinterHeader_Type(Integer32):
    """Custom type nwRprinterHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802-3", 2),
          ("ieee802-2", 4),
          ("snap", 8),
          ("ieee802-5", 16))
    )


_NwRprinterHeader_Type.__name__ = "Integer32"
_NwRprinterHeader_Object = MibScalar
nwRprinterHeader = _NwRprinterHeader_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 22),
    _NwRprinterHeader_Type()
)
nwRprinterHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRprinterHeader.setStatus("mandatory")


class _NwNDSPwd_Type(Integer32):
    """Custom type nwNDSPwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwNDSPwd_Type.__name__ = "Integer32"
_NwNDSPwd_Object = MibScalar
nwNDSPwd = _NwNDSPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 23),
    _NwNDSPwd_Type()
)
nwNDSPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPwd.setStatus("mandatory")


class _NwBinderyPwd_Type(Integer32):
    """Custom type nwBinderyPwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwBinderyPwd_Type.__name__ = "Integer32"
_NwBinderyPwd_Object = MibScalar
nwBinderyPwd = _NwBinderyPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 24),
    _NwBinderyPwd_Type()
)
nwBinderyPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwBinderyPwd.setStatus("mandatory")


class _Nw8025_Type(Integer32):
    """Custom type nw8025 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Nw8025_Type.__name__ = "Integer32"
_Nw8025_Object = MibScalar
nw8025 = _Nw8025_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 25),
    _Nw8025_Type()
)
nw8025.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nw8025.setStatus("mandatory")


class _NwPserver_Type(Integer32):
    """Custom type nwPserver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwPserver_Type.__name__ = "Integer32"
_NwPserver_Object = MibScalar
nwPserver = _NwPserver_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 26),
    _NwPserver_Type()
)
nwPserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPserver.setStatus("mandatory")


class _NwRprinter_Type(Integer32):
    """Custom type nwRprinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwRprinter_Type.__name__ = "Integer32"
_NwRprinter_Object = MibScalar
nwRprinter = _NwRprinter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 27),
    _NwRprinter_Type()
)
nwRprinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwRprinter.setStatus("mandatory")


class _NwAdvPserver_Type(DisplayString):
    """Custom type nwAdvPserver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_NwAdvPserver_Type.__name__ = "DisplayString"
_NwAdvPserver_Object = MibScalar
nwAdvPserver = _NwAdvPserver_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 28),
    _NwAdvPserver_Type()
)
nwAdvPserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwAdvPserver.setStatus("mandatory")


class _NwLogPrinter_Type(Integer32):
    """Custom type nwLogPrinter based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("lp1", 1),
          ("lp2", 2),
          ("lp3", 3),
          ("lp4", 4),
          ("lp5", 5),
          ("lp6", 6),
          ("lp7", 7),
          ("lp8", 8))
    )


_NwLogPrinter_Type.__name__ = "Integer32"
_NwLogPrinter_Object = MibScalar
nwLogPrinter = _NwLogPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 29),
    _NwLogPrinter_Type()
)
nwLogPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwLogPrinter.setStatus("mandatory")


class _NwSPXConnState_Type(Integer32):
    """Custom type nwSPXConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("preopen", 1),
          ("open", 2),
          ("listen", 3))
    )


_NwSPXConnState_Type.__name__ = "Integer32"
_NwSPXConnState_Object = MibScalar
nwSPXConnState = _NwSPXConnState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 30),
    _NwSPXConnState_Type()
)
nwSPXConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSPXConnState.setStatus("mandatory")


class _NwNDSTree_Type(DisplayString):
    """Custom type nwNDSTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NwNDSTree_Type.__name__ = "DisplayString"
_NwNDSTree_Object = MibScalar
nwNDSTree = _NwNDSTree_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 31),
    _NwNDSTree_Type()
)
nwNDSTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSTree.setStatus("mandatory")


class _NwIPX_Type(Integer32):
    """Custom type nwIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NwIPX_Type.__name__ = "Integer32"
_NwIPX_Object = MibScalar
nwIPX = _NwIPX_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 32),
    _NwIPX_Type()
)
nwIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIPX.setStatus("mandatory")
_NwMyNet_Type = Integer32
_NwMyNet_Object = MibScalar
nwMyNet = _NwMyNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 33),
    _NwMyNet_Type()
)
nwMyNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMyNet.setStatus("mandatory")


class _NwPureIp_Type(Integer32):
    """Custom type nwPureIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("udp", 1),
          ("tcp", 2))
    )


_NwPureIp_Type.__name__ = "Integer32"
_NwPureIp_Object = MibScalar
nwPureIp = _NwPureIp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 5, 34),
    _NwPureIp_Type()
)
nwPureIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPureIp.setStatus("mandatory")
_SehApple_ObjectIdentity = ObjectIdentity
sehApple = _SehApple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6)
)


class _AppleTalk_Type(Integer32):
    """Custom type appleTalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AppleTalk_Type.__name__ = "Integer32"
_AppleTalk_Object = MibScalar
appleTalk = _AppleTalk_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 1),
    _AppleTalk_Type()
)
appleTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleTalk.setStatus("mandatory")


class _AppleName_Type(DisplayString):
    """Custom type appleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppleName_Type.__name__ = "DisplayString"
_AppleName_Object = MibScalar
appleName = _AppleName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 2),
    _AppleName_Type()
)
appleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleName.setStatus("mandatory")


class _AppleZone_Type(DisplayString):
    """Custom type appleZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppleZone_Type.__name__ = "DisplayString"
_AppleZone_Object = MibScalar
appleZone = _AppleZone_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 3),
    _AppleZone_Type()
)
appleZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleZone.setStatus("mandatory")


class _ApplePrinter_Type(DisplayString):
    """Custom type applePrinter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApplePrinter_Type.__name__ = "DisplayString"
_ApplePrinter_Object = MibScalar
applePrinter = _ApplePrinter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 4),
    _ApplePrinter_Type()
)
applePrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePrinter.setStatus("mandatory")


class _AppleCurrentName_Type(DisplayString):
    """Custom type appleCurrentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppleCurrentName_Type.__name__ = "DisplayString"
_AppleCurrentName_Object = MibScalar
appleCurrentName = _AppleCurrentName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 5),
    _AppleCurrentName_Type()
)
appleCurrentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleCurrentName.setStatus("mandatory")


class _AppleCurrentZone_Type(DisplayString):
    """Custom type appleCurrentZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppleCurrentZone_Type.__name__ = "DisplayString"
_AppleCurrentZone_Object = MibScalar
appleCurrentZone = _AppleCurrentZone_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 6),
    _AppleCurrentZone_Type()
)
appleCurrentZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleCurrentZone.setStatus("mandatory")


class _AppleEntity_Type(DisplayString):
    """Custom type appleEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_AppleEntity_Type.__name__ = "DisplayString"
_AppleEntity_Object = MibScalar
appleEntity = _AppleEntity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 7),
    _AppleEntity_Type()
)
appleEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleEntity.setStatus("mandatory")
_AppleNet_Type = Integer32
_AppleNet_Object = MibScalar
appleNet = _AppleNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 8),
    _AppleNet_Type()
)
appleNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNet.setStatus("mandatory")
_AppleNode_Type = Integer32
_AppleNode_Object = MibScalar
appleNode = _AppleNode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 9),
    _AppleNode_Type()
)
appleNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNode.setStatus("mandatory")
_AppleRouterNet_Type = Integer32
_AppleRouterNet_Object = MibScalar
appleRouterNet = _AppleRouterNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 10),
    _AppleRouterNet_Type()
)
appleRouterNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleRouterNet.setStatus("mandatory")
_AppleRouterNode_Type = Integer32
_AppleRouterNode_Object = MibScalar
appleRouterNode = _AppleRouterNode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 11),
    _AppleRouterNode_Type()
)
appleRouterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleRouterNode.setStatus("mandatory")


class _AppleBidirectional_Type(Integer32):
    """Custom type appleBidirectional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AppleBidirectional_Type.__name__ = "Integer32"
_AppleBidirectional_Object = MibScalar
appleBidirectional = _AppleBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 12),
    _AppleBidirectional_Type()
)
appleBidirectional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleBidirectional.setStatus("mandatory")


class _AppleBinary_Type(Integer32):
    """Custom type appleBinary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("bcp1", 2),
          ("bcp2", 4),
          ("tbcp", 8))
    )


_AppleBinary_Type.__name__ = "Integer32"
_AppleBinary_Object = MibScalar
appleBinary = _AppleBinary_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 13),
    _AppleBinary_Type()
)
appleBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleBinary.setStatus("mandatory")


class _AppleRendezvous_Type(Integer32):
    """Custom type appleRendezvous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AppleRendezvous_Type.__name__ = "Integer32"
_AppleRendezvous_Object = MibScalar
appleRendezvous = _AppleRendezvous_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 14),
    _AppleRendezvous_Type()
)
appleRendezvous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleRendezvous.setStatus("mandatory")
_ApplePortNumber_Type = Integer32
_ApplePortNumber_Object = MibScalar
applePortNumber = _ApplePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 20),
    _ApplePortNumber_Type()
)
applePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortNumber.setStatus("mandatory")
_ApplePortTable_Object = MibTable
applePortTable = _ApplePortTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21)
)
if mibBuilder.loadTexts:
    applePortTable.setStatus("mandatory")
_ApplePortEntry_Object = MibTableRow
applePortEntry = _ApplePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1)
)
applePortEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "applePortIndex"),
)
if mibBuilder.loadTexts:
    applePortEntry.setStatus("mandatory")


class _ApplePortIndex_Type(Integer32):
    """Custom type applePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApplePortIndex_Type.__name__ = "Integer32"
_ApplePortIndex_Object = MibTableColumn
applePortIndex = _ApplePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 1),
    _ApplePortIndex_Type()
)
applePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortIndex.setStatus("mandatory")


class _ApplePortBidirectional_Type(Integer32):
    """Custom type applePortBidirectional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApplePortBidirectional_Type.__name__ = "Integer32"
_ApplePortBidirectional_Object = MibTableColumn
applePortBidirectional = _ApplePortBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 2),
    _ApplePortBidirectional_Type()
)
applePortBidirectional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortBidirectional.setStatus("mandatory")


class _ApplePortPrinter_Type(DisplayString):
    """Custom type applePortPrinter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ApplePortPrinter_Type.__name__ = "DisplayString"
_ApplePortPrinter_Object = MibTableColumn
applePortPrinter = _ApplePortPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 3),
    _ApplePortPrinter_Type()
)
applePortPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortPrinter.setStatus("mandatory")


class _ApplePortEntity_Type(DisplayString):
    """Custom type applePortEntity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ApplePortEntity_Type.__name__ = "DisplayString"
_ApplePortEntity_Object = MibTableColumn
applePortEntity = _ApplePortEntity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 4),
    _ApplePortEntity_Type()
)
applePortEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortEntity.setStatus("mandatory")


class _ApplePortBinaryEncoding_Type(Integer32):
    """Custom type applePortBinaryEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("bcp1", 2),
          ("bcp2", 4),
          ("tbcp", 8))
    )


_ApplePortBinaryEncoding_Type.__name__ = "Integer32"
_ApplePortBinaryEncoding_Object = MibTableColumn
applePortBinaryEncoding = _ApplePortBinaryEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 5),
    _ApplePortBinaryEncoding_Type()
)
applePortBinaryEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortBinaryEncoding.setStatus("mandatory")


class _ApplePortCurrentName_Type(DisplayString):
    """Custom type applePortCurrentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApplePortCurrentName_Type.__name__ = "DisplayString"
_ApplePortCurrentName_Object = MibTableColumn
applePortCurrentName = _ApplePortCurrentName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 6),
    _ApplePortCurrentName_Type()
)
applePortCurrentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortCurrentName.setStatus("mandatory")


class _AppleRendezvousPortName_Type(DisplayString):
    """Custom type appleRendezvousPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AppleRendezvousPortName_Type.__name__ = "DisplayString"
_AppleRendezvousPortName_Object = MibTableColumn
appleRendezvousPortName = _AppleRendezvousPortName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 10),
    _AppleRendezvousPortName_Type()
)
appleRendezvousPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleRendezvousPortName.setStatus("mandatory")


class _AppleRendezvousCurrentPortName_Type(DisplayString):
    """Custom type appleRendezvousCurrentPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AppleRendezvousCurrentPortName_Type.__name__ = "DisplayString"
_AppleRendezvousCurrentPortName_Object = MibTableColumn
appleRendezvousCurrentPortName = _AppleRendezvousCurrentPortName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 6, 21, 1, 11),
    _AppleRendezvousCurrentPortName_Type()
)
appleRendezvousCurrentPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleRendezvousCurrentPortName.setStatus("mandatory")
_SehSnmp_ObjectIdentity = ObjectIdentity
sehSnmp = _SehSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7)
)
_SnmpIpAddr1_Type = IpAddress
_SnmpIpAddr1_Object = MibScalar
snmpIpAddr1 = _SnmpIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 1),
    _SnmpIpAddr1_Type()
)
snmpIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpAddr1.setStatus("mandatory")
_SnmpIpAddr2_Type = IpAddress
_SnmpIpAddr2_Object = MibScalar
snmpIpAddr2 = _SnmpIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 2),
    _SnmpIpAddr2_Type()
)
snmpIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpAddr2.setStatus("mandatory")


class _SnmpIpxAddr1_Type(PhysAddress):
    """Custom type snmpIpxAddr1 based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SnmpIpxAddr1_Type.__name__ = "PhysAddress"
_SnmpIpxAddr1_Object = MibScalar
snmpIpxAddr1 = _SnmpIpxAddr1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 3),
    _SnmpIpxAddr1_Type()
)
snmpIpxAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpxAddr1.setStatus("mandatory")


class _SnmpIpxAddr2_Type(PhysAddress):
    """Custom type snmpIpxAddr2 based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SnmpIpxAddr2_Type.__name__ = "PhysAddress"
_SnmpIpxAddr2_Object = MibScalar
snmpIpxAddr2 = _SnmpIpxAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 4),
    _SnmpIpxAddr2_Type()
)
snmpIpxAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpxAddr2.setStatus("mandatory")


class _SnmpTrapComm_Type(DisplayString):
    """Custom type snmpTrapComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpTrapComm_Type.__name__ = "DisplayString"
_SnmpTrapComm_Object = MibScalar
snmpTrapComm = _SnmpTrapComm_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 5),
    _SnmpTrapComm_Type()
)
snmpTrapComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapComm.setStatus("mandatory")


class _SnmpAutTrap_Type(Integer32):
    """Custom type snmpAutTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpAutTrap_Type.__name__ = "Integer32"
_SnmpAutTrap_Object = MibScalar
snmpAutTrap = _SnmpAutTrap_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 6),
    _SnmpAutTrap_Type()
)
snmpAutTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAutTrap.setStatus("mandatory")


class _SnmpPrtTrap_Type(Integer32):
    """Custom type snmpPrtTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpPrtTrap_Type.__name__ = "Integer32"
_SnmpPrtTrap_Object = MibScalar
snmpPrtTrap = _SnmpPrtTrap_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 7),
    _SnmpPrtTrap_Type()
)
snmpPrtTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPrtTrap.setStatus("mandatory")
_SnmpTrapNumber_Type = Integer32
_SnmpTrapNumber_Object = MibScalar
snmpTrapNumber = _SnmpTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 8),
    _SnmpTrapNumber_Type()
)
snmpTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapNumber.setStatus("mandatory")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("mandatory")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "snmpTrapIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("mandatory")


class _SnmpTrapIndex_Type(Integer32):
    """Custom type snmpTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SnmpTrapIndex_Type.__name__ = "Integer32"
_SnmpTrapIndex_Object = MibTableColumn
snmpTrapIndex = _SnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 1),
    _SnmpTrapIndex_Type()
)
snmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapIndex.setStatus("mandatory")
_SnmpTrapIpAddress_Type = IpAddress
_SnmpTrapIpAddress_Object = MibTableColumn
snmpTrapIpAddress = _SnmpTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 2),
    _SnmpTrapIpAddress_Type()
)
snmpTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapIpAddress.setStatus("mandatory")


class _SnmpTrapIpxAddress_Type(PhysAddress):
    """Custom type snmpTrapIpxAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SnmpTrapIpxAddress_Type.__name__ = "PhysAddress"
_SnmpTrapIpxAddress_Object = MibTableColumn
snmpTrapIpxAddress = _SnmpTrapIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 3),
    _SnmpTrapIpxAddress_Type()
)
snmpTrapIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapIpxAddress.setStatus("mandatory")


class _SnmpTrapAuthentication_Type(Integer32):
    """Custom type snmpTrapAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpTrapAuthentication_Type.__name__ = "Integer32"
_SnmpTrapAuthentication_Object = MibTableColumn
snmpTrapAuthentication = _SnmpTrapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 4),
    _SnmpTrapAuthentication_Type()
)
snmpTrapAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAuthentication.setStatus("mandatory")


class _SnmpTrapPrinter1_Type(Integer32):
    """Custom type snmpTrapPrinter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpTrapPrinter1_Type.__name__ = "Integer32"
_SnmpTrapPrinter1_Object = MibTableColumn
snmpTrapPrinter1 = _SnmpTrapPrinter1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 5),
    _SnmpTrapPrinter1_Type()
)
snmpTrapPrinter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPrinter1.setStatus("mandatory")
_SnmpTrapMask1_Type = Integer32
_SnmpTrapMask1_Object = MibTableColumn
snmpTrapMask1 = _SnmpTrapMask1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 6),
    _SnmpTrapMask1_Type()
)
snmpTrapMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapMask1.setStatus("mandatory")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibTableColumn
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 9, 1, 7),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")


class _SnmpCommunity_Type(DisplayString):
    """Custom type snmpCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SnmpCommunity_Type.__name__ = "DisplayString"
_SnmpCommunity_Object = MibScalar
snmpCommunity = _SnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 20),
    _SnmpCommunity_Type()
)
snmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunity.setStatus("mandatory")


class _SnmpV1_Type(Integer32):
    """Custom type snmpV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpV1_Type.__name__ = "Integer32"
_SnmpV1_Object = MibScalar
snmpV1 = _SnmpV1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 21),
    _SnmpV1_Type()
)
snmpV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV1.setStatus("mandatory")


class _SnmpV1AccMode_Type(Integer32):
    """Custom type snmpV1AccMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("readwrite", 1))
    )


_SnmpV1AccMode_Type.__name__ = "Integer32"
_SnmpV1AccMode_Object = MibScalar
snmpV1AccMode = _SnmpV1AccMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 22),
    _SnmpV1AccMode_Type()
)
snmpV1AccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV1AccMode.setStatus("mandatory")


class _SnmpV3_Type(Integer32):
    """Custom type snmpV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpV3_Type.__name__ = "Integer32"
_SnmpV3_Object = MibScalar
snmpV3 = _SnmpV3_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 7, 31),
    _SnmpV3_Type()
)
snmpV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3.setStatus("mandatory")
_SehActions_ObjectIdentity = ObjectIdentity
sehActions = _SehActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8)
)


class _ActAction_Type(Integer32):
    """Custom type actAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              10,
              11,
              12,
              13,
              14,
              64,
              65,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("actionCompleted", 0),
          ("restoreFactorySettings", 9),
          ("restart", 10),
          ("printStatuspageOnChannel1", 11),
          ("printStatuspageOnChannel2", 12),
          ("printStatuspageOnChannel3", 13),
          ("printStatuspageOnChannel4", 14),
          ("mail", 64),
          ("tpReconnect", 65),
          ("actionInprogress", 254),
          ("actionError", 255))
    )


_ActAction_Type.__name__ = "Integer32"
_ActAction_Object = MibScalar
actAction = _ActAction_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 1),
    _ActAction_Type()
)
actAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actAction.setStatus("mandatory")


class _ActUpdate_Type(Integer32):
    """Custom type actUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActUpdate_Type.__name__ = "Integer32"
_ActUpdate_Object = MibScalar
actUpdate = _ActUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 10),
    _ActUpdate_Type()
)
actUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actUpdate.setStatus("mandatory")


class _ActUpdateUrl_Type(DisplayString):
    """Custom type actUpdateUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ActUpdateUrl_Type.__name__ = "DisplayString"
_ActUpdateUrl_Object = MibScalar
actUpdateUrl = _ActUpdateUrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 11),
    _ActUpdateUrl_Type()
)
actUpdateUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actUpdateUrl.setStatus("mandatory")


class _ActUpdateProxy_Type(Integer32):
    """Custom type actUpdateProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActUpdateProxy_Type.__name__ = "Integer32"
_ActUpdateProxy_Object = MibScalar
actUpdateProxy = _ActUpdateProxy_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 12),
    _ActUpdateProxy_Type()
)
actUpdateProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actUpdateProxy.setStatus("mandatory")


class _ActUpdateProxyName_Type(DisplayString):
    """Custom type actUpdateProxyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ActUpdateProxyName_Type.__name__ = "DisplayString"
_ActUpdateProxyName_Object = MibScalar
actUpdateProxyName = _ActUpdateProxyName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 13),
    _ActUpdateProxyName_Type()
)
actUpdateProxyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actUpdateProxyName.setStatus("mandatory")


class _ActPrtUpdate_Type(Integer32):
    """Custom type actPrtUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActPrtUpdate_Type.__name__ = "Integer32"
_ActPrtUpdate_Object = MibScalar
actPrtUpdate = _ActPrtUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 14),
    _ActPrtUpdate_Type()
)
actPrtUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdate.setStatus("mandatory")


class _ActPrtUpdateUrl_Type(DisplayString):
    """Custom type actPrtUpdateUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ActPrtUpdateUrl_Type.__name__ = "DisplayString"
_ActPrtUpdateUrl_Object = MibScalar
actPrtUpdateUrl = _ActPrtUpdateUrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 15),
    _ActPrtUpdateUrl_Type()
)
actPrtUpdateUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdateUrl.setStatus("mandatory")


class _ActPrtUpdateUsr_Type(DisplayString):
    """Custom type actPrtUpdateUsr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ActPrtUpdateUsr_Type.__name__ = "DisplayString"
_ActPrtUpdateUsr_Object = MibScalar
actPrtUpdateUsr = _ActPrtUpdateUsr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 16),
    _ActPrtUpdateUsr_Type()
)
actPrtUpdateUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdateUsr.setStatus("mandatory")


class _ActPrtUpdatePwd_Type(DisplayString):
    """Custom type actPrtUpdatePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ActPrtUpdatePwd_Type.__name__ = "DisplayString"
_ActPrtUpdatePwd_Object = MibScalar
actPrtUpdatePwd = _ActPrtUpdatePwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 17),
    _ActPrtUpdatePwd_Type()
)
actPrtUpdatePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdatePwd.setStatus("mandatory")


class _ActPrtUpdateProxy_Type(Integer32):
    """Custom type actPrtUpdateProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActPrtUpdateProxy_Type.__name__ = "Integer32"
_ActPrtUpdateProxy_Object = MibScalar
actPrtUpdateProxy = _ActPrtUpdateProxy_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 18),
    _ActPrtUpdateProxy_Type()
)
actPrtUpdateProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdateProxy.setStatus("mandatory")


class _ActPrtUpdateProxyName_Type(DisplayString):
    """Custom type actPrtUpdateProxyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ActPrtUpdateProxyName_Type.__name__ = "DisplayString"
_ActPrtUpdateProxyName_Object = MibScalar
actPrtUpdateProxyName = _ActPrtUpdateProxyName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 8, 19),
    _ActPrtUpdateProxyName_Type()
)
actPrtUpdateProxyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actPrtUpdateProxyName.setStatus("mandatory")
_SehTokenRing_ObjectIdentity = ObjectIdentity
sehTokenRing = _SehTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 10)
)


class _TrEarlyTokRel_Type(Integer32):
    """Custom type trEarlyTokRel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrEarlyTokRel_Type.__name__ = "Integer32"
_TrEarlyTokRel_Object = MibScalar
trEarlyTokRel = _TrEarlyTokRel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 10, 1),
    _TrEarlyTokRel_Type()
)
trEarlyTokRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trEarlyTokRel.setStatus("mandatory")


class _TrSourceRouting_Type(Integer32):
    """Custom type trSourceRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrSourceRouting_Type.__name__ = "Integer32"
_TrSourceRouting_Object = MibScalar
trSourceRouting = _TrSourceRouting_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 10, 2),
    _TrSourceRouting_Type()
)
trSourceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trSourceRouting.setStatus("mandatory")


class _TrPhysAddr_Type(PhysAddress):
    """Custom type trPhysAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TrPhysAddr_Type.__name__ = "PhysAddress"
_TrPhysAddr_Object = MibScalar
trPhysAddr = _TrPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 10, 3),
    _TrPhysAddr_Type()
)
trPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trPhysAddr.setStatus("mandatory")


class _TrRingSpeed_Type(Integer32):
    """Custom type trRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("speed4Mbps", 4),
          ("speed16Mbps", 16))
    )


_TrRingSpeed_Type.__name__ = "Integer32"
_TrRingSpeed_Object = MibScalar
trRingSpeed = _TrRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 10, 4),
    _TrRingSpeed_Type()
)
trRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trRingSpeed.setStatus("mandatory")
_SehWireless_ObjectIdentity = ObjectIdentity
sehWireless = _SehWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11)
)


class _WlanMode_Type(Integer32):
    """Custom type wlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 1),
          ("auto", 2),
          ("ad-hoc", 3),
          ("softAP", 4))
    )


_WlanMode_Type.__name__ = "Integer32"
_WlanMode_Object = MibScalar
wlanMode = _WlanMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 1),
    _WlanMode_Type()
)
wlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMode.setStatus("mandatory")
_WlanChannel_Type = Integer32
_WlanChannel_Object = MibScalar
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 2),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("mandatory")


class _WlanNetworkName_Type(DisplayString):
    """Custom type wlanNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanNetworkName_Type.__name__ = "DisplayString"
_WlanNetworkName_Object = MibScalar
wlanNetworkName = _WlanNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 3),
    _WlanNetworkName_Type()
)
wlanNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanNetworkName.setStatus("mandatory")


class _WlanEncrypt_Type(Integer32):
    """Custom type wlanEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep", 1),
          ("wep-sharedkey", 2),
          ("wpa-tkip", 3),
          ("wpa-aes", 4),
          ("wpa2-tkip", 5),
          ("wpa2-aes", 6),
          ("wpa-aes-tkip", 7),
          ("wpa2-aes-tkip", 8),
          ("wpa-auto", 9))
    )


_WlanEncrypt_Type.__name__ = "Integer32"
_WlanEncrypt_Object = MibScalar
wlanEncrypt = _WlanEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 5),
    _WlanEncrypt_Type()
)
wlanEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEncrypt.setStatus("mandatory")


class _WlanWepKey1_Type(DisplayString):
    """Custom type wlanWepKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_WlanWepKey1_Type.__name__ = "DisplayString"
_WlanWepKey1_Object = MibScalar
wlanWepKey1 = _WlanWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 6),
    _WlanWepKey1_Type()
)
wlanWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey1.setStatus("mandatory")


class _WlanDistance_Type(Integer32):
    """Custom type wlanDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 1),
          ("medium", 2),
          ("small", 3))
    )


_WlanDistance_Type.__name__ = "Integer32"
_WlanDistance_Object = MibScalar
wlanDistance = _WlanDistance_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 7),
    _WlanDistance_Type()
)
wlanDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDistance.setStatus("mandatory")
_WlanLevel_Type = Integer32
_WlanLevel_Object = MibScalar
wlanLevel = _WlanLevel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 8),
    _WlanLevel_Type()
)
wlanLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanLevel.setStatus("mandatory")


class _WlanSpeed_Type(DisplayString):
    """Custom type wlanSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_WlanSpeed_Type.__name__ = "DisplayString"
_WlanSpeed_Object = MibScalar
wlanSpeed = _WlanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 9),
    _WlanSpeed_Type()
)
wlanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSpeed.setStatus("mandatory")


class _WlanConnectionStatus_Type(Integer32):
    """Custom type wlanConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("searching", 2),
          ("ad-hoc", 3),
          ("infrastructure", 4),
          ("out-of-range", 5),
          ("softAP", 6))
    )


_WlanConnectionStatus_Type.__name__ = "Integer32"
_WlanConnectionStatus_Object = MibScalar
wlanConnectionStatus = _WlanConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 10),
    _WlanConnectionStatus_Type()
)
wlanConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanConnectionStatus.setStatus("mandatory")


class _WlanManufacturer_Type(DisplayString):
    """Custom type wlanManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanManufacturer_Type.__name__ = "DisplayString"
_WlanManufacturer_Object = MibScalar
wlanManufacturer = _WlanManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 11),
    _WlanManufacturer_Type()
)
wlanManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanManufacturer.setStatus("mandatory")


class _WlanCurrentName_Type(DisplayString):
    """Custom type wlanCurrentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanCurrentName_Type.__name__ = "DisplayString"
_WlanCurrentName_Object = MibScalar
wlanCurrentName = _WlanCurrentName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 12),
    _WlanCurrentName_Type()
)
wlanCurrentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanCurrentName.setStatus("mandatory")


class _WlanPcmciaSerial_Type(DisplayString):
    """Custom type wlanPcmciaSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_WlanPcmciaSerial_Type.__name__ = "DisplayString"
_WlanPcmciaSerial_Object = MibScalar
wlanPcmciaSerial = _WlanPcmciaSerial_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 13),
    _WlanPcmciaSerial_Type()
)
wlanPcmciaSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanPcmciaSerial.setStatus("mandatory")
_WlanKeyId_Type = Integer32
_WlanKeyId_Object = MibScalar
wlanKeyId = _WlanKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 14),
    _WlanKeyId_Type()
)
wlanKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanKeyId.setStatus("mandatory")


class _WlanWepKey2_Type(DisplayString):
    """Custom type wlanWepKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_WlanWepKey2_Type.__name__ = "DisplayString"
_WlanWepKey2_Object = MibScalar
wlanWepKey2 = _WlanWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 15),
    _WlanWepKey2_Type()
)
wlanWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey2.setStatus("mandatory")


class _WlanWepKey3_Type(DisplayString):
    """Custom type wlanWepKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_WlanWepKey3_Type.__name__ = "DisplayString"
_WlanWepKey3_Object = MibScalar
wlanWepKey3 = _WlanWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 16),
    _WlanWepKey3_Type()
)
wlanWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey3.setStatus("mandatory")


class _WlanWepKey4_Type(DisplayString):
    """Custom type wlanWepKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_WlanWepKey4_Type.__name__ = "DisplayString"
_WlanWepKey4_Object = MibScalar
wlanWepKey4 = _WlanWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 17),
    _WlanWepKey4_Type()
)
wlanWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey4.setStatus("mandatory")


class _EapAuthType_Type(Integer32):
    """Custom type eapAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedSystem", 2),
          ("radiusMD5", 3),
          ("radiusTLS", 4),
          ("ttl", 5),
          ("peap", 6),
          ("eapfast", 7))
    )


_EapAuthType_Type.__name__ = "Integer32"
_EapAuthType_Object = MibScalar
eapAuthType = _EapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 18),
    _EapAuthType_Type()
)
eapAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthType.setStatus("mandatory")


class _EapAuthName_Type(DisplayString):
    """Custom type eapAuthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EapAuthName_Type.__name__ = "DisplayString"
_EapAuthName_Object = MibScalar
eapAuthName = _EapAuthName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 19),
    _EapAuthName_Type()
)
eapAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthName.setStatus("mandatory")


class _EapAuthPwd_Type(DisplayString):
    """Custom type eapAuthPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EapAuthPwd_Type.__name__ = "DisplayString"
_EapAuthPwd_Object = MibScalar
eapAuthPwd = _EapAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 20),
    _EapAuthPwd_Type()
)
eapAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthPwd.setStatus("mandatory")


class _WlanPSK_Type(DisplayString):
    """Custom type wlanPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WlanPSK_Type.__name__ = "DisplayString"
_WlanPSK_Object = MibScalar
wlanPSK = _WlanPSK_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 21),
    _WlanPSK_Type()
)
wlanPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPSK.setStatus("mandatory")


class _WlanRoaming_Type(Integer32):
    """Custom type wlanRoaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WlanRoaming_Type.__name__ = "Integer32"
_WlanRoaming_Object = MibScalar
wlanRoaming = _WlanRoaming_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 22),
    _WlanRoaming_Type()
)
wlanRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRoaming.setStatus("mandatory")


class _EapAuthExtern_Type(Integer32):
    """Custom type eapAuthExtern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("peaplabel0", 1),
          ("peaplabel1", 2),
          ("peapversion0", 3),
          ("peapversion1", 4),
          ("eapfastprovisioning", 5))
    )


_EapAuthExtern_Type.__name__ = "Integer32"
_EapAuthExtern_Object = MibScalar
eapAuthExtern = _EapAuthExtern_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 23),
    _EapAuthExtern_Type()
)
eapAuthExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthExtern.setStatus("mandatory")


class _EapAuthIntern_Type(Integer32):
    """Custom type eapAuthIntern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mschap", 1),
          ("mschapv2", 2),
          ("pap", 3),
          ("chap", 4),
          ("eapmd5", 5),
          ("eapmschap", 6),
          ("eapmschapv2", 7),
          ("eaptls", 8))
    )


_EapAuthIntern_Type.__name__ = "Integer32"
_EapAuthIntern_Object = MibScalar
eapAuthIntern = _EapAuthIntern_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 24),
    _EapAuthIntern_Type()
)
eapAuthIntern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthIntern.setStatus("mandatory")


class _EapAuthAnonymousName_Type(DisplayString):
    """Custom type eapAuthAnonymousName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EapAuthAnonymousName_Type.__name__ = "DisplayString"
_EapAuthAnonymousName_Object = MibScalar
eapAuthAnonymousName = _EapAuthAnonymousName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 25),
    _EapAuthAnonymousName_Type()
)
eapAuthAnonymousName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthAnonymousName.setStatus("mandatory")


class _EapAuthSupplicantAddOn_Type(DisplayString):
    """Custom type eapAuthSupplicantAddOn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EapAuthSupplicantAddOn_Type.__name__ = "DisplayString"
_EapAuthSupplicantAddOn_Object = MibScalar
eapAuthSupplicantAddOn = _EapAuthSupplicantAddOn_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 26),
    _EapAuthSupplicantAddOn_Type()
)
eapAuthSupplicantAddOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapAuthSupplicantAddOn.setStatus("mandatory")
_WlandBm2Roam_Type = Integer32
_WlandBm2Roam_Object = MibScalar
wlandBm2Roam = _WlandBm2Roam_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 27),
    _WlandBm2Roam_Type()
)
wlandBm2Roam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlandBm2Roam.setStatus("mandatory")


class _WlandWps_Type(Integer32):
    """Custom type wlandWps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WlandWps_Type.__name__ = "Integer32"
_WlandWps_Object = MibScalar
wlandWps = _WlandWps_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 28),
    _WlandWps_Type()
)
wlandWps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlandWps.setStatus("mandatory")


class _Wlen_Type(Integer32):
    """Custom type wlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Wlen_Type.__name__ = "Integer32"
_Wlen_Object = MibScalar
wlen = _Wlen_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 30),
    _Wlen_Type()
)
wlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlen.setStatus("mandatory")


class _Wlan_Type(Integer32):
    """Custom type wlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Wlan_Type.__name__ = "Integer32"
_Wlan_Object = MibScalar
wlan = _Wlan_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 40),
    _Wlan_Type()
)
wlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan.setStatus("mandatory")


class _OnTheAir_Type(Integer32):
    """Custom type onTheAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wired", 0),
          ("wireless", 1))
    )


_OnTheAir_Type.__name__ = "Integer32"
_OnTheAir_Object = MibScalar
onTheAir = _OnTheAir_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 11, 41),
    _OnTheAir_Type()
)
onTheAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onTheAir.setStatus("mandatory")
_SehWin_ObjectIdentity = ObjectIdentity
sehWin = _SehWin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20)
)


class _WinSmb_Type(Integer32):
    """Custom type winSmb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WinSmb_Type.__name__ = "Integer32"
_WinSmb_Object = MibScalar
winSmb = _WinSmb_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 1),
    _WinSmb_Type()
)
winSmb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winSmb.setStatus("mandatory")


class _WinNetbiosName_Type(DisplayString):
    """Custom type winNetbiosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WinNetbiosName_Type.__name__ = "DisplayString"
_WinNetbiosName_Object = MibScalar
winNetbiosName = _WinNetbiosName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 20),
    _WinNetbiosName_Type()
)
winNetbiosName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winNetbiosName.setStatus("mandatory")


class _WinNetbiosDomain_Type(DisplayString):
    """Custom type winNetbiosDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WinNetbiosDomain_Type.__name__ = "DisplayString"
_WinNetbiosDomain_Object = MibScalar
winNetbiosDomain = _WinNetbiosDomain_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 21),
    _WinNetbiosDomain_Type()
)
winNetbiosDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winNetbiosDomain.setStatus("mandatory")
_WinNetbiosRefresh_Type = Integer32
_WinNetbiosRefresh_Object = MibScalar
winNetbiosRefresh = _WinNetbiosRefresh_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 22),
    _WinNetbiosRefresh_Type()
)
winNetbiosRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winNetbiosRefresh.setStatus("mandatory")


class _WinWinsReg_Type(Integer32):
    """Custom type winWinsReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WinWinsReg_Type.__name__ = "Integer32"
_WinWinsReg_Object = MibScalar
winWinsReg = _WinWinsReg_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 40),
    _WinWinsReg_Type()
)
winWinsReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winWinsReg.setStatus("mandatory")


class _WinWinsDHCP_Type(Integer32):
    """Custom type winWinsDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WinWinsDHCP_Type.__name__ = "Integer32"
_WinWinsDHCP_Object = MibScalar
winWinsDHCP = _WinWinsDHCP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 41),
    _WinWinsDHCP_Type()
)
winWinsDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winWinsDHCP.setStatus("mandatory")


class _WinWinsPrimarySrv_Type(DisplayString):
    """Custom type winWinsPrimarySrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WinWinsPrimarySrv_Type.__name__ = "DisplayString"
_WinWinsPrimarySrv_Object = MibScalar
winWinsPrimarySrv = _WinWinsPrimarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 42),
    _WinWinsPrimarySrv_Type()
)
winWinsPrimarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winWinsPrimarySrv.setStatus("mandatory")


class _WinWinsSecondarySrv_Type(DisplayString):
    """Custom type winWinsSecondarySrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WinWinsSecondarySrv_Type.__name__ = "DisplayString"
_WinWinsSecondarySrv_Object = MibScalar
winWinsSecondarySrv = _WinWinsSecondarySrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 20, 43),
    _WinWinsSecondarySrv_Type()
)
winWinsSecondarySrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winWinsSecondarySrv.setStatus("mandatory")
_SehTime_ObjectIdentity = ObjectIdentity
sehTime = _SehTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21)
)


class _TimeSntp_Type(Integer32):
    """Custom type timeSntp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TimeSntp_Type.__name__ = "Integer32"
_TimeSntp_Object = MibScalar
timeSntp = _TimeSntp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21, 1),
    _TimeSntp_Type()
)
timeSntp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSntp.setStatus("mandatory")


class _TimeServer_Type(DisplayString):
    """Custom type timeServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TimeServer_Type.__name__ = "DisplayString"
_TimeServer_Object = MibScalar
timeServer = _TimeServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21, 2),
    _TimeServer_Type()
)
timeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer.setStatus("mandatory")
_TimeZoneOffset_Type = Integer32
_TimeZoneOffset_Object = MibScalar
timeZoneOffset = _TimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21, 3),
    _TimeZoneOffset_Type()
)
timeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZoneOffset.setStatus("mandatory")


class _TimeDate_Type(DisplayString):
    """Custom type timeDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TimeDate_Type.__name__ = "DisplayString"
_TimeDate_Object = MibScalar
timeDate = _TimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21, 4),
    _TimeDate_Type()
)
timeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeDate.setStatus("mandatory")


class _TimeZoneNameAndRule_Type(DisplayString):
    """Custom type timeZoneNameAndRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TimeZoneNameAndRule_Type.__name__ = "DisplayString"
_TimeZoneNameAndRule_Object = MibScalar
timeZoneNameAndRule = _TimeZoneNameAndRule_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 21, 5),
    _TimeZoneNameAndRule_Type()
)
timeZoneNameAndRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZoneNameAndRule.setStatus("mandatory")
_SehPrintjob_ObjectIdentity = ObjectIdentity
sehPrintjob = _SehPrintjob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22)
)
_PjobCount_Type = Integer32
_PjobCount_Object = MibScalar
pjobCount = _PjobCount_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 1),
    _PjobCount_Type()
)
pjobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobCount.setStatus("mandatory")
_PjobTable_Object = MibTable
pjobTable = _PjobTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2)
)
if mibBuilder.loadTexts:
    pjobTable.setStatus("mandatory")
_PjobEntry_Object = MibTableRow
pjobEntry = _PjobEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1)
)
pjobEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "pjobIndex"),
)
if mibBuilder.loadTexts:
    pjobEntry.setStatus("mandatory")


class _PjobIndex_Type(Integer32):
    """Custom type pjobIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PjobIndex_Type.__name__ = "Integer32"
_PjobIndex_Object = MibTableColumn
pjobIndex = _PjobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 1),
    _PjobIndex_Type()
)
pjobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobIndex.setStatus("mandatory")


class _PjobStatus_Type(Integer32):
    """Custom type pjobStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("pending", 3),
          ("held", 4),
          ("processing", 5),
          ("stopped", 6),
          ("canceled", 7),
          ("aborted", 8),
          ("completed", 9))
    )


_PjobStatus_Type.__name__ = "Integer32"
_PjobStatus_Object = MibTableColumn
pjobStatus = _PjobStatus_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 2),
    _PjobStatus_Type()
)
pjobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobStatus.setStatus("mandatory")


class _PjobProtocol_Type(Integer32):
    """Custom type pjobProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ipp", 0),
          ("tcp", 1),
          ("lpr", 2),
          ("nds", 3),
          ("bindery", 4),
          ("rnprinter", 5),
          ("atalk", 6),
          ("ftp", 7),
          ("smb", 8),
          ("http", 9),
          ("thinprint", 10),
          ("email", 11),
          ("thinprintcs", 12),
          ("unknown", 13))
    )


_PjobProtocol_Type.__name__ = "Integer32"
_PjobProtocol_Object = MibTableColumn
pjobProtocol = _PjobProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 3),
    _PjobProtocol_Type()
)
pjobProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobProtocol.setStatus("mandatory")


class _PjobName_Type(DisplayString):
    """Custom type pjobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PjobName_Type.__name__ = "DisplayString"
_PjobName_Object = MibTableColumn
pjobName = _PjobName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 4),
    _PjobName_Type()
)
pjobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobName.setStatus("mandatory")


class _PjobSender_Type(DisplayString):
    """Custom type pjobSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PjobSender_Type.__name__ = "DisplayString"
_PjobSender_Object = MibTableColumn
pjobSender = _PjobSender_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 5),
    _PjobSender_Type()
)
pjobSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobSender.setStatus("mandatory")
_PjobSize_Type = Integer32
_PjobSize_Object = MibTableColumn
pjobSize = _PjobSize_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 6),
    _PjobSize_Type()
)
pjobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobSize.setStatus("mandatory")


class _PjobCreationTime_Type(DisplayString):
    """Custom type pjobCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PjobCreationTime_Type.__name__ = "DisplayString"
_PjobCreationTime_Object = MibTableColumn
pjobCreationTime = _PjobCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 7),
    _PjobCreationTime_Type()
)
pjobCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobCreationTime.setStatus("mandatory")
_PjobDuration_Type = Integer32
_PjobDuration_Object = MibTableColumn
pjobDuration = _PjobDuration_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 8),
    _PjobDuration_Type()
)
pjobDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobDuration.setStatus("mandatory")
_PjobPport_Type = Integer32
_PjobPport_Object = MibTableColumn
pjobPport = _PjobPport_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 9),
    _PjobPport_Type()
)
pjobPport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobPport.setStatus("mandatory")
_PjobPages_Type = Integer32
_PjobPages_Object = MibTableColumn
pjobPages = _PjobPages_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 10),
    _PjobPages_Type()
)
pjobPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobPages.setStatus("mandatory")


class _PjobSizeType_Type(Integer32):
    """Custom type pjobSizeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 0),
          ("kbytes", 1))
    )


_PjobSizeType_Type.__name__ = "Integer32"
_PjobSizeType_Object = MibTableColumn
pjobSizeType = _PjobSizeType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 22, 2, 1, 11),
    _PjobSizeType_Type()
)
pjobSizeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjobSizeType.setStatus("mandatory")
_SehNotification_ObjectIdentity = ObjectIdentity
sehNotification = _SehNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25)
)
_NfSlotNumber_Type = Integer32
_NfSlotNumber_Object = MibScalar
nfSlotNumber = _NfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 1),
    _NfSlotNumber_Type()
)
nfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfSlotNumber.setStatus("mandatory")
_NfSlotTable_Object = MibTable
nfSlotTable = _NfSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2)
)
if mibBuilder.loadTexts:
    nfSlotTable.setStatus("mandatory")
_NfSlotEntry_Object = MibTableRow
nfSlotEntry = _NfSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1)
)
nfSlotEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "nfSlotIndex"),
)
if mibBuilder.loadTexts:
    nfSlotEntry.setStatus("mandatory")


class _NfSlotIndex_Type(Integer32):
    """Custom type nfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NfSlotIndex_Type.__name__ = "Integer32"
_NfSlotIndex_Object = MibTableColumn
nfSlotIndex = _NfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 1),
    _NfSlotIndex_Type()
)
nfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfSlotIndex.setStatus("mandatory")


class _NfMailNotification_Type(Integer32):
    """Custom type nfMailNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfMailNotification_Type.__name__ = "Integer32"
_NfMailNotification_Object = MibTableColumn
nfMailNotification = _NfMailNotification_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 2),
    _NfMailNotification_Type()
)
nfMailNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfMailNotification.setStatus("mandatory")


class _NfMailAddress_Type(DisplayString):
    """Custom type nfMailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NfMailAddress_Type.__name__ = "DisplayString"
_NfMailAddress_Object = MibTableColumn
nfMailAddress = _NfMailAddress_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 3),
    _NfMailAddress_Type()
)
nfMailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfMailAddress.setStatus("mandatory")


class _NfMailServer_Type(DisplayString):
    """Custom type nfMailServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NfMailServer_Type.__name__ = "DisplayString"
_NfMailServer_Object = MibTableColumn
nfMailServer = _NfMailServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 4),
    _NfMailServer_Type()
)
nfMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfMailServer.setStatus("mandatory")
_NfTrapIpAddress_Type = IpAddress
_NfTrapIpAddress_Object = MibTableColumn
nfTrapIpAddress = _NfTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 10),
    _NfTrapIpAddress_Type()
)
nfTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfTrapIpAddress.setStatus("mandatory")


class _NfTrapIpxAddress_Type(PhysAddress):
    """Custom type nfTrapIpxAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_NfTrapIpxAddress_Type.__name__ = "PhysAddress"
_NfTrapIpxAddress_Object = MibTableColumn
nfTrapIpxAddress = _NfTrapIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 11),
    _NfTrapIpxAddress_Type()
)
nfTrapIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfTrapIpxAddress.setStatus("mandatory")


class _NfTrapAuthentication_Type(Integer32):
    """Custom type nfTrapAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfTrapAuthentication_Type.__name__ = "Integer32"
_NfTrapAuthentication_Object = MibTableColumn
nfTrapAuthentication = _NfTrapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 12),
    _NfTrapAuthentication_Type()
)
nfTrapAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfTrapAuthentication.setStatus("mandatory")


class _NfTrapPrinter_Type(Integer32):
    """Custom type nfTrapPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfTrapPrinter_Type.__name__ = "Integer32"
_NfTrapPrinter_Object = MibTableColumn
nfTrapPrinter = _NfTrapPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 13),
    _NfTrapPrinter_Type()
)
nfTrapPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfTrapPrinter.setStatus("mandatory")


class _NfTrapCommunity_Type(DisplayString):
    """Custom type nfTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NfTrapCommunity_Type.__name__ = "DisplayString"
_NfTrapCommunity_Object = MibTableColumn
nfTrapCommunity = _NfTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 14),
    _NfTrapCommunity_Type()
)
nfTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfTrapCommunity.setStatus("mandatory")


class _NfAccJobHist_Type(Integer32):
    """Custom type nfAccJobHist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfAccJobHist_Type.__name__ = "Integer32"
_NfAccJobHist_Object = MibTableColumn
nfAccJobHist = _NfAccJobHist_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 15),
    _NfAccJobHist_Type()
)
nfAccJobHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfAccJobHist.setStatus("mandatory")
_NfAccJobHistTime_Type = Integer32
_NfAccJobHistTime_Object = MibTableColumn
nfAccJobHistTime = _NfAccJobHistTime_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 16),
    _NfAccJobHistTime_Type()
)
nfAccJobHistTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfAccJobHistTime.setStatus("mandatory")
_NfAccJobHistCntr_Type = Integer32
_NfAccJobHistCntr_Object = MibTableColumn
nfAccJobHistCntr = _NfAccJobHistCntr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 2, 1, 17),
    _NfAccJobHistCntr_Type()
)
nfAccJobHistCntr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfAccJobHistCntr.setStatus("mandatory")
_NfPortNumber_Type = Integer32
_NfPortNumber_Object = MibScalar
nfPortNumber = _NfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 5),
    _NfPortNumber_Type()
)
nfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPortNumber.setStatus("mandatory")
_NfPortTable_Object = MibTable
nfPortTable = _NfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6)
)
if mibBuilder.loadTexts:
    nfPortTable.setStatus("mandatory")
_NfPortEntry_Object = MibTableRow
nfPortEntry = _NfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1)
)
nfPortEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "nfPortIndex"),
)
if mibBuilder.loadTexts:
    nfPortEntry.setStatus("mandatory")


class _NfPortIndex_Type(Integer32):
    """Custom type nfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NfPortIndex_Type.__name__ = "Integer32"
_NfPortIndex_Object = MibTableColumn
nfPortIndex = _NfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 1),
    _NfPortIndex_Type()
)
nfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPortIndex.setStatus("mandatory")
_NfPortMailMask1_Type = Integer32
_NfPortMailMask1_Object = MibTableColumn
nfPortMailMask1 = _NfPortMailMask1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 2),
    _NfPortMailMask1_Type()
)
nfPortMailMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortMailMask1.setStatus("mandatory")
_NfPortMailMask2_Type = Integer32
_NfPortMailMask2_Object = MibTableColumn
nfPortMailMask2 = _NfPortMailMask2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 3),
    _NfPortMailMask2_Type()
)
nfPortMailMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortMailMask2.setStatus("mandatory")
_NfPortTrapMask1_Type = Integer32
_NfPortTrapMask1_Object = MibTableColumn
nfPortTrapMask1 = _NfPortTrapMask1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 20),
    _NfPortTrapMask1_Type()
)
nfPortTrapMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortTrapMask1.setStatus("mandatory")
_NfPortTrapMask2_Type = Integer32
_NfPortTrapMask2_Object = MibTableColumn
nfPortTrapMask2 = _NfPortTrapMask2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 21),
    _NfPortTrapMask2_Type()
)
nfPortTrapMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortTrapMask2.setStatus("mandatory")


class _NfPortAccPageCntr1_Type(Integer32):
    """Custom type nfPortAccPageCntr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfPortAccPageCntr1_Type.__name__ = "Integer32"
_NfPortAccPageCntr1_Object = MibTableColumn
nfPortAccPageCntr1 = _NfPortAccPageCntr1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 22),
    _NfPortAccPageCntr1_Type()
)
nfPortAccPageCntr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntr1.setStatus("mandatory")


class _NfPortAccPageCntr2_Type(Integer32):
    """Custom type nfPortAccPageCntr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfPortAccPageCntr2_Type.__name__ = "Integer32"
_NfPortAccPageCntr2_Object = MibTableColumn
nfPortAccPageCntr2 = _NfPortAccPageCntr2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 23),
    _NfPortAccPageCntr2_Type()
)
nfPortAccPageCntr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntr2.setStatus("mandatory")
_NfPortAccPageCntrTime1_Type = Integer32
_NfPortAccPageCntrTime1_Object = MibTableColumn
nfPortAccPageCntrTime1 = _NfPortAccPageCntrTime1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 24),
    _NfPortAccPageCntrTime1_Type()
)
nfPortAccPageCntrTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrTime1.setStatus("mandatory")
_NfPortAccPageCntrTime2_Type = Integer32
_NfPortAccPageCntrTime2_Object = MibTableColumn
nfPortAccPageCntrTime2 = _NfPortAccPageCntrTime2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 25),
    _NfPortAccPageCntrTime2_Type()
)
nfPortAccPageCntrTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrTime2.setStatus("mandatory")
_NfPortAccPageCntrCntr1_Type = Integer32
_NfPortAccPageCntrCntr1_Object = MibTableColumn
nfPortAccPageCntrCntr1 = _NfPortAccPageCntrCntr1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 26),
    _NfPortAccPageCntrCntr1_Type()
)
nfPortAccPageCntrCntr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrCntr1.setStatus("mandatory")
_NfPortAccPageCntrCntr2_Type = Integer32
_NfPortAccPageCntrCntr2_Object = MibTableColumn
nfPortAccPageCntrCntr2 = _NfPortAccPageCntrCntr2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 27),
    _NfPortAccPageCntrCntr2_Type()
)
nfPortAccPageCntrCntr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrCntr2.setStatus("mandatory")


class _NfPortMailList1_Type(DisplayString):
    """Custom type nfPortMailList1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NfPortMailList1_Type.__name__ = "DisplayString"
_NfPortMailList1_Object = MibTableColumn
nfPortMailList1 = _NfPortMailList1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 31),
    _NfPortMailList1_Type()
)
nfPortMailList1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortMailList1.setStatus("mandatory")


class _NfPortMailList2_Type(DisplayString):
    """Custom type nfPortMailList2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NfPortMailList2_Type.__name__ = "DisplayString"
_NfPortMailList2_Object = MibTableColumn
nfPortMailList2 = _NfPortMailList2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 32),
    _NfPortMailList2_Type()
)
nfPortMailList2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortMailList2.setStatus("mandatory")


class _NfPortTrapList1_Type(DisplayString):
    """Custom type nfPortTrapList1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NfPortTrapList1_Type.__name__ = "DisplayString"
_NfPortTrapList1_Object = MibTableColumn
nfPortTrapList1 = _NfPortTrapList1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 33),
    _NfPortTrapList1_Type()
)
nfPortTrapList1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortTrapList1.setStatus("mandatory")


class _NfPortTrapList2_Type(DisplayString):
    """Custom type nfPortTrapList2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NfPortTrapList2_Type.__name__ = "DisplayString"
_NfPortTrapList2_Object = MibTableColumn
nfPortTrapList2 = _NfPortTrapList2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 34),
    _NfPortTrapList2_Type()
)
nfPortTrapList2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortTrapList2.setStatus("mandatory")
_NfPortAccPageCntrIndex1_Type = Integer32
_NfPortAccPageCntrIndex1_Object = MibTableColumn
nfPortAccPageCntrIndex1 = _NfPortAccPageCntrIndex1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 35),
    _NfPortAccPageCntrIndex1_Type()
)
nfPortAccPageCntrIndex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrIndex1.setStatus("mandatory")
_NfPortAccPageCntrIndex2_Type = Integer32
_NfPortAccPageCntrIndex2_Object = MibTableColumn
nfPortAccPageCntrIndex2 = _NfPortAccPageCntrIndex2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 6, 1, 36),
    _NfPortAccPageCntrIndex2_Type()
)
nfPortAccPageCntrIndex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPortAccPageCntrIndex2.setStatus("mandatory")


class _NfSmtpServer_Type(DisplayString):
    """Custom type nfSmtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NfSmtpServer_Type.__name__ = "DisplayString"
_NfSmtpServer_Object = MibScalar
nfSmtpServer = _NfSmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 7),
    _NfSmtpServer_Type()
)
nfSmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpServer.setStatus("mandatory")
_SehMail_ObjectIdentity = ObjectIdentity
sehMail = _SehMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8)
)


class _NfPop3_Type(Integer32):
    """Custom type nfPop3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfPop3_Type.__name__ = "Integer32"
_NfPop3_Object = MibScalar
nfPop3 = _NfPop3_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 1),
    _NfPop3_Type()
)
nfPop3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3.setStatus("mandatory")
_NfPop3Poll_Type = Integer32
_NfPop3Poll_Object = MibScalar
nfPop3Poll = _NfPop3Poll_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 2),
    _NfPop3Poll_Type()
)
nfPop3Poll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Poll.setStatus("mandatory")


class _NfPop3Srv_Type(DisplayString):
    """Custom type nfPop3Srv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfPop3Srv_Type.__name__ = "DisplayString"
_NfPop3Srv_Object = MibScalar
nfPop3Srv = _NfPop3Srv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 3),
    _NfPop3Srv_Type()
)
nfPop3Srv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Srv.setStatus("mandatory")
_NfPop3SrvPort_Type = Integer32
_NfPop3SrvPort_Object = MibScalar
nfPop3SrvPort = _NfPop3SrvPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 4),
    _NfPop3SrvPort_Type()
)
nfPop3SrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3SrvPort.setStatus("mandatory")


class _NfPop3SmtpSrv_Type(DisplayString):
    """Custom type nfPop3SmtpSrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfPop3SmtpSrv_Type.__name__ = "DisplayString"
_NfPop3SmtpSrv_Object = MibScalar
nfPop3SmtpSrv = _NfPop3SmtpSrv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 5),
    _NfPop3SmtpSrv_Type()
)
nfPop3SmtpSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3SmtpSrv.setStatus("mandatory")
_NfPop3SmtpPort_Type = Integer32
_NfPop3SmtpPort_Object = MibScalar
nfPop3SmtpPort = _NfPop3SmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 6),
    _NfPop3SmtpPort_Type()
)
nfPop3SmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3SmtpPort.setStatus("mandatory")


class _NfPop3Usr_Type(DisplayString):
    """Custom type nfPop3Usr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfPop3Usr_Type.__name__ = "DisplayString"
_NfPop3Usr_Object = MibScalar
nfPop3Usr = _NfPop3Usr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 7),
    _NfPop3Usr_Type()
)
nfPop3Usr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Usr.setStatus("mandatory")


class _NfPop3Pwd_Type(DisplayString):
    """Custom type nfPop3Pwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfPop3Pwd_Type.__name__ = "DisplayString"
_NfPop3Pwd_Object = MibScalar
nfPop3Pwd = _NfPop3Pwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 8),
    _NfPop3Pwd_Type()
)
nfPop3Pwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Pwd.setStatus("mandatory")


class _NfPop3Security_Type(Integer32):
    """Custom type nfPop3Security based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("apop", 1),
          ("ssl", 2))
    )


_NfPop3Security_Type.__name__ = "Integer32"
_NfPop3Security_Object = MibScalar
nfPop3Security = _NfPop3Security_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 9),
    _NfPop3Security_Type()
)
nfPop3Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Security.setStatus("mandatory")


class _NfPop3MDel_Type(Integer32):
    """Custom type nfPop3MDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("leaveMailOnServer", 0),
          ("deleteMailFromServer", 1))
    )


_NfPop3MDel_Type.__name__ = "Integer32"
_NfPop3MDel_Object = MibScalar
nfPop3MDel = _NfPop3MDel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 10),
    _NfPop3MDel_Type()
)
nfPop3MDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3MDel.setStatus("mandatory")
_NfPop3Limit_Type = Integer32
_NfPop3Limit_Object = MibScalar
nfPop3Limit = _NfPop3Limit_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 11),
    _NfPop3Limit_Type()
)
nfPop3Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Limit.setStatus("mandatory")


class _NfPop3Signature_Type(DisplayString):
    """Custom type nfPop3Signature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfPop3Signature_Type.__name__ = "DisplayString"
_NfPop3Signature_Object = MibScalar
nfPop3Signature = _NfPop3Signature_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 12),
    _NfPop3Signature_Type()
)
nfPop3Signature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfPop3Signature.setStatus("mandatory")


class _NfSmtpUsr_Type(DisplayString):
    """Custom type nfSmtpUsr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfSmtpUsr_Type.__name__ = "DisplayString"
_NfSmtpUsr_Object = MibScalar
nfSmtpUsr = _NfSmtpUsr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 13),
    _NfSmtpUsr_Type()
)
nfSmtpUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpUsr.setStatus("mandatory")


class _NfSmtpPwd_Type(DisplayString):
    """Custom type nfSmtpPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfSmtpPwd_Type.__name__ = "DisplayString"
_NfSmtpPwd_Object = MibScalar
nfSmtpPwd = _NfSmtpPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 14),
    _NfSmtpPwd_Type()
)
nfSmtpPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpPwd.setStatus("mandatory")


class _NfSmtpSndr_Type(DisplayString):
    """Custom type nfSmtpSndr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NfSmtpSndr_Type.__name__ = "DisplayString"
_NfSmtpSndr_Object = MibScalar
nfSmtpSndr = _NfSmtpSndr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 15),
    _NfSmtpSndr_Type()
)
nfSmtpSndr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpSndr.setStatus("mandatory")


class _NfSmtpSsl_Type(Integer32):
    """Custom type nfSmtpSsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfSmtpSsl_Type.__name__ = "Integer32"
_NfSmtpSsl_Object = MibScalar
nfSmtpSsl = _NfSmtpSsl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 16),
    _NfSmtpSsl_Type()
)
nfSmtpSsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpSsl.setStatus("mandatory")


class _NfSmtpAsPop3_Type(Integer32):
    """Custom type nfSmtpAsPop3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfSmtpAsPop3_Type.__name__ = "Integer32"
_NfSmtpAsPop3_Object = MibScalar
nfSmtpAsPop3 = _NfSmtpAsPop3_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 17),
    _NfSmtpAsPop3_Type()
)
nfSmtpAsPop3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpAsPop3.setStatus("mandatory")


class _NfSmtpAuth_Type(Integer32):
    """Custom type nfSmtpAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NfSmtpAuth_Type.__name__ = "Integer32"
_NfSmtpAuth_Object = MibScalar
nfSmtpAuth = _NfSmtpAuth_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 18),
    _NfSmtpAuth_Type()
)
nfSmtpAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfSmtpAuth.setStatus("mandatory")
_NfPop3P3His_Type = MailConnState
_NfPop3P3His_Object = MibScalar
nfPop3P3His = _NfPop3P3His_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 20),
    _NfPop3P3His_Type()
)
nfPop3P3His.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3P3His.setStatus("mandatory")
_NfPop3SMTPHis_Type = MailConnState
_NfPop3SMTPHis_Object = MibScalar
nfPop3SMTPHis = _NfPop3SMTPHis_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 21),
    _NfPop3SMTPHis_Type()
)
nfPop3SMTPHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3SMTPHis.setStatus("mandatory")
_NfPop3P3Ctr_Type = Integer32
_NfPop3P3Ctr_Object = MibScalar
nfPop3P3Ctr = _NfPop3P3Ctr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 22),
    _NfPop3P3Ctr_Type()
)
nfPop3P3Ctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3P3Ctr.setStatus("mandatory")
_NfPop3SMTPCtr_Type = Integer32
_NfPop3SMTPCtr_Object = MibScalar
nfPop3SMTPCtr = _NfPop3SMTPCtr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 23),
    _NfPop3SMTPCtr_Type()
)
nfPop3SMTPCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3SMTPCtr.setStatus("mandatory")
_NfPop3P3Err_Type = MailConnState
_NfPop3P3Err_Object = MibScalar
nfPop3P3Err = _NfPop3P3Err_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 24),
    _NfPop3P3Err_Type()
)
nfPop3P3Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3P3Err.setStatus("mandatory")
_NfPop3SmtpErr_Type = MailConnState
_NfPop3SmtpErr_Object = MibScalar
nfPop3SmtpErr = _NfPop3SmtpErr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 25),
    _NfPop3SmtpErr_Type()
)
nfPop3SmtpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3SmtpErr.setStatus("mandatory")
_NfPop3P3Next_Type = Integer32
_NfPop3P3Next_Object = MibScalar
nfPop3P3Next = _NfPop3P3Next_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 26),
    _NfPop3P3Next_Type()
)
nfPop3P3Next.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfPop3P3Next.setStatus("mandatory")


class _SmtpSMIMESig_Type(Integer32):
    """Custom type smtpSMIMESig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmtpSMIMESig_Type.__name__ = "Integer32"
_SmtpSMIMESig_Object = MibScalar
smtpSMIMESig = _SmtpSMIMESig_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 30),
    _SmtpSMIMESig_Type()
)
smtpSMIMESig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSMIMESig.setStatus("mandatory")


class _SmtpSMIMEAddKey_Type(Integer32):
    """Custom type smtpSMIMEAddKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmtpSMIMEAddKey_Type.__name__ = "Integer32"
_SmtpSMIMEAddKey_Object = MibScalar
smtpSMIMEAddKey = _SmtpSMIMEAddKey_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 31),
    _SmtpSMIMEAddKey_Type()
)
smtpSMIMEAddKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSMIMEAddKey.setStatus("mandatory")


class _SmtpSMIMEEnc_Type(Integer32):
    """Custom type smtpSMIMEEnc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SmtpSMIMEEnc_Type.__name__ = "Integer32"
_SmtpSMIMEEnc_Object = MibScalar
smtpSMIMEEnc = _SmtpSMIMEEnc_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 25, 8, 35),
    _SmtpSMIMEEnc_Type()
)
smtpSMIMEEnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSMIMEEnc.setStatus("mandatory")
_SehNat_ObjectIdentity = ObjectIdentity
sehNat = _SehNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26)
)
_NatLocal_Type = IpAddress
_NatLocal_Object = MibScalar
natLocal = _NatLocal_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 1),
    _NatLocal_Type()
)
natLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natLocal.setStatus("mandatory")
_NatRemote_Type = IpAddress
_NatRemote_Object = MibScalar
natRemote = _NatRemote_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 2),
    _NatRemote_Type()
)
natRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natRemote.setStatus("mandatory")
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 3),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("mandatory")


class _NatMasquerade_Type(Integer32):
    """Custom type natMasquerade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatMasquerade_Type.__name__ = "Integer32"
_NatMasquerade_Object = MibScalar
natMasquerade = _NatMasquerade_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 4),
    _NatMasquerade_Type()
)
natMasquerade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natMasquerade.setStatus("mandatory")


class _NatIcmp_Type(Integer32):
    """Custom type natIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatIcmp_Type.__name__ = "Integer32"
_NatIcmp_Object = MibScalar
natIcmp = _NatIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 5),
    _NatIcmp_Type()
)
natIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIcmp.setStatus("mandatory")
_SpagePort_Type = Integer32
_SpagePort_Object = MibScalar
spagePort = _SpagePort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 26, 6),
    _SpagePort_Type()
)
spagePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spagePort.setStatus("mandatory")
_SehNatDrop_ObjectIdentity = ObjectIdentity
sehNatDrop = _SehNatDrop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27)
)
_HttpsPort_Type = Integer32
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 6),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("mandatory")
_FtpPort_Type = Integer32
_FtpPort_Object = MibScalar
ftpPort = _FtpPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 7),
    _FtpPort_Type()
)
ftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPort.setStatus("mandatory")
_FtpDataPort_Type = Integer32
_FtpDataPort_Object = MibScalar
ftpDataPort = _FtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 8),
    _FtpDataPort_Type()
)
ftpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpDataPort.setStatus("mandatory")
_SnmpPort_Type = Integer32
_SnmpPort_Object = MibScalar
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 9),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("mandatory")
_AicePort_Type = Integer32
_AicePort_Object = MibScalar
aicePort = _AicePort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 10),
    _AicePort_Type()
)
aicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aicePort.setStatus("mandatory")
_NatDropNumber_Type = Integer32
_NatDropNumber_Object = MibScalar
natDropNumber = _NatDropNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 21),
    _NatDropNumber_Type()
)
natDropNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDropNumber.setStatus("mandatory")
_NatDropTable_Object = MibTable
natDropTable = _NatDropTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22)
)
if mibBuilder.loadTexts:
    natDropTable.setStatus("mandatory")
_NatDropEntry_Object = MibTableRow
natDropEntry = _NatDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1)
)
natDropEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "natDropIndex"),
)
if mibBuilder.loadTexts:
    natDropEntry.setStatus("mandatory")


class _NatDropIndex_Type(Integer32):
    """Custom type natDropIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NatDropIndex_Type.__name__ = "Integer32"
_NatDropIndex_Object = MibTableColumn
natDropIndex = _NatDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 1),
    _NatDropIndex_Type()
)
natDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDropIndex.setStatus("mandatory")
_NatDropPort_Type = Integer32
_NatDropPort_Object = MibTableColumn
natDropPort = _NatDropPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 2),
    _NatDropPort_Type()
)
natDropPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDropPort.setStatus("mandatory")


class _NatDropTcp_Type(Integer32):
    """Custom type natDropTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatDropTcp_Type.__name__ = "Integer32"
_NatDropTcp_Object = MibTableColumn
natDropTcp = _NatDropTcp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 3),
    _NatDropTcp_Type()
)
natDropTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDropTcp.setStatus("mandatory")


class _NatDropUdp_Type(Integer32):
    """Custom type natDropUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatDropUdp_Type.__name__ = "Integer32"
_NatDropUdp_Object = MibTableColumn
natDropUdp = _NatDropUdp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 4),
    _NatDropUdp_Type()
)
natDropUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDropUdp.setStatus("mandatory")


class _NatDropLan_Type(Integer32):
    """Custom type natDropLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatDropLan_Type.__name__ = "Integer32"
_NatDropLan_Object = MibTableColumn
natDropLan = _NatDropLan_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 5),
    _NatDropLan_Type()
)
natDropLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDropLan.setStatus("mandatory")


class _NatDropNat_Type(Integer32):
    """Custom type natDropNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NatDropNat_Type.__name__ = "Integer32"
_NatDropNat_Object = MibTableColumn
natDropNat = _NatDropNat_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 27, 22, 1, 6),
    _NatDropNat_Type()
)
natDropNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDropNat.setStatus("mandatory")
_SehTpg_ObjectIdentity = ObjectIdentity
sehTpg = _SehTpg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30)
)
_TpgNumber_Type = Integer32
_TpgNumber_Object = MibScalar
tpgNumber = _TpgNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 1),
    _TpgNumber_Type()
)
tpgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpgNumber.setStatus("mandatory")
_TpgTable_Object = MibTable
tpgTable = _TpgTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2)
)
if mibBuilder.loadTexts:
    tpgTable.setStatus("mandatory")
_TpgEntry_Object = MibTableRow
tpgEntry = _TpgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1)
)
tpgEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "tpgIndex"),
)
if mibBuilder.loadTexts:
    tpgEntry.setStatus("mandatory")


class _TpgIndex_Type(Integer32):
    """Custom type tpgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TpgIndex_Type.__name__ = "Integer32"
_TpgIndex_Object = MibTableColumn
tpgIndex = _TpgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 1),
    _TpgIndex_Type()
)
tpgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpgIndex.setStatus("mandatory")


class _TpgPrtName_Type(DisplayString):
    """Custom type tpgPrtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TpgPrtName_Type.__name__ = "DisplayString"
_TpgPrtName_Object = MibTableColumn
tpgPrtName = _TpgPrtName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 2),
    _TpgPrtName_Type()
)
tpgPrtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgPrtName.setStatus("mandatory")


class _TpgPrtClass_Type(DisplayString):
    """Custom type tpgPrtClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_TpgPrtClass_Type.__name__ = "DisplayString"
_TpgPrtClass_Object = MibTableColumn
tpgPrtClass = _TpgPrtClass_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 3),
    _TpgPrtClass_Type()
)
tpgPrtClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgPrtClass.setStatus("mandatory")


class _TpgPrtDriver_Type(DisplayString):
    """Custom type tpgPrtDriver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TpgPrtDriver_Type.__name__ = "DisplayString"
_TpgPrtDriver_Object = MibTableColumn
tpgPrtDriver = _TpgPrtDriver_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 4),
    _TpgPrtDriver_Type()
)
tpgPrtDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgPrtDriver.setStatus("mandatory")


class _TpgRemoteIp_Type(DisplayString):
    """Custom type tpgRemoteIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TpgRemoteIp_Type.__name__ = "DisplayString"
_TpgRemoteIp_Object = MibTableColumn
tpgRemoteIp = _TpgRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 5),
    _TpgRemoteIp_Type()
)
tpgRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemoteIp.setStatus("mandatory")
_TpgRemotePort_Type = Integer32
_TpgRemotePort_Object = MibTableColumn
tpgRemotePort = _TpgRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 6),
    _TpgRemotePort_Type()
)
tpgRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemotePort.setStatus("mandatory")


class _TpgRemoteStat_Type(Integer32):
    """Custom type tpgRemoteStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("timeout", 1),
          ("reachable", 2),
          ("unrechable", 3),
          ("unknown", 4))
    )


_TpgRemoteStat_Type.__name__ = "Integer32"
_TpgRemoteStat_Object = MibTableColumn
tpgRemoteStat = _TpgRemoteStat_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 7),
    _TpgRemoteStat_Type()
)
tpgRemoteStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpgRemoteStat.setStatus("mandatory")


class _TpgRemoteQueue_Type(DisplayString):
    """Custom type tpgRemoteQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TpgRemoteQueue_Type.__name__ = "DisplayString"
_TpgRemoteQueue_Object = MibTableColumn
tpgRemoteQueue = _TpgRemoteQueue_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 8),
    _TpgRemoteQueue_Type()
)
tpgRemoteQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemoteQueue.setStatus("mandatory")


class _TpgRemoteLPD_Type(Integer32):
    """Custom type tpgRemoteLPD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raw", 0),
          ("lpd", 1),
          ("ipp", 2))
    )


_TpgRemoteLPD_Type.__name__ = "Integer32"
_TpgRemoteLPD_Object = MibTableColumn
tpgRemoteLPD = _TpgRemoteLPD_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 9),
    _TpgRemoteLPD_Type()
)
tpgRemoteLPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemoteLPD.setStatus("mandatory")


class _TpgLpdModeRFC_Type(Integer32):
    """Custom type tpgLpdModeRFC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgLpdModeRFC_Type.__name__ = "Integer32"
_TpgLpdModeRFC_Object = MibTableColumn
tpgLpdModeRFC = _TpgLpdModeRFC_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 10),
    _TpgLpdModeRFC_Type()
)
tpgLpdModeRFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgLpdModeRFC.setStatus("mandatory")


class _TpgRemoteUrl_Type(DisplayString):
    """Custom type tpgRemoteUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TpgRemoteUrl_Type.__name__ = "DisplayString"
_TpgRemoteUrl_Object = MibTableColumn
tpgRemoteUrl = _TpgRemoteUrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 11),
    _TpgRemoteUrl_Type()
)
tpgRemoteUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemoteUrl.setStatus("mandatory")


class _TpgRemoteIPPs_Type(Integer32):
    """Custom type tpgRemoteIPPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgRemoteIPPs_Type.__name__ = "Integer32"
_TpgRemoteIPPs_Object = MibTableColumn
tpgRemoteIPPs = _TpgRemoteIPPs_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 12),
    _TpgRemoteIPPs_Type()
)
tpgRemoteIPPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgRemoteIPPs.setStatus("mandatory")


class _TpgRemoteStStr_Type(DisplayString):
    """Custom type tpgRemoteStStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TpgRemoteStStr_Type.__name__ = "DisplayString"
_TpgRemoteStStr_Object = MibTableColumn
tpgRemoteStStr = _TpgRemoteStStr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 2, 1, 13),
    _TpgRemoteStStr_Type()
)
tpgRemoteStStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpgRemoteStStr.setStatus("mandatory")
_TpgClientId_Type = Integer32
_TpgClientId_Object = MibScalar
tpgClientId = _TpgClientId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 3),
    _TpgClientId_Type()
)
tpgClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgClientId.setStatus("mandatory")
_TpgAuthKey_Type = Integer32
_TpgAuthKey_Object = MibScalar
tpgAuthKey = _TpgAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 4),
    _TpgAuthKey_Type()
)
tpgAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgAuthKey.setStatus("mandatory")


class _TpgBandwidth_Type(Integer32):
    """Custom type tpgBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgBandwidth_Type.__name__ = "Integer32"
_TpgBandwidth_Object = MibScalar
tpgBandwidth = _TpgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 5),
    _TpgBandwidth_Type()
)
tpgBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgBandwidth.setStatus("mandatory")
_TpgBandwidthVal_Type = Integer32
_TpgBandwidthVal_Object = MibScalar
tpgBandwidthVal = _TpgBandwidthVal_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 6),
    _TpgBandwidthVal_Type()
)
tpgBandwidthVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgBandwidthVal.setStatus("mandatory")


class _TpgConnServices_Type(Integer32):
    """Custom type tpgConnServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgConnServices_Type.__name__ = "Integer32"
_TpgConnServices_Object = MibScalar
tpgConnServices = _TpgConnServices_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 7),
    _TpgConnServices_Type()
)
tpgConnServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgConnServices.setStatus("mandatory")
_TpgConnServer_Type = IpAddress
_TpgConnServer_Object = MibScalar
tpgConnServer = _TpgConnServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 8),
    _TpgConnServer_Type()
)
tpgConnServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgConnServer.setStatus("mandatory")
_TpgConnServerPort_Type = Integer32
_TpgConnServerPort_Object = MibScalar
tpgConnServerPort = _TpgConnServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 9),
    _TpgConnServerPort_Type()
)
tpgConnServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgConnServerPort.setStatus("mandatory")
_TpgConnRetry_Type = Integer32
_TpgConnRetry_Object = MibScalar
tpgConnRetry = _TpgConnRetry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 10),
    _TpgConnRetry_Type()
)
tpgConnRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgConnRetry.setStatus("mandatory")
_TpgKeepAlive_Type = Integer32
_TpgKeepAlive_Object = MibScalar
tpgKeepAlive = _TpgKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 11),
    _TpgKeepAlive_Type()
)
tpgKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgKeepAlive.setStatus("mandatory")
_TpgSpagePrt_Type = Integer32
_TpgSpagePrt_Object = MibScalar
tpgSpagePrt = _TpgSpagePrt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 12),
    _TpgSpagePrt_Type()
)
tpgSpagePrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgSpagePrt.setStatus("mandatory")


class _TpgConnState_Type(Integer32):
    """Custom type tpgConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tpgINIT", 1),
          ("tpgCONNECT", 2),
          ("tpgREJECT", 3),
          ("tpgTIMEOUT", 4))
    )


_TpgConnState_Type.__name__ = "Integer32"
_TpgConnState_Object = MibScalar
tpgConnState = _TpgConnState_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 13),
    _TpgConnState_Type()
)
tpgConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpgConnState.setStatus("mandatory")


class _TpgStreamCompr_Type(Integer32):
    """Custom type tpgStreamCompr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgStreamCompr_Type.__name__ = "Integer32"
_TpgStreamCompr_Object = MibScalar
tpgStreamCompr = _TpgStreamCompr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 14),
    _TpgStreamCompr_Type()
)
tpgStreamCompr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgStreamCompr.setStatus("mandatory")


class _TpgSpage_Type(Integer32):
    """Custom type tpgSpage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgSpage_Type.__name__ = "Integer32"
_TpgSpage_Object = MibScalar
tpgSpage = _TpgSpage_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 15),
    _TpgSpage_Type()
)
tpgSpage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgSpage.setStatus("mandatory")


class _TpgPrtOpenToVal_Type(Integer32):
    """Custom type tpgPrtOpenToVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TpgPrtOpenToVal_Type.__name__ = "Integer32"
_TpgPrtOpenToVal_Object = MibScalar
tpgPrtOpenToVal = _TpgPrtOpenToVal_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 16),
    _TpgPrtOpenToVal_Type()
)
tpgPrtOpenToVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgPrtOpenToVal.setStatus("mandatory")


class _TpgJobSendTimeout_Type(Integer32):
    """Custom type tpgJobSendTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TpgJobSendTimeout_Type.__name__ = "Integer32"
_TpgJobSendTimeout_Object = MibScalar
tpgJobSendTimeout = _TpgJobSendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 17),
    _TpgJobSendTimeout_Type()
)
tpgJobSendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgJobSendTimeout.setStatus("mandatory")


class _TpgJobRecvTimeout_Type(Integer32):
    """Custom type tpgJobRecvTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TpgJobRecvTimeout_Type.__name__ = "Integer32"
_TpgJobRecvTimeout_Object = MibScalar
tpgJobRecvTimeout = _TpgJobRecvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 18),
    _TpgJobRecvTimeout_Type()
)
tpgJobRecvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgJobRecvTimeout.setStatus("mandatory")
_TpgMonitorPoll_Type = Integer32
_TpgMonitorPoll_Object = MibScalar
tpgMonitorPoll = _TpgMonitorPoll_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 20),
    _TpgMonitorPoll_Type()
)
tpgMonitorPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgMonitorPoll.setStatus("mandatory")


class _TpgMonitorPing_Type(Integer32):
    """Custom type tpgMonitorPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgMonitorPing_Type.__name__ = "Integer32"
_TpgMonitorPing_Object = MibScalar
tpgMonitorPing = _TpgMonitorPing_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 21),
    _TpgMonitorPing_Type()
)
tpgMonitorPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgMonitorPing.setStatus("mandatory")


class _TpgMonitorSnmp_Type(Integer32):
    """Custom type tpgMonitorSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TpgMonitorSnmp_Type.__name__ = "Integer32"
_TpgMonitorSnmp_Object = MibScalar
tpgMonitorSnmp = _TpgMonitorSnmp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 30, 22),
    _TpgMonitorSnmp_Type()
)
tpgMonitorSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpgMonitorSnmp.setStatus("mandatory")
_SehLrs_ObjectIdentity = ObjectIdentity
sehLrs = _SehLrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31)
)


class _LrsAesKey_Type(DisplayString):
    """Custom type lrsAesKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_LrsAesKey_Type.__name__ = "DisplayString"
_LrsAesKey_Object = MibScalar
lrsAesKey = _LrsAesKey_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 1),
    _LrsAesKey_Type()
)
lrsAesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsAesKey.setStatus("mandatory")


class _LrsAesType_Type(Integer32):
    """Custom type lrsAesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              24,
              32)
        )
    )
    namedValues = NamedValues(
        *(("aes16", 16),
          ("aes24", 24),
          ("aes32", 32))
    )


_LrsAesType_Type.__name__ = "Integer32"
_LrsAesType_Object = MibScalar
lrsAesType = _LrsAesType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 2),
    _LrsAesType_Type()
)
lrsAesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsAesType.setStatus("mandatory")
_LrsIsppPort_Type = Integer32
_LrsIsppPort_Object = MibScalar
lrsIsppPort = _LrsIsppPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 3),
    _LrsIsppPort_Type()
)
lrsIsppPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsIsppPort.setStatus("mandatory")


class _LrsUseInstallationKey_Type(Integer32):
    """Custom type lrsUseInstallationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LrsUseInstallationKey_Type.__name__ = "Integer32"
_LrsUseInstallationKey_Object = MibScalar
lrsUseInstallationKey = _LrsUseInstallationKey_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 4),
    _LrsUseInstallationKey_Type()
)
lrsUseInstallationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsUseInstallationKey.setStatus("mandatory")


class _LrsAllowKeyChange_Type(Integer32):
    """Custom type lrsAllowKeyChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LrsAllowKeyChange_Type.__name__ = "Integer32"
_LrsAllowKeyChange_Object = MibScalar
lrsAllowKeyChange = _LrsAllowKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 5),
    _LrsAllowKeyChange_Type()
)
lrsAllowKeyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsAllowKeyChange.setStatus("mandatory")
_LrsPrtPort_Type = Integer32
_LrsPrtPort_Object = MibScalar
lrsPrtPort = _LrsPrtPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 31, 6),
    _LrsPrtPort_Type()
)
lrsPrtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrsPrtPort.setStatus("mandatory")
_SehProtection_ObjectIdentity = ObjectIdentity
sehProtection = _SehProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40)
)


class _Protection_Type(Integer32):
    """Custom type protection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Protection_Type.__name__ = "Integer32"
_Protection_Object = MibScalar
protection = _Protection_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 1),
    _Protection_Type()
)
protection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protection.setStatus("mandatory")


class _ProtectionTest_Type(Integer32):
    """Custom type protectionTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ProtectionTest_Type.__name__ = "Integer32"
_ProtectionTest_Object = MibScalar
protectionTest = _ProtectionTest_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 2),
    _ProtectionTest_Type()
)
protectionTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionTest.setStatus("mandatory")


class _ProtectionLevel_Type(Integer32):
    """Custom type protectionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protectall", 1),
          ("protecttcp", 2),
          ("protectutn", 3))
    )


_ProtectionLevel_Type.__name__ = "Integer32"
_ProtectionLevel_Object = MibScalar
protectionLevel = _ProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 3),
    _ProtectionLevel_Type()
)
protectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionLevel.setStatus("mandatory")
_IpFilterNumber_Type = Integer32
_IpFilterNumber_Object = MibScalar
ipFilterNumber = _IpFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 10),
    _IpFilterNumber_Type()
)
ipFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterNumber.setStatus("mandatory")
_IpFilterTable_Object = MibTable
ipFilterTable = _IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 11)
)
if mibBuilder.loadTexts:
    ipFilterTable.setStatus("mandatory")
_IpFilterEntry_Object = MibTableRow
ipFilterEntry = _IpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 11, 1)
)
ipFilterEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipFilterIndex"),
)
if mibBuilder.loadTexts:
    ipFilterEntry.setStatus("mandatory")


class _IpFilterIndex_Type(Integer32):
    """Custom type ipFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpFilterIndex_Type.__name__ = "Integer32"
_IpFilterIndex_Object = MibTableColumn
ipFilterIndex = _IpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 11, 1, 1),
    _IpFilterIndex_Type()
)
ipFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterIndex.setStatus("mandatory")


class _IpFilterOnOff_Type(Integer32):
    """Custom type ipFilterOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_IpFilterOnOff_Type.__name__ = "Integer32"
_IpFilterOnOff_Object = MibTableColumn
ipFilterOnOff = _IpFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 11, 1, 2),
    _IpFilterOnOff_Type()
)
ipFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterOnOff.setStatus("mandatory")


class _IpFilterAddr_Type(DisplayString):
    """Custom type ipFilterAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IpFilterAddr_Type.__name__ = "DisplayString"
_IpFilterAddr_Object = MibTableColumn
ipFilterAddr = _IpFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 11, 1, 3),
    _IpFilterAddr_Type()
)
ipFilterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterAddr.setStatus("mandatory")
_MacFilterNumber_Type = Integer32
_MacFilterNumber_Object = MibScalar
macFilterNumber = _MacFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 12),
    _MacFilterNumber_Type()
)
macFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterNumber.setStatus("mandatory")
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 13)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("mandatory")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 13, 1)
)
macFilterEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "macFilterIndex"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("mandatory")


class _MacFilterIndex_Type(Integer32):
    """Custom type macFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MacFilterIndex_Type.__name__ = "Integer32"
_MacFilterIndex_Object = MibTableColumn
macFilterIndex = _MacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 13, 1, 1),
    _MacFilterIndex_Type()
)
macFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterIndex.setStatus("mandatory")


class _MacFilterOnOff_Type(Integer32):
    """Custom type macFilterOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MacFilterOnOff_Type.__name__ = "Integer32"
_MacFilterOnOff_Object = MibTableColumn
macFilterOnOff = _MacFilterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 13, 1, 2),
    _MacFilterOnOff_Type()
)
macFilterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterOnOff.setStatus("mandatory")


class _MacFilterAddr_Type(PhysAddress):
    """Custom type macFilterAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_MacFilterAddr_Type.__name__ = "PhysAddress"
_MacFilterAddr_Object = MibTableColumn
macFilterAddr = _MacFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 13, 1, 3),
    _MacFilterAddr_Type()
)
macFilterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterAddr.setStatus("mandatory")


class _CipherStrength_Type(Integer32):
    """Custom type cipherStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("default", 4))
    )


_CipherStrength_Type.__name__ = "Integer32"
_CipherStrength_Object = MibScalar
cipherStrength = _CipherStrength_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 20),
    _CipherStrength_Type()
)
cipherStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipherStrength.setStatus("mandatory")


class _RsaBits_Type(Integer32):
    """Custom type rsaBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(512,
              768,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("low", 512),
          ("middle", 768),
          ("default", 1024),
          ("high", 2048))
    )


_RsaBits_Type.__name__ = "Integer32"
_RsaBits_Object = MibScalar
rsaBits = _RsaBits_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 40, 21),
    _RsaBits_Type()
)
rsaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsaBits.setStatus("mandatory")
_SehUser_ObjectIdentity = ObjectIdentity
sehUser = _SehUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41)
)


class _UsrAnyName_Type(DisplayString):
    """Custom type usrAnyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UsrAnyName_Type.__name__ = "DisplayString"
_UsrAnyName_Object = MibScalar
usrAnyName = _UsrAnyName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 1),
    _UsrAnyName_Type()
)
usrAnyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAnyName.setStatus("mandatory")


class _UsrAnyPwd_Type(DisplayString):
    """Custom type usrAnyPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UsrAnyPwd_Type.__name__ = "DisplayString"
_UsrAnyPwd_Object = MibScalar
usrAnyPwd = _UsrAnyPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 2),
    _UsrAnyPwd_Type()
)
usrAnyPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAnyPwd.setStatus("mandatory")


class _UsrAnyAcc_Type(Integer32):
    """Custom type usrAnyAcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_UsrAnyAcc_Type.__name__ = "Integer32"
_UsrAnyAcc_Object = MibScalar
usrAnyAcc = _UsrAnyAcc_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 3),
    _UsrAnyAcc_Type()
)
usrAnyAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAnyAcc.setStatus("mandatory")


class _UsrAnyHash_Type(Integer32):
    """Custom type usrAnyHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_UsrAnyHash_Type.__name__ = "Integer32"
_UsrAnyHash_Object = MibScalar
usrAnyHash = _UsrAnyHash_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 4),
    _UsrAnyHash_Type()
)
usrAnyHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAnyHash.setStatus("mandatory")


class _UsrAnyCypher_Type(Integer32):
    """Custom type usrAnyCypher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("aes", 2),
          ("des", 3))
    )


_UsrAnyCypher_Type.__name__ = "Integer32"
_UsrAnyCypher_Object = MibScalar
usrAnyCypher = _UsrAnyCypher_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 5),
    _UsrAnyCypher_Type()
)
usrAnyCypher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAnyCypher.setStatus("mandatory")


class _UsrAdminName_Type(DisplayString):
    """Custom type usrAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UsrAdminName_Type.__name__ = "DisplayString"
_UsrAdminName_Object = MibScalar
usrAdminName = _UsrAdminName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 11),
    _UsrAdminName_Type()
)
usrAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAdminName.setStatus("mandatory")


class _UsrAdminPwd_Type(DisplayString):
    """Custom type usrAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_UsrAdminPwd_Type.__name__ = "DisplayString"
_UsrAdminPwd_Object = MibScalar
usrAdminPwd = _UsrAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 12),
    _UsrAdminPwd_Type()
)
usrAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAdminPwd.setStatus("mandatory")


class _UsrAdminAcc_Type(Integer32):
    """Custom type usrAdminAcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_UsrAdminAcc_Type.__name__ = "Integer32"
_UsrAdminAcc_Object = MibScalar
usrAdminAcc = _UsrAdminAcc_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 13),
    _UsrAdminAcc_Type()
)
usrAdminAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAdminAcc.setStatus("mandatory")


class _UsrAdminHash_Type(Integer32):
    """Custom type usrAdminHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2))
    )


_UsrAdminHash_Type.__name__ = "Integer32"
_UsrAdminHash_Object = MibScalar
usrAdminHash = _UsrAdminHash_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 14),
    _UsrAdminHash_Type()
)
usrAdminHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAdminHash.setStatus("mandatory")


class _UsrAdminCypher_Type(Integer32):
    """Custom type usrAdminCypher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("aes", 2),
          ("des", 3))
    )


_UsrAdminCypher_Type.__name__ = "Integer32"
_UsrAdminCypher_Object = MibScalar
usrAdminCypher = _UsrAdminCypher_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 41, 15),
    _UsrAdminCypher_Type()
)
usrAdminCypher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAdminCypher.setStatus("mandatory")
_SehIPsec_ObjectIdentity = ObjectIdentity
sehIPsec = _SehIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42)
)


class _IpsecIPsec_Type(Integer32):
    """Custom type ipsecIPsec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecIPsec_Type.__name__ = "Integer32"
_IpsecIPsec_Object = MibScalar
ipsecIPsec = _IpsecIPsec_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 1),
    _IpsecIPsec_Type()
)
ipsecIPsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIPsec.setStatus("mandatory")


class _IpsecConfig_Type(Integer32):
    """Custom type ipsecConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rules", 0),
          ("files", 1))
    )


_IpsecConfig_Type.__name__ = "Integer32"
_IpsecConfig_Object = MibScalar
ipsecConfig = _IpsecConfig_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 2),
    _IpsecConfig_Type()
)
ipsecConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecConfig.setStatus("mandatory")


class _IpsecDefAction_Type(Integer32):
    """Custom type ipsecDefAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("drop", 1))
    )


_IpsecDefAction_Type.__name__ = "Integer32"
_IpsecDefAction_Object = MibScalar
ipsecDefAction = _IpsecDefAction_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 3),
    _IpsecDefAction_Type()
)
ipsecDefAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecDefAction.setStatus("mandatory")
_IpsecRulesNumber_Type = Integer32
_IpsecRulesNumber_Object = MibScalar
ipsecRulesNumber = _IpsecRulesNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 4),
    _IpsecRulesNumber_Type()
)
ipsecRulesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecRulesNumber.setStatus("mandatory")
_IpsecRulesTable_Object = MibTable
ipsecRulesTable = _IpsecRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5)
)
if mibBuilder.loadTexts:
    ipsecRulesTable.setStatus("mandatory")
_IpsecRulesEntry_Object = MibTableRow
ipsecRulesEntry = _IpsecRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1)
)
ipsecRulesEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipsecRulesIndex"),
)
if mibBuilder.loadTexts:
    ipsecRulesEntry.setStatus("mandatory")


class _IpsecRulesIndex_Type(Integer32):
    """Custom type ipsecRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecRulesIndex_Type.__name__ = "Integer32"
_IpsecRulesIndex_Object = MibTableColumn
ipsecRulesIndex = _IpsecRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 1),
    _IpsecRulesIndex_Type()
)
ipsecRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecRulesIndex.setStatus("mandatory")


class _IpsecRulesEnabled_Type(Integer32):
    """Custom type ipsecRulesEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecRulesEnabled_Type.__name__ = "Integer32"
_IpsecRulesEnabled_Object = MibTableColumn
ipsecRulesEnabled = _IpsecRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 2),
    _IpsecRulesEnabled_Type()
)
ipsecRulesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRulesEnabled.setStatus("mandatory")


class _IpsecRulesIaddr_Type(Integer32):
    """Custom type ipsecRulesIaddr based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("addrtmpl1", 1),
          ("addrtmpl2", 2),
          ("addrtmpl3", 3),
          ("addrtmpl4", 4),
          ("addrtmpl5", 5),
          ("addrtmpl6", 6),
          ("addrtmpl7", 7),
          ("addrtmpl8", 8))
    )


_IpsecRulesIaddr_Type.__name__ = "Integer32"
_IpsecRulesIaddr_Object = MibTableColumn
ipsecRulesIaddr = _IpsecRulesIaddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 3),
    _IpsecRulesIaddr_Type()
)
ipsecRulesIaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRulesIaddr.setStatus("mandatory")


class _IpsecRulesIserv_Type(Integer32):
    """Custom type ipsecRulesIserv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("servtmpl1", 1),
          ("servtmpl2", 2),
          ("servtmpl3", 3),
          ("servtmpl4", 4))
    )


_IpsecRulesIserv_Type.__name__ = "Integer32"
_IpsecRulesIserv_Object = MibTableColumn
ipsecRulesIserv = _IpsecRulesIserv_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 4),
    _IpsecRulesIserv_Type()
)
ipsecRulesIserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRulesIserv.setStatus("mandatory")


class _IpsecRulesIPsec_Type(Integer32):
    """Custom type ipsecRulesIPsec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipsectmpl1", 1),
          ("ipsectmpl2", 2),
          ("ipsectmpl3", 3),
          ("ipsectmpl4", 4))
    )


_IpsecRulesIPsec_Type.__name__ = "Integer32"
_IpsecRulesIPsec_Object = MibTableColumn
ipsecRulesIPsec = _IpsecRulesIPsec_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 5),
    _IpsecRulesIPsec_Type()
)
ipsecRulesIPsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRulesIPsec.setStatus("mandatory")


class _IpsecRulesAction_Type(Integer32):
    """Custom type ipsecRulesAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("drop", 1),
          ("requie", 2))
    )


_IpsecRulesAction_Type.__name__ = "Integer32"
_IpsecRulesAction_Object = MibTableColumn
ipsecRulesAction = _IpsecRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 5, 1, 6),
    _IpsecRulesAction_Type()
)
ipsecRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRulesAction.setStatus("mandatory")
_IpsecAddrTmplNumber_Type = Integer32
_IpsecAddrTmplNumber_Object = MibScalar
ipsecAddrTmplNumber = _IpsecAddrTmplNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 6),
    _IpsecAddrTmplNumber_Type()
)
ipsecAddrTmplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAddrTmplNumber.setStatus("mandatory")
_IpsecAddrTmplTable_Object = MibTable
ipsecAddrTmplTable = _IpsecAddrTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7)
)
if mibBuilder.loadTexts:
    ipsecAddrTmplTable.setStatus("mandatory")
_IpsecAddrTmplEntry_Object = MibTableRow
ipsecAddrTmplEntry = _IpsecAddrTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1)
)
ipsecAddrTmplEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipsecAddrTmplIndex"),
)
if mibBuilder.loadTexts:
    ipsecAddrTmplEntry.setStatus("mandatory")


class _IpsecAddrTmplIndex_Type(Integer32):
    """Custom type ipsecAddrTmplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecAddrTmplIndex_Type.__name__ = "Integer32"
_IpsecAddrTmplIndex_Object = MibTableColumn
ipsecAddrTmplIndex = _IpsecAddrTmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1, 1),
    _IpsecAddrTmplIndex_Type()
)
ipsecAddrTmplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAddrTmplIndex.setStatus("mandatory")


class _IpsecAddrTmplName_Type(DisplayString):
    """Custom type ipsecAddrTmplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpsecAddrTmplName_Type.__name__ = "DisplayString"
_IpsecAddrTmplName_Object = MibTableColumn
ipsecAddrTmplName = _IpsecAddrTmplName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1, 2),
    _IpsecAddrTmplName_Type()
)
ipsecAddrTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecAddrTmplName.setStatus("mandatory")


class _IpsecAddrTmplRemoteIPv4_Type(DisplayString):
    """Custom type ipsecAddrTmplRemoteIPv4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_IpsecAddrTmplRemoteIPv4_Type.__name__ = "DisplayString"
_IpsecAddrTmplRemoteIPv4_Object = MibTableColumn
ipsecAddrTmplRemoteIPv4 = _IpsecAddrTmplRemoteIPv4_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1, 3),
    _IpsecAddrTmplRemoteIPv4_Type()
)
ipsecAddrTmplRemoteIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecAddrTmplRemoteIPv4.setStatus("mandatory")


class _IpsecAddrTmplLocalIPv6_Type(DisplayString):
    """Custom type ipsecAddrTmplLocalIPv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_IpsecAddrTmplLocalIPv6_Type.__name__ = "DisplayString"
_IpsecAddrTmplLocalIPv6_Object = MibTableColumn
ipsecAddrTmplLocalIPv6 = _IpsecAddrTmplLocalIPv6_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1, 4),
    _IpsecAddrTmplLocalIPv6_Type()
)
ipsecAddrTmplLocalIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecAddrTmplLocalIPv6.setStatus("mandatory")


class _IpsecAddrTmplRemoteIPv6_Type(DisplayString):
    """Custom type ipsecAddrTmplRemoteIPv6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_IpsecAddrTmplRemoteIPv6_Type.__name__ = "DisplayString"
_IpsecAddrTmplRemoteIPv6_Object = MibTableColumn
ipsecAddrTmplRemoteIPv6 = _IpsecAddrTmplRemoteIPv6_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 7, 1, 5),
    _IpsecAddrTmplRemoteIPv6_Type()
)
ipsecAddrTmplRemoteIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecAddrTmplRemoteIPv6.setStatus("mandatory")
_IpsecServTmplNumber_Type = Integer32
_IpsecServTmplNumber_Object = MibScalar
ipsecServTmplNumber = _IpsecServTmplNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 8),
    _IpsecServTmplNumber_Type()
)
ipsecServTmplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecServTmplNumber.setStatus("mandatory")
_IpsecServTmplTable_Object = MibTable
ipsecServTmplTable = _IpsecServTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 9)
)
if mibBuilder.loadTexts:
    ipsecServTmplTable.setStatus("mandatory")
_IpsecServTmplEntry_Object = MibTableRow
ipsecServTmplEntry = _IpsecServTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 9, 1)
)
ipsecServTmplEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipsecServTmplIndex"),
)
if mibBuilder.loadTexts:
    ipsecServTmplEntry.setStatus("mandatory")


class _IpsecServTmplIndex_Type(Integer32):
    """Custom type ipsecServTmplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecServTmplIndex_Type.__name__ = "Integer32"
_IpsecServTmplIndex_Object = MibTableColumn
ipsecServTmplIndex = _IpsecServTmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 9, 1, 1),
    _IpsecServTmplIndex_Type()
)
ipsecServTmplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecServTmplIndex.setStatus("mandatory")


class _IpsecServTmplName_Type(DisplayString):
    """Custom type ipsecServTmplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpsecServTmplName_Type.__name__ = "DisplayString"
_IpsecServTmplName_Object = MibTableColumn
ipsecServTmplName = _IpsecServTmplName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 9, 1, 2),
    _IpsecServTmplName_Type()
)
ipsecServTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecServTmplName.setStatus("mandatory")


class _IpsecServTmplServ_Type(DisplayString):
    """Custom type ipsecServTmplServ based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IpsecServTmplServ_Type.__name__ = "DisplayString"
_IpsecServTmplServ_Object = MibTableColumn
ipsecServTmplServ = _IpsecServTmplServ_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 9, 1, 3),
    _IpsecServTmplServ_Type()
)
ipsecServTmplServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecServTmplServ.setStatus("mandatory")
_IpsecSATmplNumber_Type = Integer32
_IpsecSATmplNumber_Object = MibScalar
ipsecSATmplNumber = _IpsecSATmplNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 10),
    _IpsecSATmplNumber_Type()
)
ipsecSATmplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSATmplNumber.setStatus("mandatory")
_IpsecSATmplTable_Object = MibTable
ipsecSATmplTable = _IpsecSATmplTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11)
)
if mibBuilder.loadTexts:
    ipsecSATmplTable.setStatus("mandatory")
_IpsecSATmplEntry_Object = MibTableRow
ipsecSATmplEntry = _IpsecSATmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1)
)
ipsecSATmplEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipsecSATmplIndex"),
)
if mibBuilder.loadTexts:
    ipsecSATmplEntry.setStatus("mandatory")


class _IpsecSATmplIndex_Type(Integer32):
    """Custom type ipsecSATmplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecSATmplIndex_Type.__name__ = "Integer32"
_IpsecSATmplIndex_Object = MibTableColumn
ipsecSATmplIndex = _IpsecSATmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 1),
    _IpsecSATmplIndex_Type()
)
ipsecSATmplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSATmplIndex.setStatus("mandatory")


class _IpsecSATmplName_Type(DisplayString):
    """Custom type ipsecSATmplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpsecSATmplName_Type.__name__ = "DisplayString"
_IpsecSATmplName_Object = MibTableColumn
ipsecSATmplName = _IpsecSATmplName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 2),
    _IpsecSATmplName_Type()
)
ipsecSATmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSATmplName.setStatus("mandatory")


class _IpsecSATmplCert_Type(Integer32):
    """Custom type ipsecSATmplCert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("psk", 0),
          ("certificate", 1))
    )


_IpsecSATmplCert_Type.__name__ = "Integer32"
_IpsecSATmplCert_Object = MibTableColumn
ipsecSATmplCert = _IpsecSATmplCert_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 3),
    _IpsecSATmplCert_Type()
)
ipsecSATmplCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSATmplCert.setStatus("mandatory")


class _IpsecSATmplVeri_Type(Integer32):
    """Custom type ipsecSATmplVeri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecSATmplVeri_Type.__name__ = "Integer32"
_IpsecSATmplVeri_Object = MibTableColumn
ipsecSATmplVeri = _IpsecSATmplVeri_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 4),
    _IpsecSATmplVeri_Type()
)
ipsecSATmplVeri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSATmplVeri.setStatus("mandatory")


class _IpsecSATmplPSK_Type(DisplayString):
    """Custom type ipsecSATmplPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpsecSATmplPSK_Type.__name__ = "DisplayString"
_IpsecSATmplPSK_Object = MibTableColumn
ipsecSATmplPSK = _IpsecSATmplPSK_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 5),
    _IpsecSATmplPSK_Type()
)
ipsecSATmplPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSATmplPSK.setStatus("mandatory")


class _IpsecSATmplIKE_Type(Integer32):
    """Custom type ipsecSATmplIKE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("iketmpl1", 1),
          ("iketmpl2", 2),
          ("iketmpl3", 3),
          ("iketmpl4", 4))
    )


_IpsecSATmplIKE_Type.__name__ = "Integer32"
_IpsecSATmplIKE_Object = MibTableColumn
ipsecSATmplIKE = _IpsecSATmplIKE_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 11, 1, 6),
    _IpsecSATmplIKE_Type()
)
ipsecSATmplIKE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSATmplIKE.setStatus("mandatory")
_IpsecIKETmplNumber_Type = Integer32
_IpsecIKETmplNumber_Object = MibScalar
ipsecIKETmplNumber = _IpsecIKETmplNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 12),
    _IpsecIKETmplNumber_Type()
)
ipsecIKETmplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIKETmplNumber.setStatus("mandatory")
_IpsecIKETmplTable_Object = MibTable
ipsecIKETmplTable = _IpsecIKETmplTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13)
)
if mibBuilder.loadTexts:
    ipsecIKETmplTable.setStatus("mandatory")
_IpsecIKETmplEntry_Object = MibTableRow
ipsecIKETmplEntry = _IpsecIKETmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1)
)
ipsecIKETmplEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ipsecIKETmplIndex"),
)
if mibBuilder.loadTexts:
    ipsecIKETmplEntry.setStatus("mandatory")


class _IpsecIKETmplIndex_Type(Integer32):
    """Custom type ipsecIKETmplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecIKETmplIndex_Type.__name__ = "Integer32"
_IpsecIKETmplIndex_Object = MibTableColumn
ipsecIKETmplIndex = _IpsecIKETmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 1),
    _IpsecIKETmplIndex_Type()
)
ipsecIKETmplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIKETmplIndex.setStatus("mandatory")


class _IpsecIKETmplName_Type(DisplayString):
    """Custom type ipsecIKETmplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpsecIKETmplName_Type.__name__ = "DisplayString"
_IpsecIKETmplName_Object = MibTableColumn
ipsecIKETmplName = _IpsecIKETmplName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 2),
    _IpsecIKETmplName_Type()
)
ipsecIKETmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplName.setStatus("mandatory")


class _IpsecIKETmplModes_Type(DisplayString):
    """Custom type ipsecIKETmplModes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IpsecIKETmplModes_Type.__name__ = "DisplayString"
_IpsecIKETmplModes_Object = MibTableColumn
ipsecIKETmplModes = _IpsecIKETmplModes_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 3),
    _IpsecIKETmplModes_Type()
)
ipsecIKETmplModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplModes.setStatus("mandatory")


class _IpsecIKETmplDhGroup_Type(Integer32):
    """Custom type ipsecIKETmplDhGroup based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("modp768", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6),
          ("modp6144", 7),
          ("modp8192", 8))
    )


_IpsecIKETmplDhGroup_Type.__name__ = "Integer32"
_IpsecIKETmplDhGroup_Object = MibTableColumn
ipsecIKETmplDhGroup = _IpsecIKETmplDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 4),
    _IpsecIKETmplDhGroup_Type()
)
ipsecIKETmplDhGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplDhGroup.setStatus("mandatory")


class _IpsecIKETmplEncV1_Type(Integer32):
    """Custom type ipsecIKETmplEncV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("tripledes", 1),
          ("aes", 2),
          ("cast128", 3))
    )


_IpsecIKETmplEncV1_Type.__name__ = "Integer32"
_IpsecIKETmplEncV1_Object = MibTableColumn
ipsecIKETmplEncV1 = _IpsecIKETmplEncV1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 5),
    _IpsecIKETmplEncV1_Type()
)
ipsecIKETmplEncV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplEncV1.setStatus("mandatory")


class _IpsecIKETmplAuthV1_Type(Integer32):
    """Custom type ipsecIKETmplAuthV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha1", 1),
          ("sha256", 2),
          ("sha384", 3),
          ("sha512", 4))
    )


_IpsecIKETmplAuthV1_Type.__name__ = "Integer32"
_IpsecIKETmplAuthV1_Object = MibTableColumn
ipsecIKETmplAuthV1 = _IpsecIKETmplAuthV1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 6),
    _IpsecIKETmplAuthV1_Type()
)
ipsecIKETmplAuthV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplAuthV1.setStatus("mandatory")


class _IpsecIKETmplLtV1_Type(DisplayString):
    """Custom type ipsecIKETmplLtV1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_IpsecIKETmplLtV1_Type.__name__ = "DisplayString"
_IpsecIKETmplLtV1_Object = MibTableColumn
ipsecIKETmplLtV1 = _IpsecIKETmplLtV1_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 7),
    _IpsecIKETmplLtV1_Type()
)
ipsecIKETmplLtV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplLtV1.setStatus("mandatory")


class _IpsecIKETmplEncMode_Type(Integer32):
    """Custom type ipsecIKETmplEncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("transport", 0)
    )


_IpsecIKETmplEncMode_Type.__name__ = "Integer32"
_IpsecIKETmplEncMode_Object = MibTableColumn
ipsecIKETmplEncMode = _IpsecIKETmplEncMode_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 8),
    _IpsecIKETmplEncMode_Type()
)
ipsecIKETmplEncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplEncMode.setStatus("mandatory")


class _IpsecIKETmplPfsGroup_Type(Integer32):
    """Custom type ipsecIKETmplPfsGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("nopfs", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("modp1536", 3),
          ("modp2048", 4),
          ("modp3072", 5),
          ("modp4096", 6),
          ("modp6144", 7),
          ("modp8192", 8))
    )


_IpsecIKETmplPfsGroup_Type.__name__ = "Integer32"
_IpsecIKETmplPfsGroup_Object = MibTableColumn
ipsecIKETmplPfsGroup = _IpsecIKETmplPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 9),
    _IpsecIKETmplPfsGroup_Type()
)
ipsecIKETmplPfsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplPfsGroup.setStatus("mandatory")


class _IpsecIKETmplEncV2_Type(DisplayString):
    """Custom type ipsecIKETmplEncV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IpsecIKETmplEncV2_Type.__name__ = "DisplayString"
_IpsecIKETmplEncV2_Object = MibTableColumn
ipsecIKETmplEncV2 = _IpsecIKETmplEncV2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 10),
    _IpsecIKETmplEncV2_Type()
)
ipsecIKETmplEncV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplEncV2.setStatus("mandatory")


class _IpsecIKETmplAuthV2_Type(DisplayString):
    """Custom type ipsecIKETmplAuthV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IpsecIKETmplAuthV2_Type.__name__ = "DisplayString"
_IpsecIKETmplAuthV2_Object = MibTableColumn
ipsecIKETmplAuthV2 = _IpsecIKETmplAuthV2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 11),
    _IpsecIKETmplAuthV2_Type()
)
ipsecIKETmplAuthV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplAuthV2.setStatus("mandatory")


class _IpsecIKETmplAH_Type(Integer32):
    """Custom type ipsecIKETmplAH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecIKETmplAH_Type.__name__ = "Integer32"
_IpsecIKETmplAH_Object = MibTableColumn
ipsecIKETmplAH = _IpsecIKETmplAH_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 12),
    _IpsecIKETmplAH_Type()
)
ipsecIKETmplAH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplAH.setStatus("mandatory")


class _IpsecIKETmplLtV2_Type(DisplayString):
    """Custom type ipsecIKETmplLtV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_IpsecIKETmplLtV2_Type.__name__ = "DisplayString"
_IpsecIKETmplLtV2_Object = MibTableColumn
ipsecIKETmplLtV2 = _IpsecIKETmplLtV2_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 13),
    _IpsecIKETmplLtV2_Type()
)
ipsecIKETmplLtV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplLtV2.setStatus("mandatory")


class _IpsecIKETmplLtKb_Type(DisplayString):
    """Custom type ipsecIKETmplLtKb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_IpsecIKETmplLtKb_Type.__name__ = "DisplayString"
_IpsecIKETmplLtKb_Object = MibTableColumn
ipsecIKETmplLtKb = _IpsecIKETmplLtKb_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 13, 1, 14),
    _IpsecIKETmplLtKb_Type()
)
ipsecIKETmplLtKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecIKETmplLtKb.setStatus("mandatory")


class _IpsecDHCP_Type(Integer32):
    """Custom type ipsecDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecDHCP_Type.__name__ = "Integer32"
_IpsecDHCP_Object = MibScalar
ipsecDHCP = _IpsecDHCP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 14),
    _IpsecDHCP_Type()
)
ipsecDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecDHCP.setStatus("mandatory")


class _IpsecNetbios_Type(Integer32):
    """Custom type ipsecNetbios based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecNetbios_Type.__name__ = "Integer32"
_IpsecNetbios_Object = MibScalar
ipsecNetbios = _IpsecNetbios_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 15),
    _IpsecNetbios_Type()
)
ipsecNetbios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecNetbios.setStatus("mandatory")


class _IpsecBonjour_Type(Integer32):
    """Custom type ipsecBonjour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecBonjour_Type.__name__ = "Integer32"
_IpsecBonjour_Object = MibScalar
ipsecBonjour = _IpsecBonjour_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 16),
    _IpsecBonjour_Type()
)
ipsecBonjour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecBonjour.setStatus("mandatory")


class _IpsecSLP_Type(Integer32):
    """Custom type ipsecSLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecSLP_Type.__name__ = "Integer32"
_IpsecSLP_Object = MibScalar
ipsecSLP = _IpsecSLP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 17),
    _IpsecSLP_Type()
)
ipsecSLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecSLP.setStatus("mandatory")


class _IpsecFTP_Type(Integer32):
    """Custom type ipsecFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecFTP_Type.__name__ = "Integer32"
_IpsecFTP_Object = MibScalar
ipsecFTP = _IpsecFTP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 18),
    _IpsecFTP_Type()
)
ipsecFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecFTP.setStatus("mandatory")


class _IpsecTest_Type(Integer32):
    """Custom type ipsecTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpsecTest_Type.__name__ = "Integer32"
_IpsecTest_Object = MibScalar
ipsecTest = _IpsecTest_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 42, 19),
    _IpsecTest_Type()
)
ipsecTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecTest.setStatus("mandatory")
_SehIpVLan_ObjectIdentity = ObjectIdentity
sehIpVLan = _SehIpVLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43)
)
_Ip4VLanNumber_Type = Integer32
_Ip4VLanNumber_Object = MibScalar
ip4VLanNumber = _Ip4VLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 1),
    _Ip4VLanNumber_Type()
)
ip4VLanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip4VLanNumber.setStatus("mandatory")
_Ip4VLanTable_Object = MibTable
ip4VLanTable = _Ip4VLanTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2)
)
if mibBuilder.loadTexts:
    ip4VLanTable.setStatus("mandatory")
_Ip4VLanEntry_Object = MibTableRow
ip4VLanEntry = _Ip4VLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1)
)
ip4VLanEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "ip4VLanIndex"),
)
if mibBuilder.loadTexts:
    ip4VLanEntry.setStatus("mandatory")


class _Ip4VLanIndex_Type(Integer32):
    """Custom type ip4VLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Ip4VLanIndex_Type.__name__ = "Integer32"
_Ip4VLanIndex_Object = MibTableColumn
ip4VLanIndex = _Ip4VLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 1),
    _Ip4VLanIndex_Type()
)
ip4VLanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ip4VLanIndex.setStatus("mandatory")


class _Ip4VLanOnOff_Type(Integer32):
    """Custom type ip4VLanOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Ip4VLanOnOff_Type.__name__ = "Integer32"
_Ip4VLanOnOff_Object = MibTableColumn
ip4VLanOnOff = _Ip4VLanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 2),
    _Ip4VLanOnOff_Type()
)
ip4VLanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanOnOff.setStatus("mandatory")


class _Ip4VLanAddr_Type(DisplayString):
    """Custom type ip4VLanAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ip4VLanAddr_Type.__name__ = "DisplayString"
_Ip4VLanAddr_Object = MibTableColumn
ip4VLanAddr = _Ip4VLanAddr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 3),
    _Ip4VLanAddr_Type()
)
ip4VLanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanAddr.setStatus("mandatory")


class _Ip4VLanMask_Type(DisplayString):
    """Custom type ip4VLanMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ip4VLanMask_Type.__name__ = "DisplayString"
_Ip4VLanMask_Object = MibTableColumn
ip4VLanMask = _Ip4VLanMask_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 4),
    _Ip4VLanMask_Type()
)
ip4VLanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanMask.setStatus("mandatory")


class _Ip4VLanID_Type(Integer32):
    """Custom type ip4VLanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ip4VLanID_Type.__name__ = "Integer32"
_Ip4VLanID_Object = MibTableColumn
ip4VLanID = _Ip4VLanID_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 5),
    _Ip4VLanID_Type()
)
ip4VLanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanID.setStatus("mandatory")


class _Ip4VLanGate_Type(DisplayString):
    """Custom type ip4VLanGate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ip4VLanGate_Type.__name__ = "DisplayString"
_Ip4VLanGate_Object = MibTableColumn
ip4VLanGate = _Ip4VLanGate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 2, 1, 6),
    _Ip4VLanGate_Type()
)
ip4VLanGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanGate.setStatus("mandatory")


class _Ip4VLanWeb_Type(Integer32):
    """Custom type ip4VLanWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ip4VLanWeb_Type.__name__ = "Integer32"
_Ip4VLanWeb_Object = MibScalar
ip4VLanWeb = _Ip4VLanWeb_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 3),
    _Ip4VLanWeb_Type()
)
ip4VLanWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanWeb.setStatus("mandatory")


class _Ip4VLanSNMP_Type(Integer32):
    """Custom type ip4VLanSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ip4VLanSNMP_Type.__name__ = "Integer32"
_Ip4VLanSNMP_Object = MibScalar
ip4VLanSNMP = _Ip4VLanSNMP_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 4),
    _Ip4VLanSNMP_Type()
)
ip4VLanSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanSNMP.setStatus("mandatory")


class _Ip4VLanMgmt_Type(Integer32):
    """Custom type ip4VLanMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ip4VLanMgmt_Type.__name__ = "Integer32"
_Ip4VLanMgmt_Object = MibScalar
ip4VLanMgmt = _Ip4VLanMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 10),
    _Ip4VLanMgmt_Type()
)
ip4VLanMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanMgmt.setStatus("mandatory")


class _Ip4VLanMgmtID_Type(Integer32):
    """Custom type ip4VLanMgmtID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Ip4VLanMgmtID_Type.__name__ = "Integer32"
_Ip4VLanMgmtID_Object = MibScalar
ip4VLanMgmtID = _Ip4VLanMgmtID_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 11),
    _Ip4VLanMgmtID_Type()
)
ip4VLanMgmtID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanMgmtID.setStatus("mandatory")


class _Ip4VLanMgmtAny_Type(Integer32):
    """Custom type ip4VLanMgmtAny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ip4VLanMgmtAny_Type.__name__ = "Integer32"
_Ip4VLanMgmtAny_Object = MibScalar
ip4VLanMgmtAny = _Ip4VLanMgmtAny_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 12),
    _Ip4VLanMgmtAny_Type()
)
ip4VLanMgmtAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanMgmtAny.setStatus("mandatory")


class _Ip4VLanMgmtUntag_Type(Integer32):
    """Custom type ip4VLanMgmtUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ip4VLanMgmtUntag_Type.__name__ = "Integer32"
_Ip4VLanMgmtUntag_Object = MibScalar
ip4VLanMgmtUntag = _Ip4VLanMgmtUntag_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 43, 13),
    _Ip4VLanMgmtUntag_Type()
)
ip4VLanMgmtUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4VLanMgmtUntag.setStatus("mandatory")
_SehUtn_ObjectIdentity = ObjectIdentity
sehUtn = _SehUtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50)
)
_UtnPortNumber_Type = Integer32
_UtnPortNumber_Object = MibScalar
utnPortNumber = _UtnPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 1),
    _UtnPortNumber_Type()
)
utnPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortNumber.setStatus("mandatory")
_UtnPortTable_Object = MibTable
utnPortTable = _UtnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2)
)
if mibBuilder.loadTexts:
    utnPortTable.setStatus("mandatory")
_UtnPortEntry_Object = MibTableRow
utnPortEntry = _UtnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1)
)
utnPortEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "utnPortIndex"),
)
if mibBuilder.loadTexts:
    utnPortEntry.setStatus("mandatory")


class _UtnPortIndex_Type(Integer32):
    """Custom type utnPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_UtnPortIndex_Type.__name__ = "Integer32"
_UtnPortIndex_Object = MibTableColumn
utnPortIndex = _UtnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 1),
    _UtnPortIndex_Type()
)
utnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnPortIndex.setStatus("mandatory")


class _UtnPortSecure_Type(Integer32):
    """Custom type utnPortSecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UtnPortSecure_Type.__name__ = "Integer32"
_UtnPortSecure_Object = MibTableColumn
utnPortSecure = _UtnPortSecure_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 2),
    _UtnPortSecure_Type()
)
utnPortSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortSecure.setStatus("mandatory")


class _UtnPortPoSwitch_Type(Integer32):
    """Custom type utnPortPoSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UtnPortPoSwitch_Type.__name__ = "Integer32"
_UtnPortPoSwitch_Object = MibTableColumn
utnPortPoSwitch = _UtnPortPoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 3),
    _UtnPortPoSwitch_Type()
)
utnPortPoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortPoSwitch.setStatus("mandatory")


class _UtnPortPoOffDura_Type(Integer32):
    """Custom type utnPortPoOffDura based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UtnPortPoOffDura_Type.__name__ = "Integer32"
_UtnPortPoOffDura_Object = MibTableColumn
utnPortPoOffDura = _UtnPortPoOffDura_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 4),
    _UtnPortPoOffDura_Type()
)
utnPortPoOffDura.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortPoOffDura.setStatus("mandatory")


class _UtnPortAccCtrl_Type(Integer32):
    """Custom type utnPortAccCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("key", 2),
          ("ids", 3),
          ("keyids", 4))
    )


_UtnPortAccCtrl_Type.__name__ = "Integer32"
_UtnPortAccCtrl_Object = MibTableColumn
utnPortAccCtrl = _UtnPortAccCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 5),
    _UtnPortAccCtrl_Type()
)
utnPortAccCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortAccCtrl.setStatus("mandatory")


class _UtnPortKeyVal_Type(DisplayString):
    """Custom type utnPortKeyVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnPortKeyVal_Type.__name__ = "DisplayString"
_UtnPortKeyVal_Object = MibTableColumn
utnPortKeyVal = _UtnPortKeyVal_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 6),
    _UtnPortKeyVal_Type()
)
utnPortKeyVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortKeyVal.setStatus("mandatory")


class _UtnPortProdId_Type(DisplayString):
    """Custom type utnPortProdId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_UtnPortProdId_Type.__name__ = "DisplayString"
_UtnPortProdId_Object = MibTableColumn
utnPortProdId = _UtnPortProdId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 7),
    _UtnPortProdId_Type()
)
utnPortProdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortProdId.setStatus("mandatory")


class _UtnPortVendId_Type(DisplayString):
    """Custom type utnPortVendId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_UtnPortVendId_Type.__name__ = "DisplayString"
_UtnPortVendId_Object = MibTableColumn
utnPortVendId = _UtnPortVendId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 8),
    _UtnPortVendId_Type()
)
utnPortVendId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortVendId.setStatus("mandatory")


class _UtnPortIp4Vlan_Type(Integer32):
    """Custom type utnPortIp4Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_UtnPortIp4Vlan_Type.__name__ = "Integer32"
_UtnPortIp4Vlan_Object = MibTableColumn
utnPortIp4Vlan = _UtnPortIp4Vlan_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 9),
    _UtnPortIp4Vlan_Type()
)
utnPortIp4Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortIp4Vlan.setStatus("mandatory")


class _UtnPortTag_Type(DisplayString):
    """Custom type utnPortTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UtnPortTag_Type.__name__ = "DisplayString"
_UtnPortTag_Object = MibTableColumn
utnPortTag = _UtnPortTag_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 10),
    _UtnPortTag_Type()
)
utnPortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortTag.setStatus("mandatory")


class _UtnPortComp_Type(Integer32):
    """Custom type utnPortComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UtnPortComp_Type.__name__ = "Integer32"
_UtnPortComp_Object = MibTableColumn
utnPortComp = _UtnPortComp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 11),
    _UtnPortComp_Type()
)
utnPortComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortComp.setStatus("mandatory")


class _UtnPortUsbManu_Type(DisplayString):
    """Custom type utnPortUsbManu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnPortUsbManu_Type.__name__ = "DisplayString"
_UtnPortUsbManu_Object = MibTableColumn
utnPortUsbManu = _UtnPortUsbManu_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 21),
    _UtnPortUsbManu_Type()
)
utnPortUsbManu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbManu.setStatus("mandatory")


class _UtnPortUsbProd_Type(DisplayString):
    """Custom type utnPortUsbProd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnPortUsbProd_Type.__name__ = "DisplayString"
_UtnPortUsbProd_Object = MibTableColumn
utnPortUsbProd = _UtnPortUsbProd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 22),
    _UtnPortUsbProd_Type()
)
utnPortUsbProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbProd.setStatus("mandatory")


class _UtnPortUsbVendId_Type(DisplayString):
    """Custom type utnPortUsbVendId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_UtnPortUsbVendId_Type.__name__ = "DisplayString"
_UtnPortUsbVendId_Object = MibTableColumn
utnPortUsbVendId = _UtnPortUsbVendId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 23),
    _UtnPortUsbVendId_Type()
)
utnPortUsbVendId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbVendId.setStatus("mandatory")


class _UtnPortUsbProdId_Type(DisplayString):
    """Custom type utnPortUsbProdId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_UtnPortUsbProdId_Type.__name__ = "DisplayString"
_UtnPortUsbProdId_Object = MibTableColumn
utnPortUsbProdId = _UtnPortUsbProdId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 24),
    _UtnPortUsbProdId_Type()
)
utnPortUsbProdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbProdId.setStatus("mandatory")


class _UtnPortUsbSer_Type(DisplayString):
    """Custom type utnPortUsbSer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnPortUsbSer_Type.__name__ = "DisplayString"
_UtnPortUsbSer_Object = MibTableColumn
utnPortUsbSer = _UtnPortUsbSer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 25),
    _UtnPortUsbSer_Type()
)
utnPortUsbSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbSer.setStatus("mandatory")


class _UtnPortUsbOwn_Type(DisplayString):
    """Custom type utnPortUsbOwn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnPortUsbOwn_Type.__name__ = "DisplayString"
_UtnPortUsbOwn_Object = MibTableColumn
utnPortUsbOwn = _UtnPortUsbOwn_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 26),
    _UtnPortUsbOwn_Type()
)
utnPortUsbOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnPortUsbOwn.setStatus("mandatory")


class _UtnPortSlot_Type(Integer32):
    """Custom type utnPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_UtnPortSlot_Type.__name__ = "Integer32"
_UtnPortSlot_Object = MibTableColumn
utnPortSlot = _UtnPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 2, 1, 27),
    _UtnPortSlot_Type()
)
utnPortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnPortSlot.setStatus("mandatory")


class _UtnDispDef_Type(DisplayString):
    """Custom type utnDispDef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_UtnDispDef_Type.__name__ = "DisplayString"
_UtnDispDef_Object = MibScalar
utnDispDef = _UtnDispDef_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 11),
    _UtnDispDef_Type()
)
utnDispDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnDispDef.setStatus("mandatory")


class _UtnDispErVals_Type(DisplayString):
    """Custom type utnDispErVals based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnDispErVals_Type.__name__ = "DisplayString"
_UtnDispErVals_Object = MibScalar
utnDispErVals = _UtnDispErVals_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 12),
    _UtnDispErVals_Type()
)
utnDispErVals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnDispErVals.setStatus("mandatory")


class _UtnBeepPwr_Type(Integer32):
    """Custom type utnBeepPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UtnBeepPwr_Type.__name__ = "Integer32"
_UtnBeepPwr_Object = MibScalar
utnBeepPwr = _UtnBeepPwr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 13),
    _UtnBeepPwr_Type()
)
utnBeepPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnBeepPwr.setStatus("mandatory")


class _UtnBeepSDc_Type(Integer32):
    """Custom type utnBeepSDc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UtnBeepSDc_Type.__name__ = "Integer32"
_UtnBeepSDc_Object = MibScalar
utnBeepSDc = _UtnBeepSDc_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 14),
    _UtnBeepSDc_Type()
)
utnBeepSDc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnBeepSDc.setStatus("mandatory")


class _UtnHid_Type(Integer32):
    """Custom type utnHid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UtnHid_Type.__name__ = "Integer32"
_UtnHid_Object = MibScalar
utnHid = _UtnHid_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 15),
    _UtnHid_Type()
)
utnHid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnHid.setStatus("mandatory")


class _UtnRelayOn_Type(Integer32):
    """Custom type utnRelayOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UtnRelayOn_Type.__name__ = "Integer32"
_UtnRelayOn_Object = MibScalar
utnRelayOn = _UtnRelayOn_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 16),
    _UtnRelayOn_Type()
)
utnRelayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayOn.setStatus("mandatory")


class _UtnRelayFix_Type(Integer32):
    """Custom type utnRelayFix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UtnRelayFix_Type.__name__ = "Integer32"
_UtnRelayFix_Object = MibScalar
utnRelayFix = _UtnRelayFix_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 17),
    _UtnRelayFix_Type()
)
utnRelayFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayFix.setStatus("mandatory")


class _UtnRelayEves_Type(Bits):
    """Custom type utnRelayEves based on Bits"""
    namedValues = NamedValues(
        *(("relayUnused0", 0),
          ("relayEveStart", 1),
          ("relayEveLinkDown", 2),
          ("relayEveLinkUp", 3),
          ("relayEvePwd1On", 5),
          ("relayEvePwd2On", 6),
          ("relayEvePwd1Off", 7),
          ("relayEvePwd2Off", 8),
          ("relayEveSDIn", 9),
          ("relayEveSDOut", 10),
          ("relayEveSDErr", 11),
          ("relayEveU1Con", 13),
          ("relayEveU1Dis", 14),
          ("relayEveU1Act", 15),
          ("relayEveU1Dea", 16),
          ("relayEveU2Con", 17),
          ("relayEveU2Dis", 18),
          ("relayEveU2Act", 19),
          ("relayEveU2Dea", 20))
    )

_UtnRelayEves_Type.__name__ = "Bits"
_UtnRelayEves_Object = MibScalar
utnRelayEves = _UtnRelayEves_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 18),
    _UtnRelayEves_Type()
)
utnRelayEves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utnRelayEves.setStatus("mandatory")


class _UtnRelayRestart_Type(Integer32):
    """Custom type utnRelayRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("warm", 1))
    )


_UtnRelayRestart_Type.__name__ = "Integer32"
_UtnRelayRestart_Object = MibScalar
utnRelayRestart = _UtnRelayRestart_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 21),
    _UtnRelayRestart_Type()
)
utnRelayRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayRestart.setStatus("mandatory")


class _UtnRelay1Pwr_Type(Integer32):
    """Custom type utnRelay1Pwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("pwroff", 1),
          ("pwron", 2))
    )


_UtnRelay1Pwr_Type.__name__ = "Integer32"
_UtnRelay1Pwr_Object = MibScalar
utnRelay1Pwr = _UtnRelay1Pwr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 22),
    _UtnRelay1Pwr_Type()
)
utnRelay1Pwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelay1Pwr.setStatus("mandatory")


class _UtnRelay2Pwr_Type(Integer32):
    """Custom type utnRelay2Pwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("pwroff", 1),
          ("pwron", 2))
    )


_UtnRelay2Pwr_Type.__name__ = "Integer32"
_UtnRelay2Pwr_Object = MibScalar
utnRelay2Pwr = _UtnRelay2Pwr_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 23),
    _UtnRelay2Pwr_Type()
)
utnRelay2Pwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelay2Pwr.setStatus("mandatory")


class _UtnRelayNet_Type(Integer32):
    """Custom type utnRelayNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("netoff", 1),
          ("neton", 2))
    )


_UtnRelayNet_Type.__name__ = "Integer32"
_UtnRelayNet_Object = MibScalar
utnRelayNet = _UtnRelayNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 24),
    _UtnRelayNet_Type()
)
utnRelayNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayNet.setStatus("mandatory")


class _UtnRelaySDCard_Type(Integer32):
    """Custom type utnRelaySDCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("sdin", 1),
          ("sdout", 2),
          ("sderr", 3))
    )


_UtnRelaySDCard_Type.__name__ = "Integer32"
_UtnRelaySDCard_Object = MibScalar
utnRelaySDCard = _UtnRelaySDCard_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 25),
    _UtnRelaySDCard_Type()
)
utnRelaySDCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelaySDCard.setStatus("mandatory")


class _UtnRelayUsbCon_Type(Integer32):
    """Custom type utnRelayUsbCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayUsbCon_Type.__name__ = "Integer32"
_UtnRelayUsbCon_Object = MibScalar
utnRelayUsbCon = _UtnRelayUsbCon_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 26),
    _UtnRelayUsbCon_Type()
)
utnRelayUsbCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayUsbCon.setStatus("mandatory")


class _UtnRelayUsbDisco_Type(Integer32):
    """Custom type utnRelayUsbDisco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayUsbDisco_Type.__name__ = "Integer32"
_UtnRelayUsbDisco_Object = MibScalar
utnRelayUsbDisco = _UtnRelayUsbDisco_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 27),
    _UtnRelayUsbDisco_Type()
)
utnRelayUsbDisco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayUsbDisco.setStatus("mandatory")


class _UtnRelayUsbActivate_Type(Integer32):
    """Custom type utnRelayUsbActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayUsbActivate_Type.__name__ = "Integer32"
_UtnRelayUsbActivate_Object = MibScalar
utnRelayUsbActivate = _UtnRelayUsbActivate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 28),
    _UtnRelayUsbActivate_Type()
)
utnRelayUsbActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayUsbActivate.setStatus("mandatory")


class _UtnRelayUsbDeActivate_Type(Integer32):
    """Custom type utnRelayUsbDeActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayUsbDeActivate_Type.__name__ = "Integer32"
_UtnRelayUsbDeActivate_Object = MibScalar
utnRelayUsbDeActivate = _UtnRelayUsbDeActivate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 29),
    _UtnRelayUsbDeActivate_Type()
)
utnRelayUsbDeActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayUsbDeActivate.setStatus("mandatory")


class _UtnRelayCtrl_Type(Integer32):
    """Custom type utnRelayCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix", 0),
          ("event", 1),
          ("state", 2))
    )


_UtnRelayCtrl_Type.__name__ = "Integer32"
_UtnRelayCtrl_Object = MibScalar
utnRelayCtrl = _UtnRelayCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 40),
    _UtnRelayCtrl_Type()
)
utnRelayCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayCtrl.setStatus("mandatory")


class _UtnRelayStateNet_Type(Integer32):
    """Custom type utnRelayStateNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("netoff", 1),
          ("neton", 2))
    )


_UtnRelayStateNet_Type.__name__ = "Integer32"
_UtnRelayStateNet_Object = MibScalar
utnRelayStateNet = _UtnRelayStateNet_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 44),
    _UtnRelayStateNet_Type()
)
utnRelayStateNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayStateNet.setStatus("mandatory")


class _UtnRelayStateUsbCon_Type(Integer32):
    """Custom type utnRelayStateUsbCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayStateUsbCon_Type.__name__ = "Integer32"
_UtnRelayStateUsbCon_Object = MibScalar
utnRelayStateUsbCon = _UtnRelayStateUsbCon_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 46),
    _UtnRelayStateUsbCon_Type()
)
utnRelayStateUsbCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayStateUsbCon.setStatus("mandatory")


class _UtnRelayStateUsbDisco_Type(Integer32):
    """Custom type utnRelayStateUsbDisco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayStateUsbDisco_Type.__name__ = "Integer32"
_UtnRelayStateUsbDisco_Object = MibScalar
utnRelayStateUsbDisco = _UtnRelayStateUsbDisco_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 47),
    _UtnRelayStateUsbDisco_Type()
)
utnRelayStateUsbDisco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayStateUsbDisco.setStatus("mandatory")


class _UtnRelayStateUsbActivate_Type(Integer32):
    """Custom type utnRelayStateUsbActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayStateUsbActivate_Type.__name__ = "Integer32"
_UtnRelayStateUsbActivate_Object = MibScalar
utnRelayStateUsbActivate = _UtnRelayStateUsbActivate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 48),
    _UtnRelayStateUsbActivate_Type()
)
utnRelayStateUsbActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayStateUsbActivate.setStatus("mandatory")


class _UtnRelayStateUsbDeActivate_Type(Integer32):
    """Custom type utnRelayStateUsbDeActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("any", 1),
          ("port1", 2),
          ("port2", 3))
    )


_UtnRelayStateUsbDeActivate_Type.__name__ = "Integer32"
_UtnRelayStateUsbDeActivate_Object = MibScalar
utnRelayStateUsbDeActivate = _UtnRelayStateUsbDeActivate_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 50, 49),
    _UtnRelayStateUsbDeActivate_Type()
)
utnRelayStateUsbDeActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utnRelayStateUsbDeActivate.setStatus("mandatory")
_SehUtnEvent_ObjectIdentity = ObjectIdentity
sehUtnEvent = _SehUtnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51)
)


class _UtnEventType_Type(Integer32):
    """Custom type utnEventType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("misc", 1),
          ("error", 2),
          ("usbAattached", 3),
          ("usbDetached", 4),
          ("connect", 5),
          ("disconnect", 6),
          ("cardreader", 7),
          ("usbConnect", 8),
          ("usbDisconnect", 9),
          ("printjob", 10),
          ("powersupply", 11),
          ("sdcardPlugIn", 12),
          ("sdcardPlugOut", 13),
          ("sdcardMissing", 14),
          ("sdcardUnusable", 15),
          ("sdcardRdOnly", 16),
          ("link", 17),
          ("deviceHeat", 18),
          ("usbPowerConsumption", 19))
    )


_UtnEventType_Type.__name__ = "Integer32"
_UtnEventType_Object = MibScalar
utnEventType = _UtnEventType_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 1),
    _UtnEventType_Type()
)
utnEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventType.setStatus("mandatory")
_UtnEventPort_Type = Integer32
_UtnEventPort_Object = MibScalar
utnEventPort = _UtnEventPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 2),
    _UtnEventPort_Type()
)
utnEventPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventPort.setStatus("mandatory")


class _UtnEventMsg_Type(DisplayString):
    """Custom type utnEventMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnEventMsg_Type.__name__ = "DisplayString"
_UtnEventMsg_Object = MibScalar
utnEventMsg = _UtnEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 3),
    _UtnEventMsg_Type()
)
utnEventMsg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventMsg.setStatus("mandatory")


class _UtnEventManu_Type(DisplayString):
    """Custom type utnEventManu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnEventManu_Type.__name__ = "DisplayString"
_UtnEventManu_Object = MibScalar
utnEventManu = _UtnEventManu_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 4),
    _UtnEventManu_Type()
)
utnEventManu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventManu.setStatus("mandatory")
_UtnEventManuId_Type = Integer32
_UtnEventManuId_Object = MibScalar
utnEventManuId = _UtnEventManuId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 5),
    _UtnEventManuId_Type()
)
utnEventManuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventManuId.setStatus("mandatory")


class _UtnEventProd_Type(DisplayString):
    """Custom type utnEventProd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnEventProd_Type.__name__ = "DisplayString"
_UtnEventProd_Object = MibScalar
utnEventProd = _UtnEventProd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 6),
    _UtnEventProd_Type()
)
utnEventProd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventProd.setStatus("mandatory")
_UtnEventProdId_Type = Integer32
_UtnEventProdId_Object = MibScalar
utnEventProdId = _UtnEventProdId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 7),
    _UtnEventProdId_Type()
)
utnEventProdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventProdId.setStatus("mandatory")


class _UtnEventSerial_Type(DisplayString):
    """Custom type utnEventSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UtnEventSerial_Type.__name__ = "DisplayString"
_UtnEventSerial_Object = MibScalar
utnEventSerial = _UtnEventSerial_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 8),
    _UtnEventSerial_Type()
)
utnEventSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    utnEventSerial.setStatus("mandatory")


class _TniEventCard_Type(DisplayString):
    """Custom type tniEventCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TniEventCard_Type.__name__ = "DisplayString"
_TniEventCard_Object = MibScalar
tniEventCard = _TniEventCard_Object(
    (1, 3, 6, 1, 4, 1, 1229, 2, 51, 9),
    _TniEventCard_Type()
)
tniEventCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tniEventCard.setStatus("mandatory")
_SehSnd_ObjectIdentity = ObjectIdentity
sehSnd = _SehSnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 10)
)
_SehSndUser_ObjectIdentity = ObjectIdentity
sehSndUser = _SehSndUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1)
)
_SndUserNumber_Type = Integer32
_SndUserNumber_Object = MibScalar
sndUserNumber = _SndUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 1),
    _SndUserNumber_Type()
)
sndUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndUserNumber.setStatus("mandatory")
_SndUserTable_Object = MibTable
sndUserTable = _SndUserTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2)
)
if mibBuilder.loadTexts:
    sndUserTable.setStatus("mandatory")
_SndUserEntry_Object = MibTableRow
sndUserEntry = _SndUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1)
)
sndUserEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "sndUserIndex"),
)
if mibBuilder.loadTexts:
    sndUserEntry.setStatus("mandatory")


class _SndUserIndex_Type(Integer32):
    """Custom type sndUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SndUserIndex_Type.__name__ = "Integer32"
_SndUserIndex_Object = MibTableColumn
sndUserIndex = _SndUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 1),
    _SndUserIndex_Type()
)
sndUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sndUserIndex.setStatus("mandatory")


class _SndUserActive_Type(Integer32):
    """Custom type sndUserActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SndUserActive_Type.__name__ = "Integer32"
_SndUserActive_Object = MibTableColumn
sndUserActive = _SndUserActive_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 2),
    _SndUserActive_Type()
)
sndUserActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserActive.setStatus("mandatory")


class _SndUserName_Type(DisplayString):
    """Custom type sndUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndUserName_Type.__name__ = "DisplayString"
_SndUserName_Object = MibTableColumn
sndUserName = _SndUserName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 3),
    _SndUserName_Type()
)
sndUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserName.setStatus("mandatory")


class _SndUserPwd_Type(DisplayString):
    """Custom type sndUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndUserPwd_Type.__name__ = "DisplayString"
_SndUserPwd_Object = MibTableColumn
sndUserPwd = _SndUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 4),
    _SndUserPwd_Type()
)
sndUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserPwd.setStatus("mandatory")


class _SndUserEmail_Type(DisplayString):
    """Custom type sndUserEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndUserEmail_Type.__name__ = "DisplayString"
_SndUserEmail_Object = MibTableColumn
sndUserEmail = _SndUserEmail_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 5),
    _SndUserEmail_Type()
)
sndUserEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserEmail.setStatus("mandatory")


class _SndUserFFilter_Type(Integer32):
    """Custom type sndUserFFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SndUserFFilter_Type.__name__ = "Integer32"
_SndUserFFilter_Object = MibTableColumn
sndUserFFilter = _SndUserFFilter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 6),
    _SndUserFFilter_Type()
)
sndUserFFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserFFilter.setStatus("mandatory")


class _SndUserRAdm_Type(Integer32):
    """Custom type sndUserRAdm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndUserRAdm_Type.__name__ = "Integer32"
_SndUserRAdm_Object = MibTableColumn
sndUserRAdm = _SndUserRAdm_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 7),
    _SndUserRAdm_Type()
)
sndUserRAdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserRAdm.setStatus("mandatory")


class _SndUserRDLoad_Type(Integer32):
    """Custom type sndUserRDLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndUserRDLoad_Type.__name__ = "Integer32"
_SndUserRDLoad_Object = MibTableColumn
sndUserRDLoad = _SndUserRDLoad_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 8),
    _SndUserRDLoad_Type()
)
sndUserRDLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserRDLoad.setStatus("mandatory")


class _SndUserRSend_Type(Integer32):
    """Custom type sndUserRSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndUserRSend_Type.__name__ = "Integer32"
_SndUserRSend_Object = MibTableColumn
sndUserRSend = _SndUserRSend_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 9),
    _SndUserRSend_Type()
)
sndUserRSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserRSend.setStatus("mandatory")


class _SndUserRTogg_Type(Integer32):
    """Custom type sndUserRTogg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndUserRTogg_Type.__name__ = "Integer32"
_SndUserRTogg_Object = MibTableColumn
sndUserRTogg = _SndUserRTogg_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 10),
    _SndUserRTogg_Type()
)
sndUserRTogg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserRTogg.setStatus("mandatory")


class _SndUserRWrt_Type(Integer32):
    """Custom type sndUserRWrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndUserRWrt_Type.__name__ = "Integer32"
_SndUserRWrt_Object = MibTableColumn
sndUserRWrt = _SndUserRWrt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 1, 2, 1, 11),
    _SndUserRWrt_Type()
)
sndUserRWrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndUserRWrt.setStatus("mandatory")
_SehSndSender_ObjectIdentity = ObjectIdentity
sehSndSender = _SehSndSender_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2)
)


class _SndSendMaxFiles_Type(Integer32):
    """Custom type sndSendMaxFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SndSendMaxFiles_Type.__name__ = "Integer32"
_SndSendMaxFiles_Object = MibScalar
sndSendMaxFiles = _SndSendMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 1),
    _SndSendMaxFiles_Type()
)
sndSendMaxFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSendMaxFiles.setStatus("mandatory")


class _SndSendMaxKb_Type(Integer32):
    """Custom type sndSendMaxKb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_SndSendMaxKb_Type.__name__ = "Integer32"
_SndSendMaxKb_Object = MibScalar
sndSendMaxKb = _SndSendMaxKb_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 2),
    _SndSendMaxKb_Type()
)
sndSendMaxKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSendMaxKb.setStatus("mandatory")


class _SndSenderPDMedia_Type(Integer32):
    """Custom type sndSenderPDMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndSenderPDMedia_Type.__name__ = "Integer32"
_SndSenderPDMedia_Object = MibScalar
sndSenderPDMedia = _SndSenderPDMedia_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 3),
    _SndSenderPDMedia_Type()
)
sndSenderPDMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderPDMedia.setStatus("mandatory")


class _SndSenderPDDir_Type(DisplayString):
    """Custom type sndSenderPDDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSenderPDDir_Type.__name__ = "DisplayString"
_SndSenderPDDir_Object = MibScalar
sndSenderPDDir = _SndSenderPDDir_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 4),
    _SndSenderPDDir_Type()
)
sndSenderPDDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderPDDir.setStatus("mandatory")


class _SndSenderPDExt_Type(DisplayString):
    """Custom type sndSenderPDExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSenderPDExt_Type.__name__ = "DisplayString"
_SndSenderPDExt_Object = MibScalar
sndSenderPDExt = _SndSenderPDExt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 5),
    _SndSenderPDExt_Type()
)
sndSenderPDExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderPDExt.setStatus("mandatory")


class _SndSenderPDaBit_Type(Integer32):
    """Custom type sndSenderPDaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("archBit", 1))
    )


_SndSenderPDaBit_Type.__name__ = "Integer32"
_SndSenderPDaBit_Object = MibScalar
sndSenderPDaBit = _SndSenderPDaBit_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 6),
    _SndSenderPDaBit_Type()
)
sndSenderPDaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderPDaBit.setStatus("mandatory")
_SndSenderPDRcpNum_Type = Integer32
_SndSenderPDRcpNum_Object = MibScalar
sndSenderPDRcpNum = _SndSenderPDRcpNum_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 7),
    _SndSenderPDRcpNum_Type()
)
sndSenderPDRcpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndSenderPDRcpNum.setStatus("mandatory")
_SndSenderPDRcpTable_Object = MibTable
sndSenderPDRcpTable = _SndSenderPDRcpTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 8)
)
if mibBuilder.loadTexts:
    sndSenderPDRcpTable.setStatus("mandatory")
_SndSenderPDRcpEntry_Object = MibTableRow
sndSenderPDRcpEntry = _SndSenderPDRcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 8, 1)
)
sndSenderPDRcpEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "sndPDRcpIndex"),
)
if mibBuilder.loadTexts:
    sndSenderPDRcpEntry.setStatus("mandatory")


class _SndPDRcpIndex_Type(Integer32):
    """Custom type sndPDRcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SndPDRcpIndex_Type.__name__ = "Integer32"
_SndPDRcpIndex_Object = MibTableColumn
sndPDRcpIndex = _SndPDRcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 8, 1, 1),
    _SndPDRcpIndex_Type()
)
sndPDRcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sndPDRcpIndex.setStatus("mandatory")


class _SndPDRcpEmail_Type(DisplayString):
    """Custom type sndPDRcpEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndPDRcpEmail_Type.__name__ = "DisplayString"
_SndPDRcpEmail_Object = MibTableColumn
sndPDRcpEmail = _SndPDRcpEmail_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 8, 1, 2),
    _SndPDRcpEmail_Type()
)
sndPDRcpEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndPDRcpEmail.setStatus("mandatory")


class _SndSenderSDActive_Type(Integer32):
    """Custom type sndSenderSDActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SndSenderSDActive_Type.__name__ = "Integer32"
_SndSenderSDActive_Object = MibScalar
sndSenderSDActive = _SndSenderSDActive_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 20),
    _SndSenderSDActive_Type()
)
sndSenderSDActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderSDActive.setStatus("mandatory")


class _SndSenderSDRcp_Type(DisplayString):
    """Custom type sndSenderSDRcp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSenderSDRcp_Type.__name__ = "DisplayString"
_SndSenderSDRcp_Object = MibScalar
sndSenderSDRcp = _SndSenderSDRcp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 21),
    _SndSenderSDRcp_Type()
)
sndSenderSDRcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSenderSDRcp.setStatus("mandatory")
_SndSenderSDNum_Type = Integer32
_SndSenderSDNum_Object = MibScalar
sndSenderSDNum = _SndSenderSDNum_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 30),
    _SndSenderSDNum_Type()
)
sndSenderSDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndSenderSDNum.setStatus("mandatory")
_SndSenderSDTable_Object = MibTable
sndSenderSDTable = _SndSenderSDTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31)
)
if mibBuilder.loadTexts:
    sndSenderSDTable.setStatus("mandatory")
_SndSenderSDEntry_Object = MibTableRow
sndSenderSDEntry = _SndSenderSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1)
)
sndSenderSDEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "sndSDIndex"),
)
if mibBuilder.loadTexts:
    sndSenderSDEntry.setStatus("mandatory")


class _SndSDIndex_Type(Integer32):
    """Custom type sndSDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SndSDIndex_Type.__name__ = "Integer32"
_SndSDIndex_Object = MibTableColumn
sndSDIndex = _SndSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1, 1),
    _SndSDIndex_Type()
)
sndSDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sndSDIndex.setStatus("mandatory")


class _SndSDMedia_Type(Integer32):
    """Custom type sndSDMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndSDMedia_Type.__name__ = "Integer32"
_SndSDMedia_Object = MibTableColumn
sndSDMedia = _SndSDMedia_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1, 2),
    _SndSDMedia_Type()
)
sndSDMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDMedia.setStatus("mandatory")


class _SndSDDir_Type(DisplayString):
    """Custom type sndSDDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SndSDDir_Type.__name__ = "DisplayString"
_SndSDDir_Object = MibTableColumn
sndSDDir = _SndSDDir_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1, 3),
    _SndSDDir_Type()
)
sndSDDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDDir.setStatus("mandatory")


class _SndSDExt_Type(DisplayString):
    """Custom type sndSDExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSDExt_Type.__name__ = "DisplayString"
_SndSDExt_Object = MibTableColumn
sndSDExt = _SndSDExt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1, 4),
    _SndSDExt_Type()
)
sndSDExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDExt.setStatus("mandatory")


class _SndSDaBit_Type(Integer32):
    """Custom type sndSDaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("archBit", 1))
    )


_SndSDaBit_Type.__name__ = "Integer32"
_SndSDaBit_Object = MibTableColumn
sndSDaBit = _SndSDaBit_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 2, 31, 1, 5),
    _SndSDaBit_Type()
)
sndSDaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDaBit.setStatus("mandatory")
_SehSndFFilter_ObjectIdentity = ObjectIdentity
sehSndFFilter = _SehSndFFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3)
)
_SndFFilterNum_Type = Integer32
_SndFFilterNum_Object = MibScalar
sndFFilterNum = _SndFFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 1),
    _SndFFilterNum_Type()
)
sndFFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndFFilterNum.setStatus("mandatory")
_SndFFilterTable_Object = MibTable
sndFFilterTable = _SndFFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 2)
)
if mibBuilder.loadTexts:
    sndFFilterTable.setStatus("mandatory")
_SndFFilterEntry_Object = MibTableRow
sndFFilterEntry = _SndFFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 2, 1)
)
sndFFilterEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "sndFFilterIndex"),
)
if mibBuilder.loadTexts:
    sndFFilterEntry.setStatus("mandatory")


class _SndFFilterIndex_Type(Integer32):
    """Custom type sndFFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SndFFilterIndex_Type.__name__ = "Integer32"
_SndFFilterIndex_Object = MibTableColumn
sndFFilterIndex = _SndFFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 2, 1, 1),
    _SndFFilterIndex_Type()
)
sndFFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sndFFilterIndex.setStatus("mandatory")


class _SndFFilterName_Type(DisplayString):
    """Custom type sndFFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndFFilterName_Type.__name__ = "DisplayString"
_SndFFilterName_Object = MibTableColumn
sndFFilterName = _SndFFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 2, 1, 2),
    _SndFFilterName_Type()
)
sndFFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndFFilterName.setStatus("mandatory")


class _SndFFilter_Type(DisplayString):
    """Custom type sndFFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SndFFilter_Type.__name__ = "DisplayString"
_SndFFilter_Object = MibTableColumn
sndFFilter = _SndFFilter_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 3, 2, 1, 3),
    _SndFFilter_Type()
)
sndFFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndFFilter.setStatus("mandatory")
_SehSndSDCard_ObjectIdentity = ObjectIdentity
sehSndSDCard = _SehSndSDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4)
)
_SndSDCardNum_Type = Integer32
_SndSDCardNum_Object = MibScalar
sndSDCardNum = _SndSDCardNum_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 1),
    _SndSDCardNum_Type()
)
sndSDCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndSDCardNum.setStatus("mandatory")
_SndSDCardTable_Object = MibTable
sndSDCardTable = _SndSDCardTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2)
)
if mibBuilder.loadTexts:
    sndSDCardTable.setStatus("mandatory")
_SndSDCardEntry_Object = MibTableRow
sndSDCardEntry = _SndSDCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1)
)
sndSDCardEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "sndSDCardIndex"),
)
if mibBuilder.loadTexts:
    sndSDCardEntry.setStatus("mandatory")


class _SndSDCardIndex_Type(Integer32):
    """Custom type sndSDCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SndSDCardIndex_Type.__name__ = "Integer32"
_SndSDCardIndex_Object = MibTableColumn
sndSDCardIndex = _SndSDCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1, 1),
    _SndSDCardIndex_Type()
)
sndSDCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sndSDCardIndex.setStatus("mandatory")


class _SndSDCardCid_Type(DisplayString):
    """Custom type sndSDCardCid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SndSDCardCid_Type.__name__ = "DisplayString"
_SndSDCardCid_Object = MibTableColumn
sndSDCardCid = _SndSDCardCid_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1, 2),
    _SndSDCardCid_Type()
)
sndSDCardCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndSDCardCid.setStatus("mandatory")


class _SndSDCardName_Type(DisplayString):
    """Custom type sndSDCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSDCardName_Type.__name__ = "DisplayString"
_SndSDCardName_Object = MibTableColumn
sndSDCardName = _SndSDCardName_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1, 3),
    _SndSDCardName_Type()
)
sndSDCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDCardName.setStatus("mandatory")


class _SndSDCardUList_Type(DisplayString):
    """Custom type sndSDCardUList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SndSDCardUList_Type.__name__ = "DisplayString"
_SndSDCardUList_Object = MibTableColumn
sndSDCardUList = _SndSDCardUList_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1, 4),
    _SndSDCardUList_Type()
)
sndSDCardUList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDCardUList.setStatus("mandatory")


class _SndSDCardARcp_Type(DisplayString):
    """Custom type sndSDCardARcp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SndSDCardARcp_Type.__name__ = "DisplayString"
_SndSDCardARcp_Object = MibTableColumn
sndSDCardARcp = _SndSDCardARcp_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 4, 2, 1, 5),
    _SndSDCardARcp_Type()
)
sndSDCardARcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndSDCardARcp.setStatus("mandatory")


class _SndPDPort_Type(Integer32):
    """Custom type sndPDPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SndPDPort_Type.__name__ = "Integer32"
_SndPDPort_Object = MibScalar
sndPDPort = _SndPDPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 10, 10),
    _SndPDPort_Type()
)
sndPDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndPDPort.setStatus("mandatory")
_SehPPS_ObjectIdentity = ObjectIdentity
sehPPS = _SehPPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 11)
)


class _Pps_Type(Integer32):
    """Custom type pps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pps_Type.__name__ = "Integer32"
_Pps_Object = MibScalar
pps = _Pps_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 1),
    _Pps_Type()
)
pps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps.setStatus("mandatory")


class _PpsPIN_Type(DisplayString):
    """Custom type ppsPIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PpsPIN_Type.__name__ = "DisplayString"
_PpsPIN_Object = MibScalar
ppsPIN = _PpsPIN_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 2),
    _PpsPIN_Type()
)
ppsPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsPIN.setStatus("mandatory")


class _PpsPrtId_Type(DisplayString):
    """Custom type ppsPrtId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpsPrtId_Type.__name__ = "DisplayString"
_PpsPrtId_Object = MibScalar
ppsPrtId = _PpsPrtId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 3),
    _PpsPrtId_Type()
)
ppsPrtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsPrtId.setStatus("mandatory")


class _PpsDelete_Type(Integer32):
    """Custom type ppsDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("server", 1),
          ("tpr", 2))
    )


_PpsDelete_Type.__name__ = "Integer32"
_PpsDelete_Object = MibScalar
ppsDelete = _PpsDelete_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 4),
    _PpsDelete_Type()
)
ppsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsDelete.setStatus("mandatory")


class _PpsDelelteDelay_Type(Integer32):
    """Custom type ppsDelelteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PpsDelelteDelay_Type.__name__ = "Integer32"
_PpsDelelteDelay_Object = MibScalar
ppsDelelteDelay = _PpsDelelteDelay_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 5),
    _PpsDelelteDelay_Type()
)
ppsDelelteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsDelelteDelay.setStatus("mandatory")


class _PpsSingle_Type(Integer32):
    """Custom type ppsSingle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PpsSingle_Type.__name__ = "Integer32"
_PpsSingle_Object = MibScalar
ppsSingle = _PpsSingle_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 6),
    _PpsSingle_Type()
)
ppsSingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsSingle.setStatus("mandatory")


class _PpsBeep_Type(Integer32):
    """Custom type ppsBeep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PpsBeep_Type.__name__ = "Integer32"
_PpsBeep_Object = MibScalar
ppsBeep = _PpsBeep_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 7),
    _PpsBeep_Type()
)
ppsBeep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsBeep.setStatus("mandatory")


class _PpsUSRForm_Type(Integer32):
    """Custom type ppsUSRForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("raw", 0),
          ("formatted", 1))
    )


_PpsUSRForm_Type.__name__ = "Integer32"
_PpsUSRForm_Object = MibScalar
ppsUSRForm = _PpsUSRForm_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 8),
    _PpsUSRForm_Type()
)
ppsUSRForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsUSRForm.setStatus("mandatory")


class _PpsPWD_Type(DisplayString):
    """Custom type ppsPWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PpsPWD_Type.__name__ = "DisplayString"
_PpsPWD_Object = MibScalar
ppsPWD = _PpsPWD_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 9),
    _PpsPWD_Type()
)
ppsPWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsPWD.setStatus("mandatory")


class _PpsPort_Type(Integer32):
    """Custom type ppsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PpsPort_Type.__name__ = "Integer32"
_PpsPort_Object = MibScalar
ppsPort = _PpsPort_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 10),
    _PpsPort_Type()
)
ppsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsPort.setStatus("mandatory")


class _PpsSSL_Type(Integer32):
    """Custom type ppsSSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PpsSSL_Type.__name__ = "Integer32"
_PpsSSL_Object = MibScalar
ppsSSL = _PpsSSL_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 11),
    _PpsSSL_Type()
)
ppsSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsSSL.setStatus("mandatory")


class _PpsVerify_Type(Integer32):
    """Custom type ppsVerify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PpsVerify_Type.__name__ = "Integer32"
_PpsVerify_Object = MibScalar
ppsVerify = _PpsVerify_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 12),
    _PpsVerify_Type()
)
ppsVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsVerify.setStatus("mandatory")


class _PpsServer_Type(DisplayString):
    """Custom type ppsServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpsServer_Type.__name__ = "DisplayString"
_PpsServer_Object = MibScalar
ppsServer = _PpsServer_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 20),
    _PpsServer_Type()
)
ppsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsServer.setStatus("mandatory")


class _PpsServerAlt_Type(DisplayString):
    """Custom type ppsServerAlt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PpsServerAlt_Type.__name__ = "DisplayString"
_PpsServerAlt_Object = MibScalar
ppsServerAlt = _PpsServerAlt_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 21),
    _PpsServerAlt_Type()
)
ppsServerAlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppsServerAlt.setStatus("mandatory")
_PpsNumber_Type = Integer32
_PpsNumber_Object = MibScalar
ppsNumber = _PpsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 30),
    _PpsNumber_Type()
)
ppsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppsNumber.setStatus("mandatory")
_PpsTable_Object = MibTable
ppsTable = _PpsTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31)
)
if mibBuilder.loadTexts:
    ppsTable.setStatus("mandatory")
_PpsEntry_Object = MibTableRow
ppsEntry = _PpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1)
)
ppsEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "pps-Index"),
)
if mibBuilder.loadTexts:
    ppsEntry.setStatus("mandatory")


class _Pps_Index_Type(Integer32):
    """Custom type pps_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Pps_Index_Type.__name__ = "Integer32"
_Pps_Index_Object = MibTableColumn
pps_Index = _Pps_Index_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 1),
    _Pps_Index_Type()
)
pps_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pps_Index.setStatus("mandatory")


class _Pps_On_Type(Integer32):
    """Custom type pps_On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pps_On_Type.__name__ = "Integer32"
_Pps_On_Object = MibTableColumn
pps_On = _Pps_On_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 2),
    _Pps_On_Type()
)
pps_On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_On.setStatus("mandatory")


class _Pps_Server_Type(DisplayString):
    """Custom type pps_Server based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pps_Server_Type.__name__ = "DisplayString"
_Pps_Server_Object = MibTableColumn
pps_Server = _Pps_Server_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 3),
    _Pps_Server_Type()
)
pps_Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_Server.setStatus("mandatory")


class _Pps_PIN_Type(DisplayString):
    """Custom type pps_PIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pps_PIN_Type.__name__ = "DisplayString"
_Pps_PIN_Object = MibTableColumn
pps_PIN = _Pps_PIN_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 4),
    _Pps_PIN_Type()
)
pps_PIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_PIN.setStatus("mandatory")


class _Pps_PWD_Type(DisplayString):
    """Custom type pps_PWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pps_PWD_Type.__name__ = "DisplayString"
_Pps_PWD_Object = MibTableColumn
pps_PWD = _Pps_PWD_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 5),
    _Pps_PWD_Type()
)
pps_PWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_PWD.setStatus("mandatory")


class _Pps_Port_Type(Integer32):
    """Custom type pps_Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pps_Port_Type.__name__ = "Integer32"
_Pps_Port_Object = MibTableColumn
pps_Port = _Pps_Port_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 6),
    _Pps_Port_Type()
)
pps_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_Port.setStatus("mandatory")


class _Pps_SSL_Type(Integer32):
    """Custom type pps_SSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pps_SSL_Type.__name__ = "Integer32"
_Pps_SSL_Object = MibTableColumn
pps_SSL = _Pps_SSL_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 7),
    _Pps_SSL_Type()
)
pps_SSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_SSL.setStatus("mandatory")


class _Pps_Verify_Type(Integer32):
    """Custom type pps_Verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pps_Verify_Type.__name__ = "Integer32"
_Pps_Verify_Object = MibTableColumn
pps_Verify = _Pps_Verify_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 8),
    _Pps_Verify_Type()
)
pps_Verify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_Verify.setStatus("mandatory")


class _Pps_PrtId_Type(DisplayString):
    """Custom type pps_PrtId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pps_PrtId_Type.__name__ = "DisplayString"
_Pps_PrtId_Object = MibTableColumn
pps_PrtId = _Pps_PrtId_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 9),
    _Pps_PrtId_Type()
)
pps_PrtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_PrtId.setStatus("mandatory")


class _Pps_Delete_Type(Integer32):
    """Custom type pps_Delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("server", 1),
          ("tpr", 2))
    )


_Pps_Delete_Type.__name__ = "Integer32"
_Pps_Delete_Object = MibTableColumn
pps_Delete = _Pps_Delete_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 10),
    _Pps_Delete_Type()
)
pps_Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_Delete.setStatus("mandatory")


class _Pps_DelelteDelay_Type(Integer32):
    """Custom type pps_DelelteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Pps_DelelteDelay_Type.__name__ = "Integer32"
_Pps_DelelteDelay_Object = MibTableColumn
pps_DelelteDelay = _Pps_DelelteDelay_Object(
    (1, 3, 6, 1, 4, 1, 1229, 11, 31, 1, 11),
    _Pps_DelelteDelay_Type()
)
pps_DelelteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pps_DelelteDelay.setStatus("mandatory")
_SehTSE_ObjectIdentity = ObjectIdentity
sehTSE = _SehTSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1229, 12)
)
_TseNumber_Type = Integer32
_TseNumber_Object = MibScalar
tseNumber = _TseNumber_Object(
    (1, 3, 6, 1, 4, 1, 1229, 12, 1),
    _TseNumber_Type()
)
tseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tseNumber.setStatus("mandatory")
_TseTable_Object = MibTable
tseTable = _TseTable_Object(
    (1, 3, 6, 1, 4, 1, 1229, 12, 2)
)
if mibBuilder.loadTexts:
    tseTable.setStatus("mandatory")
_TseEntry_Object = MibTableRow
tseEntry = _TseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1229, 12, 2, 1)
)
tseEntry.setIndexNames(
    (0, "SEH-PSRV-MIB", "tse-Index"),
)
if mibBuilder.loadTexts:
    tseEntry.setStatus("mandatory")


class _Tse_Index_Type(Integer32):
    """Custom type tse_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Tse_Index_Type.__name__ = "Integer32"
_Tse_Index_Object = MibTableColumn
tse_Index = _Tse_Index_Object(
    (1, 3, 6, 1, 4, 1, 1229, 12, 2, 1, 1),
    _Tse_Index_Type()
)
tse_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tse_Index.setStatus("mandatory")

# Managed Objects groups


# Notification objects

prtFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1229, 0, 1)
)
prtFault.setObjects(
    ("SEH-PSRV-MIB", "pprtError")
)
if mibBuilder.loadTexts:
    prtFault.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEH-PSRV-MIB",
    **{"MailConnState": MailConnState,
       "seh": seh,
       "prtFault": prtFault,
       "sehDevice": sehDevice,
       "sehDevInfo": sehDevInfo,
       "sehPSrv": sehPSrv,
       "sehGeneral": sehGeneral,
       "sehSysInfo": sehSysInfo,
       "sehDefName": sehDefName,
       "sehPhysAddr": sehPhysAddr,
       "sehHwPn": sehHwPn,
       "sehBiosId": sehBiosId,
       "sehBiosVer": sehBiosVer,
       "sehCmpId": sehCmpId,
       "sehCmplevel": sehCmplevel,
       "sehSerNum": sehSerNum,
       "sehPrdYear": sehPrdYear,
       "sehPrdMonth": sehPrdMonth,
       "sehSwVer": sehSwVer,
       "sehSwRel": sehSwRel,
       "sehSwSub": sehSwSub,
       "sehSpMode": sehSpMode,
       "sehHwMajor": sehHwMajor,
       "sehHwMinor": sehHwMinor,
       "sehPassword": sehPassword,
       "sehAccessControl": sehAccessControl,
       "sehDealer": sehDealer,
       "sehDealerURL": sehDealerURL,
       "sehLocalisation": sehLocalisation,
       "sehHpJetAdminCompatibility": sehHpJetAdminCompatibility,
       "sehEnpcSupport": sehEnpcSupport,
       "sehAdminGroup": sehAdminGroup,
       "sehUpdateState": sehUpdateState,
       "sehJobRecvTimeout": sehJobRecvTimeout,
       "sehThinPrintPort": sehThinPrintPort,
       "sehHpHttpDaemon": sehHpHttpDaemon,
       "sehBaseLine": sehBaseLine,
       "sehEthernetConfig": sehEthernetConfig,
       "sehSwId": sehSwId,
       "sehNetworkType": sehNetworkType,
       "sehUtnPort": sehUtnPort,
       "sehZebraPort": sehZebraPort,
       "sehServiceInfo": sehServiceInfo,
       "sehButtonPressed": sehButtonPressed,
       "sehUtnSSLPort": sehUtnSSLPort,
       "sehUtnCiphert": sehUtnCiphert,
       "sehSwFeatures": sehSwFeatures,
       "sehPprinter": sehPprinter,
       "pprtNumber": pprtNumber,
       "pprtTable": pprtTable,
       "pprtEntry": pprtEntry,
       "pprtIndex": pprtIndex,
       "pprtError": pprtError,
       "pprtType": pprtType,
       "pprtEcp": pprtEcp,
       "pprtPanel": pprtPanel,
       "pprtMailNotification1": pprtMailNotification1,
       "pprtMailAddress1": pprtMailAddress1,
       "pprtMailServer1": pprtMailServer1,
       "pprtMailMask1": pprtMailMask1,
       "pprtMailNotification2": pprtMailNotification2,
       "pprtMailAddress2": pprtMailAddress2,
       "pprtMailServer2": pprtMailServer2,
       "pprtMailMask2": pprtMailMask2,
       "pprtModel": pprtModel,
       "pprtManufacturer": pprtManufacturer,
       "pprtEmulations": pprtEmulations,
       "pprtFast": pprtFast,
       "pprtBaudrate": pprtBaudrate,
       "pprtParity": pprtParity,
       "pprtDatabits": pprtDatabits,
       "pprtStopbits": pprtStopbits,
       "pprtFlowControl": pprtFlowControl,
       "pprtDeviceID": pprtDeviceID,
       "pprtDot4": pprtDot4,
       "pprtPortMode": pprtPortMode,
       "pprtPjl": pprtPjl,
       "pprtDynUpdate": pprtDynUpdate,
       "pprtDynUpdateUrl": pprtDynUpdateUrl,
       "pprtDynUpdateUsr": pprtDynUpdateUsr,
       "pprtDynUpdatePwd": pprtDynUpdatePwd,
       "pprtDynStatusPath": pprtDynStatusPath,
       "pprtDynUpdateHour": pprtDynUpdateHour,
       "pprtDynReportMin": pprtDynReportMin,
       "sehLprinter": sehLprinter,
       "lprtNumber": lprtNumber,
       "lprtTable": lprtTable,
       "lprtEntry": lprtEntry,
       "lprtIndex": lprtIndex,
       "lprtStart": lprtStart,
       "lprtEnd": lprtEnd,
       "lprtPhyPrt": lprtPhyPrt,
       "lprtTCPPort": lprtTCPPort,
       "lprtCRLF": lprtCRLF,
       "lprtHexDp": lprtHexDp,
       "lprtBp": lprtBp,
       "lprtAsPs": lprtAsPs,
       "lprtMode": lprtMode,
       "lprtRsoSpool": lprtRsoSpool,
       "lprtSearch": lprtSearch,
       "lprtReplace": lprtReplace,
       "lprtBinaryPS": lprtBinaryPS,
       "sehIp": sehIp,
       "ipIpAddr": ipIpAddr,
       "ipNetMask": ipNetMask,
       "ipDefGate": ipDefGate,
       "ipBOOTP": ipBOOTP,
       "ipRARP": ipRARP,
       "ipAutoconf": ipAutoconf,
       "ipDHCP": ipDHCP,
       "ipZeroConf": ipZeroConf,
       "ipSetBy": ipSetBy,
       "ipWinsPrimarySrv": ipWinsPrimarySrv,
       "ipWinsSecondarySrv": ipWinsSecondarySrv,
       "ipTCP": ipTCP,
       "ipDNS": ipDNS,
       "ipDomainName": ipDomainName,
       "ipDnsPrimarySrv": ipDnsPrimarySrv,
       "ipDnsSecondarySrv": ipDnsSecondarySrv,
       "ipSenderNumber": ipSenderNumber,
       "ipSenderTable": ipSenderTable,
       "ipSenderEntry": ipSenderEntry,
       "ipSenderIndex": ipSenderIndex,
       "ipSender": ipSender,
       "ipAutoGate": ipAutoGate,
       "ipZeroConfig": ipZeroConfig,
       "ipHTTP": ipHTTP,
       "ipIPv6": ipIPv6,
       "ipIPv6Addr": ipIPv6Addr,
       "ipIPv6Plen": ipIPv6Plen,
       "ipIPv6Gate": ipIPv6Gate,
       "ipIPv6Auto": ipIPv6Auto,
       "ipFTP": ipFTP,
       "sehNovell": sehNovell,
       "nwName": nwName,
       "nwNDS": nwNDS,
       "nwBindery": nwBindery,
       "nw8022": nw8022,
       "nw8023": nw8023,
       "nwEthII": nwEthII,
       "nwSNAP": nwSNAP,
       "nwUpdate": nwUpdate,
       "nwUpdTime": nwUpdTime,
       "nwPollTime": nwPollTime,
       "nwServer1": nwServer1,
       "nwServer2": nwServer2,
       "nwServer3": nwServer3,
       "nwServer4": nwServer4,
       "nwNDSCommonName": nwNDSCommonName,
       "nwNDSTreeFound": nwNDSTreeFound,
       "nwNDSFound": nwNDSFound,
       "nwConnNumber": nwConnNumber,
       "nwConnTable": nwConnTable,
       "nwConnEntry": nwConnEntry,
       "nwConnIndex": nwConnIndex,
       "nwConnServer": nwConnServer,
       "nwConnState": nwConnState,
       "nwConnLastError": nwConnLastError,
       "nwConnServerState": nwConnServerState,
       "nwConnHeader": nwConnHeader,
       "nwConnNet": nwConnNet,
       "nwQueueNumber": nwQueueNumber,
       "nwQueueTable": nwQueueTable,
       "nwQueueEntry": nwQueueEntry,
       "nwQueueIndex": nwQueueIndex,
       "nwQueueName": nwQueueName,
       "nwQueueConnId": nwQueueConnId,
       "nwQueuePort": nwQueuePort,
       "nwQueueState": nwQueueState,
       "nwRprinterHeader": nwRprinterHeader,
       "nwNDSPwd": nwNDSPwd,
       "nwBinderyPwd": nwBinderyPwd,
       "nw8025": nw8025,
       "nwPserver": nwPserver,
       "nwRprinter": nwRprinter,
       "nwAdvPserver": nwAdvPserver,
       "nwLogPrinter": nwLogPrinter,
       "nwSPXConnState": nwSPXConnState,
       "nwNDSTree": nwNDSTree,
       "nwIPX": nwIPX,
       "nwMyNet": nwMyNet,
       "nwPureIp": nwPureIp,
       "sehApple": sehApple,
       "appleTalk": appleTalk,
       "appleName": appleName,
       "appleZone": appleZone,
       "applePrinter": applePrinter,
       "appleCurrentName": appleCurrentName,
       "appleCurrentZone": appleCurrentZone,
       "appleEntity": appleEntity,
       "appleNet": appleNet,
       "appleNode": appleNode,
       "appleRouterNet": appleRouterNet,
       "appleRouterNode": appleRouterNode,
       "appleBidirectional": appleBidirectional,
       "appleBinary": appleBinary,
       "appleRendezvous": appleRendezvous,
       "applePortNumber": applePortNumber,
       "applePortTable": applePortTable,
       "applePortEntry": applePortEntry,
       "applePortIndex": applePortIndex,
       "applePortBidirectional": applePortBidirectional,
       "applePortPrinter": applePortPrinter,
       "applePortEntity": applePortEntity,
       "applePortBinaryEncoding": applePortBinaryEncoding,
       "applePortCurrentName": applePortCurrentName,
       "appleRendezvousPortName": appleRendezvousPortName,
       "appleRendezvousCurrentPortName": appleRendezvousCurrentPortName,
       "sehSnmp": sehSnmp,
       "snmpIpAddr1": snmpIpAddr1,
       "snmpIpAddr2": snmpIpAddr2,
       "snmpIpxAddr1": snmpIpxAddr1,
       "snmpIpxAddr2": snmpIpxAddr2,
       "snmpTrapComm": snmpTrapComm,
       "snmpAutTrap": snmpAutTrap,
       "snmpPrtTrap": snmpPrtTrap,
       "snmpTrapNumber": snmpTrapNumber,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapIndex": snmpTrapIndex,
       "snmpTrapIpAddress": snmpTrapIpAddress,
       "snmpTrapIpxAddress": snmpTrapIpxAddress,
       "snmpTrapAuthentication": snmpTrapAuthentication,
       "snmpTrapPrinter1": snmpTrapPrinter1,
       "snmpTrapMask1": snmpTrapMask1,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpCommunity": snmpCommunity,
       "snmpV1": snmpV1,
       "snmpV1AccMode": snmpV1AccMode,
       "snmpV3": snmpV3,
       "sehActions": sehActions,
       "actAction": actAction,
       "actUpdate": actUpdate,
       "actUpdateUrl": actUpdateUrl,
       "actUpdateProxy": actUpdateProxy,
       "actUpdateProxyName": actUpdateProxyName,
       "actPrtUpdate": actPrtUpdate,
       "actPrtUpdateUrl": actPrtUpdateUrl,
       "actPrtUpdateUsr": actPrtUpdateUsr,
       "actPrtUpdatePwd": actPrtUpdatePwd,
       "actPrtUpdateProxy": actPrtUpdateProxy,
       "actPrtUpdateProxyName": actPrtUpdateProxyName,
       "sehTokenRing": sehTokenRing,
       "trEarlyTokRel": trEarlyTokRel,
       "trSourceRouting": trSourceRouting,
       "trPhysAddr": trPhysAddr,
       "trRingSpeed": trRingSpeed,
       "sehWireless": sehWireless,
       "wlanMode": wlanMode,
       "wlanChannel": wlanChannel,
       "wlanNetworkName": wlanNetworkName,
       "wlanEncrypt": wlanEncrypt,
       "wlanWepKey1": wlanWepKey1,
       "wlanDistance": wlanDistance,
       "wlanLevel": wlanLevel,
       "wlanSpeed": wlanSpeed,
       "wlanConnectionStatus": wlanConnectionStatus,
       "wlanManufacturer": wlanManufacturer,
       "wlanCurrentName": wlanCurrentName,
       "wlanPcmciaSerial": wlanPcmciaSerial,
       "wlanKeyId": wlanKeyId,
       "wlanWepKey2": wlanWepKey2,
       "wlanWepKey3": wlanWepKey3,
       "wlanWepKey4": wlanWepKey4,
       "eapAuthType": eapAuthType,
       "eapAuthName": eapAuthName,
       "eapAuthPwd": eapAuthPwd,
       "wlanPSK": wlanPSK,
       "wlanRoaming": wlanRoaming,
       "eapAuthExtern": eapAuthExtern,
       "eapAuthIntern": eapAuthIntern,
       "eapAuthAnonymousName": eapAuthAnonymousName,
       "eapAuthSupplicantAddOn": eapAuthSupplicantAddOn,
       "wlandBm2Roam": wlandBm2Roam,
       "wlandWps": wlandWps,
       "wlen": wlen,
       "wlan": wlan,
       "onTheAir": onTheAir,
       "sehWin": sehWin,
       "winSmb": winSmb,
       "winNetbiosName": winNetbiosName,
       "winNetbiosDomain": winNetbiosDomain,
       "winNetbiosRefresh": winNetbiosRefresh,
       "winWinsReg": winWinsReg,
       "winWinsDHCP": winWinsDHCP,
       "winWinsPrimarySrv": winWinsPrimarySrv,
       "winWinsSecondarySrv": winWinsSecondarySrv,
       "sehTime": sehTime,
       "timeSntp": timeSntp,
       "timeServer": timeServer,
       "timeZoneOffset": timeZoneOffset,
       "timeDate": timeDate,
       "timeZoneNameAndRule": timeZoneNameAndRule,
       "sehPrintjob": sehPrintjob,
       "pjobCount": pjobCount,
       "pjobTable": pjobTable,
       "pjobEntry": pjobEntry,
       "pjobIndex": pjobIndex,
       "pjobStatus": pjobStatus,
       "pjobProtocol": pjobProtocol,
       "pjobName": pjobName,
       "pjobSender": pjobSender,
       "pjobSize": pjobSize,
       "pjobCreationTime": pjobCreationTime,
       "pjobDuration": pjobDuration,
       "pjobPport": pjobPport,
       "pjobPages": pjobPages,
       "pjobSizeType": pjobSizeType,
       "sehNotification": sehNotification,
       "nfSlotNumber": nfSlotNumber,
       "nfSlotTable": nfSlotTable,
       "nfSlotEntry": nfSlotEntry,
       "nfSlotIndex": nfSlotIndex,
       "nfMailNotification": nfMailNotification,
       "nfMailAddress": nfMailAddress,
       "nfMailServer": nfMailServer,
       "nfTrapIpAddress": nfTrapIpAddress,
       "nfTrapIpxAddress": nfTrapIpxAddress,
       "nfTrapAuthentication": nfTrapAuthentication,
       "nfTrapPrinter": nfTrapPrinter,
       "nfTrapCommunity": nfTrapCommunity,
       "nfAccJobHist": nfAccJobHist,
       "nfAccJobHistTime": nfAccJobHistTime,
       "nfAccJobHistCntr": nfAccJobHistCntr,
       "nfPortNumber": nfPortNumber,
       "nfPortTable": nfPortTable,
       "nfPortEntry": nfPortEntry,
       "nfPortIndex": nfPortIndex,
       "nfPortMailMask1": nfPortMailMask1,
       "nfPortMailMask2": nfPortMailMask2,
       "nfPortTrapMask1": nfPortTrapMask1,
       "nfPortTrapMask2": nfPortTrapMask2,
       "nfPortAccPageCntr1": nfPortAccPageCntr1,
       "nfPortAccPageCntr2": nfPortAccPageCntr2,
       "nfPortAccPageCntrTime1": nfPortAccPageCntrTime1,
       "nfPortAccPageCntrTime2": nfPortAccPageCntrTime2,
       "nfPortAccPageCntrCntr1": nfPortAccPageCntrCntr1,
       "nfPortAccPageCntrCntr2": nfPortAccPageCntrCntr2,
       "nfPortMailList1": nfPortMailList1,
       "nfPortMailList2": nfPortMailList2,
       "nfPortTrapList1": nfPortTrapList1,
       "nfPortTrapList2": nfPortTrapList2,
       "nfPortAccPageCntrIndex1": nfPortAccPageCntrIndex1,
       "nfPortAccPageCntrIndex2": nfPortAccPageCntrIndex2,
       "nfSmtpServer": nfSmtpServer,
       "sehMail": sehMail,
       "nfPop3": nfPop3,
       "nfPop3Poll": nfPop3Poll,
       "nfPop3Srv": nfPop3Srv,
       "nfPop3SrvPort": nfPop3SrvPort,
       "nfPop3SmtpSrv": nfPop3SmtpSrv,
       "nfPop3SmtpPort": nfPop3SmtpPort,
       "nfPop3Usr": nfPop3Usr,
       "nfPop3Pwd": nfPop3Pwd,
       "nfPop3Security": nfPop3Security,
       "nfPop3MDel": nfPop3MDel,
       "nfPop3Limit": nfPop3Limit,
       "nfPop3Signature": nfPop3Signature,
       "nfSmtpUsr": nfSmtpUsr,
       "nfSmtpPwd": nfSmtpPwd,
       "nfSmtpSndr": nfSmtpSndr,
       "nfSmtpSsl": nfSmtpSsl,
       "nfSmtpAsPop3": nfSmtpAsPop3,
       "nfSmtpAuth": nfSmtpAuth,
       "nfPop3P3His": nfPop3P3His,
       "nfPop3SMTPHis": nfPop3SMTPHis,
       "nfPop3P3Ctr": nfPop3P3Ctr,
       "nfPop3SMTPCtr": nfPop3SMTPCtr,
       "nfPop3P3Err": nfPop3P3Err,
       "nfPop3SmtpErr": nfPop3SmtpErr,
       "nfPop3P3Next": nfPop3P3Next,
       "smtpSMIMESig": smtpSMIMESig,
       "smtpSMIMEAddKey": smtpSMIMEAddKey,
       "smtpSMIMEEnc": smtpSMIMEEnc,
       "sehNat": sehNat,
       "natLocal": natLocal,
       "natRemote": natRemote,
       "httpPort": httpPort,
       "natMasquerade": natMasquerade,
       "natIcmp": natIcmp,
       "spagePort": spagePort,
       "sehNatDrop": sehNatDrop,
       "httpsPort": httpsPort,
       "ftpPort": ftpPort,
       "ftpDataPort": ftpDataPort,
       "snmpPort": snmpPort,
       "aicePort": aicePort,
       "natDropNumber": natDropNumber,
       "natDropTable": natDropTable,
       "natDropEntry": natDropEntry,
       "natDropIndex": natDropIndex,
       "natDropPort": natDropPort,
       "natDropTcp": natDropTcp,
       "natDropUdp": natDropUdp,
       "natDropLan": natDropLan,
       "natDropNat": natDropNat,
       "sehTpg": sehTpg,
       "tpgNumber": tpgNumber,
       "tpgTable": tpgTable,
       "tpgEntry": tpgEntry,
       "tpgIndex": tpgIndex,
       "tpgPrtName": tpgPrtName,
       "tpgPrtClass": tpgPrtClass,
       "tpgPrtDriver": tpgPrtDriver,
       "tpgRemoteIp": tpgRemoteIp,
       "tpgRemotePort": tpgRemotePort,
       "tpgRemoteStat": tpgRemoteStat,
       "tpgRemoteQueue": tpgRemoteQueue,
       "tpgRemoteLPD": tpgRemoteLPD,
       "tpgLpdModeRFC": tpgLpdModeRFC,
       "tpgRemoteUrl": tpgRemoteUrl,
       "tpgRemoteIPPs": tpgRemoteIPPs,
       "tpgRemoteStStr": tpgRemoteStStr,
       "tpgClientId": tpgClientId,
       "tpgAuthKey": tpgAuthKey,
       "tpgBandwidth": tpgBandwidth,
       "tpgBandwidthVal": tpgBandwidthVal,
       "tpgConnServices": tpgConnServices,
       "tpgConnServer": tpgConnServer,
       "tpgConnServerPort": tpgConnServerPort,
       "tpgConnRetry": tpgConnRetry,
       "tpgKeepAlive": tpgKeepAlive,
       "tpgSpagePrt": tpgSpagePrt,
       "tpgConnState": tpgConnState,
       "tpgStreamCompr": tpgStreamCompr,
       "tpgSpage": tpgSpage,
       "tpgPrtOpenToVal": tpgPrtOpenToVal,
       "tpgJobSendTimeout": tpgJobSendTimeout,
       "tpgJobRecvTimeout": tpgJobRecvTimeout,
       "tpgMonitorPoll": tpgMonitorPoll,
       "tpgMonitorPing": tpgMonitorPing,
       "tpgMonitorSnmp": tpgMonitorSnmp,
       "sehLrs": sehLrs,
       "lrsAesKey": lrsAesKey,
       "lrsAesType": lrsAesType,
       "lrsIsppPort": lrsIsppPort,
       "lrsUseInstallationKey": lrsUseInstallationKey,
       "lrsAllowKeyChange": lrsAllowKeyChange,
       "lrsPrtPort": lrsPrtPort,
       "sehProtection": sehProtection,
       "protection": protection,
       "protectionTest": protectionTest,
       "protectionLevel": protectionLevel,
       "ipFilterNumber": ipFilterNumber,
       "ipFilterTable": ipFilterTable,
       "ipFilterEntry": ipFilterEntry,
       "ipFilterIndex": ipFilterIndex,
       "ipFilterOnOff": ipFilterOnOff,
       "ipFilterAddr": ipFilterAddr,
       "macFilterNumber": macFilterNumber,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterIndex": macFilterIndex,
       "macFilterOnOff": macFilterOnOff,
       "macFilterAddr": macFilterAddr,
       "cipherStrength": cipherStrength,
       "rsaBits": rsaBits,
       "sehUser": sehUser,
       "usrAnyName": usrAnyName,
       "usrAnyPwd": usrAnyPwd,
       "usrAnyAcc": usrAnyAcc,
       "usrAnyHash": usrAnyHash,
       "usrAnyCypher": usrAnyCypher,
       "usrAdminName": usrAdminName,
       "usrAdminPwd": usrAdminPwd,
       "usrAdminAcc": usrAdminAcc,
       "usrAdminHash": usrAdminHash,
       "usrAdminCypher": usrAdminCypher,
       "sehIPsec": sehIPsec,
       "ipsecIPsec": ipsecIPsec,
       "ipsecConfig": ipsecConfig,
       "ipsecDefAction": ipsecDefAction,
       "ipsecRulesNumber": ipsecRulesNumber,
       "ipsecRulesTable": ipsecRulesTable,
       "ipsecRulesEntry": ipsecRulesEntry,
       "ipsecRulesIndex": ipsecRulesIndex,
       "ipsecRulesEnabled": ipsecRulesEnabled,
       "ipsecRulesIaddr": ipsecRulesIaddr,
       "ipsecRulesIserv": ipsecRulesIserv,
       "ipsecRulesIPsec": ipsecRulesIPsec,
       "ipsecRulesAction": ipsecRulesAction,
       "ipsecAddrTmplNumber": ipsecAddrTmplNumber,
       "ipsecAddrTmplTable": ipsecAddrTmplTable,
       "ipsecAddrTmplEntry": ipsecAddrTmplEntry,
       "ipsecAddrTmplIndex": ipsecAddrTmplIndex,
       "ipsecAddrTmplName": ipsecAddrTmplName,
       "ipsecAddrTmplRemoteIPv4": ipsecAddrTmplRemoteIPv4,
       "ipsecAddrTmplLocalIPv6": ipsecAddrTmplLocalIPv6,
       "ipsecAddrTmplRemoteIPv6": ipsecAddrTmplRemoteIPv6,
       "ipsecServTmplNumber": ipsecServTmplNumber,
       "ipsecServTmplTable": ipsecServTmplTable,
       "ipsecServTmplEntry": ipsecServTmplEntry,
       "ipsecServTmplIndex": ipsecServTmplIndex,
       "ipsecServTmplName": ipsecServTmplName,
       "ipsecServTmplServ": ipsecServTmplServ,
       "ipsecSATmplNumber": ipsecSATmplNumber,
       "ipsecSATmplTable": ipsecSATmplTable,
       "ipsecSATmplEntry": ipsecSATmplEntry,
       "ipsecSATmplIndex": ipsecSATmplIndex,
       "ipsecSATmplName": ipsecSATmplName,
       "ipsecSATmplCert": ipsecSATmplCert,
       "ipsecSATmplVeri": ipsecSATmplVeri,
       "ipsecSATmplPSK": ipsecSATmplPSK,
       "ipsecSATmplIKE": ipsecSATmplIKE,
       "ipsecIKETmplNumber": ipsecIKETmplNumber,
       "ipsecIKETmplTable": ipsecIKETmplTable,
       "ipsecIKETmplEntry": ipsecIKETmplEntry,
       "ipsecIKETmplIndex": ipsecIKETmplIndex,
       "ipsecIKETmplName": ipsecIKETmplName,
       "ipsecIKETmplModes": ipsecIKETmplModes,
       "ipsecIKETmplDhGroup": ipsecIKETmplDhGroup,
       "ipsecIKETmplEncV1": ipsecIKETmplEncV1,
       "ipsecIKETmplAuthV1": ipsecIKETmplAuthV1,
       "ipsecIKETmplLtV1": ipsecIKETmplLtV1,
       "ipsecIKETmplEncMode": ipsecIKETmplEncMode,
       "ipsecIKETmplPfsGroup": ipsecIKETmplPfsGroup,
       "ipsecIKETmplEncV2": ipsecIKETmplEncV2,
       "ipsecIKETmplAuthV2": ipsecIKETmplAuthV2,
       "ipsecIKETmplAH": ipsecIKETmplAH,
       "ipsecIKETmplLtV2": ipsecIKETmplLtV2,
       "ipsecIKETmplLtKb": ipsecIKETmplLtKb,
       "ipsecDHCP": ipsecDHCP,
       "ipsecNetbios": ipsecNetbios,
       "ipsecBonjour": ipsecBonjour,
       "ipsecSLP": ipsecSLP,
       "ipsecFTP": ipsecFTP,
       "ipsecTest": ipsecTest,
       "sehIpVLan": sehIpVLan,
       "ip4VLanNumber": ip4VLanNumber,
       "ip4VLanTable": ip4VLanTable,
       "ip4VLanEntry": ip4VLanEntry,
       "ip4VLanIndex": ip4VLanIndex,
       "ip4VLanOnOff": ip4VLanOnOff,
       "ip4VLanAddr": ip4VLanAddr,
       "ip4VLanMask": ip4VLanMask,
       "ip4VLanID": ip4VLanID,
       "ip4VLanGate": ip4VLanGate,
       "ip4VLanWeb": ip4VLanWeb,
       "ip4VLanSNMP": ip4VLanSNMP,
       "ip4VLanMgmt": ip4VLanMgmt,
       "ip4VLanMgmtID": ip4VLanMgmtID,
       "ip4VLanMgmtAny": ip4VLanMgmtAny,
       "ip4VLanMgmtUntag": ip4VLanMgmtUntag,
       "sehUtn": sehUtn,
       "utnPortNumber": utnPortNumber,
       "utnPortTable": utnPortTable,
       "utnPortEntry": utnPortEntry,
       "utnPortIndex": utnPortIndex,
       "utnPortSecure": utnPortSecure,
       "utnPortPoSwitch": utnPortPoSwitch,
       "utnPortPoOffDura": utnPortPoOffDura,
       "utnPortAccCtrl": utnPortAccCtrl,
       "utnPortKeyVal": utnPortKeyVal,
       "utnPortProdId": utnPortProdId,
       "utnPortVendId": utnPortVendId,
       "utnPortIp4Vlan": utnPortIp4Vlan,
       "utnPortTag": utnPortTag,
       "utnPortComp": utnPortComp,
       "utnPortUsbManu": utnPortUsbManu,
       "utnPortUsbProd": utnPortUsbProd,
       "utnPortUsbVendId": utnPortUsbVendId,
       "utnPortUsbProdId": utnPortUsbProdId,
       "utnPortUsbSer": utnPortUsbSer,
       "utnPortUsbOwn": utnPortUsbOwn,
       "utnPortSlot": utnPortSlot,
       "utnDispDef": utnDispDef,
       "utnDispErVals": utnDispErVals,
       "utnBeepPwr": utnBeepPwr,
       "utnBeepSDc": utnBeepSDc,
       "utnHid": utnHid,
       "utnRelayOn": utnRelayOn,
       "utnRelayFix": utnRelayFix,
       "utnRelayEves": utnRelayEves,
       "utnRelayRestart": utnRelayRestart,
       "utnRelay1Pwr": utnRelay1Pwr,
       "utnRelay2Pwr": utnRelay2Pwr,
       "utnRelayNet": utnRelayNet,
       "utnRelaySDCard": utnRelaySDCard,
       "utnRelayUsbCon": utnRelayUsbCon,
       "utnRelayUsbDisco": utnRelayUsbDisco,
       "utnRelayUsbActivate": utnRelayUsbActivate,
       "utnRelayUsbDeActivate": utnRelayUsbDeActivate,
       "utnRelayCtrl": utnRelayCtrl,
       "utnRelayStateNet": utnRelayStateNet,
       "utnRelayStateUsbCon": utnRelayStateUsbCon,
       "utnRelayStateUsbDisco": utnRelayStateUsbDisco,
       "utnRelayStateUsbActivate": utnRelayStateUsbActivate,
       "utnRelayStateUsbDeActivate": utnRelayStateUsbDeActivate,
       "sehUtnEvent": sehUtnEvent,
       "utnEventType": utnEventType,
       "utnEventPort": utnEventPort,
       "utnEventMsg": utnEventMsg,
       "utnEventManu": utnEventManu,
       "utnEventManuId": utnEventManuId,
       "utnEventProd": utnEventProd,
       "utnEventProdId": utnEventProdId,
       "utnEventSerial": utnEventSerial,
       "tniEventCard": tniEventCard,
       "sehSnd": sehSnd,
       "sehSndUser": sehSndUser,
       "sndUserNumber": sndUserNumber,
       "sndUserTable": sndUserTable,
       "sndUserEntry": sndUserEntry,
       "sndUserIndex": sndUserIndex,
       "sndUserActive": sndUserActive,
       "sndUserName": sndUserName,
       "sndUserPwd": sndUserPwd,
       "sndUserEmail": sndUserEmail,
       "sndUserFFilter": sndUserFFilter,
       "sndUserRAdm": sndUserRAdm,
       "sndUserRDLoad": sndUserRDLoad,
       "sndUserRSend": sndUserRSend,
       "sndUserRTogg": sndUserRTogg,
       "sndUserRWrt": sndUserRWrt,
       "sehSndSender": sehSndSender,
       "sndSendMaxFiles": sndSendMaxFiles,
       "sndSendMaxKb": sndSendMaxKb,
       "sndSenderPDMedia": sndSenderPDMedia,
       "sndSenderPDDir": sndSenderPDDir,
       "sndSenderPDExt": sndSenderPDExt,
       "sndSenderPDaBit": sndSenderPDaBit,
       "sndSenderPDRcpNum": sndSenderPDRcpNum,
       "sndSenderPDRcpTable": sndSenderPDRcpTable,
       "sndSenderPDRcpEntry": sndSenderPDRcpEntry,
       "sndPDRcpIndex": sndPDRcpIndex,
       "sndPDRcpEmail": sndPDRcpEmail,
       "sndSenderSDActive": sndSenderSDActive,
       "sndSenderSDRcp": sndSenderSDRcp,
       "sndSenderSDNum": sndSenderSDNum,
       "sndSenderSDTable": sndSenderSDTable,
       "sndSenderSDEntry": sndSenderSDEntry,
       "sndSDIndex": sndSDIndex,
       "sndSDMedia": sndSDMedia,
       "sndSDDir": sndSDDir,
       "sndSDExt": sndSDExt,
       "sndSDaBit": sndSDaBit,
       "sehSndFFilter": sehSndFFilter,
       "sndFFilterNum": sndFFilterNum,
       "sndFFilterTable": sndFFilterTable,
       "sndFFilterEntry": sndFFilterEntry,
       "sndFFilterIndex": sndFFilterIndex,
       "sndFFilterName": sndFFilterName,
       "sndFFilter": sndFFilter,
       "sehSndSDCard": sehSndSDCard,
       "sndSDCardNum": sndSDCardNum,
       "sndSDCardTable": sndSDCardTable,
       "sndSDCardEntry": sndSDCardEntry,
       "sndSDCardIndex": sndSDCardIndex,
       "sndSDCardCid": sndSDCardCid,
       "sndSDCardName": sndSDCardName,
       "sndSDCardUList": sndSDCardUList,
       "sndSDCardARcp": sndSDCardARcp,
       "sndPDPort": sndPDPort,
       "sehPPS": sehPPS,
       "pps": pps,
       "ppsPIN": ppsPIN,
       "ppsPrtId": ppsPrtId,
       "ppsDelete": ppsDelete,
       "ppsDelelteDelay": ppsDelelteDelay,
       "ppsSingle": ppsSingle,
       "ppsBeep": ppsBeep,
       "ppsUSRForm": ppsUSRForm,
       "ppsPWD": ppsPWD,
       "ppsPort": ppsPort,
       "ppsSSL": ppsSSL,
       "ppsVerify": ppsVerify,
       "ppsServer": ppsServer,
       "ppsServerAlt": ppsServerAlt,
       "ppsNumber": ppsNumber,
       "ppsTable": ppsTable,
       "ppsEntry": ppsEntry,
       "pps-Index": pps_Index,
       "pps-On": pps_On,
       "pps-Server": pps_Server,
       "pps-PIN": pps_PIN,
       "pps-PWD": pps_PWD,
       "pps-Port": pps_Port,
       "pps-SSL": pps_SSL,
       "pps-Verify": pps_Verify,
       "pps-PrtId": pps_PrtId,
       "pps-Delete": pps_Delete,
       "pps-DelelteDelay": pps_DelelteDelay,
       "sehTSE": sehTSE,
       "tseNumber": tseNumber,
       "tseTable": tseTable,
       "tseEntry": tseEntry,
       "tse-Index": tse_Index}
)
