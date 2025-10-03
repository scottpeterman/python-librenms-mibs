# SNMP MIB module (DASAN-SHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-SHDSL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:11 2025
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

dasanShdslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanShdslLineMIB_ObjectIdentity = ObjectIdentity
dasanShdslLineMIB = _DasanShdslLineMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1)
)
_DasanShdslMIBObjects_ObjectIdentity = ObjectIdentity
dasanShdslMIBObjects = _DasanShdslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1)
)
_DsShdslCapabilityGroup_ObjectIdentity = ObjectIdentity
dsShdslCapabilityGroup = _DsShdslCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 1)
)


class _DsShdslCapabilityLineTxCap_Type(Bits):
    """Custom type dsShdslCapabilityLineTxCap based on Bits"""
    namedValues = NamedValues(
        *(("region1", 0),
          ("region2", 1))
    )

_DsShdslCapabilityLineTxCap_Type.__name__ = "Bits"
_DsShdslCapabilityLineTxCap_Object = MibScalar
dsShdslCapabilityLineTxCap = _DsShdslCapabilityLineTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 1, 1),
    _DsShdslCapabilityLineTxCap_Type()
)
dsShdslCapabilityLineTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslCapabilityLineTxCap.setStatus("current")
_DsShdslLineStatusTable_Object = MibTable
dsShdslLineStatusTable = _DsShdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dsShdslLineStatusTable.setStatus("current")
_DsShdslLineStatusEntry_Object = MibTableRow
dsShdslLineStatusEntry = _DsShdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1)
)
dsShdslLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsShdslLineStatusEntry.setStatus("current")


class _DsShdslOpState_Type(Integer32):
    """Custom type dsShdslOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8,
              9,
              16,
              20,
              24,
              26,
              27,
              29,
              128,
              130,
              131,
              133,
              138,
              139,
              142,
              143,
              144,
              145,
              146)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("data", 1),
          ("bootupLoad", 8),
          ("bootupLoadDone", 9),
          ("handshake", 16),
          ("pmms", 20),
          ("training", 24),
          ("framerGearShift", 26),
          ("framerManualReset", 27),
          ("silence", 29),
          ("analogLb", 128),
          ("rmtFramerLb", 130),
          ("digitalLb", 131),
          ("spectrumTest", 133),
          ("selt", 138),
          ("pSDTest", 139),
          ("lclFramerLb", 142),
          ("interfaceLb", 143),
          ("bertTest", 144),
          ("analogLbBertTest", 145),
          ("digLbBertTest", 146))
    )


_DsShdslOpState_Type.__name__ = "Integer32"
_DsShdslOpState_Object = MibTableColumn
dsShdslOpState = _DsShdslOpState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 1),
    _DsShdslOpState_Type()
)
dsShdslOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslOpState.setStatus("current")


class _DsShdslStartProgress_Type(Integer32):
    """Custom type dsShdslStartProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              7,
              8,
              55,
              56,
              57,
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
              113,
              114,
              115,
              116,
              117,
              118,
              128,
              129,
              130,
              131,
              144,
              145,
              146,
              147)
        )
    )
    namedValues = NamedValues(
        *(("noActivity", 0),
          ("preActivation", 1),
          ("activation", 4),
          ("checkBitrate", 7),
          ("pmmsChkComnRate", 8),
          ("transmitCr", 55),
          ("transmitSc", 56),
          ("transmitSr", 57),
          ("coLineAgc", 64),
          ("cpLineAgc", 65),
          ("fdEcTrain", 66),
          ("equalizerTrain", 67),
          ("tipRingAligned", 68),
          ("transmitTc", 69),
          ("receiveTr", 70),
          ("transmitFc1", 71),
          ("transmitFc2", 72),
          ("receiveTc", 73),
          ("transmitTr", 74),
          ("receiveFc", 75),
          ("spectTestOk", 113),
          ("albTestOk", 114),
          ("dlbTestOk", 115),
          ("crcFail", 116),
          ("framerSyncFail", 117),
          ("snrMarginFail", 118),
          ("loadCppa", 128),
          ("loadCptrain", 129),
          ("loadCptom", 130),
          ("loadCpdm", 131),
          ("loadCopa", 144),
          ("loadCotrain", 145),
          ("loadCotom", 146),
          ("loadCodm", 147))
    )


_DsShdslStartProgress_Type.__name__ = "Integer32"
_DsShdslStartProgress_Object = MibTableColumn
dsShdslStartProgress = _DsShdslStartProgress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 2),
    _DsShdslStartProgress_Type()
)
dsShdslStartProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslStartProgress.setStatus("current")


class _DsShdslFwRelease_Type(OctetString):
    """Custom type dsShdslFwRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsShdslFwRelease_Type.__name__ = "OctetString"
_DsShdslFwRelease_Object = MibTableColumn
dsShdslFwRelease = _DsShdslFwRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 3),
    _DsShdslFwRelease_Type()
)
dsShdslFwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslFwRelease.setStatus("current")


class _DsShdslLineSwap_Type(Integer32):
    """Custom type dsShdslLineSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unswapped", 0),
          ("swapped", 1))
    )


_DsShdslLineSwap_Type.__name__ = "Integer32"
_DsShdslLineSwap_Object = MibTableColumn
dsShdslLineSwap = _DsShdslLineSwap_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 4),
    _DsShdslLineSwap_Type()
)
dsShdslLineSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslLineSwap.setStatus("current")


class _DsShdslRmtCountryCode_Type(OctetString):
    """Custom type dsShdslRmtCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsShdslRmtCountryCode_Type.__name__ = "OctetString"
_DsShdslRmtCountryCode_Object = MibTableColumn
dsShdslRmtCountryCode = _DsShdslRmtCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 5),
    _DsShdslRmtCountryCode_Type()
)
dsShdslRmtCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtCountryCode.setStatus("current")
_DsShdslRmtEncoderA_Type = Integer32
_DsShdslRmtEncoderA_Object = MibTableColumn
dsShdslRmtEncoderA = _DsShdslRmtEncoderA_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 6),
    _DsShdslRmtEncoderA_Type()
)
dsShdslRmtEncoderA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtEncoderA.setStatus("current")
_DsShdslRmtEncoderB_Type = Integer32
_DsShdslRmtEncoderB_Object = MibTableColumn
dsShdslRmtEncoderB = _DsShdslRmtEncoderB_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 7),
    _DsShdslRmtEncoderB_Type()
)
dsShdslRmtEncoderB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtEncoderB.setStatus("current")


class _DsShdslRmtProviderCode_Type(OctetString):
    """Custom type dsShdslRmtProviderCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsShdslRmtProviderCode_Type.__name__ = "OctetString"
_DsShdslRmtProviderCode_Object = MibTableColumn
dsShdslRmtProviderCode = _DsShdslRmtProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 8),
    _DsShdslRmtProviderCode_Type()
)
dsShdslRmtProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtProviderCode.setStatus("current")
_DsShdslLocDetect_Type = Integer32
_DsShdslLocDetect_Object = MibTableColumn
dsShdslLocDetect = _DsShdslLocDetect_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 9),
    _DsShdslLocDetect_Type()
)
dsShdslLocDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslLocDetect.setStatus("current")
_DsShdslTxPower_Type = Integer32
_DsShdslTxPower_Object = MibTableColumn
dsShdslTxPower = _DsShdslTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 10),
    _DsShdslTxPower_Type()
)
dsShdslTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslTxPower.setStatus("current")


class _DsShdslFramerSync_Type(Integer32):
    """Custom type dsShdslFramerSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 0),
          ("inSync", 1))
    )


_DsShdslFramerSync_Type.__name__ = "Integer32"
_DsShdslFramerSync_Object = MibTableColumn
dsShdslFramerSync = _DsShdslFramerSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 11),
    _DsShdslFramerSync_Type()
)
dsShdslFramerSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslFramerSync.setStatus("current")
_DsShdslRmtTomData_Type = Integer32
_DsShdslRmtTomData_Object = MibTableColumn
dsShdslRmtTomData = _DsShdslRmtTomData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 12),
    _DsShdslRmtTomData_Type()
)
dsShdslRmtTomData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtTomData.setStatus("current")
_DsShdslDriftAlarm_Type = Integer32
_DsShdslDriftAlarm_Object = MibTableColumn
dsShdslDriftAlarm = _DsShdslDriftAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 13),
    _DsShdslDriftAlarm_Type()
)
dsShdslDriftAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslDriftAlarm.setStatus("current")
_DsShdslReceiverGain_Type = Integer32
_DsShdslReceiverGain_Object = MibTableColumn
dsShdslReceiverGain = _DsShdslReceiverGain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 14),
    _DsShdslReceiverGain_Type()
)
dsShdslReceiverGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslReceiverGain.setStatus("current")


class _DsShdslBertError_Type(Integer32):
    """Custom type dsShdslBertError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 0),
          ("framedSync", 64),
          ("unframedSync", 128))
    )


_DsShdslBertError_Type.__name__ = "Integer32"
_DsShdslBertError_Object = MibTableColumn
dsShdslBertError = _DsShdslBertError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 15),
    _DsShdslBertError_Type()
)
dsShdslBertError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslBertError.setStatus("current")


class _DsShdslFramerOHAndDefects_Type(OctetString):
    """Custom type dsShdslFramerOHAndDefects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsShdslFramerOHAndDefects_Type.__name__ = "OctetString"
_DsShdslFramerOHAndDefects_Object = MibTableColumn
dsShdslFramerOHAndDefects = _DsShdslFramerOHAndDefects_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 16),
    _DsShdslFramerOHAndDefects_Type()
)
dsShdslFramerOHAndDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslFramerOHAndDefects.setStatus("current")
_DsShdslRmtFwVersion_Type = Integer32
_DsShdslRmtFwVersion_Object = MibTableColumn
dsShdslRmtFwVersion = _DsShdslRmtFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 17),
    _DsShdslRmtFwVersion_Type()
)
dsShdslRmtFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtFwVersion.setStatus("current")


class _DsShdslUtopiaCellDelineation_Type(Integer32):
    """Custom type dsShdslUtopiaCellDelineation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              160,
              240)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("preSync", 160),
          ("hunt", 240))
    )


_DsShdslUtopiaCellDelineation_Type.__name__ = "Integer32"
_DsShdslUtopiaCellDelineation_Object = MibTableColumn
dsShdslUtopiaCellDelineation = _DsShdslUtopiaCellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 18),
    _DsShdslUtopiaCellDelineation_Type()
)
dsShdslUtopiaCellDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaCellDelineation.setStatus("current")
_DsShdslUtopiaRxCellCnt_Type = Integer32
_DsShdslUtopiaRxCellCnt_Object = MibTableColumn
dsShdslUtopiaRxCellCnt = _DsShdslUtopiaRxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 19),
    _DsShdslUtopiaRxCellCnt_Type()
)
dsShdslUtopiaRxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaRxCellCnt.setStatus("current")
_DsShdslUtopiaCellDropCnt_Type = Integer32
_DsShdslUtopiaCellDropCnt_Object = MibTableColumn
dsShdslUtopiaCellDropCnt = _DsShdslUtopiaCellDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 20),
    _DsShdslUtopiaCellDropCnt_Type()
)
dsShdslUtopiaCellDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaCellDropCnt.setStatus("current")
_DsShdslUtopiaRxHecErrorCnt_Type = Integer32
_DsShdslUtopiaRxHecErrorCnt_Object = MibTableColumn
dsShdslUtopiaRxHecErrorCnt = _DsShdslUtopiaRxHecErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 21),
    _DsShdslUtopiaRxHecErrorCnt_Type()
)
dsShdslUtopiaRxHecErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaRxHecErrorCnt.setStatus("current")
_DsShdslUtopiaTxCellCnt_Type = Integer32
_DsShdslUtopiaTxCellCnt_Object = MibTableColumn
dsShdslUtopiaTxCellCnt = _DsShdslUtopiaTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 22),
    _DsShdslUtopiaTxCellCnt_Type()
)
dsShdslUtopiaTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaTxCellCnt.setStatus("current")
_DsShdslRmtNsfCusId_Type = Integer32
_DsShdslRmtNsfCusId_Object = MibTableColumn
dsShdslRmtNsfCusId = _DsShdslRmtNsfCusId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 23),
    _DsShdslRmtNsfCusId_Type()
)
dsShdslRmtNsfCusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtNsfCusId.setStatus("current")


class _DsShdslRmtNsfCusData_Type(OctetString):
    """Custom type dsShdslRmtNsfCusData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DsShdslRmtNsfCusData_Type.__name__ = "OctetString"
_DsShdslRmtNsfCusData_Object = MibTableColumn
dsShdslRmtNsfCusData = _DsShdslRmtNsfCusData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 24),
    _DsShdslRmtNsfCusData_Type()
)
dsShdslRmtNsfCusData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtNsfCusData.setStatus("current")


class _DsShdslLocalHandshake_Type(OctetString):
    """Custom type dsShdslLocalHandshake based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 52),
    )


_DsShdslLocalHandshake_Type.__name__ = "OctetString"
_DsShdslLocalHandshake_Object = MibTableColumn
dsShdslLocalHandshake = _DsShdslLocalHandshake_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 25),
    _DsShdslLocalHandshake_Type()
)
dsShdslLocalHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslLocalHandshake.setStatus("current")


class _DsShdslRemoteHandshake_Type(OctetString):
    """Custom type dsShdslRemoteHandshake based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 52),
    )


_DsShdslRemoteHandshake_Type.__name__ = "OctetString"
_DsShdslRemoteHandshake_Object = MibTableColumn
dsShdslRemoteHandshake = _DsShdslRemoteHandshake_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 26),
    _DsShdslRemoteHandshake_Type()
)
dsShdslRemoteHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRemoteHandshake.setStatus("current")


class _DsShdslActualHandshake_Type(OctetString):
    """Custom type dsShdslActualHandshake based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 52),
    )


_DsShdslActualHandshake_Type.__name__ = "OctetString"
_DsShdslActualHandshake_Object = MibTableColumn
dsShdslActualHandshake = _DsShdslActualHandshake_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 27),
    _DsShdslActualHandshake_Type()
)
dsShdslActualHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslActualHandshake.setStatus("current")
_DsShdslRmtTxPower_Type = Integer32
_DsShdslRmtTxPower_Object = MibTableColumn
dsShdslRmtTxPower = _DsShdslRmtTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 28),
    _DsShdslRmtTxPower_Type()
)
dsShdslRmtTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtTxPower.setStatus("current")


class _DsShdslRmtPowerBackoff_Type(Integer32):
    """Custom type dsShdslRmtPowerBackoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 32768))
    )


_DsShdslRmtPowerBackoff_Type.__name__ = "Integer32"
_DsShdslRmtPowerBackoff_Object = MibTableColumn
dsShdslRmtPowerBackoff = _DsShdslRmtPowerBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 29),
    _DsShdslRmtPowerBackoff_Type()
)
dsShdslRmtPowerBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslRmtPowerBackoff.setStatus("current")
_DsShdslAutoRetrainCount_Type = Integer32
_DsShdslAutoRetrainCount_Object = MibTableColumn
dsShdslAutoRetrainCount = _DsShdslAutoRetrainCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 30),
    _DsShdslAutoRetrainCount_Type()
)
dsShdslAutoRetrainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslAutoRetrainCount.setStatus("current")


class _DsShdslEocState_Type(Integer32):
    """Custom type dsShdslEocState based on Integer32"""
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
        *(("online", 0),
          ("discovery", 1),
          ("inventory", 2),
          ("configuration", 3),
          ("cmdInProgress", 4))
    )


_DsShdslEocState_Type.__name__ = "Integer32"
_DsShdslEocState_Object = MibTableColumn
dsShdslEocState = _DsShdslEocState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 31),
    _DsShdslEocState_Type()
)
dsShdslEocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslEocState.setStatus("current")


class _DsShdslFramerOneSecondCnt_Type(OctetString):
    """Custom type dsShdslFramerOneSecondCnt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DsShdslFramerOneSecondCnt_Type.__name__ = "OctetString"
_DsShdslFramerOneSecondCnt_Object = MibTableColumn
dsShdslFramerOneSecondCnt = _DsShdslFramerOneSecondCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 32),
    _DsShdslFramerOneSecondCnt_Type()
)
dsShdslFramerOneSecondCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslFramerOneSecondCnt.setStatus("current")


class _DsShdslNtrFault_Type(Integer32):
    """Custom type dsShdslNtrFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("present", 0),
          ("absent", 1))
    )


_DsShdslNtrFault_Type.__name__ = "Integer32"
_DsShdslNtrFault_Object = MibTableColumn
dsShdslNtrFault = _DsShdslNtrFault_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 33),
    _DsShdslNtrFault_Type()
)
dsShdslNtrFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslNtrFault.setStatus("current")


class _DsShdslCpeMasterCore_Type(Integer32):
    """Custom type dsShdslCpeMasterCore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128)
        )
    )
    namedValues = NamedValues(
        *(("core0", 0),
          ("core1", 16),
          ("core2", 32),
          ("core3", 48),
          ("core4", 64),
          ("core5", 80),
          ("core6", 96),
          ("core7", 112),
          ("noMasterCore", 128))
    )


_DsShdslCpeMasterCore_Type.__name__ = "Integer32"
_DsShdslCpeMasterCore_Object = MibTableColumn
dsShdslCpeMasterCore = _DsShdslCpeMasterCore_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 34),
    _DsShdslCpeMasterCore_Type()
)
dsShdslCpeMasterCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslCpeMasterCore.setStatus("current")


class _DsShdslParametricTestResult_Type(Integer32):
    """Custom type dsShdslParametricTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pass", 0),
          ("fail", 1))
    )


_DsShdslParametricTestResult_Type.__name__ = "Integer32"
_DsShdslParametricTestResult_Object = MibTableColumn
dsShdslParametricTestResult = _DsShdslParametricTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 35),
    _DsShdslParametricTestResult_Type()
)
dsShdslParametricTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslParametricTestResult.setStatus("current")


class _DsShdslParametricTestArray_Type(OctetString):
    """Custom type dsShdslParametricTestArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DsShdslParametricTestArray_Type.__name__ = "OctetString"
_DsShdslParametricTestArray_Object = MibTableColumn
dsShdslParametricTestArray = _DsShdslParametricTestArray_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 2, 1, 36),
    _DsShdslParametricTestArray_Type()
)
dsShdslParametricTestArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslParametricTestArray.setStatus("current")
_DsShdslLineParamsTable_Object = MibTable
dsShdslLineParamsTable = _DsShdslLineParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dsShdslLineParamsTable.setStatus("current")
_DsShdslLineParamsEntry_Object = MibTableRow
dsShdslLineParamsEntry = _DsShdslLineParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1)
)
dsShdslLineParamsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsShdslLineParamsEntry.setStatus("current")


class _DsShdslAction_Type(Integer32):
    """Custom type dsShdslAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              6,
              8,
              17,
              18,
              20,
              25,
              26,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("startUp", 0),
          ("abortReq", 2),
          ("gearShiftReq", 6),
          ("downloadReq", 8),
          ("bertStartTxReq", 17),
          ("bertStartRxReq", 18),
          ("bertStopReq", 20),
          ("spectrumDownReq", 25),
          ("spectrumUpReq", 26),
          ("spectrumTxRxReq", 32),
          ("hybridLossTestReq", 33),
          ("residualEchoReq", 34),
          ("totalEchoReq", 35),
          ("nextPsdReq", 36),
          ("autoRetrainOnReq", 37),
          ("autoRetrainOffReq", 38),
          ("propEocOnReq", 45),
          ("propEocOffReq", 46),
          ("rmtAtmCellStatusReq", 47),
          ("rmtFullStatusReq", 48))
    )


_DsShdslAction_Type.__name__ = "Integer32"
_DsShdslAction_Object = MibTableColumn
dsShdslAction = _DsShdslAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 1),
    _DsShdslAction_Type()
)
dsShdslAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslAction.setStatus("current")


class _DsShdslMode_Type(Integer32):
    """Custom type dsShdslMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("co", 0),
          ("cpe", 1))
    )


_DsShdslMode_Type.__name__ = "Integer32"
_DsShdslMode_Object = MibTableColumn
dsShdslMode = _DsShdslMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 2),
    _DsShdslMode_Type()
)
dsShdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslMode.setStatus("current")


class _DsShdslPowerScale_Type(Integer32):
    """Custom type dsShdslPowerScale based on Integer32"""
    defaultValue = 26112

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            26112
        )
    )
    namedValues = NamedValues(
        ("defaultScale", 26112)
    )


_DsShdslPowerScale_Type.__name__ = "Integer32"
_DsShdslPowerScale_Object = MibTableColumn
dsShdslPowerScale = _DsShdslPowerScale_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 3),
    _DsShdslPowerScale_Type()
)
dsShdslPowerScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslPowerScale.setStatus("current")


class _DsShdslFramerType_Type(Integer32):
    """Custom type dsShdslFramerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unframed", 0),
          ("t1Slotted", 1),
          ("e1Slotted", 2),
          ("utopiaL2", 3),
          ("nx64", 6),
          ("serialATM", 7),
          ("vC12", 8),
          ("iMA", 9))
    )


_DsShdslFramerType_Type.__name__ = "Integer32"
_DsShdslFramerType_Object = MibTableColumn
dsShdslFramerType = _DsShdslFramerType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 4),
    _DsShdslFramerType_Type()
)
dsShdslFramerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslFramerType.setStatus("current")


class _DsShdslAFEType_Type(Integer32):
    """Custom type dsShdslAFEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("saturn", 3),
          ("saturnLg", 4))
    )


_DsShdslAFEType_Type.__name__ = "Integer32"
_DsShdslAFEType_Object = MibTableColumn
dsShdslAFEType = _DsShdslAFEType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 5),
    _DsShdslAFEType_Type()
)
dsShdslAFEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslAFEType.setStatus("current")


class _DsShdslEncodeCoeffA_Type(Integer32):
    """Custom type dsShdslEncodeCoeffA based on Integer32"""
    defaultValue = 366

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            366
        )
    )
    namedValues = NamedValues(
        ("default", 366)
    )


_DsShdslEncodeCoeffA_Type.__name__ = "Integer32"
_DsShdslEncodeCoeffA_Object = MibTableColumn
dsShdslEncodeCoeffA = _DsShdslEncodeCoeffA_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 6),
    _DsShdslEncodeCoeffA_Type()
)
dsShdslEncodeCoeffA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslEncodeCoeffA.setStatus("current")


class _DsShdslEncodeCoeffB_Type(Integer32):
    """Custom type dsShdslEncodeCoeffB based on Integer32"""
    defaultValue = 817

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            817
        )
    )
    namedValues = NamedValues(
        ("default", 817)
    )


_DsShdslEncodeCoeffB_Type.__name__ = "Integer32"
_DsShdslEncodeCoeffB_Object = MibTableColumn
dsShdslEncodeCoeffB = _DsShdslEncodeCoeffB_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 7),
    _DsShdslEncodeCoeffB_Type()
)
dsShdslEncodeCoeffB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslEncodeCoeffB.setStatus("current")


class _DsShdslTxEOCBufferLen_Type(Integer32):
    """Custom type dsShdslTxEOCBufferLen based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable10", 10),
          ("dsShdslLineParamsTable15", 15),
          ("dsShdslLineParamsTable20", 20),
          ("dsShdslLineParamsTable25", 25),
          ("dsShdslLineParamsTable30", 30),
          ("dsShdslLineParamsTable35", 35),
          ("dsShdslLineParamsTable40", 40),
          ("dsShdslLineParamsTable45", 45),
          ("dsShdslLineParamsTable50", 50),
          ("dsShdslLineParamsTable55", 55),
          ("dsShdslLineParamsTable60", 60))
    )


_DsShdslTxEOCBufferLen_Type.__name__ = "Integer32"
_DsShdslTxEOCBufferLen_Object = MibTableColumn
dsShdslTxEOCBufferLen = _DsShdslTxEOCBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 8),
    _DsShdslTxEOCBufferLen_Type()
)
dsShdslTxEOCBufferLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTxEOCBufferLen.setStatus("current")


class _DsShdslRxEOCBufferLen_Type(Integer32):
    """Custom type dsShdslRxEOCBufferLen based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              50,
              55,
              60)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable10", 10),
          ("dsShdslLineParamsTable15", 15),
          ("dsShdslLineParamsTable20", 20),
          ("dsShdslLineParamsTable25", 25),
          ("dsShdslLineParamsTable30", 30),
          ("dsShdslLineParamsTable35", 35),
          ("dsShdslLineParamsTable40", 40),
          ("dsShdslLineParamsTable45", 45),
          ("dsShdslLineParamsTable50", 50),
          ("dsShdslLineParamsTable55", 55),
          ("dsShdslLineParamsTable60", 60))
    )


_DsShdslRxEOCBufferLen_Type.__name__ = "Integer32"
_DsShdslRxEOCBufferLen_Object = MibTableColumn
dsShdslRxEOCBufferLen = _DsShdslRxEOCBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 9),
    _DsShdslRxEOCBufferLen_Type()
)
dsShdslRxEOCBufferLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxEOCBufferLen.setStatus("current")


class _DsShdslNTR_Type(Integer32):
    """Custom type dsShdslNTR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("refClkIp8k", 2),
          ("refClkOp4096k", 4))
    )


_DsShdslNTR_Type.__name__ = "Integer32"
_DsShdslNTR_Object = MibTableColumn
dsShdslNTR = _DsShdslNTR_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 10),
    _DsShdslNTR_Type()
)
dsShdslNTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslNTR.setStatus("current")


class _DsShdslRxUpstreamFrameSync_Type(Integer32):
    """Custom type dsShdslRxUpstreamFrameSync based on Integer32"""
    defaultValue = 13727


_DsShdslRxUpstreamFrameSync_Type.__name__ = "Integer32"
_DsShdslRxUpstreamFrameSync_Object = MibTableColumn
dsShdslRxUpstreamFrameSync = _DsShdslRxUpstreamFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 11),
    _DsShdslRxUpstreamFrameSync_Type()
)
dsShdslRxUpstreamFrameSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxUpstreamFrameSync.setStatus("current")


class _DsShdslRxDownstreamFrameSync_Type(Integer32):
    """Custom type dsShdslRxDownstreamFrameSync based on Integer32"""
    defaultValue = 13727


_DsShdslRxDownstreamFrameSync_Type.__name__ = "Integer32"
_DsShdslRxDownstreamFrameSync_Object = MibTableColumn
dsShdslRxDownstreamFrameSync = _DsShdslRxDownstreamFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 12),
    _DsShdslRxDownstreamFrameSync_Type()
)
dsShdslRxDownstreamFrameSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxDownstreamFrameSync.setStatus("current")


class _DsShdslRxUpstreamStuffBits_Type(Integer32):
    """Custom type dsShdslRxUpstreamStuffBits based on Integer32"""
    defaultValue = 15


_DsShdslRxUpstreamStuffBits_Type.__name__ = "Integer32"
_DsShdslRxUpstreamStuffBits_Object = MibTableColumn
dsShdslRxUpstreamStuffBits = _DsShdslRxUpstreamStuffBits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 13),
    _DsShdslRxUpstreamStuffBits_Type()
)
dsShdslRxUpstreamStuffBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxUpstreamStuffBits.setStatus("current")


class _DsShdslRxDownstreamStuffBits_Type(Integer32):
    """Custom type dsShdslRxDownstreamStuffBits based on Integer32"""
    defaultValue = 15


_DsShdslRxDownstreamStuffBits_Type.__name__ = "Integer32"
_DsShdslRxDownstreamStuffBits_Object = MibTableColumn
dsShdslRxDownstreamStuffBits = _DsShdslRxDownstreamStuffBits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 14),
    _DsShdslRxDownstreamStuffBits_Type()
)
dsShdslRxDownstreamStuffBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxDownstreamStuffBits.setStatus("current")


class _DsShdslInitiate_Type(Integer32):
    """Custom type dsShdslInitiate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("co", 1),
          ("cpe", 2))
    )


_DsShdslInitiate_Type.__name__ = "Integer32"
_DsShdslInitiate_Object = MibTableColumn
dsShdslInitiate = _DsShdslInitiate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 15),
    _DsShdslInitiate_Type()
)
dsShdslInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslInitiate.setStatus("current")


class _DsShdslFramerRxClockMode_Type(Integer32):
    """Custom type dsShdslFramerRxClockMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slave", 2),
          ("internal", 3))
    )


_DsShdslFramerRxClockMode_Type.__name__ = "Integer32"
_DsShdslFramerRxClockMode_Object = MibTableColumn
dsShdslFramerRxClockMode = _DsShdslFramerRxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 16),
    _DsShdslFramerRxClockMode_Type()
)
dsShdslFramerRxClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslFramerRxClockMode.setStatus("current")


class _DsShdslFramerRxPllMode_Type(Integer32):
    """Custom type dsShdslFramerRxPllMode based on Integer32"""
    defaultValue = 0

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


_DsShdslFramerRxPllMode_Type.__name__ = "Integer32"
_DsShdslFramerRxPllMode_Object = MibTableColumn
dsShdslFramerRxPllMode = _DsShdslFramerRxPllMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 17),
    _DsShdslFramerRxPllMode_Type()
)
dsShdslFramerRxPllMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslFramerRxPllMode.setStatus("current")


class _DsShdslSerialAtmCiuBufferSize_Type(Integer32):
    """Custom type dsShdslSerialAtmCiuBufferSize based on Integer32"""
    defaultValue = 53

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              53)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable24", 24),
          ("dsShdslLineParamsTable53", 53))
    )


_DsShdslSerialAtmCiuBufferSize_Type.__name__ = "Integer32"
_DsShdslSerialAtmCiuBufferSize_Object = MibTableColumn
dsShdslSerialAtmCiuBufferSize = _DsShdslSerialAtmCiuBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 18),
    _DsShdslSerialAtmCiuBufferSize_Type()
)
dsShdslSerialAtmCiuBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSerialAtmCiuBufferSize.setStatus("current")
_DsShdslUtopiaL2TxAddress_Type = Integer32
_DsShdslUtopiaL2TxAddress_Object = MibTableColumn
dsShdslUtopiaL2TxAddress = _DsShdslUtopiaL2TxAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 19),
    _DsShdslUtopiaL2TxAddress_Type()
)
dsShdslUtopiaL2TxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaL2TxAddress.setStatus("current")
_DsShdslUtopiaL2RxAddress_Type = Integer32
_DsShdslUtopiaL2RxAddress_Object = MibTableColumn
dsShdslUtopiaL2RxAddress = _DsShdslUtopiaL2RxAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 20),
    _DsShdslUtopiaL2RxAddress_Type()
)
dsShdslUtopiaL2RxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaL2RxAddress.setStatus("current")


class _DsShdslTxFramerPulseDelay_Type(Integer32):
    """Custom type dsShdslTxFramerPulseDelay based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable0", 0),
          ("dsShdslLineParamsTable1", 1),
          ("dsShdslLineParamsTable2", 2),
          ("dsShdslLineParamsTable3", 3),
          ("dsShdslLineParamsTable4", 4),
          ("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable6", 6),
          ("dsShdslLineParamsTable7", 7))
    )


_DsShdslTxFramerPulseDelay_Type.__name__ = "Integer32"
_DsShdslTxFramerPulseDelay_Object = MibTableColumn
dsShdslTxFramerPulseDelay = _DsShdslTxFramerPulseDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 21),
    _DsShdslTxFramerPulseDelay_Type()
)
dsShdslTxFramerPulseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTxFramerPulseDelay.setStatus("current")


class _DsShdslRxFramerPulseDelay_Type(Integer32):
    """Custom type dsShdslRxFramerPulseDelay based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable0", 0),
          ("dsShdslLineParamsTable1", 1),
          ("dsShdslLineParamsTable2", 2),
          ("dsShdslLineParamsTable3", 3),
          ("dsShdslLineParamsTable4", 4),
          ("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable6", 6),
          ("dsShdslLineParamsTable7", 7))
    )


_DsShdslRxFramerPulseDelay_Type.__name__ = "Integer32"
_DsShdslRxFramerPulseDelay_Object = MibTableColumn
dsShdslRxFramerPulseDelay = _DsShdslRxFramerPulseDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 22),
    _DsShdslRxFramerPulseDelay_Type()
)
dsShdslRxFramerPulseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxFramerPulseDelay.setStatus("current")


class _DsShdslMultiFrameMode_Type(Integer32):
    """Custom type dsShdslMultiFrameMode based on Integer32"""
    defaultValue = 0

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


_DsShdslMultiFrameMode_Type.__name__ = "Integer32"
_DsShdslMultiFrameMode_Object = MibTableColumn
dsShdslMultiFrameMode = _DsShdslMultiFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 23),
    _DsShdslMultiFrameMode_Type()
)
dsShdslMultiFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslMultiFrameMode.setStatus("current")


class _DsShdslEnable4or6MbpsBitrate_Type(Integer32):
    """Custom type dsShdslEnable4or6MbpsBitrate based on Integer32"""
    defaultValue = 0

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


_DsShdslEnable4or6MbpsBitrate_Type.__name__ = "Integer32"
_DsShdslEnable4or6MbpsBitrate_Object = MibTableColumn
dsShdslEnable4or6MbpsBitrate = _DsShdslEnable4or6MbpsBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 24),
    _DsShdslEnable4or6MbpsBitrate_Type()
)
dsShdslEnable4or6MbpsBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslEnable4or6MbpsBitrate.setStatus("current")


class _DsShdslTomDataWord1_Type(Integer32):
    """Custom type dsShdslTomDataWord1 based on Integer32"""
    defaultValue = 0


_DsShdslTomDataWord1_Type.__name__ = "Integer32"
_DsShdslTomDataWord1_Object = MibTableColumn
dsShdslTomDataWord1 = _DsShdslTomDataWord1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 25),
    _DsShdslTomDataWord1_Type()
)
dsShdslTomDataWord1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTomDataWord1.setStatus("current")


class _DsShdslTomDataWord2_Type(Integer32):
    """Custom type dsShdslTomDataWord2 based on Integer32"""
    defaultValue = 0


_DsShdslTomDataWord2_Type.__name__ = "Integer32"
_DsShdslTomDataWord2_Object = MibTableColumn
dsShdslTomDataWord2 = _DsShdslTomDataWord2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 26),
    _DsShdslTomDataWord2_Type()
)
dsShdslTomDataWord2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTomDataWord2.setStatus("current")


class _DsShdslTomDataWord3_Type(Integer32):
    """Custom type dsShdslTomDataWord3 based on Integer32"""
    defaultValue = 0


_DsShdslTomDataWord3_Type.__name__ = "Integer32"
_DsShdslTomDataWord3_Object = MibTableColumn
dsShdslTomDataWord3 = _DsShdslTomDataWord3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 27),
    _DsShdslTomDataWord3_Type()
)
dsShdslTomDataWord3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTomDataWord3.setStatus("current")


class _DsShdslTomDataWord4_Type(Integer32):
    """Custom type dsShdslTomDataWord4 based on Integer32"""
    defaultValue = 0


_DsShdslTomDataWord4_Type.__name__ = "Integer32"
_DsShdslTomDataWord4_Object = MibTableColumn
dsShdslTomDataWord4 = _DsShdslTomDataWord4_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 28),
    _DsShdslTomDataWord4_Type()
)
dsShdslTomDataWord4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTomDataWord4.setStatus("current")


class _DsShdslSetReqSilenceMode_Type(Integer32):
    """Custom type dsShdslSetReqSilenceMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 4))
    )


_DsShdslSetReqSilenceMode_Type.__name__ = "Integer32"
_DsShdslSetReqSilenceMode_Object = MibTableColumn
dsShdslSetReqSilenceMode = _DsShdslSetReqSilenceMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 29),
    _DsShdslSetReqSilenceMode_Type()
)
dsShdslSetReqSilenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSetReqSilenceMode.setStatus("current")


class _DsShdslSetIndividualRates1_Type(Integer32):
    """Custom type dsShdslSetIndividualRates1 based on Integer32"""
    defaultValue = 65535


_DsShdslSetIndividualRates1_Type.__name__ = "Integer32"
_DsShdslSetIndividualRates1_Object = MibTableColumn
dsShdslSetIndividualRates1 = _DsShdslSetIndividualRates1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 30),
    _DsShdslSetIndividualRates1_Type()
)
dsShdslSetIndividualRates1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSetIndividualRates1.setStatus("current")


class _DsShdslSetIndividualRates2_Type(Integer32):
    """Custom type dsShdslSetIndividualRates2 based on Integer32"""
    defaultValue = 65535


_DsShdslSetIndividualRates2_Type.__name__ = "Integer32"
_DsShdslSetIndividualRates2_Object = MibTableColumn
dsShdslSetIndividualRates2 = _DsShdslSetIndividualRates2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 31),
    _DsShdslSetIndividualRates2_Type()
)
dsShdslSetIndividualRates2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSetIndividualRates2.setStatus("current")


class _DsShdslSetIndividualRates3_Type(Integer32):
    """Custom type dsShdslSetIndividualRates3 based on Integer32"""
    defaultValue = 15


_DsShdslSetIndividualRates3_Type.__name__ = "Integer32"
_DsShdslSetIndividualRates3_Object = MibTableColumn
dsShdslSetIndividualRates3 = _DsShdslSetIndividualRates3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 32),
    _DsShdslSetIndividualRates3_Type()
)
dsShdslSetIndividualRates3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSetIndividualRates3.setStatus("current")


class _DsShdslSatmCellDelineation_Type(Integer32):
    """Custom type dsShdslSatmCellDelineation based on Integer32"""
    defaultValue = 0

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


_DsShdslSatmCellDelineation_Type.__name__ = "Integer32"
_DsShdslSatmCellDelineation_Object = MibTableColumn
dsShdslSatmCellDelineation = _DsShdslSatmCellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 33),
    _DsShdslSatmCellDelineation_Type()
)
dsShdslSatmCellDelineation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSatmCellDelineation.setStatus("current")


class _DsShdslFramerCellDropOnError_Type(Integer32):
    """Custom type dsShdslFramerCellDropOnError based on Integer32"""
    defaultValue = 0

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


_DsShdslFramerCellDropOnError_Type.__name__ = "Integer32"
_DsShdslFramerCellDropOnError_Object = MibTableColumn
dsShdslFramerCellDropOnError = _DsShdslFramerCellDropOnError_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 34),
    _DsShdslFramerCellDropOnError_Type()
)
dsShdslFramerCellDropOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslFramerCellDropOnError.setStatus("current")


class _DsShdslGearShiftType_Type(Integer32):
    """Custom type dsShdslGearShiftType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable0", 0),
          ("dsShdslLineParamsTable1", 1))
    )


_DsShdslGearShiftType_Type.__name__ = "Integer32"
_DsShdslGearShiftType_Object = MibTableColumn
dsShdslGearShiftType = _DsShdslGearShiftType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 35),
    _DsShdslGearShiftType_Type()
)
dsShdslGearShiftType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslGearShiftType.setStatus("current")


class _DsShdslHsNsf_Type(Integer32):
    """Custom type dsShdslHsNsf based on Integer32"""
    defaultValue = 0

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


_DsShdslHsNsf_Type.__name__ = "Integer32"
_DsShdslHsNsf_Object = MibTableColumn
dsShdslHsNsf = _DsShdslHsNsf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 36),
    _DsShdslHsNsf_Type()
)
dsShdslHsNsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsNsf.setStatus("current")


class _DsShdslHsMaxBitsPerBaud_Type(Integer32):
    """Custom type dsShdslHsMaxBitsPerBaud based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable1bits", 1),
          ("dsShdslLineParamsTable2bits", 2),
          ("default", 3))
    )


_DsShdslHsMaxBitsPerBaud_Type.__name__ = "Integer32"
_DsShdslHsMaxBitsPerBaud_Object = MibTableColumn
dsShdslHsMaxBitsPerBaud = _DsShdslHsMaxBitsPerBaud_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 37),
    _DsShdslHsMaxBitsPerBaud_Type()
)
dsShdslHsMaxBitsPerBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsMaxBitsPerBaud.setStatus("current")


class _DsShdslHsCusId_Type(Integer32):
    """Custom type dsShdslHsCusId based on Integer32"""
    defaultValue = 0


_DsShdslHsCusId_Type.__name__ = "Integer32"
_DsShdslHsCusId_Object = MibTableColumn
dsShdslHsCusId = _DsShdslHsCusId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 38),
    _DsShdslHsCusId_Type()
)
dsShdslHsCusId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsCusId.setStatus("current")


class _DsShdslHsCusData0_Type(Integer32):
    """Custom type dsShdslHsCusData0 based on Integer32"""
    defaultValue = 0


_DsShdslHsCusData0_Type.__name__ = "Integer32"
_DsShdslHsCusData0_Object = MibTableColumn
dsShdslHsCusData0 = _DsShdslHsCusData0_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 39),
    _DsShdslHsCusData0_Type()
)
dsShdslHsCusData0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsCusData0.setStatus("current")


class _DsShdslHsCusData1_Type(Integer32):
    """Custom type dsShdslHsCusData1 based on Integer32"""
    defaultValue = 0


_DsShdslHsCusData1_Type.__name__ = "Integer32"
_DsShdslHsCusData1_Object = MibTableColumn
dsShdslHsCusData1 = _DsShdslHsCusData1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 40),
    _DsShdslHsCusData1_Type()
)
dsShdslHsCusData1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsCusData1.setStatus("current")


class _DsShdslHsAnnexBType_Type(Integer32):
    """Custom type dsShdslHsAnnexBType based on Integer32"""
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
        *(("default", 1),
          ("anfp", 2),
          ("annexbOrAnfp", 3))
    )


_DsShdslHsAnnexBType_Type.__name__ = "Integer32"
_DsShdslHsAnnexBType_Object = MibTableColumn
dsShdslHsAnnexBType = _DsShdslHsAnnexBType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 41),
    _DsShdslHsAnnexBType_Type()
)
dsShdslHsAnnexBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslHsAnnexBType.setStatus("current")


class _DsShdslAutoRetrain_Type(Integer32):
    """Custom type dsShdslAutoRetrain based on Integer32"""
    defaultValue = 0

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


_DsShdslAutoRetrain_Type.__name__ = "Integer32"
_DsShdslAutoRetrain_Object = MibTableColumn
dsShdslAutoRetrain = _DsShdslAutoRetrain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 42),
    _DsShdslAutoRetrain_Type()
)
dsShdslAutoRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslAutoRetrain.setStatus("current")


class _DsShdslArCrcCheck_Type(Integer32):
    """Custom type dsShdslArCrcCheck based on Integer32"""
    defaultValue = 0

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


_DsShdslArCrcCheck_Type.__name__ = "Integer32"
_DsShdslArCrcCheck_Object = MibTableColumn
dsShdslArCrcCheck = _DsShdslArCrcCheck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 43),
    _DsShdslArCrcCheck_Type()
)
dsShdslArCrcCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArCrcCheck.setStatus("current")


class _DsShdslArFramerSyncCheck_Type(Integer32):
    """Custom type dsShdslArFramerSyncCheck based on Integer32"""
    defaultValue = 0

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


_DsShdslArFramerSyncCheck_Type.__name__ = "Integer32"
_DsShdslArFramerSyncCheck_Object = MibTableColumn
dsShdslArFramerSyncCheck = _DsShdslArFramerSyncCheck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 44),
    _DsShdslArFramerSyncCheck_Type()
)
dsShdslArFramerSyncCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArFramerSyncCheck.setStatus("current")


class _DsShdslArSnrMarginCheck_Type(Integer32):
    """Custom type dsShdslArSnrMarginCheck based on Integer32"""
    defaultValue = 0

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


_DsShdslArSnrMarginCheck_Type.__name__ = "Integer32"
_DsShdslArSnrMarginCheck_Object = MibTableColumn
dsShdslArSnrMarginCheck = _DsShdslArSnrMarginCheck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 45),
    _DsShdslArSnrMarginCheck_Type()
)
dsShdslArSnrMarginCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArSnrMarginCheck.setStatus("current")


class _DsShdslArCrcThreshold_Type(Integer32):
    """Custom type dsShdslArCrcThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DsShdslArCrcThreshold_Type.__name__ = "Integer32"
_DsShdslArCrcThreshold_Object = MibTableColumn
dsShdslArCrcThreshold = _DsShdslArCrcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 46),
    _DsShdslArCrcThreshold_Type()
)
dsShdslArCrcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArCrcThreshold.setStatus("current")


class _DsShdslArSnrMarginThreshold_Type(Integer32):
    """Custom type dsShdslArSnrMarginThreshold based on Integer32"""
    defaultValue = 1

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
        *(("dsShdslLineParamsTable1", 1),
          ("dsShdslLineParamsTable2", 2),
          ("dsShdslLineParamsTable3", 3),
          ("dsShdslLineParamsTable4", 4),
          ("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable6", 6))
    )


_DsShdslArSnrMarginThreshold_Type.__name__ = "Integer32"
_DsShdslArSnrMarginThreshold_Object = MibTableColumn
dsShdslArSnrMarginThreshold = _DsShdslArSnrMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 47),
    _DsShdslArSnrMarginThreshold_Type()
)
dsShdslArSnrMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArSnrMarginThreshold.setStatus("current")


class _DsShdslArRetrainTime_Type(Integer32):
    """Custom type dsShdslArRetrainTime based on Integer32"""
    defaultValue = 3

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsShdslLineParamsTable1", 1),
          ("dsShdslLineParamsTable2", 2),
          ("dsShdslLineParamsTable3", 3),
          ("dsShdslLineParamsTable4", 4),
          ("dsShdslLineParamsTable5", 5),
          ("dsShdslLineParamsTable6", 6),
          ("dsShdslLineParamsTable7", 7),
          ("dsShdslLineParamsTable8", 8),
          ("dsShdslLineParamsTable9", 9),
          ("dsShdslLineParamsTable10", 10))
    )


_DsShdslArRetrainTime_Type.__name__ = "Integer32"
_DsShdslArRetrainTime_Object = MibTableColumn
dsShdslArRetrainTime = _DsShdslArRetrainTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 48),
    _DsShdslArRetrainTime_Type()
)
dsShdslArRetrainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslArRetrainTime.setStatus("current")


class _DsShdslOpStateTrapEnable_Type(Integer32):
    """Custom type dsShdslOpStateTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsShdslOpStateTrapEnable_Type.__name__ = "Integer32"
_DsShdslOpStateTrapEnable_Object = MibTableColumn
dsShdslOpStateTrapEnable = _DsShdslOpStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 49),
    _DsShdslOpStateTrapEnable_Type()
)
dsShdslOpStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslOpStateTrapEnable.setStatus("current")


class _DsShdslTxFrmrDataClkEdge_Type(Integer32):
    """Custom type dsShdslTxFrmrDataClkEdge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1))
    )


_DsShdslTxFrmrDataClkEdge_Type.__name__ = "Integer32"
_DsShdslTxFrmrDataClkEdge_Object = MibTableColumn
dsShdslTxFrmrDataClkEdge = _DsShdslTxFrmrDataClkEdge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 50),
    _DsShdslTxFrmrDataClkEdge_Type()
)
dsShdslTxFrmrDataClkEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTxFrmrDataClkEdge.setStatus("current")


class _DsShdslRxFrmrDataClkEdge_Type(Integer32):
    """Custom type dsShdslRxFrmrDataClkEdge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1))
    )


_DsShdslRxFrmrDataClkEdge_Type.__name__ = "Integer32"
_DsShdslRxFrmrDataClkEdge_Object = MibTableColumn
dsShdslRxFrmrDataClkEdge = _DsShdslRxFrmrDataClkEdge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 51),
    _DsShdslRxFrmrDataClkEdge_Type()
)
dsShdslRxFrmrDataClkEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxFrmrDataClkEdge.setStatus("current")


class _DsShdslTxFrmrPulseClkEdge_Type(Integer32):
    """Custom type dsShdslTxFrmrPulseClkEdge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1))
    )


_DsShdslTxFrmrPulseClkEdge_Type.__name__ = "Integer32"
_DsShdslTxFrmrPulseClkEdge_Object = MibTableColumn
dsShdslTxFrmrPulseClkEdge = _DsShdslTxFrmrPulseClkEdge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 52),
    _DsShdslTxFrmrPulseClkEdge_Type()
)
dsShdslTxFrmrPulseClkEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTxFrmrPulseClkEdge.setStatus("current")


class _DsShdslRxFrmrPulseClkEdge_Type(Integer32):
    """Custom type dsShdslRxFrmrPulseClkEdge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1))
    )


_DsShdslRxFrmrPulseClkEdge_Type.__name__ = "Integer32"
_DsShdslRxFrmrPulseClkEdge_Object = MibTableColumn
dsShdslRxFrmrPulseClkEdge = _DsShdslRxFrmrPulseClkEdge_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 53),
    _DsShdslRxFrmrPulseClkEdge_Type()
)
dsShdslRxFrmrPulseClkEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxFrmrPulseClkEdge.setStatus("current")


class _DsShdslTxFrmrPulseLvl_Type(Integer32):
    """Custom type dsShdslTxFrmrPulseLvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_DsShdslTxFrmrPulseLvl_Type.__name__ = "Integer32"
_DsShdslTxFrmrPulseLvl_Object = MibTableColumn
dsShdslTxFrmrPulseLvl = _DsShdslTxFrmrPulseLvl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 54),
    _DsShdslTxFrmrPulseLvl_Type()
)
dsShdslTxFrmrPulseLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslTxFrmrPulseLvl.setStatus("current")


class _DsShdslRxFrmrPulseLvl_Type(Integer32):
    """Custom type dsShdslRxFrmrPulseLvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_DsShdslRxFrmrPulseLvl_Type.__name__ = "Integer32"
_DsShdslRxFrmrPulseLvl_Object = MibTableColumn
dsShdslRxFrmrPulseLvl = _DsShdslRxFrmrPulseLvl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 55),
    _DsShdslRxFrmrPulseLvl_Type()
)
dsShdslRxFrmrPulseLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslRxFrmrPulseLvl.setStatus("current")


class _DsShdslUtopiaDataBusWidth_Type(Integer32):
    """Custom type dsShdslUtopiaDataBusWidth based on Integer32"""
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
        *(("tx8Rx8", 0),
          ("tx16Rx16", 1),
          ("tx16Rx8", 2),
          ("tx8Rx16", 3))
    )


_DsShdslUtopiaDataBusWidth_Type.__name__ = "Integer32"
_DsShdslUtopiaDataBusWidth_Object = MibTableColumn
dsShdslUtopiaDataBusWidth = _DsShdslUtopiaDataBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 56),
    _DsShdslUtopiaDataBusWidth_Type()
)
dsShdslUtopiaDataBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslUtopiaDataBusWidth.setStatus("current")


class _DsShdslFrmrOH_Type(Integer32):
    """Custom type dsShdslFrmrOH based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsShdslFrmrOH_Type.__name__ = "Integer32"
_DsShdslFrmrOH_Object = MibTableColumn
dsShdslFrmrOH = _DsShdslFrmrOH_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 57),
    _DsShdslFrmrOH_Type()
)
dsShdslFrmrOH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslFrmrOH.setStatus("current")


class _DsShdslLoopAttenCrossingTrapEnable_Type(Integer32):
    """Custom type dsShdslLoopAttenCrossingTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsShdslLoopAttenCrossingTrapEnable_Type.__name__ = "Integer32"
_DsShdslLoopAttenCrossingTrapEnable_Object = MibTableColumn
dsShdslLoopAttenCrossingTrapEnable = _DsShdslLoopAttenCrossingTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 58),
    _DsShdslLoopAttenCrossingTrapEnable_Type()
)
dsShdslLoopAttenCrossingTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslLoopAttenCrossingTrapEnable.setStatus("current")


class _DsShdslSNRMarginCrossingTrapEnable_Type(Integer32):
    """Custom type dsShdslSNRMarginCrossingTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsShdslSNRMarginCrossingTrapEnable_Type.__name__ = "Integer32"
_DsShdslSNRMarginCrossingTrapEnable_Object = MibTableColumn
dsShdslSNRMarginCrossingTrapEnable = _DsShdslSNRMarginCrossingTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 59),
    _DsShdslSNRMarginCrossingTrapEnable_Type()
)
dsShdslSNRMarginCrossingTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslSNRMarginCrossingTrapEnable.setStatus("current")


class _DsShdslFramerOHAndDefectsTrapEnable_Type(Integer32):
    """Custom type dsShdslFramerOHAndDefectsTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DsShdslFramerOHAndDefectsTrapEnable_Type.__name__ = "Integer32"
_DsShdslFramerOHAndDefectsTrapEnable_Object = MibTableColumn
dsShdslFramerOHAndDefectsTrapEnable = _DsShdslFramerOHAndDefectsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 60),
    _DsShdslFramerOHAndDefectsTrapEnable_Type()
)
dsShdslFramerOHAndDefectsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslFramerOHAndDefectsTrapEnable.setStatus("current")


class _DsShdslParametricTestInputFile_Type(DisplayString):
    """Custom type dsShdslParametricTestInputFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_DsShdslParametricTestInputFile_Type.__name__ = "DisplayString"
_DsShdslParametricTestInputFile_Object = MibTableColumn
dsShdslParametricTestInputFile = _DsShdslParametricTestInputFile_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 61),
    _DsShdslParametricTestInputFile_Type()
)
dsShdslParametricTestInputFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslParametricTestInputFile.setStatus("current")


class _DsShdslParamHybridLossTestStart_Type(Integer32):
    """Custom type dsShdslParamHybridLossTestStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsShdslParamHybridLossTestStart_Type.__name__ = "Integer32"
_DsShdslParamHybridLossTestStart_Object = MibTableColumn
dsShdslParamHybridLossTestStart = _DsShdslParamHybridLossTestStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 62),
    _DsShdslParamHybridLossTestStart_Type()
)
dsShdslParamHybridLossTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslParamHybridLossTestStart.setStatus("current")


class _DsShdslParamHybridLossTestEnd_Type(Integer32):
    """Custom type dsShdslParamHybridLossTestEnd based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsShdslParamHybridLossTestEnd_Type.__name__ = "Integer32"
_DsShdslParamHybridLossTestEnd_Object = MibTableColumn
dsShdslParamHybridLossTestEnd = _DsShdslParamHybridLossTestEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 3, 1, 63),
    _DsShdslParamHybridLossTestEnd_Type()
)
dsShdslParamHybridLossTestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsShdslParamHybridLossTestEnd.setStatus("current")
_DsShdslSpanStatusExtnTable_Object = MibTable
dsShdslSpanStatusExtnTable = _DsShdslSpanStatusExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dsShdslSpanStatusExtnTable.setStatus("current")
_DsShdslSpanStatusExtnEntry_Object = MibTableRow
dsShdslSpanStatusExtnEntry = _DsShdslSpanStatusExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 4, 1)
)
dsShdslSpanStatusExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsShdslSpanStatusExtnEntry.setStatus("current")


class _DsShdslStatusPMMSMaxLineRate_Type(Unsigned32):
    """Custom type dsShdslStatusPMMSMaxLineRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4112000),
    )


_DsShdslStatusPMMSMaxLineRate_Type.__name__ = "Unsigned32"
_DsShdslStatusPMMSMaxLineRate_Object = MibTableColumn
dsShdslStatusPMMSMaxLineRate = _DsShdslStatusPMMSMaxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 4, 1, 1),
    _DsShdslStatusPMMSMaxLineRate_Type()
)
dsShdslStatusPMMSMaxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslStatusPMMSMaxLineRate.setStatus("current")


class _DsShdslStatus4WireHsMode_Type(Integer32):
    """Custom type dsShdslStatus4WireHsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("enhanced", 1))
    )


_DsShdslStatus4WireHsMode_Type.__name__ = "Integer32"
_DsShdslStatus4WireHsMode_Object = MibTableColumn
dsShdslStatus4WireHsMode = _DsShdslStatus4WireHsMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 6, 1, 1, 4, 1, 2),
    _DsShdslStatus4WireHsMode_Type()
)
dsShdslStatus4WireHsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsShdslStatus4WireHsMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-SHDSL-MIB",
    **{"dasanShdslMIB": dasanShdslMIB,
       "dasanShdslLineMIB": dasanShdslLineMIB,
       "dasanShdslMIBObjects": dasanShdslMIBObjects,
       "dsShdslCapabilityGroup": dsShdslCapabilityGroup,
       "dsShdslCapabilityLineTxCap": dsShdslCapabilityLineTxCap,
       "dsShdslLineStatusTable": dsShdslLineStatusTable,
       "dsShdslLineStatusEntry": dsShdslLineStatusEntry,
       "dsShdslOpState": dsShdslOpState,
       "dsShdslStartProgress": dsShdslStartProgress,
       "dsShdslFwRelease": dsShdslFwRelease,
       "dsShdslLineSwap": dsShdslLineSwap,
       "dsShdslRmtCountryCode": dsShdslRmtCountryCode,
       "dsShdslRmtEncoderA": dsShdslRmtEncoderA,
       "dsShdslRmtEncoderB": dsShdslRmtEncoderB,
       "dsShdslRmtProviderCode": dsShdslRmtProviderCode,
       "dsShdslLocDetect": dsShdslLocDetect,
       "dsShdslTxPower": dsShdslTxPower,
       "dsShdslFramerSync": dsShdslFramerSync,
       "dsShdslRmtTomData": dsShdslRmtTomData,
       "dsShdslDriftAlarm": dsShdslDriftAlarm,
       "dsShdslReceiverGain": dsShdslReceiverGain,
       "dsShdslBertError": dsShdslBertError,
       "dsShdslFramerOHAndDefects": dsShdslFramerOHAndDefects,
       "dsShdslRmtFwVersion": dsShdslRmtFwVersion,
       "dsShdslUtopiaCellDelineation": dsShdslUtopiaCellDelineation,
       "dsShdslUtopiaRxCellCnt": dsShdslUtopiaRxCellCnt,
       "dsShdslUtopiaCellDropCnt": dsShdslUtopiaCellDropCnt,
       "dsShdslUtopiaRxHecErrorCnt": dsShdslUtopiaRxHecErrorCnt,
       "dsShdslUtopiaTxCellCnt": dsShdslUtopiaTxCellCnt,
       "dsShdslRmtNsfCusId": dsShdslRmtNsfCusId,
       "dsShdslRmtNsfCusData": dsShdslRmtNsfCusData,
       "dsShdslLocalHandshake": dsShdslLocalHandshake,
       "dsShdslRemoteHandshake": dsShdslRemoteHandshake,
       "dsShdslActualHandshake": dsShdslActualHandshake,
       "dsShdslRmtTxPower": dsShdslRmtTxPower,
       "dsShdslRmtPowerBackoff": dsShdslRmtPowerBackoff,
       "dsShdslAutoRetrainCount": dsShdslAutoRetrainCount,
       "dsShdslEocState": dsShdslEocState,
       "dsShdslFramerOneSecondCnt": dsShdslFramerOneSecondCnt,
       "dsShdslNtrFault": dsShdslNtrFault,
       "dsShdslCpeMasterCore": dsShdslCpeMasterCore,
       "dsShdslParametricTestResult": dsShdslParametricTestResult,
       "dsShdslParametricTestArray": dsShdslParametricTestArray,
       "dsShdslLineParamsTable": dsShdslLineParamsTable,
       "dsShdslLineParamsEntry": dsShdslLineParamsEntry,
       "dsShdslAction": dsShdslAction,
       "dsShdslMode": dsShdslMode,
       "dsShdslPowerScale": dsShdslPowerScale,
       "dsShdslFramerType": dsShdslFramerType,
       "dsShdslAFEType": dsShdslAFEType,
       "dsShdslEncodeCoeffA": dsShdslEncodeCoeffA,
       "dsShdslEncodeCoeffB": dsShdslEncodeCoeffB,
       "dsShdslTxEOCBufferLen": dsShdslTxEOCBufferLen,
       "dsShdslRxEOCBufferLen": dsShdslRxEOCBufferLen,
       "dsShdslNTR": dsShdslNTR,
       "dsShdslRxUpstreamFrameSync": dsShdslRxUpstreamFrameSync,
       "dsShdslRxDownstreamFrameSync": dsShdslRxDownstreamFrameSync,
       "dsShdslRxUpstreamStuffBits": dsShdslRxUpstreamStuffBits,
       "dsShdslRxDownstreamStuffBits": dsShdslRxDownstreamStuffBits,
       "dsShdslInitiate": dsShdslInitiate,
       "dsShdslFramerRxClockMode": dsShdslFramerRxClockMode,
       "dsShdslFramerRxPllMode": dsShdslFramerRxPllMode,
       "dsShdslSerialAtmCiuBufferSize": dsShdslSerialAtmCiuBufferSize,
       "dsShdslUtopiaL2TxAddress": dsShdslUtopiaL2TxAddress,
       "dsShdslUtopiaL2RxAddress": dsShdslUtopiaL2RxAddress,
       "dsShdslTxFramerPulseDelay": dsShdslTxFramerPulseDelay,
       "dsShdslRxFramerPulseDelay": dsShdslRxFramerPulseDelay,
       "dsShdslMultiFrameMode": dsShdslMultiFrameMode,
       "dsShdslEnable4or6MbpsBitrate": dsShdslEnable4or6MbpsBitrate,
       "dsShdslTomDataWord1": dsShdslTomDataWord1,
       "dsShdslTomDataWord2": dsShdslTomDataWord2,
       "dsShdslTomDataWord3": dsShdslTomDataWord3,
       "dsShdslTomDataWord4": dsShdslTomDataWord4,
       "dsShdslSetReqSilenceMode": dsShdslSetReqSilenceMode,
       "dsShdslSetIndividualRates1": dsShdslSetIndividualRates1,
       "dsShdslSetIndividualRates2": dsShdslSetIndividualRates2,
       "dsShdslSetIndividualRates3": dsShdslSetIndividualRates3,
       "dsShdslSatmCellDelineation": dsShdslSatmCellDelineation,
       "dsShdslFramerCellDropOnError": dsShdslFramerCellDropOnError,
       "dsShdslGearShiftType": dsShdslGearShiftType,
       "dsShdslHsNsf": dsShdslHsNsf,
       "dsShdslHsMaxBitsPerBaud": dsShdslHsMaxBitsPerBaud,
       "dsShdslHsCusId": dsShdslHsCusId,
       "dsShdslHsCusData0": dsShdslHsCusData0,
       "dsShdslHsCusData1": dsShdslHsCusData1,
       "dsShdslHsAnnexBType": dsShdslHsAnnexBType,
       "dsShdslAutoRetrain": dsShdslAutoRetrain,
       "dsShdslArCrcCheck": dsShdslArCrcCheck,
       "dsShdslArFramerSyncCheck": dsShdslArFramerSyncCheck,
       "dsShdslArSnrMarginCheck": dsShdslArSnrMarginCheck,
       "dsShdslArCrcThreshold": dsShdslArCrcThreshold,
       "dsShdslArSnrMarginThreshold": dsShdslArSnrMarginThreshold,
       "dsShdslArRetrainTime": dsShdslArRetrainTime,
       "dsShdslOpStateTrapEnable": dsShdslOpStateTrapEnable,
       "dsShdslTxFrmrDataClkEdge": dsShdslTxFrmrDataClkEdge,
       "dsShdslRxFrmrDataClkEdge": dsShdslRxFrmrDataClkEdge,
       "dsShdslTxFrmrPulseClkEdge": dsShdslTxFrmrPulseClkEdge,
       "dsShdslRxFrmrPulseClkEdge": dsShdslRxFrmrPulseClkEdge,
       "dsShdslTxFrmrPulseLvl": dsShdslTxFrmrPulseLvl,
       "dsShdslRxFrmrPulseLvl": dsShdslRxFrmrPulseLvl,
       "dsShdslUtopiaDataBusWidth": dsShdslUtopiaDataBusWidth,
       "dsShdslFrmrOH": dsShdslFrmrOH,
       "dsShdslLoopAttenCrossingTrapEnable": dsShdslLoopAttenCrossingTrapEnable,
       "dsShdslSNRMarginCrossingTrapEnable": dsShdslSNRMarginCrossingTrapEnable,
       "dsShdslFramerOHAndDefectsTrapEnable": dsShdslFramerOHAndDefectsTrapEnable,
       "dsShdslParametricTestInputFile": dsShdslParametricTestInputFile,
       "dsShdslParamHybridLossTestStart": dsShdslParamHybridLossTestStart,
       "dsShdslParamHybridLossTestEnd": dsShdslParamHybridLossTestEnd,
       "dsShdslSpanStatusExtnTable": dsShdslSpanStatusExtnTable,
       "dsShdslSpanStatusExtnEntry": dsShdslSpanStatusExtnEntry,
       "dsShdslStatusPMMSMaxLineRate": dsShdslStatusPMMSMaxLineRate,
       "dsShdslStatus4WireHsMode": dsShdslStatus4WireHsMode}
)
