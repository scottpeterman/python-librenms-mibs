# SNMP MIB module (DASAN-ADSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ADSL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:58 2025
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

(adslAtucChanIntervalNumber,
 adslAtucIntervalNumber,
 adslAturChanIntervalNumber,
 adslLineAlarmConfProfileName,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslAtucChanIntervalNumber",
    "adslAtucIntervalNumber",
    "adslAturChanIntervalNumber",
    "adslLineAlarmConfProfileName",
    "adslLineConfProfileName")

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dasanAdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanAdslLineMIB_ObjectIdentity = ObjectIdentity
dasanAdslLineMIB = _DasanAdslLineMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1)
)
_DasanAdslMIBObjects_ObjectIdentity = ObjectIdentity
dasanAdslMIBObjects = _DasanAdslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1)
)
_DsDslSystemParamGroup_ObjectIdentity = ObjectIdentity
dsDslSystemParamGroup = _DsDslSystemParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 1)
)


class _DsDslSystemDslType_Type(Integer32):
    """Custom type dsDslSystemDslType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 1),
          ("sdsl", 2),
          ("shdsl", 3))
    )


_DsDslSystemDslType_Type.__name__ = "Integer32"
_DsDslSystemDslType_Object = MibScalar
dsDslSystemDslType = _DsDslSystemDslType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 1, 1),
    _DsDslSystemDslType_Type()
)
dsDslSystemDslType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDslSystemDslType.setStatus("current")


class _DsDslSystemLineCodingType_Type(Integer32):
    """Custom type dsDslSystemLineCodingType based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("dmt", 2),
          ("cap", 3),
          ("qam", 4))
    )


_DsDslSystemLineCodingType_Type.__name__ = "Integer32"
_DsDslSystemLineCodingType_Object = MibScalar
dsDslSystemLineCodingType = _DsDslSystemLineCodingType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 1, 2),
    _DsDslSystemLineCodingType_Type()
)
dsDslSystemLineCodingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDslSystemLineCodingType.setStatus("current")


class _DsDslSystemLineTxCfg_Type(Bits):
    """Custom type dsDslSystemLineTxCfg based on Bits"""
    defaultHexValue = "0c"

    namedValues = NamedValues(
        *(("ansit1413", 0),
          ("etsi", 1),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921IsdnOverlapped", 5),
          ("q9921TcmIsdnNonOverlapped", 6),
          ("q9921TcmIsdnOverlapped", 7),
          ("q9922PotsNonOverlapped", 8),
          ("q9922PotsOverlapped", 9),
          ("q9922TcmIsdnNonOverlapped", 10),
          ("q9922TcmIsdnOverlapped", 11),
          ("q9921TcmIsdnSymmetric", 12))
    )

_DsDslSystemLineTxCfg_Type.__name__ = "Bits"
_DsDslSystemLineTxCfg_Object = MibScalar
dsDslSystemLineTxCfg = _DsDslSystemLineTxCfg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 1, 3),
    _DsDslSystemLineTxCfg_Type()
)
dsDslSystemLineTxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDslSystemLineTxCfg.setStatus("current")
_DsAdslCapabilityGroup_ObjectIdentity = ObjectIdentity
dsAdslCapabilityGroup = _DsAdslCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 2)
)


class _DsAdslCapabilityLineTxCap_Type(Bits):
    """Custom type dsAdslCapabilityLineTxCap based on Bits"""
    namedValues = NamedValues(
        *(("ansit1413", 0),
          ("etsi", 1),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921IsdnOverlapped", 5),
          ("q9921TcmIsdnNonOverlapped", 6),
          ("q9921TcmIsdnOverlapped", 7),
          ("q9922PotsNonOverlapped", 8),
          ("q9922PotsOverlapped", 9),
          ("q9922TcmIsdnNonOverlapped", 10),
          ("q9922TcmIsdnOverlapped", 11),
          ("q9921TcmIsdnSymmetric", 12),
          ("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921GspanPlusPotsNonOverlapped", 31))
    )

_DsAdslCapabilityLineTxCap_Type.__name__ = "Bits"
_DsAdslCapabilityLineTxCap_Object = MibScalar
dsAdslCapabilityLineTxCap = _DsAdslCapabilityLineTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 2, 1),
    _DsAdslCapabilityLineTxCap_Type()
)
dsAdslCapabilityLineTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslCapabilityLineTxCap.setStatus("current")
_DsAdslLineExtnTable_Object = MibTable
dsAdslLineExtnTable = _DsAdslLineExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dsAdslLineExtnTable.setStatus("current")
_DsAdslLineExtnEntry_Object = MibTableRow
dsAdslLineExtnEntry = _DsAdslLineExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1)
)
dsAdslLineExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslLineExtnEntry.setStatus("current")


class _DsAdslLineExtnAction_Type(Integer32):
    """Custom type dsAdslLineExtnAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6,
              7,
              10,
              26,
              27,
              30,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              101,
              102,
              4134)
        )
    )
    namedValues = NamedValues(
        *(("startup", 0),
          ("spectrumReverb", 5),
          ("analogLb", 6),
          ("digitalLb", 7),
          ("atmLp", 10),
          ("spectrumMedley", 26),
          ("spectrumPilot", 27),
          ("spectrumCMtpr", 30),
          ("spectrumRMtpr", 32),
          ("hybridLossTest", 33),
          ("rcvLinearityTest", 34),
          ("rcvFilterTest", 35),
          ("rcvPowerPerBinTest", 36),
          ("idleNoisePerBinTest", 37),
          ("totalIdleNoiseTest", 38),
          ("shutdown", 101),
          ("wakeup", 102),
          ("selt", 4134))
    )


_DsAdslLineExtnAction_Type.__name__ = "Integer32"
_DsAdslLineExtnAction_Object = MibTableColumn
dsAdslLineExtnAction = _DsAdslLineExtnAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 1),
    _DsAdslLineExtnAction_Type()
)
dsAdslLineExtnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineExtnAction.setStatus("current")


class _DsAdslLineExtnUtopiaL2RxAddr_Type(Integer32):
    """Custom type dsAdslLineExtnUtopiaL2RxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DsAdslLineExtnUtopiaL2RxAddr_Type.__name__ = "Integer32"
_DsAdslLineExtnUtopiaL2RxAddr_Object = MibTableColumn
dsAdslLineExtnUtopiaL2RxAddr = _DsAdslLineExtnUtopiaL2RxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 2),
    _DsAdslLineExtnUtopiaL2RxAddr_Type()
)
dsAdslLineExtnUtopiaL2RxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnUtopiaL2RxAddr.setStatus("current")


class _DsAdslLineExtnUtopiaL2TxAddr_Type(Integer32):
    """Custom type dsAdslLineExtnUtopiaL2TxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DsAdslLineExtnUtopiaL2TxAddr_Type.__name__ = "Integer32"
_DsAdslLineExtnUtopiaL2TxAddr_Object = MibTableColumn
dsAdslLineExtnUtopiaL2TxAddr = _DsAdslLineExtnUtopiaL2TxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 3),
    _DsAdslLineExtnUtopiaL2TxAddr_Type()
)
dsAdslLineExtnUtopiaL2TxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnUtopiaL2TxAddr.setStatus("current")


class _DsAdslLineExtnTransAtucCap_Type(Bits):
    """Custom type dsAdslLineExtnTransAtucCap based on Bits"""
    namedValues = NamedValues(
        *(("ansit1413", 0),
          ("etsi", 1),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9921tcmIsdnSymmetric", 12),
          ("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("vdslOverlapped", 24),
          ("vdslNonOverlapped", 25),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921GspanPlusPotsNonOverlapped", 31))
    )

_DsAdslLineExtnTransAtucCap_Type.__name__ = "Bits"
_DsAdslLineExtnTransAtucCap_Object = MibTableColumn
dsAdslLineExtnTransAtucCap = _DsAdslLineExtnTransAtucCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 4),
    _DsAdslLineExtnTransAtucCap_Type()
)
dsAdslLineExtnTransAtucCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnTransAtucCap.setStatus("current")


class _DsAdslLineExtnTransAtucActual_Type(Bits):
    """Custom type dsAdslLineExtnTransAtucActual based on Bits"""
    namedValues = NamedValues(
        *(("ansit1413", 0),
          ("etsi", 1),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9921tcmIsdnSymmetric", 12),
          ("adslPlusPotsNonOverlapped", 13))
    )

_DsAdslLineExtnTransAtucActual_Type.__name__ = "Bits"
_DsAdslLineExtnTransAtucActual_Object = MibTableColumn
dsAdslLineExtnTransAtucActual = _DsAdslLineExtnTransAtucActual_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 5),
    _DsAdslLineExtnTransAtucActual_Type()
)
dsAdslLineExtnTransAtucActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnTransAtucActual.setStatus("current")


class _DsAdslLineExtnClockType_Type(Integer32):
    """Custom type dsAdslLineExtnClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oscillator", 0),
          ("crystal", 4))
    )


_DsAdslLineExtnClockType_Type.__name__ = "Integer32"
_DsAdslLineExtnClockType_Object = MibTableColumn
dsAdslLineExtnClockType = _DsAdslLineExtnClockType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 6),
    _DsAdslLineExtnClockType_Type()
)
dsAdslLineExtnClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnClockType.setStatus("current")


class _DsAdslLineExtnLineDmtTrellis_Type(Integer32):
    """Custom type dsAdslLineExtnLineDmtTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trellisOn", 1),
          ("trellisOff", 2))
    )


_DsAdslLineExtnLineDmtTrellis_Type.__name__ = "Integer32"
_DsAdslLineExtnLineDmtTrellis_Object = MibTableColumn
dsAdslLineExtnLineDmtTrellis = _DsAdslLineExtnLineDmtTrellis_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 3, 1, 7),
    _DsAdslLineExtnLineDmtTrellis_Type()
)
dsAdslLineExtnLineDmtTrellis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineExtnLineDmtTrellis.setStatus("current")
_DsAdslAtucPhysExtnTable_Object = MibTable
dsAdslAtucPhysExtnTable = _DsAdslAtucPhysExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnTable.setStatus("current")
_DsAdslAtucPhysExtnEntry_Object = MibTableRow
dsAdslAtucPhysExtnEntry = _DsAdslAtucPhysExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1)
)
dsAdslAtucPhysExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnEntry.setStatus("current")


class _DsAdslAtucPhysExtnOpState_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8,
              16,
              24,
              26,
              27,
              46,
              128,
              131,
              132,
              133,
              139,
              140)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("data", 1),
          ("bootupLoad", 8),
          ("handshake", 16),
          ("training", 24),
          ("framerSync", 26),
          ("fastRetrainInProg", 27),
          ("discovery", 46),
          ("llTest", 128),
          ("dlTest", 131),
          ("txTest", 132),
          ("atmLpTest", 133),
          ("deltTraining", 139),
          ("delt", 140))
    )


_DsAdslAtucPhysExtnOpState_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnOpState_Object = MibTableColumn
dsAdslAtucPhysExtnOpState = _DsAdslAtucPhysExtnOpState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 1),
    _DsAdslAtucPhysExtnOpState_Type()
)
dsAdslAtucPhysExtnOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnOpState.setStatus("current")


class _DsAdslAtucPhysExtnActualStd_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnActualStd based on Integer32"""
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
              9,
              26,
              27,
              28,
              29,
              30,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("t1413", 0),
          ("gLite", 1),
          ("gDmt", 2),
          ("alctl14", 3),
          ("multimode", 4),
          ("adi", 5),
          ("alctl", 6),
          ("t1413auto", 9),
          ("adsl2", 26),
          ("adsl2Plus", 27),
          ("reAdsl2", 28),
          ("adsl2Auto", 29),
          ("adsl2PlusAuto", 30),
          ("adslPlus", 48),
          ("gspanPlus", 64))
    )


_DsAdslAtucPhysExtnActualStd_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnActualStd_Object = MibTableColumn
dsAdslAtucPhysExtnActualStd = _DsAdslAtucPhysExtnActualStd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 2),
    _DsAdslAtucPhysExtnActualStd_Type()
)
dsAdslAtucPhysExtnActualStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnActualStd.setStatus("current")
_DsAdslAtucPhysExtnBertError_Type = Integer32
_DsAdslAtucPhysExtnBertError_Object = MibTableColumn
dsAdslAtucPhysExtnBertError = _DsAdslAtucPhysExtnBertError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 3),
    _DsAdslAtucPhysExtnBertError_Type()
)
dsAdslAtucPhysExtnBertError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnBertError.setStatus("current")
_DsAdslAtucPhysExtnTxAtmCellCounter_Type = Counter32
_DsAdslAtucPhysExtnTxAtmCellCounter_Object = MibTableColumn
dsAdslAtucPhysExtnTxAtmCellCounter = _DsAdslAtucPhysExtnTxAtmCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 4),
    _DsAdslAtucPhysExtnTxAtmCellCounter_Type()
)
dsAdslAtucPhysExtnTxAtmCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnTxAtmCellCounter.setStatus("current")
_DsAdslAtucPhysExtnRxAtmCellCounter_Type = Integer32
_DsAdslAtucPhysExtnRxAtmCellCounter_Object = MibTableColumn
dsAdslAtucPhysExtnRxAtmCellCounter = _DsAdslAtucPhysExtnRxAtmCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 5),
    _DsAdslAtucPhysExtnRxAtmCellCounter_Type()
)
dsAdslAtucPhysExtnRxAtmCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnRxAtmCellCounter.setStatus("current")
_DsAdslAtucPhysExtnStartProgress_Type = Integer32
_DsAdslAtucPhysExtnStartProgress_Object = MibTableColumn
dsAdslAtucPhysExtnStartProgress = _DsAdslAtucPhysExtnStartProgress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 6),
    _DsAdslAtucPhysExtnStartProgress_Type()
)
dsAdslAtucPhysExtnStartProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnStartProgress.setStatus("current")
_DsAdslAtucPhysExtnIdleBertError_Type = Integer32
_DsAdslAtucPhysExtnIdleBertError_Object = MibTableColumn
dsAdslAtucPhysExtnIdleBertError = _DsAdslAtucPhysExtnIdleBertError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 7),
    _DsAdslAtucPhysExtnIdleBertError_Type()
)
dsAdslAtucPhysExtnIdleBertError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnIdleBertError.setStatus("current")
_DsAdslAtucPhysExtnIdleBertCells_Type = Integer32
_DsAdslAtucPhysExtnIdleBertCells_Object = MibTableColumn
dsAdslAtucPhysExtnIdleBertCells = _DsAdslAtucPhysExtnIdleBertCells_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 8),
    _DsAdslAtucPhysExtnIdleBertCells_Type()
)
dsAdslAtucPhysExtnIdleBertCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnIdleBertCells.setStatus("current")


class _DsAdslAtucPhysExtnBertSync_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnBertSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bertOutOfSync", 0),
          ("bertInSync", 128))
    )


_DsAdslAtucPhysExtnBertSync_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnBertSync_Object = MibTableColumn
dsAdslAtucPhysExtnBertSync = _DsAdslAtucPhysExtnBertSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 9),
    _DsAdslAtucPhysExtnBertSync_Type()
)
dsAdslAtucPhysExtnBertSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnBertSync.setStatus("current")


class _DsAdslAtucPhysExtnParametricTestResult_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnParametricTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fail", 1),
          ("dspIfFail", 2))
    )


_DsAdslAtucPhysExtnParametricTestResult_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnParametricTestResult_Object = MibTableColumn
dsAdslAtucPhysExtnParametricTestResult = _DsAdslAtucPhysExtnParametricTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 10),
    _DsAdslAtucPhysExtnParametricTestResult_Type()
)
dsAdslAtucPhysExtnParametricTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnParametricTestResult.setStatus("current")


class _DsAdslAtucPhysExtnDataBoostStatus_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnDataBoostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 32768))
    )


_DsAdslAtucPhysExtnDataBoostStatus_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnDataBoostStatus_Object = MibTableColumn
dsAdslAtucPhysExtnDataBoostStatus = _DsAdslAtucPhysExtnDataBoostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 21),
    _DsAdslAtucPhysExtnDataBoostStatus_Type()
)
dsAdslAtucPhysExtnDataBoostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDataBoostStatus.setStatus("current")


class _DsAdslAtucPhysExtnTestArray_Type(OctetString):
    """Custom type dsAdslAtucPhysExtnTestArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAtucPhysExtnTestArray_Type.__name__ = "OctetString"
_DsAdslAtucPhysExtnTestArray_Object = MibTableColumn
dsAdslAtucPhysExtnTestArray = _DsAdslAtucPhysExtnTestArray_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 22),
    _DsAdslAtucPhysExtnTestArray_Type()
)
dsAdslAtucPhysExtnTestArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnTestArray.setStatus("current")
_DsAdslAtucPhysExtnChanPerfCD_Type = Integer32
_DsAdslAtucPhysExtnChanPerfCD_Object = MibTableColumn
dsAdslAtucPhysExtnChanPerfCD = _DsAdslAtucPhysExtnChanPerfCD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 23),
    _DsAdslAtucPhysExtnChanPerfCD_Type()
)
dsAdslAtucPhysExtnChanPerfCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnChanPerfCD.setStatus("current")
_DsAdslAtucPhysExtnChanPerfBE_Type = Integer32
_DsAdslAtucPhysExtnChanPerfBE_Object = MibTableColumn
dsAdslAtucPhysExtnChanPerfBE = _DsAdslAtucPhysExtnChanPerfBE_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 24),
    _DsAdslAtucPhysExtnChanPerfBE_Type()
)
dsAdslAtucPhysExtnChanPerfBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnChanPerfBE.setStatus("current")
_DsAdslAtucPhysExtnDeltHLINSCus_Type = Integer32
_DsAdslAtucPhysExtnDeltHLINSCus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltHLINSCus = _DsAdslAtucPhysExtnDeltHLINSCus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 25),
    _DsAdslAtucPhysExtnDeltHLINSCus_Type()
)
dsAdslAtucPhysExtnDeltHLINSCus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltHLINSCus.setStatus("current")


class _DsAdslAtucPhysExtnDeltHLINpsus_Type(OctetString):
    """Custom type dsAdslAtucPhysExtnDeltHLINpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAtucPhysExtnDeltHLINpsus_Type.__name__ = "OctetString"
_DsAdslAtucPhysExtnDeltHLINpsus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltHLINpsus = _DsAdslAtucPhysExtnDeltHLINpsus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 26),
    _DsAdslAtucPhysExtnDeltHLINpsus_Type()
)
dsAdslAtucPhysExtnDeltHLINpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltHLINpsus.setStatus("current")
_DsAdslAtucPhysExtnDeltHLOGMTus_Type = Integer32
_DsAdslAtucPhysExtnDeltHLOGMTus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltHLOGMTus = _DsAdslAtucPhysExtnDeltHLOGMTus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 27),
    _DsAdslAtucPhysExtnDeltHLOGMTus_Type()
)
dsAdslAtucPhysExtnDeltHLOGMTus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltHLOGMTus.setStatus("current")


class _DsAdslAtucPhysExtnDeltHLOGpsus_Type(OctetString):
    """Custom type dsAdslAtucPhysExtnDeltHLOGpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAtucPhysExtnDeltHLOGpsus_Type.__name__ = "OctetString"
_DsAdslAtucPhysExtnDeltHLOGpsus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltHLOGpsus = _DsAdslAtucPhysExtnDeltHLOGpsus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 28),
    _DsAdslAtucPhysExtnDeltHLOGpsus_Type()
)
dsAdslAtucPhysExtnDeltHLOGpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltHLOGpsus.setStatus("current")
_DsAdslAtucPhysExtnDeltQLNMTus_Type = Integer32
_DsAdslAtucPhysExtnDeltQLNMTus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltQLNMTus = _DsAdslAtucPhysExtnDeltQLNMTus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 29),
    _DsAdslAtucPhysExtnDeltQLNMTus_Type()
)
dsAdslAtucPhysExtnDeltQLNMTus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltQLNMTus.setStatus("current")


class _DsAdslAtucPhysExtnDeltQLNpsus_Type(OctetString):
    """Custom type dsAdslAtucPhysExtnDeltQLNpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAtucPhysExtnDeltQLNpsus_Type.__name__ = "OctetString"
_DsAdslAtucPhysExtnDeltQLNpsus_Object = MibTableColumn
dsAdslAtucPhysExtnDeltQLNpsus = _DsAdslAtucPhysExtnDeltQLNpsus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 30),
    _DsAdslAtucPhysExtnDeltQLNpsus_Type()
)
dsAdslAtucPhysExtnDeltQLNpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltQLNpsus.setStatus("current")


class _DsAdslAtucPhysExtnDeltLastTxState_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnDeltLastTxState based on Integer32"""
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
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dmtatucg9941", 0),
          ("dmtatucquiet1", 1),
          ("dmtatuccomb1", 2),
          ("dmtatucquiet2", 3),
          ("dmtatuccomb2", 4),
          ("dmtatucicomb1", 5),
          ("dmtatuclineprob", 6),
          ("dmtatucquiet3", 7),
          ("dmtatuccomb3", 8),
          ("dmtatucicomb2", 9),
          ("dmtatucmsgfmt", 10),
          ("dmtatucmsgpcb", 11),
          ("dmtatucquiet4", 12),
          ("dmtatucreverb1", 13),
          ("dmtatuctref1", 14),
          ("dmtatucreverb2", 15),
          ("dmtatucect", 16),
          ("dmtatucreverb3", 17),
          ("dmtatuctref2", 18),
          ("dmtatucreverb4", 19),
          ("dmtatucsegue1", 20),
          ("dmtatucmsg1", 21),
          ("dmtatucreverb5", 22),
          ("dmtatucsegue2", 23),
          ("dmtatucmedley", 24),
          ("dmtatucexchmarker", 25),
          ("dmtatucmsg2", 26),
          ("dmtatucreverb6", 27),
          ("dmtatucsegue3", 28),
          ("dmtatucparams", 29),
          ("dmtatucreverb7", 30),
          ("dmtatucsegue4", 31),
          ("dmtatucshowtime", 32))
    )


_DsAdslAtucPhysExtnDeltLastTxState_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnDeltLastTxState_Object = MibTableColumn
dsAdslAtucPhysExtnDeltLastTxState = _DsAdslAtucPhysExtnDeltLastTxState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 31),
    _DsAdslAtucPhysExtnDeltLastTxState_Type()
)
dsAdslAtucPhysExtnDeltLastTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnDeltLastTxState.setStatus("current")


class _DsAdslAtucPhysExtnPMState_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnPMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              141)
        )
    )
    namedValues = NamedValues(
        *(("idleop", 0),
          ("dataop", 1),
          ("l2op", 141))
    )


_DsAdslAtucPhysExtnPMState_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnPMState_Object = MibTableColumn
dsAdslAtucPhysExtnPMState = _DsAdslAtucPhysExtnPMState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 32),
    _DsAdslAtucPhysExtnPMState_Type()
)
dsAdslAtucPhysExtnPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnPMState.setStatus("current")
_DsAdslAtucPhysExtnChanPerfCU_Type = Integer32
_DsAdslAtucPhysExtnChanPerfCU_Object = MibTableColumn
dsAdslAtucPhysExtnChanPerfCU = _DsAdslAtucPhysExtnChanPerfCU_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 33),
    _DsAdslAtucPhysExtnChanPerfCU_Type()
)
dsAdslAtucPhysExtnChanPerfCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnChanPerfCU.setStatus("current")


class _DsAdslAtucPhysExtnExtendedPsdStatus_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnExtendedPsdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("jj100", 1),
          ("extended", 32768))
    )


_DsAdslAtucPhysExtnExtendedPsdStatus_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnExtendedPsdStatus_Object = MibTableColumn
dsAdslAtucPhysExtnExtendedPsdStatus = _DsAdslAtucPhysExtnExtendedPsdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 34),
    _DsAdslAtucPhysExtnExtendedPsdStatus_Type()
)
dsAdslAtucPhysExtnExtendedPsdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnExtendedPsdStatus.setStatus("current")
_DsAdslAtucPhysExtnChipVersion_Type = Integer32
_DsAdslAtucPhysExtnChipVersion_Object = MibTableColumn
dsAdslAtucPhysExtnChipVersion = _DsAdslAtucPhysExtnChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 35),
    _DsAdslAtucPhysExtnChipVersion_Type()
)
dsAdslAtucPhysExtnChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnChipVersion.setStatus("current")
_DsAdslAtucPhysExtnPilotTone_Type = Integer32
_DsAdslAtucPhysExtnPilotTone_Object = MibTableColumn
dsAdslAtucPhysExtnPilotTone = _DsAdslAtucPhysExtnPilotTone_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 36),
    _DsAdslAtucPhysExtnPilotTone_Type()
)
dsAdslAtucPhysExtnPilotTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnPilotTone.setStatus("current")
_DsAdslAtucMSGds_Type = Gauge32
_DsAdslAtucMSGds_Object = MibTableColumn
dsAdslAtucMSGds = _DsAdslAtucMSGds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 37),
    _DsAdslAtucMSGds_Type()
)
dsAdslAtucMSGds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucMSGds.setStatus("current")


class _DsAdslAtucPhysExtnPsdMaskMode_Type(Integer32):
    """Custom type dsAdslAtucPhysExtnPsdMaskMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              32768,
              32771,
              32772,
              49152)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 0),
          ("hsadslM1", 3),
          ("hsadslM2", 4),
          ("msk2Rfi", 32768),
          ("flatMskRfi", 32771),
          ("cabMsk2Rfi", 32772),
          ("coMsk2Rfi0", 49152))
    )


_DsAdslAtucPhysExtnPsdMaskMode_Type.__name__ = "Integer32"
_DsAdslAtucPhysExtnPsdMaskMode_Object = MibTableColumn
dsAdslAtucPhysExtnPsdMaskMode = _DsAdslAtucPhysExtnPsdMaskMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 4, 1, 38),
    _DsAdslAtucPhysExtnPsdMaskMode_Type()
)
dsAdslAtucPhysExtnPsdMaskMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPhysExtnPsdMaskMode.setStatus("current")
_DsAdslAturPhysExtnTable_Object = MibTable
dsAdslAturPhysExtnTable = _DsAdslAturPhysExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnTable.setStatus("current")
_DsAdslAturPhysExtnEntry_Object = MibTableRow
dsAdslAturPhysExtnEntry = _DsAdslAturPhysExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1)
)
dsAdslAturPhysExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnEntry.setStatus("current")


class _DsAdslAturPhysExtnConfig_Type(OctetString):
    """Custom type dsAdslAturPhysExtnConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsAdslAturPhysExtnConfig_Type.__name__ = "OctetString"
_DsAdslAturPhysExtnConfig_Object = MibTableColumn
dsAdslAturPhysExtnConfig = _DsAdslAturPhysExtnConfig_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 1),
    _DsAdslAturPhysExtnConfig_Type()
)
dsAdslAturPhysExtnConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnConfig.setStatus("current")
_DsAdslAturPhysExtnChanPerfCD_Type = Integer32
_DsAdslAturPhysExtnChanPerfCD_Object = MibTableColumn
dsAdslAturPhysExtnChanPerfCD = _DsAdslAturPhysExtnChanPerfCD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 2),
    _DsAdslAturPhysExtnChanPerfCD_Type()
)
dsAdslAturPhysExtnChanPerfCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnChanPerfCD.setStatus("current")
_DsAdslAturPhysExtnChanPerfCU_Type = Integer32
_DsAdslAturPhysExtnChanPerfCU_Object = MibTableColumn
dsAdslAturPhysExtnChanPerfCU = _DsAdslAturPhysExtnChanPerfCU_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 3),
    _DsAdslAturPhysExtnChanPerfCU_Type()
)
dsAdslAturPhysExtnChanPerfCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnChanPerfCU.setStatus("current")
_DsAdslAturPhysExtnChanPerfBE_Type = Integer32
_DsAdslAturPhysExtnChanPerfBE_Object = MibTableColumn
dsAdslAturPhysExtnChanPerfBE = _DsAdslAturPhysExtnChanPerfBE_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 4),
    _DsAdslAturPhysExtnChanPerfBE_Type()
)
dsAdslAturPhysExtnChanPerfBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnChanPerfBE.setStatus("current")
_DsAdslAturPhysExtnDeltHLINSCds_Type = Integer32
_DsAdslAturPhysExtnDeltHLINSCds_Object = MibTableColumn
dsAdslAturPhysExtnDeltHLINSCds = _DsAdslAturPhysExtnDeltHLINSCds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 5),
    _DsAdslAturPhysExtnDeltHLINSCds_Type()
)
dsAdslAturPhysExtnDeltHLINSCds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltHLINSCds.setStatus("current")


class _DsAdslAturPhysExtnDeltHLINpsds_Type(OctetString):
    """Custom type dsAdslAturPhysExtnDeltHLINpsds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAturPhysExtnDeltHLINpsds_Type.__name__ = "OctetString"
_DsAdslAturPhysExtnDeltHLINpsds_Object = MibTableColumn
dsAdslAturPhysExtnDeltHLINpsds = _DsAdslAturPhysExtnDeltHLINpsds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 6),
    _DsAdslAturPhysExtnDeltHLINpsds_Type()
)
dsAdslAturPhysExtnDeltHLINpsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltHLINpsds.setStatus("current")
_DsAdslAturPhysExtnDeltHLOGMTds_Type = Integer32
_DsAdslAturPhysExtnDeltHLOGMTds_Object = MibTableColumn
dsAdslAturPhysExtnDeltHLOGMTds = _DsAdslAturPhysExtnDeltHLOGMTds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 7),
    _DsAdslAturPhysExtnDeltHLOGMTds_Type()
)
dsAdslAturPhysExtnDeltHLOGMTds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltHLOGMTds.setStatus("current")


class _DsAdslAturPhysExtnDeltHLOGpsus_Type(OctetString):
    """Custom type dsAdslAturPhysExtnDeltHLOGpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAturPhysExtnDeltHLOGpsus_Type.__name__ = "OctetString"
_DsAdslAturPhysExtnDeltHLOGpsus_Object = MibTableColumn
dsAdslAturPhysExtnDeltHLOGpsus = _DsAdslAturPhysExtnDeltHLOGpsus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 8),
    _DsAdslAturPhysExtnDeltHLOGpsus_Type()
)
dsAdslAturPhysExtnDeltHLOGpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltHLOGpsus.setStatus("current")
_DsAdslAturPhysExtnDeltQLNMTds_Type = Integer32
_DsAdslAturPhysExtnDeltQLNMTds_Object = MibTableColumn
dsAdslAturPhysExtnDeltQLNMTds = _DsAdslAturPhysExtnDeltQLNMTds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 9),
    _DsAdslAturPhysExtnDeltQLNMTds_Type()
)
dsAdslAturPhysExtnDeltQLNMTds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltQLNMTds.setStatus("current")


class _DsAdslAturPhysExtnDeltQLNpsds_Type(OctetString):
    """Custom type dsAdslAturPhysExtnDeltQLNpsds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_DsAdslAturPhysExtnDeltQLNpsds_Type.__name__ = "OctetString"
_DsAdslAturPhysExtnDeltQLNpsds_Object = MibTableColumn
dsAdslAturPhysExtnDeltQLNpsds = _DsAdslAturPhysExtnDeltQLNpsds_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 10),
    _DsAdslAturPhysExtnDeltQLNpsds_Type()
)
dsAdslAturPhysExtnDeltQLNpsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltQLNpsds.setStatus("current")


class _DsAdslAturPhysExtnDeltLastTxState_Type(Integer32):
    """Custom type dsAdslAturPhysExtnDeltLastTxState based on Integer32"""
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
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("dmtaturg9941", 0),
          ("dmtaturquiet1", 1),
          ("dmtaturcomb1", 2),
          ("dmtaturquiet2", 3),
          ("dmtaturcomb2", 4),
          ("dmtaturicomb1", 5),
          ("dmtaturlineprob", 6),
          ("dmtaturquiet3", 7),
          ("dmtaturcomb3", 8),
          ("dmtaturicomb2", 9),
          ("dmtaturmsgfmt", 10),
          ("dmtaturmsgpcb", 11),
          ("dmtaturreverb1", 12),
          ("dmtaturquiet4", 13),
          ("dmtaturreverb2", 14),
          ("dmtaturquiet5", 15),
          ("dmtaturreverb3", 16),
          ("dmtaturect", 17),
          ("dmtaturreverb4", 18),
          ("dmtatursegue1", 19),
          ("dmtaturreverb5", 20),
          ("dmtatursegue2", 21),
          ("dmtaturmsg1", 22),
          ("dmtaturmedley", 23),
          ("dmtaturexchmarker", 24),
          ("dmtaturmsg2", 25),
          ("dmtaturreverb6", 26),
          ("dmtatursegue3", 27),
          ("dmtaturparams", 28),
          ("dmtaturreverb7", 29),
          ("dmtatursegue4", 30),
          ("dmtaturshowtime", 31))
    )


_DsAdslAturPhysExtnDeltLastTxState_Type.__name__ = "Integer32"
_DsAdslAturPhysExtnDeltLastTxState_Object = MibTableColumn
dsAdslAturPhysExtnDeltLastTxState = _DsAdslAturPhysExtnDeltLastTxState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 11),
    _DsAdslAturPhysExtnDeltLastTxState_Type()
)
dsAdslAturPhysExtnDeltLastTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPhysExtnDeltLastTxState.setStatus("current")
_DsAdslAturMSGus_Type = Gauge32
_DsAdslAturMSGus_Object = MibTableColumn
dsAdslAturMSGus = _DsAdslAturMSGus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 5, 1, 12),
    _DsAdslAturMSGus_Type()
)
dsAdslAturMSGus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturMSGus.setStatus("current")
_DsAdslAtucChanExtnTable_Object = MibTable
dsAdslAtucChanExtnTable = _DsAdslAtucChanExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnTable.setStatus("current")
_DsAdslAtucChanExtnEntry_Object = MibTableRow
dsAdslAtucChanExtnEntry = _DsAdslAtucChanExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6, 1)
)
dsAdslAtucChanExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnEntry.setStatus("current")


class _DsAdslAtucChanExtnCurrAtmStatus_Type(Integer32):
    """Custom type dsAdslAtucChanExtnCurrAtmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAtmDefect", 0),
          ("noCellDelineation", 1),
          ("lossOfCellDelineation", 2))
    )


_DsAdslAtucChanExtnCurrAtmStatus_Type.__name__ = "Integer32"
_DsAdslAtucChanExtnCurrAtmStatus_Object = MibTableColumn
dsAdslAtucChanExtnCurrAtmStatus = _DsAdslAtucChanExtnCurrAtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6, 1, 1),
    _DsAdslAtucChanExtnCurrAtmStatus_Type()
)
dsAdslAtucChanExtnCurrAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnCurrAtmStatus.setStatus("current")
_DsAdslAtucChanExtnRsSymbols_Type = Integer32
_DsAdslAtucChanExtnRsSymbols_Object = MibTableColumn
dsAdslAtucChanExtnRsSymbols = _DsAdslAtucChanExtnRsSymbols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6, 1, 2),
    _DsAdslAtucChanExtnRsSymbols_Type()
)
dsAdslAtucChanExtnRsSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnRsSymbols.setStatus("current")
_DsAdslAtucChanExtnRsDepth_Type = Integer32
_DsAdslAtucChanExtnRsDepth_Object = MibTableColumn
dsAdslAtucChanExtnRsDepth = _DsAdslAtucChanExtnRsDepth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6, 1, 3),
    _DsAdslAtucChanExtnRsDepth_Type()
)
dsAdslAtucChanExtnRsDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnRsDepth.setStatus("current")
_DsAdslAtucChanExtnRsRedundancy_Type = Integer32
_DsAdslAtucChanExtnRsRedundancy_Object = MibTableColumn
dsAdslAtucChanExtnRsRedundancy = _DsAdslAtucChanExtnRsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 6, 1, 4),
    _DsAdslAtucChanExtnRsRedundancy_Type()
)
dsAdslAtucChanExtnRsRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanExtnRsRedundancy.setStatus("current")
_DsAdslAturChanExtnTable_Object = MibTable
dsAdslAturChanExtnTable = _DsAdslAturChanExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dsAdslAturChanExtnTable.setStatus("current")
_DsAdslAturChanExtnEntry_Object = MibTableRow
dsAdslAturChanExtnEntry = _DsAdslAturChanExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7, 1)
)
dsAdslAturChanExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAturChanExtnEntry.setStatus("current")


class _DsAdslAturChanExtnCurrAtmStatus_Type(Integer32):
    """Custom type dsAdslAturChanExtnCurrAtmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAtmDefect", 0),
          ("noCellDelineation", 1),
          ("lossOfCellDelineation", 2))
    )


_DsAdslAturChanExtnCurrAtmStatus_Type.__name__ = "Integer32"
_DsAdslAturChanExtnCurrAtmStatus_Object = MibTableColumn
dsAdslAturChanExtnCurrAtmStatus = _DsAdslAturChanExtnCurrAtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7, 1, 1),
    _DsAdslAturChanExtnCurrAtmStatus_Type()
)
dsAdslAturChanExtnCurrAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanExtnCurrAtmStatus.setStatus("current")
_DsAdslAturChanExtnRsSymbols_Type = Unsigned32
_DsAdslAturChanExtnRsSymbols_Object = MibTableColumn
dsAdslAturChanExtnRsSymbols = _DsAdslAturChanExtnRsSymbols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7, 1, 2),
    _DsAdslAturChanExtnRsSymbols_Type()
)
dsAdslAturChanExtnRsSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanExtnRsSymbols.setStatus("current")
_DsAdslAturChanExtnRsDepth_Type = Unsigned32
_DsAdslAturChanExtnRsDepth_Object = MibTableColumn
dsAdslAturChanExtnRsDepth = _DsAdslAturChanExtnRsDepth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7, 1, 3),
    _DsAdslAturChanExtnRsDepth_Type()
)
dsAdslAturChanExtnRsDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanExtnRsDepth.setStatus("current")
_DsAdslAturChanExtnRsRedundancy_Type = Unsigned32
_DsAdslAturChanExtnRsRedundancy_Object = MibTableColumn
dsAdslAturChanExtnRsRedundancy = _DsAdslAturChanExtnRsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 7, 1, 4),
    _DsAdslAturChanExtnRsRedundancy_Type()
)
dsAdslAturChanExtnRsRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanExtnRsRedundancy.setStatus("current")
_DsAdslAtucPerfDataExtnTable_Object = MibTable
dsAdslAtucPerfDataExtnTable = _DsAdslAtucPerfDataExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnTable.setStatus("current")
_DsAdslAtucPerfDataExtnEntry_Object = MibTableRow
dsAdslAtucPerfDataExtnEntry = _DsAdslAtucPerfDataExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1)
)
dsAdslAtucPerfDataExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnEntry.setStatus("current")
_DsAdslAtucPerfDataExtnStatFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnStatFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatFastR = _DsAdslAtucPerfDataExtnStatFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 1),
    _DsAdslAtucPerfDataExtnStatFastR_Type()
)
dsAdslAtucPerfDataExtnStatFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatFastR.setStatus("current")
_DsAdslAtucPerfDataExtnStatFailedFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnStatFailedFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatFailedFastR = _DsAdslAtucPerfDataExtnStatFailedFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 2),
    _DsAdslAtucPerfDataExtnStatFailedFastR_Type()
)
dsAdslAtucPerfDataExtnStatFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatFailedFastR.setStatus("current")
_DsAdslAtucPerfDataExtnStatSesL_Type = Gauge32
_DsAdslAtucPerfDataExtnStatSesL_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatSesL = _DsAdslAtucPerfDataExtnStatSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 3),
    _DsAdslAtucPerfDataExtnStatSesL_Type()
)
dsAdslAtucPerfDataExtnStatSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatSesL.setStatus("current")
_DsAdslAtucPerfDataExtnStatUasL_Type = Gauge32
_DsAdslAtucPerfDataExtnStatUasL_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatUasL = _DsAdslAtucPerfDataExtnStatUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 4),
    _DsAdslAtucPerfDataExtnStatUasL_Type()
)
dsAdslAtucPerfDataExtnStatUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatUasL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFastR = _DsAdslAtucPerfDataExtnCurr15MinFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 5),
    _DsAdslAtucPerfDataExtnCurr15MinFastR_Type()
)
dsAdslAtucPerfDataExtnCurr15MinFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinFastR.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFailedFastR = _DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 6),
    _DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Type()
)
dsAdslAtucPerfDataExtnCurr15MinFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinFailedFastR.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinSesL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinSesL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinSesL = _DsAdslAtucPerfDataExtnCurr15MinSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 7),
    _DsAdslAtucPerfDataExtnCurr15MinSesL_Type()
)
dsAdslAtucPerfDataExtnCurr15MinSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinSesL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinUasL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinUasL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinUasL = _DsAdslAtucPerfDataExtnCurr15MinUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 8),
    _DsAdslAtucPerfDataExtnCurr15MinUasL_Type()
)
dsAdslAtucPerfDataExtnCurr15MinUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinUasL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DayFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFastR = _DsAdslAtucPerfDataExtnCurr1DayFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 9),
    _DsAdslAtucPerfDataExtnCurr1DayFastR_Type()
)
dsAdslAtucPerfDataExtnCurr1DayFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DayFastR.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFailedFastR = _DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 10),
    _DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Type()
)
dsAdslAtucPerfDataExtnCurr1DayFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DayFailedFastR.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DaySesL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DaySesL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DaySesL = _DsAdslAtucPerfDataExtnCurr1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 11),
    _DsAdslAtucPerfDataExtnCurr1DaySesL_Type()
)
dsAdslAtucPerfDataExtnCurr1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DaySesL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DayUasL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DayUasL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayUasL = _DsAdslAtucPerfDataExtnCurr1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 12),
    _DsAdslAtucPerfDataExtnCurr1DayUasL_Type()
)
dsAdslAtucPerfDataExtnCurr1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DayUasL.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFastR = _DsAdslAtucPerfDataExtnPrev1DayFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 13),
    _DsAdslAtucPerfDataExtnPrev1DayFastR_Type()
)
dsAdslAtucPerfDataExtnPrev1DayFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayFastR.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFailedFastR = _DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 14),
    _DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Type()
)
dsAdslAtucPerfDataExtnPrev1DayFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayFailedFastR.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DaySesL_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DaySesL_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DaySesL = _DsAdslAtucPerfDataExtnPrev1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 15),
    _DsAdslAtucPerfDataExtnPrev1DaySesL_Type()
)
dsAdslAtucPerfDataExtnPrev1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DaySesL.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayUasL_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayUasL_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayUasL = _DsAdslAtucPerfDataExtnPrev1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 16),
    _DsAdslAtucPerfDataExtnPrev1DayUasL_Type()
)
dsAdslAtucPerfDataExtnPrev1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayUasL.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayTimeElapsed = _DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 17),
    _DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Type()
)
dsAdslAtucPerfDataExtnPrev1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayTimeElapsed.setStatus("current")
_DsAdslAtucPerfDataExtnStatFecsL_Type = Gauge32
_DsAdslAtucPerfDataExtnStatFecsL_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatFecsL = _DsAdslAtucPerfDataExtnStatFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 18),
    _DsAdslAtucPerfDataExtnStatFecsL_Type()
)
dsAdslAtucPerfDataExtnStatFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatFecsL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinFecsL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFecsL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFecsL = _DsAdslAtucPerfDataExtnCurr15MinFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 19),
    _DsAdslAtucPerfDataExtnCurr15MinFecsL_Type()
)
dsAdslAtucPerfDataExtnCurr15MinFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinFecsL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DayFecsL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFecsL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFecsL = _DsAdslAtucPerfDataExtnCurr1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 20),
    _DsAdslAtucPerfDataExtnCurr1DayFecsL_Type()
)
dsAdslAtucPerfDataExtnCurr1DayFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DayFecsL.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayFecsL_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFecsL_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFecsL = _DsAdslAtucPerfDataExtnPrev1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 21),
    _DsAdslAtucPerfDataExtnPrev1DayFecsL_Type()
)
dsAdslAtucPerfDataExtnPrev1DayFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayFecsL.setStatus("current")
_DsAdslAtucPerfDataExtnStatLossL_Type = Gauge32
_DsAdslAtucPerfDataExtnStatLossL_Object = MibTableColumn
dsAdslAtucPerfDataExtnStatLossL = _DsAdslAtucPerfDataExtnStatLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 22),
    _DsAdslAtucPerfDataExtnStatLossL_Type()
)
dsAdslAtucPerfDataExtnStatLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnStatLossL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr15MinLossL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr15MinLossL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinLossL = _DsAdslAtucPerfDataExtnCurr15MinLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 23),
    _DsAdslAtucPerfDataExtnCurr15MinLossL_Type()
)
dsAdslAtucPerfDataExtnCurr15MinLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr15MinLossL.setStatus("current")
_DsAdslAtucPerfDataExtnCurr1DayLossL_Type = Gauge32
_DsAdslAtucPerfDataExtnCurr1DayLossL_Object = MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayLossL = _DsAdslAtucPerfDataExtnCurr1DayLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 24),
    _DsAdslAtucPerfDataExtnCurr1DayLossL_Type()
)
dsAdslAtucPerfDataExtnCurr1DayLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnCurr1DayLossL.setStatus("current")
_DsAdslAtucPerfDataExtnPrev1DayLossL_Type = Gauge32
_DsAdslAtucPerfDataExtnPrev1DayLossL_Object = MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayLossL = _DsAdslAtucPerfDataExtnPrev1DayLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 8, 1, 25),
    _DsAdslAtucPerfDataExtnPrev1DayLossL_Type()
)
dsAdslAtucPerfDataExtnPrev1DayLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucPerfDataExtnPrev1DayLossL.setStatus("current")
_DsAdslAturPerfDataExtnTable_Object = MibTable
dsAdslAturPerfDataExtnTable = _DsAdslAturPerfDataExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnTable.setStatus("current")
_DsAdslAturPerfDataExtnEntry_Object = MibTableRow
dsAdslAturPerfDataExtnEntry = _DsAdslAturPerfDataExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1)
)
dsAdslAturPerfDataExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnEntry.setStatus("current")
_DsAdslAturPerfDataExtnStatSesL_Type = Counter32
_DsAdslAturPerfDataExtnStatSesL_Object = MibTableColumn
dsAdslAturPerfDataExtnStatSesL = _DsAdslAturPerfDataExtnStatSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 1),
    _DsAdslAturPerfDataExtnStatSesL_Type()
)
dsAdslAturPerfDataExtnStatSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnStatSesL.setStatus("current")
_DsAdslAturPerfDataExtnCurr15MinSesL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr15MinSesL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr15MinSesL = _DsAdslAturPerfDataExtnCurr15MinSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 2),
    _DsAdslAturPerfDataExtnCurr15MinSesL_Type()
)
dsAdslAturPerfDataExtnCurr15MinSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr15MinSesL.setStatus("current")
_DsAdslAturPerfDataExtnCurr1DaySesL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr1DaySesL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr1DaySesL = _DsAdslAturPerfDataExtnCurr1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 3),
    _DsAdslAturPerfDataExtnCurr1DaySesL_Type()
)
dsAdslAturPerfDataExtnCurr1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr1DaySesL.setStatus("current")
_DsAdslAturPerfDataExtnPrev1DaySesL_Type = Gauge32
_DsAdslAturPerfDataExtnPrev1DaySesL_Object = MibTableColumn
dsAdslAturPerfDataExtnPrev1DaySesL = _DsAdslAturPerfDataExtnPrev1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 4),
    _DsAdslAturPerfDataExtnPrev1DaySesL_Type()
)
dsAdslAturPerfDataExtnPrev1DaySesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnPrev1DaySesL.setStatus("current")
_DsAdslAturPerfDataExtnStatUasL_Type = Counter32
_DsAdslAturPerfDataExtnStatUasL_Object = MibTableColumn
dsAdslAturPerfDataExtnStatUasL = _DsAdslAturPerfDataExtnStatUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 5),
    _DsAdslAturPerfDataExtnStatUasL_Type()
)
dsAdslAturPerfDataExtnStatUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnStatUasL.setStatus("current")
_DsAdslAturPerfDataExtnCurr15MinUasL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr15MinUasL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr15MinUasL = _DsAdslAturPerfDataExtnCurr15MinUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 6),
    _DsAdslAturPerfDataExtnCurr15MinUasL_Type()
)
dsAdslAturPerfDataExtnCurr15MinUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr15MinUasL.setStatus("current")
_DsAdslAturPerfDataExtnCurr1DayUasL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr1DayUasL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr1DayUasL = _DsAdslAturPerfDataExtnCurr1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 7),
    _DsAdslAturPerfDataExtnCurr1DayUasL_Type()
)
dsAdslAturPerfDataExtnCurr1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr1DayUasL.setStatus("current")
_DsAdslAturPerfDataExtnPrev1DayUasL_Type = Gauge32
_DsAdslAturPerfDataExtnPrev1DayUasL_Object = MibTableColumn
dsAdslAturPerfDataExtnPrev1DayUasL = _DsAdslAturPerfDataExtnPrev1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 8),
    _DsAdslAturPerfDataExtnPrev1DayUasL_Type()
)
dsAdslAturPerfDataExtnPrev1DayUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnPrev1DayUasL.setStatus("current")
_DsAdslAturPerfDataExtnStatFecsL_Type = Counter32
_DsAdslAturPerfDataExtnStatFecsL_Object = MibTableColumn
dsAdslAturPerfDataExtnStatFecsL = _DsAdslAturPerfDataExtnStatFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 9),
    _DsAdslAturPerfDataExtnStatFecsL_Type()
)
dsAdslAturPerfDataExtnStatFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnStatFecsL.setStatus("current")
_DsAdslAturPerfDataExtnCurr15MinFecsL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr15MinFecsL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr15MinFecsL = _DsAdslAturPerfDataExtnCurr15MinFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 10),
    _DsAdslAturPerfDataExtnCurr15MinFecsL_Type()
)
dsAdslAturPerfDataExtnCurr15MinFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr15MinFecsL.setStatus("current")
_DsAdslAturPerfDataExtnCurr1DayFecsL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr1DayFecsL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr1DayFecsL = _DsAdslAturPerfDataExtnCurr1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 11),
    _DsAdslAturPerfDataExtnCurr1DayFecsL_Type()
)
dsAdslAturPerfDataExtnCurr1DayFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr1DayFecsL.setStatus("current")
_DsAdslAturPerfDataExtnPrev1DayFecsL_Type = Gauge32
_DsAdslAturPerfDataExtnPrev1DayFecsL_Object = MibTableColumn
dsAdslAturPerfDataExtnPrev1DayFecsL = _DsAdslAturPerfDataExtnPrev1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 12),
    _DsAdslAturPerfDataExtnPrev1DayFecsL_Type()
)
dsAdslAturPerfDataExtnPrev1DayFecsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnPrev1DayFecsL.setStatus("current")
_DsAdslAturPerfDataExtnStatLossL_Type = Counter32
_DsAdslAturPerfDataExtnStatLossL_Object = MibTableColumn
dsAdslAturPerfDataExtnStatLossL = _DsAdslAturPerfDataExtnStatLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 13),
    _DsAdslAturPerfDataExtnStatLossL_Type()
)
dsAdslAturPerfDataExtnStatLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnStatLossL.setStatus("current")
_DsAdslAturPerfDataExtnCurr15MinLossL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr15MinLossL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr15MinLossL = _DsAdslAturPerfDataExtnCurr15MinLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 14),
    _DsAdslAturPerfDataExtnCurr15MinLossL_Type()
)
dsAdslAturPerfDataExtnCurr15MinLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr15MinLossL.setStatus("current")
_DsAdslAturPerfDataExtnCurr1DayLossL_Type = Gauge32
_DsAdslAturPerfDataExtnCurr1DayLossL_Object = MibTableColumn
dsAdslAturPerfDataExtnCurr1DayLossL = _DsAdslAturPerfDataExtnCurr1DayLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 15),
    _DsAdslAturPerfDataExtnCurr1DayLossL_Type()
)
dsAdslAturPerfDataExtnCurr1DayLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnCurr1DayLossL.setStatus("current")
_DsAdslAturPerfDataExtnPrev1DayLossL_Type = Gauge32
_DsAdslAturPerfDataExtnPrev1DayLossL_Object = MibTableColumn
dsAdslAturPerfDataExtnPrev1DayLossL = _DsAdslAturPerfDataExtnPrev1DayLossL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 9, 1, 16),
    _DsAdslAturPerfDataExtnPrev1DayLossL_Type()
)
dsAdslAturPerfDataExtnPrev1DayLossL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturPerfDataExtnPrev1DayLossL.setStatus("current")
_DsAdslAtucIntervalExtnTable_Object = MibTable
dsAdslAtucIntervalExtnTable = _DsAdslAtucIntervalExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnTable.setStatus("current")
_DsAdslAtucIntervalExtnEntry_Object = MibTableRow
dsAdslAtucIntervalExtnEntry = _DsAdslAtucIntervalExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1)
)
dsAdslAtucIntervalExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAtucIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnEntry.setStatus("current")
_DsAdslAtucIntervalExtnFastR_Type = Gauge32
_DsAdslAtucIntervalExtnFastR_Object = MibTableColumn
dsAdslAtucIntervalExtnFastR = _DsAdslAtucIntervalExtnFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1, 1),
    _DsAdslAtucIntervalExtnFastR_Type()
)
dsAdslAtucIntervalExtnFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnFastR.setStatus("current")
_DsAdslAtucIntervalExtnFailedFastR_Type = Gauge32
_DsAdslAtucIntervalExtnFailedFastR_Object = MibTableColumn
dsAdslAtucIntervalExtnFailedFastR = _DsAdslAtucIntervalExtnFailedFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1, 2),
    _DsAdslAtucIntervalExtnFailedFastR_Type()
)
dsAdslAtucIntervalExtnFailedFastR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnFailedFastR.setStatus("current")
_DsAdslAtucIntervalExtnSesL_Type = Gauge32
_DsAdslAtucIntervalExtnSesL_Object = MibTableColumn
dsAdslAtucIntervalExtnSesL = _DsAdslAtucIntervalExtnSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1, 3),
    _DsAdslAtucIntervalExtnSesL_Type()
)
dsAdslAtucIntervalExtnSesL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnSesL.setStatus("current")
_DsAdslAtucIntervalExtnUasL_Type = Gauge32
_DsAdslAtucIntervalExtnUasL_Object = MibTableColumn
dsAdslAtucIntervalExtnUasL = _DsAdslAtucIntervalExtnUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1, 4),
    _DsAdslAtucIntervalExtnUasL_Type()
)
dsAdslAtucIntervalExtnUasL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnUasL.setStatus("current")
_DsAdslAtucIntervalExtnTimeElapsed_Type = Gauge32
_DsAdslAtucIntervalExtnTimeElapsed_Object = MibTableColumn
dsAdslAtucIntervalExtnTimeElapsed = _DsAdslAtucIntervalExtnTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 10, 1, 5),
    _DsAdslAtucIntervalExtnTimeElapsed_Type()
)
dsAdslAtucIntervalExtnTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucIntervalExtnTimeElapsed.setStatus("current")
_DsAdslAtucChanPerfDataExtnTable_Object = MibTable
dsAdslAtucChanPerfDataExtnTable = _DsAdslAtucChanPerfDataExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnTable.setStatus("current")
_DsAdslAtucChanPerfDataExtnEntry_Object = MibTableRow
dsAdslAtucChanPerfDataExtnEntry = _DsAdslAtucChanPerfDataExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1)
)
dsAdslAtucChanPerfDataExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnEntry.setStatus("current")
_DsAdslAtucChanPerfDataExtnTimeElapsed_Type = Gauge32
_DsAdslAtucChanPerfDataExtnTimeElapsed_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnTimeElapsed = _DsAdslAtucChanPerfDataExtnTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 1),
    _DsAdslAtucChanPerfDataExtnTimeElapsed_Type()
)
dsAdslAtucChanPerfDataExtnTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnTimeElapsed.setStatus("current")
_DsAdslAtucChanPerfDataExtnNcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnNcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnNcd = _DsAdslAtucChanPerfDataExtnNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 2),
    _DsAdslAtucChanPerfDataExtnNcd_Type()
)
dsAdslAtucChanPerfDataExtnNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnNcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnOcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnOcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnOcd = _DsAdslAtucChanPerfDataExtnOcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 3),
    _DsAdslAtucChanPerfDataExtnOcd_Type()
)
dsAdslAtucChanPerfDataExtnOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnOcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnHec_Type = Gauge32
_DsAdslAtucChanPerfDataExtnHec_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnHec = _DsAdslAtucChanPerfDataExtnHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 4),
    _DsAdslAtucChanPerfDataExtnHec_Type()
)
dsAdslAtucChanPerfDataExtnHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnHec.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinNcd = _DsAdslAtucChanPerfDataExtnCurr15MinNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 5),
    _DsAdslAtucChanPerfDataExtnCurr15MinNcd_Type()
)
dsAdslAtucChanPerfDataExtnCurr15MinNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr15MinNcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinOcd = _DsAdslAtucChanPerfDataExtnCurr15MinOcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 6),
    _DsAdslAtucChanPerfDataExtnCurr15MinOcd_Type()
)
dsAdslAtucChanPerfDataExtnCurr15MinOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr15MinOcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr15MinHec_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinHec_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinHec = _DsAdslAtucChanPerfDataExtnCurr15MinHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 7),
    _DsAdslAtucChanPerfDataExtnCurr15MinHec_Type()
)
dsAdslAtucChanPerfDataExtnCurr15MinHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr15MinHec.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayNcd = _DsAdslAtucChanPerfDataExtnCurr1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 8),
    _DsAdslAtucChanPerfDataExtnCurr1DayNcd_Type()
)
dsAdslAtucChanPerfDataExtnCurr1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr1DayNcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayOcd = _DsAdslAtucChanPerfDataExtnCurr1DayOcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 9),
    _DsAdslAtucChanPerfDataExtnCurr1DayOcd_Type()
)
dsAdslAtucChanPerfDataExtnCurr1DayOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr1DayOcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnCurr1DayHec_Type = Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayHec_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayHec = _DsAdslAtucChanPerfDataExtnCurr1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 10),
    _DsAdslAtucChanPerfDataExtnCurr1DayHec_Type()
)
dsAdslAtucChanPerfDataExtnCurr1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnCurr1DayHec.setStatus("current")
_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayNcd = _DsAdslAtucChanPerfDataExtnPrev1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 11),
    _DsAdslAtucChanPerfDataExtnPrev1DayNcd_Type()
)
dsAdslAtucChanPerfDataExtnPrev1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnPrev1DayNcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Type = Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayOcd = _DsAdslAtucChanPerfDataExtnPrev1DayOcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 12),
    _DsAdslAtucChanPerfDataExtnPrev1DayOcd_Type()
)
dsAdslAtucChanPerfDataExtnPrev1DayOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnPrev1DayOcd.setStatus("current")
_DsAdslAtucChanPerfDataExtnPrev1DayHec_Type = Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayHec_Object = MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayHec = _DsAdslAtucChanPerfDataExtnPrev1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 12, 1, 13),
    _DsAdslAtucChanPerfDataExtnPrev1DayHec_Type()
)
dsAdslAtucChanPerfDataExtnPrev1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanPerfDataExtnPrev1DayHec.setStatus("current")
_DsAdslAturChanPerfDataExtnTable_Object = MibTable
dsAdslAturChanPerfDataExtnTable = _DsAdslAturChanPerfDataExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnTable.setStatus("current")
_DsAdslAturChanPerfDataExtnEntry_Object = MibTableRow
dsAdslAturChanPerfDataExtnEntry = _DsAdslAturChanPerfDataExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1)
)
dsAdslAturChanPerfDataExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnEntry.setStatus("current")
_DsAdslAturChanPerfDataExtnNcd_Type = Gauge32
_DsAdslAturChanPerfDataExtnNcd_Object = MibTableColumn
dsAdslAturChanPerfDataExtnNcd = _DsAdslAturChanPerfDataExtnNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 1),
    _DsAdslAturChanPerfDataExtnNcd_Type()
)
dsAdslAturChanPerfDataExtnNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnNcd.setStatus("current")
_DsAdslAturChanPerfDataExtnHec_Type = Gauge32
_DsAdslAturChanPerfDataExtnHec_Object = MibTableColumn
dsAdslAturChanPerfDataExtnHec = _DsAdslAturChanPerfDataExtnHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 2),
    _DsAdslAturChanPerfDataExtnHec_Type()
)
dsAdslAturChanPerfDataExtnHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnHec.setStatus("current")
_DsAdslAturChanPerfDataExtnCurr15MinNcd_Type = Gauge32
_DsAdslAturChanPerfDataExtnCurr15MinNcd_Object = MibTableColumn
dsAdslAturChanPerfDataExtnCurr15MinNcd = _DsAdslAturChanPerfDataExtnCurr15MinNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 3),
    _DsAdslAturChanPerfDataExtnCurr15MinNcd_Type()
)
dsAdslAturChanPerfDataExtnCurr15MinNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnCurr15MinNcd.setStatus("current")
_DsAdslAturChanPerfDataExtnCurr15MinHec_Type = Gauge32
_DsAdslAturChanPerfDataExtnCurr15MinHec_Object = MibTableColumn
dsAdslAturChanPerfDataExtnCurr15MinHec = _DsAdslAturChanPerfDataExtnCurr15MinHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 4),
    _DsAdslAturChanPerfDataExtnCurr15MinHec_Type()
)
dsAdslAturChanPerfDataExtnCurr15MinHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnCurr15MinHec.setStatus("current")
_DsAdslAturChanPerfDataExtnCurr1DayNcd_Type = Gauge32
_DsAdslAturChanPerfDataExtnCurr1DayNcd_Object = MibTableColumn
dsAdslAturChanPerfDataExtnCurr1DayNcd = _DsAdslAturChanPerfDataExtnCurr1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 5),
    _DsAdslAturChanPerfDataExtnCurr1DayNcd_Type()
)
dsAdslAturChanPerfDataExtnCurr1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnCurr1DayNcd.setStatus("current")
_DsAdslAturChanPerfDataExtnCurr1DayHec_Type = Gauge32
_DsAdslAturChanPerfDataExtnCurr1DayHec_Object = MibTableColumn
dsAdslAturChanPerfDataExtnCurr1DayHec = _DsAdslAturChanPerfDataExtnCurr1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 6),
    _DsAdslAturChanPerfDataExtnCurr1DayHec_Type()
)
dsAdslAturChanPerfDataExtnCurr1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnCurr1DayHec.setStatus("current")
_DsAdslAturChanPerfDataExtnPrev1DayNcd_Type = Gauge32
_DsAdslAturChanPerfDataExtnPrev1DayNcd_Object = MibTableColumn
dsAdslAturChanPerfDataExtnPrev1DayNcd = _DsAdslAturChanPerfDataExtnPrev1DayNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 7),
    _DsAdslAturChanPerfDataExtnPrev1DayNcd_Type()
)
dsAdslAturChanPerfDataExtnPrev1DayNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnPrev1DayNcd.setStatus("current")
_DsAdslAturChanPerfDataExtnPrev1DayHec_Type = Gauge32
_DsAdslAturChanPerfDataExtnPrev1DayHec_Object = MibTableColumn
dsAdslAturChanPerfDataExtnPrev1DayHec = _DsAdslAturChanPerfDataExtnPrev1DayHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 13, 1, 8),
    _DsAdslAturChanPerfDataExtnPrev1DayHec_Type()
)
dsAdslAturChanPerfDataExtnPrev1DayHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanPerfDataExtnPrev1DayHec.setStatus("current")
_DsAdslAtucChanIntervalExtnTable_Object = MibTable
dsAdslAtucChanIntervalExtnTable = _DsAdslAtucChanIntervalExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnTable.setStatus("current")
_DsAdslAtucChanIntervalExtnEntry_Object = MibTableRow
dsAdslAtucChanIntervalExtnEntry = _DsAdslAtucChanIntervalExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14, 1)
)
dsAdslAtucChanIntervalExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAtucChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnEntry.setStatus("current")
_DsAdslAtucChanIntervalExtnTimeElapsed_Type = Counter32
_DsAdslAtucChanIntervalExtnTimeElapsed_Object = MibTableColumn
dsAdslAtucChanIntervalExtnTimeElapsed = _DsAdslAtucChanIntervalExtnTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14, 1, 1),
    _DsAdslAtucChanIntervalExtnTimeElapsed_Type()
)
dsAdslAtucChanIntervalExtnTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnTimeElapsed.setStatus("current")
_DsAdslAtucChanIntervalExtnNcd_Type = Counter32
_DsAdslAtucChanIntervalExtnNcd_Object = MibTableColumn
dsAdslAtucChanIntervalExtnNcd = _DsAdslAtucChanIntervalExtnNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14, 1, 2),
    _DsAdslAtucChanIntervalExtnNcd_Type()
)
dsAdslAtucChanIntervalExtnNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnNcd.setStatus("current")
_DsAdslAtucChanIntervalExtnOcd_Type = Counter32
_DsAdslAtucChanIntervalExtnOcd_Object = MibTableColumn
dsAdslAtucChanIntervalExtnOcd = _DsAdslAtucChanIntervalExtnOcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14, 1, 3),
    _DsAdslAtucChanIntervalExtnOcd_Type()
)
dsAdslAtucChanIntervalExtnOcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnOcd.setStatus("current")
_DsAdslAtucChanIntervalExtnHec_Type = Counter32
_DsAdslAtucChanIntervalExtnHec_Object = MibTableColumn
dsAdslAtucChanIntervalExtnHec = _DsAdslAtucChanIntervalExtnHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 14, 1, 4),
    _DsAdslAtucChanIntervalExtnHec_Type()
)
dsAdslAtucChanIntervalExtnHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAtucChanIntervalExtnHec.setStatus("current")
_DsAdslAturChanIntervalExtnTable_Object = MibTable
dsAdslAturChanIntervalExtnTable = _DsAdslAturChanIntervalExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    dsAdslAturChanIntervalExtnTable.setStatus("current")
_DsAdslAturChanIntervalExtnEntry_Object = MibTableRow
dsAdslAturChanIntervalExtnEntry = _DsAdslAturChanIntervalExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 15, 1)
)
dsAdslAturChanIntervalExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAturChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsAdslAturChanIntervalExtnEntry.setStatus("current")
_DsAdslAturChanIntervalExtnNcd_Type = Gauge32
_DsAdslAturChanIntervalExtnNcd_Object = MibTableColumn
dsAdslAturChanIntervalExtnNcd = _DsAdslAturChanIntervalExtnNcd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 15, 1, 1),
    _DsAdslAturChanIntervalExtnNcd_Type()
)
dsAdslAturChanIntervalExtnNcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanIntervalExtnNcd.setStatus("current")
_DsAdslAturChanIntervalExtnHec_Type = Gauge32
_DsAdslAturChanIntervalExtnHec_Object = MibTableColumn
dsAdslAturChanIntervalExtnHec = _DsAdslAturChanIntervalExtnHec_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 15, 1, 2),
    _DsAdslAturChanIntervalExtnHec_Type()
)
dsAdslAturChanIntervalExtnHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslAturChanIntervalExtnHec.setStatus("current")
_DsAdslLineConfProfileExtnTable_Object = MibTable
dsAdslLineConfProfileExtnTable = _DsAdslLineConfProfileExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16)
)
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnTable.setStatus("current")
_DsAdslLineConfProfileExtnEntry_Object = MibTableRow
dsAdslLineConfProfileExtnEntry = _DsAdslLineConfProfileExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1)
)
dsAdslLineConfProfileExtnEntry.setIndexNames(
    (0, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnEntry.setStatus("current")


class _DsAdslLineConfProfileName_Type(OctetString):
    """Custom type dsAdslLineConfProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsAdslLineConfProfileName_Type.__name__ = "OctetString"
_DsAdslLineConfProfileName_Object = MibTableColumn
dsAdslLineConfProfileName = _DsAdslLineConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 1),
    _DsAdslLineConfProfileName_Type()
)
dsAdslLineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileName.setStatus("current")


class _DsAdslLineConfProfileExtnRsIntCorrectionUp_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRsIntCorrectionUp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable125us", 3),
          ("dsAdslLineConfProfileExtnTable250us", 4),
          ("dsAdslLineConfProfileExtnTable500us", 5),
          ("dsAdslLineConfProfileExtnTable1ms", 6),
          ("dsAdslLineConfProfileExtnTable2ms", 7),
          ("dsAdslLineConfProfileExtnTable4ms", 8),
          ("disable", 15))
    )


_DsAdslLineConfProfileExtnRsIntCorrectionUp_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRsIntCorrectionUp_Object = MibTableColumn
dsAdslLineConfProfileExtnRsIntCorrectionUp = _DsAdslLineConfProfileExtnRsIntCorrectionUp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 3),
    _DsAdslLineConfProfileExtnRsIntCorrectionUp_Type()
)
dsAdslLineConfProfileExtnRsIntCorrectionUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRsIntCorrectionUp.setStatus("current")


class _DsAdslLineConfProfileExtnLineType_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnLineType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3),
          ("fastOrInterleaved", 4),
          ("fastAndInterleaved", 5))
    )


_DsAdslLineConfProfileExtnLineType_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnLineType_Object = MibTableColumn
dsAdslLineConfProfileExtnLineType = _DsAdslLineConfProfileExtnLineType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 4),
    _DsAdslLineConfProfileExtnLineType_Type()
)
dsAdslLineConfProfileExtnLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnLineType.setStatus("current")


class _DsAdslLineConfProfileExtnTxEndBin_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnTxEndBin based on Integer32"""
    defaultValue = 511

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 511),
    )


_DsAdslLineConfProfileExtnTxEndBin_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnTxEndBin_Object = MibTableColumn
dsAdslLineConfProfileExtnTxEndBin = _DsAdslLineConfProfileExtnTxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 5),
    _DsAdslLineConfProfileExtnTxEndBin_Type()
)
dsAdslLineConfProfileExtnTxEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnTxEndBin.setStatus("current")


class _DsAdslLineConfProfileExtnTxStartBin_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnTxStartBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 511),
    )


_DsAdslLineConfProfileExtnTxStartBin_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnTxStartBin_Object = MibTableColumn
dsAdslLineConfProfileExtnTxStartBin = _DsAdslLineConfProfileExtnTxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 6),
    _DsAdslLineConfProfileExtnTxStartBin_Type()
)
dsAdslLineConfProfileExtnTxStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnTxStartBin.setStatus("current")


class _DsAdslLineConfProfileExtnRxStartBin_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRxStartBin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_DsAdslLineConfProfileExtnRxStartBin_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRxStartBin_Object = MibTableColumn
dsAdslLineConfProfileExtnRxStartBin = _DsAdslLineConfProfileExtnRxStartBin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 8),
    _DsAdslLineConfProfileExtnRxStartBin_Type()
)
dsAdslLineConfProfileExtnRxStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRxStartBin.setStatus("current")


class _DsAdslLineConfProfileExtnRxEndBin_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRxEndBin based on Integer32"""
    defaultValue = 511

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 511),
    )


_DsAdslLineConfProfileExtnRxEndBin_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRxEndBin_Object = MibTableColumn
dsAdslLineConfProfileExtnRxEndBin = _DsAdslLineConfProfileExtnRxEndBin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 9),
    _DsAdslLineConfProfileExtnRxEndBin_Type()
)
dsAdslLineConfProfileExtnRxEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRxEndBin.setStatus("current")


class _DsAdslLineConfProfileExtnRxBinAdjust_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRxBinAdjust based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("disable", 0)
    )


_DsAdslLineConfProfileExtnRxBinAdjust_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRxBinAdjust_Object = MibTableColumn
dsAdslLineConfProfileExtnRxBinAdjust = _DsAdslLineConfProfileExtnRxBinAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 10),
    _DsAdslLineConfProfileExtnRxBinAdjust_Type()
)
dsAdslLineConfProfileExtnRxBinAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRxBinAdjust.setStatus("current")


class _DsAdslLineConfProfileExtnStandard_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnStandard based on Integer32"""
    defaultValue = 27

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
              9,
              26,
              27,
              28,
              29,
              30,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("t1413", 0),
          ("gLite", 1),
          ("gDmt", 2),
          ("alctl14", 3),
          ("multimode", 4),
          ("adi", 5),
          ("alctl", 6),
          ("t1413Auto", 9),
          ("adsl2", 26),
          ("adsl2Plus", 27),
          ("readsl2", 28),
          ("adsl2Auto", 29),
          ("adsl2PlusAuto", 30),
          ("adslPlus", 48),
          ("gspanPlus", 49))
    )


_DsAdslLineConfProfileExtnStandard_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnStandard_Object = MibTableColumn
dsAdslLineConfProfileExtnStandard = _DsAdslLineConfProfileExtnStandard_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 13),
    _DsAdslLineConfProfileExtnStandard_Type()
)
dsAdslLineConfProfileExtnStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnStandard.setStatus("current")


class _DsAdslLineConfProfileExtnTxPowerAttenuation_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnTxPowerAttenuation based on Integer32"""
    defaultValue = 0

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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              32781,
              32782,
              32783,
              32784,
              32785,
              32786,
              32787,
              32788,
              32789,
              32790,
              32791,
              32792,
              32793,
              32794,
              32795,
              32796,
              32797,
              32798,
              32799,
              32800,
              32801,
              32802,
              32803,
              32804,
              32805,
              32806,
              32807,
              32808)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable0", 0),
          ("dsAdslLineConfProfileExtnTable1", 1),
          ("dsAdslLineConfProfileExtnTable2", 2),
          ("dsAdslLineConfProfileExtnTable3", 3),
          ("dsAdslLineConfProfileExtnTable4", 4),
          ("dsAdslLineConfProfileExtnTable5", 5),
          ("dsAdslLineConfProfileExtnTable6", 6),
          ("dsAdslLineConfProfileExtnTable7", 7),
          ("dsAdslLineConfProfileExtnTable8", 8),
          ("dsAdslLineConfProfileExtnTable9", 9),
          ("dsAdslLineConfProfileExtnTable10", 10),
          ("dsAdslLineConfProfileExtnTable11", 11),
          ("dsAdslLineConfProfileExtnTable12", 12),
          ("point1", 13),
          ("point2", 14),
          ("point3", 15),
          ("point4", 16),
          ("point5", 17),
          ("point6", 18),
          ("point7", 19),
          ("point8", 20),
          ("point9", 21),
          ("dsAdslLineConfProfileExtnTable13", 32781),
          ("dsAdslLineConfProfileExtnTable14", 32782),
          ("dsAdslLineConfProfileExtnTable15", 32783),
          ("dsAdslLineConfProfileExtnTable16", 32784),
          ("dsAdslLineConfProfileExtnTable17", 32785),
          ("dsAdslLineConfProfileExtnTable18", 32786),
          ("dsAdslLineConfProfileExtnTable19", 32787),
          ("dsAdslLineConfProfileExtnTable20", 32788),
          ("dsAdslLineConfProfileExtnTable21", 32789),
          ("dsAdslLineConfProfileExtnTable22", 32790),
          ("dsAdslLineConfProfileExtnTable23", 32791),
          ("dsAdslLineConfProfileExtnTable24", 32792),
          ("dsAdslLineConfProfileExtnTable25", 32793),
          ("dsAdslLineConfProfileExtnTable26", 32794),
          ("dsAdslLineConfProfileExtnTable27", 32795),
          ("dsAdslLineConfProfileExtnTable28", 32796),
          ("dsAdslLineConfProfileExtnTable29", 32797),
          ("dsAdslLineConfProfileExtnTable30", 32798),
          ("dsAdslLineConfProfileExtnTable31", 32799),
          ("dsAdslLineConfProfileExtnTable32", 32800),
          ("dsAdslLineConfProfileExtnTable33", 32801),
          ("dsAdslLineConfProfileExtnTable34", 32802),
          ("dsAdslLineConfProfileExtnTable35", 32803),
          ("dsAdslLineConfProfileExtnTable36", 32804),
          ("dsAdslLineConfProfileExtnTable37", 32805),
          ("dsAdslLineConfProfileExtnTable38", 32806),
          ("dsAdslLineConfProfileExtnTable39", 32807),
          ("dsAdslLineConfProfileExtnTable40", 32808))
    )


_DsAdslLineConfProfileExtnTxPowerAttenuation_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnTxPowerAttenuation_Object = MibTableColumn
dsAdslLineConfProfileExtnTxPowerAttenuation = _DsAdslLineConfProfileExtnTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 15),
    _DsAdslLineConfProfileExtnTxPowerAttenuation_Type()
)
dsAdslLineConfProfileExtnTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnTxPowerAttenuation.setStatus("current")


class _DsAdslLineConfProfileExtnRsFastOvrhdDown_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRsFastOvrhdDown based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable50", 1),
          ("dsAdslLineConfProfileExtnTable25", 2),
          ("dsAdslLineConfProfileExtnTable12", 3),
          ("dsAdslLineConfProfileExtnTable6", 4),
          ("dsAdslLineConfProfileExtnTable3", 5),
          ("dsAdslLineConfProfileExtnTable1", 7),
          ("disable", 15))
    )


_DsAdslLineConfProfileExtnRsFastOvrhdDown_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRsFastOvrhdDown_Object = MibTableColumn
dsAdslLineConfProfileExtnRsFastOvrhdDown = _DsAdslLineConfProfileExtnRsFastOvrhdDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 17),
    _DsAdslLineConfProfileExtnRsFastOvrhdDown_Type()
)
dsAdslLineConfProfileExtnRsFastOvrhdDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRsFastOvrhdDown.setStatus("current")


class _DsAdslLineConfProfileExtnIntCorrectionDown_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnIntCorrectionDown based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable125Us", 3),
          ("dsAdslLineConfProfileExtnTable250Us", 4),
          ("dsAdslLineConfProfileExtnTable500Us", 5),
          ("dsAdslLineConfProfileExtnTable1Ms", 6),
          ("dsAdslLineConfProfileExtnTable2Ms", 7),
          ("dsAdslLineConfProfileExtnTable4Ms", 8),
          ("disable", 15))
    )


_DsAdslLineConfProfileExtnIntCorrectionDown_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnIntCorrectionDown_Object = MibTableColumn
dsAdslLineConfProfileExtnIntCorrectionDown = _DsAdslLineConfProfileExtnIntCorrectionDown_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 18),
    _DsAdslLineConfProfileExtnIntCorrectionDown_Type()
)
dsAdslLineConfProfileExtnIntCorrectionDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnIntCorrectionDown.setStatus("current")


class _DsAdslLineConfProfileExtnRsFastOvrhdUp_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnRsFastOvrhdUp based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable50", 1),
          ("dsAdslLineConfProfileExtnTable25", 2),
          ("dsAdslLineConfProfileExtnTable12", 3),
          ("dsAdslLineConfProfileExtnTable6", 4),
          ("dsAdslLineConfProfileExtnTable3", 5),
          ("dsAdslLineConfProfileExtnTable1", 7),
          ("disable", 15))
    )


_DsAdslLineConfProfileExtnRsFastOvrhdUp_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnRsFastOvrhdUp_Object = MibTableColumn
dsAdslLineConfProfileExtnRsFastOvrhdUp = _DsAdslLineConfProfileExtnRsFastOvrhdUp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 19),
    _DsAdslLineConfProfileExtnRsFastOvrhdUp_Type()
)
dsAdslLineConfProfileExtnRsFastOvrhdUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnRsFastOvrhdUp.setStatus("current")


class _DsAdslLineConfProfileExtnAnnexType_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnAnnexType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 0),
          ("annexB", 1),
          ("highSpeed", 2),
          ("annexADSL2", 5))
    )


_DsAdslLineConfProfileExtnAnnexType_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnAnnexType_Object = MibTableColumn
dsAdslLineConfProfileExtnAnnexType = _DsAdslLineConfProfileExtnAnnexType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 26),
    _DsAdslLineConfProfileExtnAnnexType_Type()
)
dsAdslLineConfProfileExtnAnnexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnAnnexType.setStatus("current")


class _DsAdslLineConfProfileExtnMaxDCo_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnMaxDCo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192)
        )
    )
    namedValues = NamedValues(
        *(("dsAdslLineConfProfileExtnTable64", 0),
          ("dsAdslLineConfProfileExtnTable128", 4096),
          ("dsAdslLineConfProfileExtnTable256", 8192))
    )


_DsAdslLineConfProfileExtnMaxDCo_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnMaxDCo_Object = MibTableColumn
dsAdslLineConfProfileExtnMaxDCo = _DsAdslLineConfProfileExtnMaxDCo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 30),
    _DsAdslLineConfProfileExtnMaxDCo_Type()
)
dsAdslLineConfProfileExtnMaxDCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnMaxDCo.setStatus("current")


class _DsAdslLineConfProfileExtnAdvertisedCapabilities_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnAdvertisedCapabilities based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("annexa", 1),
          ("annexb", 2),
          ("adslplus", 16))
    )


_DsAdslLineConfProfileExtnAdvertisedCapabilities_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnAdvertisedCapabilities_Object = MibTableColumn
dsAdslLineConfProfileExtnAdvertisedCapabilities = _DsAdslLineConfProfileExtnAdvertisedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 32),
    _DsAdslLineConfProfileExtnAdvertisedCapabilities_Type()
)
dsAdslLineConfProfileExtnAdvertisedCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnAdvertisedCapabilities.setStatus("current")


class _DsAdslLineConfProfileExtnPsdMaskType_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPsdMaskType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              259,
              275,
              291,
              32768,
              32771,
              32772,
              49152)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 0),
          ("hsadslM1", 3),
          ("hsadslM2", 4),
          ("adls2NonovlpFlat", 259),
          ("adsl2NonovlpM1", 275),
          ("adls2NonovlpM2", 291),
          ("msk2Rfi", 32768),
          ("flatMskRfi", 32771),
          ("cabMsk2Rfi", 32772),
          ("coMsk2Rfio", 49152))
    )


_DsAdslLineConfProfileExtnPsdMaskType_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPsdMaskType_Object = MibTableColumn
dsAdslLineConfProfileExtnPsdMaskType = _DsAdslLineConfProfileExtnPsdMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 33),
    _DsAdslLineConfProfileExtnPsdMaskType_Type()
)
dsAdslLineConfProfileExtnPsdMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPsdMaskType.setStatus("current")


class _DsAdslLineConfProfileExtnLineDmtConfMode_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnLineDmtConfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecMode", 1),
          ("fdmMode", 2))
    )


_DsAdslLineConfProfileExtnLineDmtConfMode_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnLineDmtConfMode_Object = MibTableColumn
dsAdslLineConfProfileExtnLineDmtConfMode = _DsAdslLineConfProfileExtnLineDmtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 34),
    _DsAdslLineConfProfileExtnLineDmtConfMode_Type()
)
dsAdslLineConfProfileExtnLineDmtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnLineDmtConfMode.setStatus("current")


class _DsAdslLineConfProfileExtnUpstreamPSD_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnUpstreamPSD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("jj100", 1),
          ("extended", 32768))
    )


_DsAdslLineConfProfileExtnUpstreamPSD_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnUpstreamPSD_Object = MibTableColumn
dsAdslLineConfProfileExtnUpstreamPSD = _DsAdslLineConfProfileExtnUpstreamPSD_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 41),
    _DsAdslLineConfProfileExtnUpstreamPSD_Type()
)
dsAdslLineConfProfileExtnUpstreamPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnUpstreamPSD.setStatus("current")


class _DsAdslLineConfProfileExtnPMMode_Type(Bits):
    """Custom type dsAdslLineConfProfileExtnPMMode based on Bits"""
    namedValues = NamedValues(
        *(("pmstatel3enable", 0),
          ("pmstatel2enable", 1))
    )

_DsAdslLineConfProfileExtnPMMode_Type.__name__ = "Bits"
_DsAdslLineConfProfileExtnPMMode_Object = MibTableColumn
dsAdslLineConfProfileExtnPMMode = _DsAdslLineConfProfileExtnPMMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 42),
    _DsAdslLineConfProfileExtnPMMode_Type()
)
dsAdslLineConfProfileExtnPMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPMMode.setStatus("current")


class _DsAdslLineConfProfileExtnPML0Time_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML0Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsAdslLineConfProfileExtnPML0Time_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML0Time_Object = MibTableColumn
dsAdslLineConfProfileExtnPML0Time = _DsAdslLineConfProfileExtnPML0Time_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 43),
    _DsAdslLineConfProfileExtnPML0Time_Type()
)
dsAdslLineConfProfileExtnPML0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML0Time.setStatus("current")


class _DsAdslLineConfProfileExtnPML2Time_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsAdslLineConfProfileExtnPML2Time_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2Time_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2Time = _DsAdslLineConfProfileExtnPML2Time_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 44),
    _DsAdslLineConfProfileExtnPML2Time_Type()
)
dsAdslLineConfProfileExtnPML2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2Time.setStatus("current")


class _DsAdslLineConfProfileExtnPML2ATPR_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2ATPR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DsAdslLineConfProfileExtnPML2ATPR_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2ATPR_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2ATPR = _DsAdslLineConfProfileExtnPML2ATPR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 45),
    _DsAdslLineConfProfileExtnPML2ATPR_Type()
)
dsAdslLineConfProfileExtnPML2ATPR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2ATPR.setStatus("current")


class _DsAdslLineConfProfileExtnPML2Rate_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256000, 1024000),
    )


_DsAdslLineConfProfileExtnPML2Rate_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2Rate_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2Rate = _DsAdslLineConfProfileExtnPML2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 46),
    _DsAdslLineConfProfileExtnPML2Rate_Type()
)
dsAdslLineConfProfileExtnPML2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2Rate.setStatus("current")


class _DsAdslLineConfProfileExtnAtucConfMinINP_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnAtucConfMinINP based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_DsAdslLineConfProfileExtnAtucConfMinINP_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnAtucConfMinINP_Object = MibTableColumn
dsAdslLineConfProfileExtnAtucConfMinINP = _DsAdslLineConfProfileExtnAtucConfMinINP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 63),
    _DsAdslLineConfProfileExtnAtucConfMinINP_Type()
)
dsAdslLineConfProfileExtnAtucConfMinINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnAtucConfMinINP.setStatus("current")


class _DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2EntryThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256000, 1024000),
    )


_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2EntryThresholdRate = _DsAdslLineConfProfileExtnPML2EntryThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 64),
    _DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type()
)
dsAdslLineConfProfileExtnPML2EntryThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2EntryThresholdRate.setStatus("current")


class _DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2ExitThresholdRate based on Integer32"""
    defaultValue = 512000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256000, 1024000),
    )


_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2ExitThresholdRate = _DsAdslLineConfProfileExtnPML2ExitThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 65),
    _DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type()
)
dsAdslLineConfProfileExtnPML2ExitThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2ExitThresholdRate.setStatus("current")


class _DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type(Integer32):
    """Custom type dsAdslLineConfProfileExtnPML2EntryRateMinTime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 65535),
    )


_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type.__name__ = "Integer32"
_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Object = MibTableColumn
dsAdslLineConfProfileExtnPML2EntryRateMinTime = _DsAdslLineConfProfileExtnPML2EntryRateMinTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 16, 1, 66),
    _DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type()
)
dsAdslLineConfProfileExtnPML2EntryRateMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineConfProfileExtnPML2EntryRateMinTime.setStatus("current")
_DsAdslLineAlarmConfProfileExtnTable_Object = MibTable
dsAdslLineAlarmConfProfileExtnTable = _DsAdslLineAlarmConfProfileExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17)
)
if mibBuilder.loadTexts:
    dsAdslLineAlarmConfProfileExtnTable.setStatus("current")
_DsAdslLineAlarmConfProfileExtnEntry_Object = MibTableRow
dsAdslLineAlarmConfProfileExtnEntry = _DsAdslLineAlarmConfProfileExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1)
)
dsAdslLineAlarmConfProfileExtnEntry.setIndexNames(
    (0, "ADSL-LINE-MIB", "adslLineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    dsAdslLineAlarmConfProfileExtnEntry.setStatus("current")


class _DsAdslLineAlarmConfProfileName_Type(OctetString):
    """Custom type dsAdslLineAlarmConfProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsAdslLineAlarmConfProfileName_Type.__name__ = "OctetString"
_DsAdslLineAlarmConfProfileName_Object = MibTableColumn
dsAdslLineAlarmConfProfileName = _DsAdslLineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 1),
    _DsAdslLineAlarmConfProfileName_Type()
)
dsAdslLineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsAdslLineAlarmConfProfileName.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh15MinFailFastR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinFailFastR = _DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 2),
    _DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type()
)
dsAdslLineAlarmExtnAtucThresh15MinFailFastR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh15MinFailFastR.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh15MinSesL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh15MinSesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAtucThresh15MinSesL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh15MinSesL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinSesL = _DsAdslLineAlarmExtnAtucThresh15MinSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 3),
    _DsAdslLineAlarmExtnAtucThresh15MinSesL_Type()
)
dsAdslLineAlarmExtnAtucThresh15MinSesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh15MinSesL.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh15MinUasL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh15MinUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAtucThresh15MinUasL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh15MinUasL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinUasL = _DsAdslLineAlarmExtnAtucThresh15MinUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 4),
    _DsAdslLineAlarmExtnAtucThresh15MinUasL_Type()
)
dsAdslLineAlarmExtnAtucThresh15MinUasL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh15MinUasL.setStatus("current")


class _DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucOpStateTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Object = MibTableColumn
dsAdslLineAlarmExtnAtucOpStateTrapEnable = _DsAdslLineAlarmExtnAtucOpStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 5),
    _DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type()
)
dsAdslLineAlarmExtnAtucOpStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucOpStateTrapEnable.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh15MinFecsL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinFecsL = _DsAdslLineAlarmExtnAtucThresh15MinFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 6),
    _DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type()
)
dsAdslLineAlarmExtnAtucThresh15MinFecsL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh15MinFecsL.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayLofs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayLofs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayLofs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayLofs_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLofs = _DsAdslLineAlarmExtnAtucThresh1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 7),
    _DsAdslLineAlarmExtnAtucThresh1DayLofs_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayLofs.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayLoss_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayLoss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayLoss_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayLoss_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLoss = _DsAdslLineAlarmExtnAtucThresh1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 8),
    _DsAdslLineAlarmExtnAtucThresh1DayLoss_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayLoss.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayLols_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayLols based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayLols_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayLols_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLols = _DsAdslLineAlarmExtnAtucThresh1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 9),
    _DsAdslLineAlarmExtnAtucThresh1DayLols_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayLols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayLols.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayLprs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayLprs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayLprs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayLprs_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLprs = _DsAdslLineAlarmExtnAtucThresh1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 10),
    _DsAdslLineAlarmExtnAtucThresh1DayLprs_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayLprs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayLprs.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayESs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayESs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayESs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayESs_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayESs = _DsAdslLineAlarmExtnAtucThresh1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 11),
    _DsAdslLineAlarmExtnAtucThresh1DayESs_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayESs.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DaySesL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DaySesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DaySesL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DaySesL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DaySesL = _DsAdslLineAlarmExtnAtucThresh1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 12),
    _DsAdslLineAlarmExtnAtucThresh1DaySesL_Type()
)
dsAdslLineAlarmExtnAtucThresh1DaySesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DaySesL.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayUasL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayUasL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayUasL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayUasL = _DsAdslLineAlarmExtnAtucThresh1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 13),
    _DsAdslLineAlarmExtnAtucThresh1DayUasL_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayUasL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayUasL.setStatus("current")


class _DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucThresh1DayFecsL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Object = MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayFecsL = _DsAdslLineAlarmExtnAtucThresh1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 14),
    _DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type()
)
dsAdslLineAlarmExtnAtucThresh1DayFecsL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucThresh1DayFecsL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh15MinFecsL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh15MinFecsL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAturThresh15MinFecsL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh15MinFecsL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinFecsL = _DsAdslLineAlarmExtnAturThresh15MinFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 15),
    _DsAdslLineAlarmExtnAturThresh15MinFecsL_Type()
)
dsAdslLineAlarmExtnAturThresh15MinFecsL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh15MinFecsL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayLofs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayLofs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayLofs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayLofs_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLofs = _DsAdslLineAlarmExtnAturThresh1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 16),
    _DsAdslLineAlarmExtnAturThresh1DayLofs_Type()
)
dsAdslLineAlarmExtnAturThresh1DayLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayLofs.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayLoss_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayLoss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayLoss_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayLoss_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLoss = _DsAdslLineAlarmExtnAturThresh1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 17),
    _DsAdslLineAlarmExtnAturThresh1DayLoss_Type()
)
dsAdslLineAlarmExtnAturThresh1DayLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayLoss.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayLprs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayLprs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayLprs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayLprs_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLprs = _DsAdslLineAlarmExtnAturThresh1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 18),
    _DsAdslLineAlarmExtnAturThresh1DayLprs_Type()
)
dsAdslLineAlarmExtnAturThresh1DayLprs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayLprs.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayESs_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayESs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayESs_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayESs_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayESs = _DsAdslLineAlarmExtnAturThresh1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 19),
    _DsAdslLineAlarmExtnAturThresh1DayESs_Type()
)
dsAdslLineAlarmExtnAturThresh1DayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayESs.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DaySesL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DaySesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DaySesL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DaySesL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DaySesL = _DsAdslLineAlarmExtnAturThresh1DaySesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 20),
    _DsAdslLineAlarmExtnAturThresh1DaySesL_Type()
)
dsAdslLineAlarmExtnAturThresh1DaySesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DaySesL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayUasL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayUasL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayUasL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayUasL = _DsAdslLineAlarmExtnAturThresh1DayUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 21),
    _DsAdslLineAlarmExtnAturThresh1DayUasL_Type()
)
dsAdslLineAlarmExtnAturThresh1DayUasL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayUasL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh1DayFecsL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh1DayFecsL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DsAdslLineAlarmExtnAturThresh1DayFecsL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh1DayFecsL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayFecsL = _DsAdslLineAlarmExtnAturThresh1DayFecsL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 22),
    _DsAdslLineAlarmExtnAturThresh1DayFecsL_Type()
)
dsAdslLineAlarmExtnAturThresh1DayFecsL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh1DayFecsL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh15MinSesL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh15MinSesL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAturThresh15MinSesL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh15MinSesL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinSesL = _DsAdslLineAlarmExtnAturThresh15MinSesL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 23),
    _DsAdslLineAlarmExtnAturThresh15MinSesL_Type()
)
dsAdslLineAlarmExtnAturThresh15MinSesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh15MinSesL.setStatus("current")


class _DsAdslLineAlarmExtnAturThresh15MinUasL_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAturThresh15MinUasL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAdslLineAlarmExtnAturThresh15MinUasL_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAturThresh15MinUasL_Object = MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinUasL = _DsAdslLineAlarmExtnAturThresh15MinUasL_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 24),
    _DsAdslLineAlarmExtnAturThresh15MinUasL_Type()
)
dsAdslLineAlarmExtnAturThresh15MinUasL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAturThresh15MinUasL.setStatus("current")


class _DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type(Integer32):
    """Custom type dsAdslLineAlarmExtnAtucPmStateTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type.__name__ = "Integer32"
_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Object = MibTableColumn
dsAdslLineAlarmExtnAtucPmStateTrapEnable = _DsAdslLineAlarmExtnAtucPmStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 1, 17, 1, 25),
    _DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type()
)
dsAdslLineAlarmExtnAtucPmStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAdslLineAlarmExtnAtucPmStateTrapEnable.setStatus("current")
_DsAdslTrap_ObjectIdentity = ObjectIdentity
dsAdslTrap = _DsAdslTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2)
)
_DsAdslAtucTraps_ObjectIdentity = ObjectIdentity
dsAdslAtucTraps = _DsAdslAtucTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1)
)
_DsAdslAturTraps_ObjectIdentity = ObjectIdentity
dsAdslAturTraps = _DsAdslAturTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2)
)

# Managed Objects groups


# Notification objects

dsAdslAtucOpStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 1)
)
dsAdslAtucOpStateChangeTrap.setObjects(
    ("DASAN-ADSL-MIB", "dsAdslAtucPhysExtnOpState")
)
if mibBuilder.loadTexts:
    dsAdslAtucOpStateChangeTrap.setStatus(
        "current"
    )

dsAdslAtucPmStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 2)
)
dsAdslAtucPmStateChangeTrap.setObjects(
    ("DASAN-ADSL-MIB", "dsAdslAtucPhysExtnPMState")
)
if mibBuilder.loadTexts:
    dsAdslAtucPmStateChangeTrap.setStatus(
        "current"
    )

dsAdslAtucPerfFailedFastRThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 3)
)
dsAdslAtucPerfFailedFastRThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr15MinFailedFastR"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh15MinFailFastR"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfFailedFastRThreshTrap.setStatus(
        "current"
    )

dsAdslAtucPerfSesLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 4)
)
dsAdslAtucPerfSesLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr15MinSesL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh15MinSesL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfSesLThreshTrap.setStatus(
        "current"
    )

dsAdslAtucPerfUasLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 5)
)
dsAdslAtucPerfUasLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr15MinUasL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh15MinUasL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfUasLThreshTrap.setStatus(
        "current"
    )

dsAdslAtucPerfFecsLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 6)
)
dsAdslAtucPerfFecsLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr15MinFecsL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh15MinFecsL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfFecsLThreshTrap.setStatus(
        "current"
    )

dsAdslAtucPerfLofsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 7)
)
dsAdslAtucPerfLofsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAtucPerfCurr1DayLofs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayLofs"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfLofsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfLossThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 8)
)
dsAdslAtucPerfLossThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAtucPerfCurr1DayLoss"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayLoss"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfLossThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfLolsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 9)
)
dsAdslAtucPerfLolsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAtucPerfCurr1DayLols"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayLols"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfLolsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfLprsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 10)
)
dsAdslAtucPerfLprsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAtucPerfCurr1DayLprs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayLprs"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfLprsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfESsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 11)
)
dsAdslAtucPerfESsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAtucPerfCurr1DayESs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayESs"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfESsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfSesLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 12)
)
dsAdslAtucPerfSesLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr1DaySesL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DaySesL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfSesLThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfUasLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 13)
)
dsAdslAtucPerfUasLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr1DayUasL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayUasL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfUasLThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAtucPerfFecsLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 1, 14)
)
dsAdslAtucPerfFecsLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAtucPerfDataExtnCurr1DayFecsL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAtucThresh1DayFecsL"))
)
if mibBuilder.loadTexts:
    dsAdslAtucPerfFecsLThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturSesLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 1)
)
dsAdslAturSesLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr15MinSesL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh15MinSesL"))
)
if mibBuilder.loadTexts:
    dsAdslAturSesLThreshTrap.setStatus(
        "current"
    )

dsAdslAturUasLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 2)
)
dsAdslAturUasLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr15MinUasL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh15MinUasL"))
)
if mibBuilder.loadTexts:
    dsAdslAturUasLThreshTrap.setStatus(
        "current"
    )

dsAdslAturPerfFecsLThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 3)
)
dsAdslAturPerfFecsLThreshTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr15MinFecsL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh15MinFecsL"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfFecsLThreshTrap.setStatus(
        "current"
    )

dsAdslAturPerfLofsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 4)
)
dsAdslAturPerfLofsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAturPerfCurr1DayLofs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayLofs"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfLofsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfLossThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 5)
)
dsAdslAturPerfLossThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAturPerfCurr1DayLoss"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayLoss"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfLossThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfLprsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 6)
)
dsAdslAturPerfLprsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAturPerfCurr1DayLprs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayLprs"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfLprsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfESsThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 7)
)
dsAdslAturPerfESsThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "adslAturPerfCurr1DayESs"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayESs"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfESsThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfSesLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 8)
)
dsAdslAturPerfSesLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr1DaySesL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DaySesL"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfSesLThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfUasLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 9)
)
dsAdslAturPerfUasLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr1DayUasL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayUasL"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfUasLThresh1DayTrap.setStatus(
        "current"
    )

dsAdslAturPerfFecsLThresh1DayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 9, 5, 1, 2, 2, 10)
)
dsAdslAturPerfFecsLThresh1DayTrap.setObjects(
      *(("DASAN-ADSL-MIB", "dsAdslAturPerfDataExtnCurr1DayFecsL"),
        ("DASAN-ADSL-MIB", "dsAdslLineAlarmExtnAturThresh1DayFecsL"))
)
if mibBuilder.loadTexts:
    dsAdslAturPerfFecsLThresh1DayTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ADSL-MIB",
    **{"dasanAdslMIB": dasanAdslMIB,
       "dasanAdslLineMIB": dasanAdslLineMIB,
       "dasanAdslMIBObjects": dasanAdslMIBObjects,
       "dsDslSystemParamGroup": dsDslSystemParamGroup,
       "dsDslSystemDslType": dsDslSystemDslType,
       "dsDslSystemLineCodingType": dsDslSystemLineCodingType,
       "dsDslSystemLineTxCfg": dsDslSystemLineTxCfg,
       "dsAdslCapabilityGroup": dsAdslCapabilityGroup,
       "dsAdslCapabilityLineTxCap": dsAdslCapabilityLineTxCap,
       "dsAdslLineExtnTable": dsAdslLineExtnTable,
       "dsAdslLineExtnEntry": dsAdslLineExtnEntry,
       "dsAdslLineExtnAction": dsAdslLineExtnAction,
       "dsAdslLineExtnUtopiaL2RxAddr": dsAdslLineExtnUtopiaL2RxAddr,
       "dsAdslLineExtnUtopiaL2TxAddr": dsAdslLineExtnUtopiaL2TxAddr,
       "dsAdslLineExtnTransAtucCap": dsAdslLineExtnTransAtucCap,
       "dsAdslLineExtnTransAtucActual": dsAdslLineExtnTransAtucActual,
       "dsAdslLineExtnClockType": dsAdslLineExtnClockType,
       "dsAdslLineExtnLineDmtTrellis": dsAdslLineExtnLineDmtTrellis,
       "dsAdslAtucPhysExtnTable": dsAdslAtucPhysExtnTable,
       "dsAdslAtucPhysExtnEntry": dsAdslAtucPhysExtnEntry,
       "dsAdslAtucPhysExtnOpState": dsAdslAtucPhysExtnOpState,
       "dsAdslAtucPhysExtnActualStd": dsAdslAtucPhysExtnActualStd,
       "dsAdslAtucPhysExtnBertError": dsAdslAtucPhysExtnBertError,
       "dsAdslAtucPhysExtnTxAtmCellCounter": dsAdslAtucPhysExtnTxAtmCellCounter,
       "dsAdslAtucPhysExtnRxAtmCellCounter": dsAdslAtucPhysExtnRxAtmCellCounter,
       "dsAdslAtucPhysExtnStartProgress": dsAdslAtucPhysExtnStartProgress,
       "dsAdslAtucPhysExtnIdleBertError": dsAdslAtucPhysExtnIdleBertError,
       "dsAdslAtucPhysExtnIdleBertCells": dsAdslAtucPhysExtnIdleBertCells,
       "dsAdslAtucPhysExtnBertSync": dsAdslAtucPhysExtnBertSync,
       "dsAdslAtucPhysExtnParametricTestResult": dsAdslAtucPhysExtnParametricTestResult,
       "dsAdslAtucPhysExtnDataBoostStatus": dsAdslAtucPhysExtnDataBoostStatus,
       "dsAdslAtucPhysExtnTestArray": dsAdslAtucPhysExtnTestArray,
       "dsAdslAtucPhysExtnChanPerfCD": dsAdslAtucPhysExtnChanPerfCD,
       "dsAdslAtucPhysExtnChanPerfBE": dsAdslAtucPhysExtnChanPerfBE,
       "dsAdslAtucPhysExtnDeltHLINSCus": dsAdslAtucPhysExtnDeltHLINSCus,
       "dsAdslAtucPhysExtnDeltHLINpsus": dsAdslAtucPhysExtnDeltHLINpsus,
       "dsAdslAtucPhysExtnDeltHLOGMTus": dsAdslAtucPhysExtnDeltHLOGMTus,
       "dsAdslAtucPhysExtnDeltHLOGpsus": dsAdslAtucPhysExtnDeltHLOGpsus,
       "dsAdslAtucPhysExtnDeltQLNMTus": dsAdslAtucPhysExtnDeltQLNMTus,
       "dsAdslAtucPhysExtnDeltQLNpsus": dsAdslAtucPhysExtnDeltQLNpsus,
       "dsAdslAtucPhysExtnDeltLastTxState": dsAdslAtucPhysExtnDeltLastTxState,
       "dsAdslAtucPhysExtnPMState": dsAdslAtucPhysExtnPMState,
       "dsAdslAtucPhysExtnChanPerfCU": dsAdslAtucPhysExtnChanPerfCU,
       "dsAdslAtucPhysExtnExtendedPsdStatus": dsAdslAtucPhysExtnExtendedPsdStatus,
       "dsAdslAtucPhysExtnChipVersion": dsAdslAtucPhysExtnChipVersion,
       "dsAdslAtucPhysExtnPilotTone": dsAdslAtucPhysExtnPilotTone,
       "dsAdslAtucMSGds": dsAdslAtucMSGds,
       "dsAdslAtucPhysExtnPsdMaskMode": dsAdslAtucPhysExtnPsdMaskMode,
       "dsAdslAturPhysExtnTable": dsAdslAturPhysExtnTable,
       "dsAdslAturPhysExtnEntry": dsAdslAturPhysExtnEntry,
       "dsAdslAturPhysExtnConfig": dsAdslAturPhysExtnConfig,
       "dsAdslAturPhysExtnChanPerfCD": dsAdslAturPhysExtnChanPerfCD,
       "dsAdslAturPhysExtnChanPerfCU": dsAdslAturPhysExtnChanPerfCU,
       "dsAdslAturPhysExtnChanPerfBE": dsAdslAturPhysExtnChanPerfBE,
       "dsAdslAturPhysExtnDeltHLINSCds": dsAdslAturPhysExtnDeltHLINSCds,
       "dsAdslAturPhysExtnDeltHLINpsds": dsAdslAturPhysExtnDeltHLINpsds,
       "dsAdslAturPhysExtnDeltHLOGMTds": dsAdslAturPhysExtnDeltHLOGMTds,
       "dsAdslAturPhysExtnDeltHLOGpsus": dsAdslAturPhysExtnDeltHLOGpsus,
       "dsAdslAturPhysExtnDeltQLNMTds": dsAdslAturPhysExtnDeltQLNMTds,
       "dsAdslAturPhysExtnDeltQLNpsds": dsAdslAturPhysExtnDeltQLNpsds,
       "dsAdslAturPhysExtnDeltLastTxState": dsAdslAturPhysExtnDeltLastTxState,
       "dsAdslAturMSGus": dsAdslAturMSGus,
       "dsAdslAtucChanExtnTable": dsAdslAtucChanExtnTable,
       "dsAdslAtucChanExtnEntry": dsAdslAtucChanExtnEntry,
       "dsAdslAtucChanExtnCurrAtmStatus": dsAdslAtucChanExtnCurrAtmStatus,
       "dsAdslAtucChanExtnRsSymbols": dsAdslAtucChanExtnRsSymbols,
       "dsAdslAtucChanExtnRsDepth": dsAdslAtucChanExtnRsDepth,
       "dsAdslAtucChanExtnRsRedundancy": dsAdslAtucChanExtnRsRedundancy,
       "dsAdslAturChanExtnTable": dsAdslAturChanExtnTable,
       "dsAdslAturChanExtnEntry": dsAdslAturChanExtnEntry,
       "dsAdslAturChanExtnCurrAtmStatus": dsAdslAturChanExtnCurrAtmStatus,
       "dsAdslAturChanExtnRsSymbols": dsAdslAturChanExtnRsSymbols,
       "dsAdslAturChanExtnRsDepth": dsAdslAturChanExtnRsDepth,
       "dsAdslAturChanExtnRsRedundancy": dsAdslAturChanExtnRsRedundancy,
       "dsAdslAtucPerfDataExtnTable": dsAdslAtucPerfDataExtnTable,
       "dsAdslAtucPerfDataExtnEntry": dsAdslAtucPerfDataExtnEntry,
       "dsAdslAtucPerfDataExtnStatFastR": dsAdslAtucPerfDataExtnStatFastR,
       "dsAdslAtucPerfDataExtnStatFailedFastR": dsAdslAtucPerfDataExtnStatFailedFastR,
       "dsAdslAtucPerfDataExtnStatSesL": dsAdslAtucPerfDataExtnStatSesL,
       "dsAdslAtucPerfDataExtnStatUasL": dsAdslAtucPerfDataExtnStatUasL,
       "dsAdslAtucPerfDataExtnCurr15MinFastR": dsAdslAtucPerfDataExtnCurr15MinFastR,
       "dsAdslAtucPerfDataExtnCurr15MinFailedFastR": dsAdslAtucPerfDataExtnCurr15MinFailedFastR,
       "dsAdslAtucPerfDataExtnCurr15MinSesL": dsAdslAtucPerfDataExtnCurr15MinSesL,
       "dsAdslAtucPerfDataExtnCurr15MinUasL": dsAdslAtucPerfDataExtnCurr15MinUasL,
       "dsAdslAtucPerfDataExtnCurr1DayFastR": dsAdslAtucPerfDataExtnCurr1DayFastR,
       "dsAdslAtucPerfDataExtnCurr1DayFailedFastR": dsAdslAtucPerfDataExtnCurr1DayFailedFastR,
       "dsAdslAtucPerfDataExtnCurr1DaySesL": dsAdslAtucPerfDataExtnCurr1DaySesL,
       "dsAdslAtucPerfDataExtnCurr1DayUasL": dsAdslAtucPerfDataExtnCurr1DayUasL,
       "dsAdslAtucPerfDataExtnPrev1DayFastR": dsAdslAtucPerfDataExtnPrev1DayFastR,
       "dsAdslAtucPerfDataExtnPrev1DayFailedFastR": dsAdslAtucPerfDataExtnPrev1DayFailedFastR,
       "dsAdslAtucPerfDataExtnPrev1DaySesL": dsAdslAtucPerfDataExtnPrev1DaySesL,
       "dsAdslAtucPerfDataExtnPrev1DayUasL": dsAdslAtucPerfDataExtnPrev1DayUasL,
       "dsAdslAtucPerfDataExtnPrev1DayTimeElapsed": dsAdslAtucPerfDataExtnPrev1DayTimeElapsed,
       "dsAdslAtucPerfDataExtnStatFecsL": dsAdslAtucPerfDataExtnStatFecsL,
       "dsAdslAtucPerfDataExtnCurr15MinFecsL": dsAdslAtucPerfDataExtnCurr15MinFecsL,
       "dsAdslAtucPerfDataExtnCurr1DayFecsL": dsAdslAtucPerfDataExtnCurr1DayFecsL,
       "dsAdslAtucPerfDataExtnPrev1DayFecsL": dsAdslAtucPerfDataExtnPrev1DayFecsL,
       "dsAdslAtucPerfDataExtnStatLossL": dsAdslAtucPerfDataExtnStatLossL,
       "dsAdslAtucPerfDataExtnCurr15MinLossL": dsAdslAtucPerfDataExtnCurr15MinLossL,
       "dsAdslAtucPerfDataExtnCurr1DayLossL": dsAdslAtucPerfDataExtnCurr1DayLossL,
       "dsAdslAtucPerfDataExtnPrev1DayLossL": dsAdslAtucPerfDataExtnPrev1DayLossL,
       "dsAdslAturPerfDataExtnTable": dsAdslAturPerfDataExtnTable,
       "dsAdslAturPerfDataExtnEntry": dsAdslAturPerfDataExtnEntry,
       "dsAdslAturPerfDataExtnStatSesL": dsAdslAturPerfDataExtnStatSesL,
       "dsAdslAturPerfDataExtnCurr15MinSesL": dsAdslAturPerfDataExtnCurr15MinSesL,
       "dsAdslAturPerfDataExtnCurr1DaySesL": dsAdslAturPerfDataExtnCurr1DaySesL,
       "dsAdslAturPerfDataExtnPrev1DaySesL": dsAdslAturPerfDataExtnPrev1DaySesL,
       "dsAdslAturPerfDataExtnStatUasL": dsAdslAturPerfDataExtnStatUasL,
       "dsAdslAturPerfDataExtnCurr15MinUasL": dsAdslAturPerfDataExtnCurr15MinUasL,
       "dsAdslAturPerfDataExtnCurr1DayUasL": dsAdslAturPerfDataExtnCurr1DayUasL,
       "dsAdslAturPerfDataExtnPrev1DayUasL": dsAdslAturPerfDataExtnPrev1DayUasL,
       "dsAdslAturPerfDataExtnStatFecsL": dsAdslAturPerfDataExtnStatFecsL,
       "dsAdslAturPerfDataExtnCurr15MinFecsL": dsAdslAturPerfDataExtnCurr15MinFecsL,
       "dsAdslAturPerfDataExtnCurr1DayFecsL": dsAdslAturPerfDataExtnCurr1DayFecsL,
       "dsAdslAturPerfDataExtnPrev1DayFecsL": dsAdslAturPerfDataExtnPrev1DayFecsL,
       "dsAdslAturPerfDataExtnStatLossL": dsAdslAturPerfDataExtnStatLossL,
       "dsAdslAturPerfDataExtnCurr15MinLossL": dsAdslAturPerfDataExtnCurr15MinLossL,
       "dsAdslAturPerfDataExtnCurr1DayLossL": dsAdslAturPerfDataExtnCurr1DayLossL,
       "dsAdslAturPerfDataExtnPrev1DayLossL": dsAdslAturPerfDataExtnPrev1DayLossL,
       "dsAdslAtucIntervalExtnTable": dsAdslAtucIntervalExtnTable,
       "dsAdslAtucIntervalExtnEntry": dsAdslAtucIntervalExtnEntry,
       "dsAdslAtucIntervalExtnFastR": dsAdslAtucIntervalExtnFastR,
       "dsAdslAtucIntervalExtnFailedFastR": dsAdslAtucIntervalExtnFailedFastR,
       "dsAdslAtucIntervalExtnSesL": dsAdslAtucIntervalExtnSesL,
       "dsAdslAtucIntervalExtnUasL": dsAdslAtucIntervalExtnUasL,
       "dsAdslAtucIntervalExtnTimeElapsed": dsAdslAtucIntervalExtnTimeElapsed,
       "dsAdslAtucChanPerfDataExtnTable": dsAdslAtucChanPerfDataExtnTable,
       "dsAdslAtucChanPerfDataExtnEntry": dsAdslAtucChanPerfDataExtnEntry,
       "dsAdslAtucChanPerfDataExtnTimeElapsed": dsAdslAtucChanPerfDataExtnTimeElapsed,
       "dsAdslAtucChanPerfDataExtnNcd": dsAdslAtucChanPerfDataExtnNcd,
       "dsAdslAtucChanPerfDataExtnOcd": dsAdslAtucChanPerfDataExtnOcd,
       "dsAdslAtucChanPerfDataExtnHec": dsAdslAtucChanPerfDataExtnHec,
       "dsAdslAtucChanPerfDataExtnCurr15MinNcd": dsAdslAtucChanPerfDataExtnCurr15MinNcd,
       "dsAdslAtucChanPerfDataExtnCurr15MinOcd": dsAdslAtucChanPerfDataExtnCurr15MinOcd,
       "dsAdslAtucChanPerfDataExtnCurr15MinHec": dsAdslAtucChanPerfDataExtnCurr15MinHec,
       "dsAdslAtucChanPerfDataExtnCurr1DayNcd": dsAdslAtucChanPerfDataExtnCurr1DayNcd,
       "dsAdslAtucChanPerfDataExtnCurr1DayOcd": dsAdslAtucChanPerfDataExtnCurr1DayOcd,
       "dsAdslAtucChanPerfDataExtnCurr1DayHec": dsAdslAtucChanPerfDataExtnCurr1DayHec,
       "dsAdslAtucChanPerfDataExtnPrev1DayNcd": dsAdslAtucChanPerfDataExtnPrev1DayNcd,
       "dsAdslAtucChanPerfDataExtnPrev1DayOcd": dsAdslAtucChanPerfDataExtnPrev1DayOcd,
       "dsAdslAtucChanPerfDataExtnPrev1DayHec": dsAdslAtucChanPerfDataExtnPrev1DayHec,
       "dsAdslAturChanPerfDataExtnTable": dsAdslAturChanPerfDataExtnTable,
       "dsAdslAturChanPerfDataExtnEntry": dsAdslAturChanPerfDataExtnEntry,
       "dsAdslAturChanPerfDataExtnNcd": dsAdslAturChanPerfDataExtnNcd,
       "dsAdslAturChanPerfDataExtnHec": dsAdslAturChanPerfDataExtnHec,
       "dsAdslAturChanPerfDataExtnCurr15MinNcd": dsAdslAturChanPerfDataExtnCurr15MinNcd,
       "dsAdslAturChanPerfDataExtnCurr15MinHec": dsAdslAturChanPerfDataExtnCurr15MinHec,
       "dsAdslAturChanPerfDataExtnCurr1DayNcd": dsAdslAturChanPerfDataExtnCurr1DayNcd,
       "dsAdslAturChanPerfDataExtnCurr1DayHec": dsAdslAturChanPerfDataExtnCurr1DayHec,
       "dsAdslAturChanPerfDataExtnPrev1DayNcd": dsAdslAturChanPerfDataExtnPrev1DayNcd,
       "dsAdslAturChanPerfDataExtnPrev1DayHec": dsAdslAturChanPerfDataExtnPrev1DayHec,
       "dsAdslAtucChanIntervalExtnTable": dsAdslAtucChanIntervalExtnTable,
       "dsAdslAtucChanIntervalExtnEntry": dsAdslAtucChanIntervalExtnEntry,
       "dsAdslAtucChanIntervalExtnTimeElapsed": dsAdslAtucChanIntervalExtnTimeElapsed,
       "dsAdslAtucChanIntervalExtnNcd": dsAdslAtucChanIntervalExtnNcd,
       "dsAdslAtucChanIntervalExtnOcd": dsAdslAtucChanIntervalExtnOcd,
       "dsAdslAtucChanIntervalExtnHec": dsAdslAtucChanIntervalExtnHec,
       "dsAdslAturChanIntervalExtnTable": dsAdslAturChanIntervalExtnTable,
       "dsAdslAturChanIntervalExtnEntry": dsAdslAturChanIntervalExtnEntry,
       "dsAdslAturChanIntervalExtnNcd": dsAdslAturChanIntervalExtnNcd,
       "dsAdslAturChanIntervalExtnHec": dsAdslAturChanIntervalExtnHec,
       "dsAdslLineConfProfileExtnTable": dsAdslLineConfProfileExtnTable,
       "dsAdslLineConfProfileExtnEntry": dsAdslLineConfProfileExtnEntry,
       "dsAdslLineConfProfileName": dsAdslLineConfProfileName,
       "dsAdslLineConfProfileExtnRsIntCorrectionUp": dsAdslLineConfProfileExtnRsIntCorrectionUp,
       "dsAdslLineConfProfileExtnLineType": dsAdslLineConfProfileExtnLineType,
       "dsAdslLineConfProfileExtnTxEndBin": dsAdslLineConfProfileExtnTxEndBin,
       "dsAdslLineConfProfileExtnTxStartBin": dsAdslLineConfProfileExtnTxStartBin,
       "dsAdslLineConfProfileExtnRxStartBin": dsAdslLineConfProfileExtnRxStartBin,
       "dsAdslLineConfProfileExtnRxEndBin": dsAdslLineConfProfileExtnRxEndBin,
       "dsAdslLineConfProfileExtnRxBinAdjust": dsAdslLineConfProfileExtnRxBinAdjust,
       "dsAdslLineConfProfileExtnStandard": dsAdslLineConfProfileExtnStandard,
       "dsAdslLineConfProfileExtnTxPowerAttenuation": dsAdslLineConfProfileExtnTxPowerAttenuation,
       "dsAdslLineConfProfileExtnRsFastOvrhdDown": dsAdslLineConfProfileExtnRsFastOvrhdDown,
       "dsAdslLineConfProfileExtnIntCorrectionDown": dsAdslLineConfProfileExtnIntCorrectionDown,
       "dsAdslLineConfProfileExtnRsFastOvrhdUp": dsAdslLineConfProfileExtnRsFastOvrhdUp,
       "dsAdslLineConfProfileExtnAnnexType": dsAdslLineConfProfileExtnAnnexType,
       "dsAdslLineConfProfileExtnMaxDCo": dsAdslLineConfProfileExtnMaxDCo,
       "dsAdslLineConfProfileExtnAdvertisedCapabilities": dsAdslLineConfProfileExtnAdvertisedCapabilities,
       "dsAdslLineConfProfileExtnPsdMaskType": dsAdslLineConfProfileExtnPsdMaskType,
       "dsAdslLineConfProfileExtnLineDmtConfMode": dsAdslLineConfProfileExtnLineDmtConfMode,
       "dsAdslLineConfProfileExtnUpstreamPSD": dsAdslLineConfProfileExtnUpstreamPSD,
       "dsAdslLineConfProfileExtnPMMode": dsAdslLineConfProfileExtnPMMode,
       "dsAdslLineConfProfileExtnPML0Time": dsAdslLineConfProfileExtnPML0Time,
       "dsAdslLineConfProfileExtnPML2Time": dsAdslLineConfProfileExtnPML2Time,
       "dsAdslLineConfProfileExtnPML2ATPR": dsAdslLineConfProfileExtnPML2ATPR,
       "dsAdslLineConfProfileExtnPML2Rate": dsAdslLineConfProfileExtnPML2Rate,
       "dsAdslLineConfProfileExtnAtucConfMinINP": dsAdslLineConfProfileExtnAtucConfMinINP,
       "dsAdslLineConfProfileExtnPML2EntryThresholdRate": dsAdslLineConfProfileExtnPML2EntryThresholdRate,
       "dsAdslLineConfProfileExtnPML2ExitThresholdRate": dsAdslLineConfProfileExtnPML2ExitThresholdRate,
       "dsAdslLineConfProfileExtnPML2EntryRateMinTime": dsAdslLineConfProfileExtnPML2EntryRateMinTime,
       "dsAdslLineAlarmConfProfileExtnTable": dsAdslLineAlarmConfProfileExtnTable,
       "dsAdslLineAlarmConfProfileExtnEntry": dsAdslLineAlarmConfProfileExtnEntry,
       "dsAdslLineAlarmConfProfileName": dsAdslLineAlarmConfProfileName,
       "dsAdslLineAlarmExtnAtucThresh15MinFailFastR": dsAdslLineAlarmExtnAtucThresh15MinFailFastR,
       "dsAdslLineAlarmExtnAtucThresh15MinSesL": dsAdslLineAlarmExtnAtucThresh15MinSesL,
       "dsAdslLineAlarmExtnAtucThresh15MinUasL": dsAdslLineAlarmExtnAtucThresh15MinUasL,
       "dsAdslLineAlarmExtnAtucOpStateTrapEnable": dsAdslLineAlarmExtnAtucOpStateTrapEnable,
       "dsAdslLineAlarmExtnAtucThresh15MinFecsL": dsAdslLineAlarmExtnAtucThresh15MinFecsL,
       "dsAdslLineAlarmExtnAtucThresh1DayLofs": dsAdslLineAlarmExtnAtucThresh1DayLofs,
       "dsAdslLineAlarmExtnAtucThresh1DayLoss": dsAdslLineAlarmExtnAtucThresh1DayLoss,
       "dsAdslLineAlarmExtnAtucThresh1DayLols": dsAdslLineAlarmExtnAtucThresh1DayLols,
       "dsAdslLineAlarmExtnAtucThresh1DayLprs": dsAdslLineAlarmExtnAtucThresh1DayLprs,
       "dsAdslLineAlarmExtnAtucThresh1DayESs": dsAdslLineAlarmExtnAtucThresh1DayESs,
       "dsAdslLineAlarmExtnAtucThresh1DaySesL": dsAdslLineAlarmExtnAtucThresh1DaySesL,
       "dsAdslLineAlarmExtnAtucThresh1DayUasL": dsAdslLineAlarmExtnAtucThresh1DayUasL,
       "dsAdslLineAlarmExtnAtucThresh1DayFecsL": dsAdslLineAlarmExtnAtucThresh1DayFecsL,
       "dsAdslLineAlarmExtnAturThresh15MinFecsL": dsAdslLineAlarmExtnAturThresh15MinFecsL,
       "dsAdslLineAlarmExtnAturThresh1DayLofs": dsAdslLineAlarmExtnAturThresh1DayLofs,
       "dsAdslLineAlarmExtnAturThresh1DayLoss": dsAdslLineAlarmExtnAturThresh1DayLoss,
       "dsAdslLineAlarmExtnAturThresh1DayLprs": dsAdslLineAlarmExtnAturThresh1DayLprs,
       "dsAdslLineAlarmExtnAturThresh1DayESs": dsAdslLineAlarmExtnAturThresh1DayESs,
       "dsAdslLineAlarmExtnAturThresh1DaySesL": dsAdslLineAlarmExtnAturThresh1DaySesL,
       "dsAdslLineAlarmExtnAturThresh1DayUasL": dsAdslLineAlarmExtnAturThresh1DayUasL,
       "dsAdslLineAlarmExtnAturThresh1DayFecsL": dsAdslLineAlarmExtnAturThresh1DayFecsL,
       "dsAdslLineAlarmExtnAturThresh15MinSesL": dsAdslLineAlarmExtnAturThresh15MinSesL,
       "dsAdslLineAlarmExtnAturThresh15MinUasL": dsAdslLineAlarmExtnAturThresh15MinUasL,
       "dsAdslLineAlarmExtnAtucPmStateTrapEnable": dsAdslLineAlarmExtnAtucPmStateTrapEnable,
       "dsAdslTrap": dsAdslTrap,
       "dsAdslAtucTraps": dsAdslAtucTraps,
       "dsAdslAtucOpStateChangeTrap": dsAdslAtucOpStateChangeTrap,
       "dsAdslAtucPmStateChangeTrap": dsAdslAtucPmStateChangeTrap,
       "dsAdslAtucPerfFailedFastRThreshTrap": dsAdslAtucPerfFailedFastRThreshTrap,
       "dsAdslAtucPerfSesLThreshTrap": dsAdslAtucPerfSesLThreshTrap,
       "dsAdslAtucPerfUasLThreshTrap": dsAdslAtucPerfUasLThreshTrap,
       "dsAdslAtucPerfFecsLThreshTrap": dsAdslAtucPerfFecsLThreshTrap,
       "dsAdslAtucPerfLofsThresh1DayTrap": dsAdslAtucPerfLofsThresh1DayTrap,
       "dsAdslAtucPerfLossThresh1DayTrap": dsAdslAtucPerfLossThresh1DayTrap,
       "dsAdslAtucPerfLolsThresh1DayTrap": dsAdslAtucPerfLolsThresh1DayTrap,
       "dsAdslAtucPerfLprsThresh1DayTrap": dsAdslAtucPerfLprsThresh1DayTrap,
       "dsAdslAtucPerfESsThresh1DayTrap": dsAdslAtucPerfESsThresh1DayTrap,
       "dsAdslAtucPerfSesLThresh1DayTrap": dsAdslAtucPerfSesLThresh1DayTrap,
       "dsAdslAtucPerfUasLThresh1DayTrap": dsAdslAtucPerfUasLThresh1DayTrap,
       "dsAdslAtucPerfFecsLThresh1DayTrap": dsAdslAtucPerfFecsLThresh1DayTrap,
       "dsAdslAturTraps": dsAdslAturTraps,
       "dsAdslAturSesLThreshTrap": dsAdslAturSesLThreshTrap,
       "dsAdslAturUasLThreshTrap": dsAdslAturUasLThreshTrap,
       "dsAdslAturPerfFecsLThreshTrap": dsAdslAturPerfFecsLThreshTrap,
       "dsAdslAturPerfLofsThresh1DayTrap": dsAdslAturPerfLofsThresh1DayTrap,
       "dsAdslAturPerfLossThresh1DayTrap": dsAdslAturPerfLossThresh1DayTrap,
       "dsAdslAturPerfLprsThresh1DayTrap": dsAdslAturPerfLprsThresh1DayTrap,
       "dsAdslAturPerfESsThresh1DayTrap": dsAdslAturPerfESsThresh1DayTrap,
       "dsAdslAturPerfSesLThresh1DayTrap": dsAdslAturPerfSesLThresh1DayTrap,
       "dsAdslAturPerfUasLThresh1DayTrap": dsAdslAturPerfUasLThresh1DayTrap,
       "dsAdslAturPerfFecsLThresh1DayTrap": dsAdslAturPerfFecsLThresh1DayTrap}
)
