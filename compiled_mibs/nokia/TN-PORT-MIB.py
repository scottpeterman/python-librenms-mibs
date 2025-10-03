# SNMP MIB module (TN-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TN-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:02 2025
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TItemLongDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxEnabledDisabled,
 TmnxPortID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemLongDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxEnabledDisabled",
    "TmnxPortID")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 25)
)
if mibBuilder.loadTexts:
    tnPortMIBModule.setRevisions(
        ("2020-05-01 00:00",
         "2020-01-10 00:00",
         "2019-11-15 00:00",
         "2019-10-25 00:00",
         "2019-06-07 00:00",
         "2019-03-08 00:00",
         "2019-03-01 00:00",
         "2019-02-15 00:00",
         "2019-01-25 00:00",
         "2018-12-28 00:00",
         "2018-12-14 00:00",
         "2018-01-05 00:00",
         "2017-08-02 00:00",
         "2017-05-31 00:00",
         "2017-03-10 00:00",
         "2016-10-19 00:00",
         "2015-09-02 00:00",
         "2015-01-22 00:00",
         "2013-08-22 00:00",
         "2012-12-05 00:00",
         "2012-11-06 00:00",
         "2012-10-12 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-16 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPortOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("diagnosing", 4),
          ("failed", 5))
    )



class TmnxPortEtherReportStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("signalFailure", 1),
          ("remoteFault", 2),
          ("localFault", 3),
          ("noFrameLock", 4),
          ("highBer", 5),
          ("noBlockLock", 6),
          ("noAmLock", 7),
          ("duplicateLane", 8))
    )


class TmnxPortClass(TextualConvention, Integer32):
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
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("faste", 2),
          ("gige", 3),
          ("xgige", 4),
          ("sonet", 5),
          ("vport", 6),
          ("unused", 7),
          ("xcme", 8),
          ("tdm", 9),
          ("xlgige", 10),
          ("cgige", 11),
          ("xcmbar", 12),
          ("oduflex", 13),
          ("vsme", 14),
          ("tfgige", 15),
          ("cpri3", 16),
          ("cpri5", 17),
          ("cpri6", 18),
          ("cpri7", 19),
          ("cpri8", 20),
          ("cpri10", 21),
          ("obsai8", 22),
          ("obsai4", 23),
          ("cpri4", 24))
    )



class TmnxPortConnectorType(TextualConvention, Unsigned32):
    status = "current"


class TmnxPortState(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("ghost", 2),
          ("linkDown", 3),
          ("linkUp", 4),
          ("up", 5),
          ("diagnose", 6))
    )



class TmnxPortType(TextualConvention, Unsigned32):
    status = "current"


class TmnxAlarmState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("alarmActive", 1),
          ("alarmCleared", 2))
    )



class TmnxPortAdminStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("noop", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("diagnose", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnHwObjs_ObjectIdentity = ObjectIdentity
tnHwObjs = _TnHwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2)
)
_TnPortObjs_ObjectIdentity = ObjectIdentity
tnPortObjs = _TnPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4)
)
_TnPortTableLastChange_Type = TimeStamp
_TnPortTableLastChange_Object = MibScalar
tnPortTableLastChange = _TnPortTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 1),
    _TnPortTableLastChange_Type()
)
tnPortTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTableLastChange.setStatus("current")
_TnPortTable_Object = MibTable
tnPortTable = _TnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnPortTable.setStatus("current")
_TnPortEntry_Object = MibTableRow
tnPortEntry = _TnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1)
)
tnPortEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
)
if mibBuilder.loadTexts:
    tnPortEntry.setStatus("current")
_TnPortPortID_Type = TmnxPortID
_TnPortPortID_Object = MibTableColumn
tnPortPortID = _TnPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 1),
    _TnPortPortID_Type()
)
tnPortPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortPortID.setStatus("current")
_TnPortLastChangeTime_Type = TimeStamp
_TnPortLastChangeTime_Object = MibTableColumn
tnPortLastChangeTime = _TnPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 2),
    _TnPortLastChangeTime_Type()
)
tnPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLastChangeTime.setStatus("current")
_TnPortType_Type = TmnxPortType
_TnPortType_Object = MibTableColumn
tnPortType = _TnPortType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 3),
    _TnPortType_Type()
)
tnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortType.setStatus("current")
_TnPortClass_Type = TmnxPortClass
_TnPortClass_Object = MibTableColumn
tnPortClass = _TnPortClass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 4),
    _TnPortClass_Type()
)
tnPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortClass.setStatus("current")


class _TnPortDescription_Type(TItemLongDescription):
    """Custom type tnPortDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TnPortDescription_Type.__name__ = "TItemLongDescription"
_TnPortDescription_Object = MibTableColumn
tnPortDescription = _TnPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 5),
    _TnPortDescription_Type()
)
tnPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortDescription.setStatus("current")
_TnPortName_Type = TNamedItemOrEmpty
_TnPortName_Object = MibTableColumn
tnPortName = _TnPortName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 6),
    _TnPortName_Type()
)
tnPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortName.setStatus("current")


class _TnPortAlias_Type(TNamedItemOrEmpty):
    """Custom type tnPortAlias based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnPortAlias_Type.__name__ = "TNamedItemOrEmpty"
_TnPortAlias_Object = MibTableColumn
tnPortAlias = _TnPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 7),
    _TnPortAlias_Type()
)
tnPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortAlias.setStatus("current")


class _TnPortUserAssignedMac_Type(TruthValue):
    """Custom type tnPortUserAssignedMac based on TruthValue"""
    defaultValue = 2


_TnPortUserAssignedMac_Type.__name__ = "TruthValue"
_TnPortUserAssignedMac_Object = MibTableColumn
tnPortUserAssignedMac = _TnPortUserAssignedMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 8),
    _TnPortUserAssignedMac_Type()
)
tnPortUserAssignedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortUserAssignedMac.setStatus("current")


class _TnPortMacAddress_Type(MacAddress):
    """Custom type tnPortMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnPortMacAddress_Type.__name__ = "MacAddress"
_TnPortMacAddress_Object = MibTableColumn
tnPortMacAddress = _TnPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 9),
    _TnPortMacAddress_Type()
)
tnPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortMacAddress.setStatus("current")
_TnPortHwMacAddress_Type = MacAddress
_TnPortHwMacAddress_Object = MibTableColumn
tnPortHwMacAddress = _TnPortHwMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 10),
    _TnPortHwMacAddress_Type()
)
tnPortHwMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortHwMacAddress.setStatus("current")


class _TnPortMode_Type(Integer32):
    """Custom type tnPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("access", 1),
          ("network", 2))
    )


_TnPortMode_Type.__name__ = "Integer32"
_TnPortMode_Object = MibTableColumn
tnPortMode = _TnPortMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 11),
    _TnPortMode_Type()
)
tnPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortMode.setStatus("current")


class _TnPortEncapType_Type(Integer32):
    """Custom type tnPortEncapType based on Integer32"""
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
        *(("unknown", 0),
          ("nullEncap", 1),
          ("qEncap", 2),
          ("mplsEncap", 3),
          ("bcpNullEncap", 4),
          ("bcpDot1qEncap", 5),
          ("ipcpEncap", 6),
          ("frEncap", 7),
          ("pppAutoEncap", 8),
          ("atmEncap", 9),
          ("qinqEncap", 10),
          ("wanMirrorEncap", 11),
          ("ciscoHDLCEncap", 12),
          ("cemEncap", 13))
    )


_TnPortEncapType_Type.__name__ = "Integer32"
_TnPortEncapType_Object = MibTableColumn
tnPortEncapType = _TnPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 12),
    _TnPortEncapType_Type()
)
tnPortEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEncapType.setStatus("current")


class _TnPortLagId_Type(Unsigned32):
    """Custom type tnPortLagId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TnPortLagId_Type.__name__ = "Unsigned32"
_TnPortLagId_Object = MibTableColumn
tnPortLagId = _TnPortLagId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 13),
    _TnPortLagId_Type()
)
tnPortLagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLagId.setStatus("current")


class _TnPortHoldTimeUp_Type(Unsigned32):
    """Custom type tnPortHoldTimeUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_TnPortHoldTimeUp_Type.__name__ = "Unsigned32"
_TnPortHoldTimeUp_Object = MibTableColumn
tnPortHoldTimeUp = _TnPortHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 14),
    _TnPortHoldTimeUp_Type()
)
tnPortHoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortHoldTimeUp.setStatus("current")


class _TnPortHoldTimeDown_Type(Unsigned32):
    """Custom type tnPortHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_TnPortHoldTimeDown_Type.__name__ = "Unsigned32"
_TnPortHoldTimeDown_Object = MibTableColumn
tnPortHoldTimeDown = _TnPortHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 15),
    _TnPortHoldTimeDown_Type()
)
tnPortHoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortHoldTimeDown.setStatus("current")


class _TnPortUpProtocols_Type(Bits):
    """Custom type tnPortUpProtocols based on Bits"""
    namedValues = NamedValues(
        *(("portUpIpv4", 0),
          ("portUpMpls", 1),
          ("portUpBcp", 2),
          ("portUpIso", 3),
          ("portUpFr", 4),
          ("portUpAtm", 5),
          ("portUpChdlc", 6),
          ("portUpIma", 7),
          ("portUpIpv6", 8))
    )

_TnPortUpProtocols_Type.__name__ = "Bits"
_TnPortUpProtocols_Object = MibTableColumn
tnPortUpProtocols = _TnPortUpProtocols_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 16),
    _TnPortUpProtocols_Type()
)
tnPortUpProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortUpProtocols.setStatus("current")
_TnPortConnectorType_Type = TmnxPortConnectorType
_TnPortConnectorType_Object = MibTableColumn
tnPortConnectorType = _TnPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 17),
    _TnPortConnectorType_Type()
)
tnPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortConnectorType.setStatus("current")


class _TnPortTransceiverType_Type(Integer32):
    """Custom type tnPortTransceiverType based on Integer32"""
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
              130)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gbic", 1),
          ("moduleConnectorSolderedToMotherboard", 2),
          ("sfpTransceiver", 3),
          ("xbiTransceiver", 4),
          ("xenpakTransceiver", 5),
          ("xfpTransceiver", 6),
          ("xffTransceiver", 7),
          ("xfpeTransceiver", 8),
          ("xpakTransceiver", 9),
          ("x2Transceiver", 10),
          ("dwdmSfpTransceiver", 11),
          ("qsfpTransceiver", 12),
          ("qsfpPlusTransceiver", 13),
          ("cfpTransceiver", 14),
          ("shieldedMiniMultilaneHd4x", 15),
          ("shieldedMiniMultilaneHd8x", 16),
          ("qsfp28Transceiver", 17),
          ("cfp4Transceiver", 18),
          ("cdfpStyle1or2Transceiver", 19),
          ("shieldedMiniMultilaneHd4xFc", 20),
          ("shieldedMiniMultilaneHd8xFc", 21),
          ("cdfpStyle3Transceiver", 22),
          ("microQsfpTransceiver", 23),
          ("qsfpDd8xTransceiver", 24),
          ("osfp8xTransceiver", 25),
          ("sfpDd2xTransceiver", 26),
          ("tsopSmartSfpTransceiver", 130))
    )


_TnPortTransceiverType_Type.__name__ = "Integer32"
_TnPortTransceiverType_Object = MibTableColumn
tnPortTransceiverType = _TnPortTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 25),
    _TnPortTransceiverType_Type()
)
tnPortTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTransceiverType.setStatus("current")
_TnPortTransceiverLaserWaveLen_Type = Unsigned32
_TnPortTransceiverLaserWaveLen_Object = MibTableColumn
tnPortTransceiverLaserWaveLen = _TnPortTransceiverLaserWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 27),
    _TnPortTransceiverLaserWaveLen_Type()
)
tnPortTransceiverLaserWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTransceiverLaserWaveLen.setStatus("current")


class _TnPortTransceiverDiagCapable_Type(Integer32):
    """Custom type tnPortTransceiverDiagCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("true", 1),
          ("false", 2))
    )


_TnPortTransceiverDiagCapable_Type.__name__ = "Integer32"
_TnPortTransceiverDiagCapable_Object = MibTableColumn
tnPortTransceiverDiagCapable = _TnPortTransceiverDiagCapable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 28),
    _TnPortTransceiverDiagCapable_Type()
)
tnPortTransceiverDiagCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTransceiverDiagCapable.setStatus("current")
_TnPortTransceiverModelNumber_Type = TNamedItemOrEmpty
_TnPortTransceiverModelNumber_Object = MibTableColumn
tnPortTransceiverModelNumber = _TnPortTransceiverModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 29),
    _TnPortTransceiverModelNumber_Type()
)
tnPortTransceiverModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTransceiverModelNumber.setStatus("current")


class _TnPortSFPConnectorCode_Type(Integer32):
    """Custom type tnPortSFPConnectorCode based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              128)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sc", 1),
          ("fiberChannel-Style1-CopperConnector", 2),
          ("fiberChannel-Style2-CopperConnector", 3),
          ("bncortnc", 4),
          ("fiberChannelCoaxialHeaders", 5),
          ("fiberJack", 6),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("sg", 10),
          ("opticalPigtail", 11),
          ("mpo1x12", 12),
          ("mpo2x16", 13),
          ("hssdcII", 32),
          ("copperPigtail", 33),
          ("rj45", 34),
          ("noSeparableConnector", 35),
          ("mxc2x16", 36),
          ("csOptical", 37),
          ("miniCsOptical", 38),
          ("copperGigE", 128))
    )


_TnPortSFPConnectorCode_Type.__name__ = "Integer32"
_TnPortSFPConnectorCode_Object = MibTableColumn
tnPortSFPConnectorCode = _TnPortSFPConnectorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 30),
    _TnPortSFPConnectorCode_Type()
)
tnPortSFPConnectorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPConnectorCode.setStatus("current")
_TnPortSFPVendorOUI_Type = Unsigned32
_TnPortSFPVendorOUI_Object = MibTableColumn
tnPortSFPVendorOUI = _TnPortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 31),
    _TnPortSFPVendorOUI_Type()
)
tnPortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPVendorOUI.setStatus("current")
_TnPortSFPVendorManufactureDate_Type = DateAndTime
_TnPortSFPVendorManufactureDate_Object = MibTableColumn
tnPortSFPVendorManufactureDate = _TnPortSFPVendorManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 32),
    _TnPortSFPVendorManufactureDate_Type()
)
tnPortSFPVendorManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPVendorManufactureDate.setStatus("current")


class _TnPortSFPMedia_Type(Integer32):
    """Custom type tnPortSFPMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ethernet", 1),
          ("sonetsdh", 2))
    )


_TnPortSFPMedia_Type.__name__ = "Integer32"
_TnPortSFPMedia_Object = MibTableColumn
tnPortSFPMedia = _TnPortSFPMedia_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 33),
    _TnPortSFPMedia_Type()
)
tnPortSFPMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPMedia.setStatus("current")
_TnPortSFPEquipped_Type = TruthValue
_TnPortSFPEquipped_Object = MibTableColumn
tnPortSFPEquipped = _TnPortSFPEquipped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 34),
    _TnPortSFPEquipped_Type()
)
tnPortSFPEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPEquipped.setStatus("current")
_TnPortEquipped_Type = TruthValue
_TnPortEquipped_Object = MibTableColumn
tnPortEquipped = _TnPortEquipped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 35),
    _TnPortEquipped_Type()
)
tnPortEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEquipped.setStatus("current")
_TnPortLinkStatus_Type = TruthValue
_TnPortLinkStatus_Object = MibTableColumn
tnPortLinkStatus = _TnPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 36),
    _TnPortLinkStatus_Type()
)
tnPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLinkStatus.setStatus("current")


class _TnPortAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tnPortAdminStatus based on TmnxPortAdminStatus"""
    defaultValue = 2


_TnPortAdminStatus_Type.__name__ = "TmnxPortAdminStatus"
_TnPortAdminStatus_Object = MibTableColumn
tnPortAdminStatus = _TnPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 37),
    _TnPortAdminStatus_Type()
)
tnPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortAdminStatus.setStatus("current")
_TnPortOperStatus_Type = TmnxPortOperStatus
_TnPortOperStatus_Object = MibTableColumn
tnPortOperStatus = _TnPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 38),
    _TnPortOperStatus_Type()
)
tnPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortOperStatus.setStatus("current")
_TnPortState_Type = TmnxPortState
_TnPortState_Object = MibTableColumn
tnPortState = _TnPortState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 39),
    _TnPortState_Type()
)
tnPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortState.setStatus("current")
_TnPortPrevState_Type = TmnxPortState
_TnPortPrevState_Object = MibTableColumn
tnPortPrevState = _TnPortPrevState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 40),
    _TnPortPrevState_Type()
)
tnPortPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortPrevState.setStatus("current")
_TnPortNumAlarms_Type = Unsigned32
_TnPortNumAlarms_Object = MibTableColumn
tnPortNumAlarms = _TnPortNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 41),
    _TnPortNumAlarms_Type()
)
tnPortNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNumAlarms.setStatus("current")
_TnPortAlarmState_Type = TmnxAlarmState
_TnPortAlarmState_Object = MibTableColumn
tnPortAlarmState = _TnPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 42),
    _TnPortAlarmState_Type()
)
tnPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortAlarmState.setStatus("current")
_TnPortLastAlarmEvent_Type = RowPointer
_TnPortLastAlarmEvent_Object = MibTableColumn
tnPortLastAlarmEvent = _TnPortLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 43),
    _TnPortLastAlarmEvent_Type()
)
tnPortLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLastAlarmEvent.setStatus("current")


class _TnPortClearAlarms_Type(TmnxActionType):
    """Custom type tnPortClearAlarms based on TmnxActionType"""
    defaultValue = 2


_TnPortClearAlarms_Type.__name__ = "TmnxActionType"
_TnPortClearAlarms_Object = MibTableColumn
tnPortClearAlarms = _TnPortClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 44),
    _TnPortClearAlarms_Type()
)
tnPortClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortClearAlarms.setStatus("current")
_TnPortSFPVendorSerialNum_Type = TNamedItemOrEmpty
_TnPortSFPVendorSerialNum_Object = MibTableColumn
tnPortSFPVendorSerialNum = _TnPortSFPVendorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 45),
    _TnPortSFPVendorSerialNum_Type()
)
tnPortSFPVendorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPVendorSerialNum.setStatus("current")
_TnPortSFPVendorPartNum_Type = TNamedItemOrEmpty
_TnPortSFPVendorPartNum_Object = MibTableColumn
tnPortSFPVendorPartNum = _TnPortSFPVendorPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 46),
    _TnPortSFPVendorPartNum_Type()
)
tnPortSFPVendorPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPVendorPartNum.setStatus("current")
_TnPortLastStateChanged_Type = TimeStamp
_TnPortLastStateChanged_Object = MibTableColumn
tnPortLastStateChanged = _TnPortLastStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 48),
    _TnPortLastStateChanged_Type()
)
tnPortLastStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLastStateChanged.setStatus("current")
_TnPortNumChannels_Type = Unsigned32
_TnPortNumChannels_Object = MibTableColumn
tnPortNumChannels = _TnPortNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 49),
    _TnPortNumChannels_Type()
)
tnPortNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNumChannels.setStatus("current")
_TnPortNetworkEgrQueues_Type = TNamedItemOrEmpty
_TnPortNetworkEgrQueues_Object = MibTableColumn
tnPortNetworkEgrQueues = _TnPortNetworkEgrQueues_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 50),
    _TnPortNetworkEgrQueues_Type()
)
tnPortNetworkEgrQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortNetworkEgrQueues.setStatus("current")


class _TnPortBundleNumber_Type(Integer32):
    """Custom type tnPortBundleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TnPortBundleNumber_Type.__name__ = "Integer32"
_TnPortBundleNumber_Object = MibTableColumn
tnPortBundleNumber = _TnPortBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 51),
    _TnPortBundleNumber_Type()
)
tnPortBundleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortBundleNumber.setStatus("current")
_TnPortIsLeaf_Type = TruthValue
_TnPortIsLeaf_Object = MibTableColumn
tnPortIsLeaf = _TnPortIsLeaf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 52),
    _TnPortIsLeaf_Type()
)
tnPortIsLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortIsLeaf.setStatus("current")
_TnPortParentPortID_Type = TmnxPortID
_TnPortParentPortID_Object = MibTableColumn
tnPortParentPortID = _TnPortParentPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 54),
    _TnPortParentPortID_Type()
)
tnPortParentPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortParentPortID.setStatus("current")


class _TnPortOpticalCompliance_Type(OctetString):
    """Custom type tnPortOpticalCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnPortOpticalCompliance_Type.__name__ = "OctetString"
_TnPortOpticalCompliance_Object = MibTableColumn
tnPortOpticalCompliance = _TnPortOpticalCompliance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 55),
    _TnPortOpticalCompliance_Type()
)
tnPortOpticalCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortOpticalCompliance.setStatus("current")


class _TnPortLoadBalanceAlgorithm_Type(Integer32):
    """Custom type tnPortLoadBalanceAlgorithm based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 0),
          ("default", 1),
          ("includeL4", 2),
          ("excludeL4", 3))
    )


_TnPortLoadBalanceAlgorithm_Type.__name__ = "Integer32"
_TnPortLoadBalanceAlgorithm_Object = MibTableColumn
tnPortLoadBalanceAlgorithm = _TnPortLoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 56),
    _TnPortLoadBalanceAlgorithm_Type()
)
tnPortLoadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoadBalanceAlgorithm.setStatus("current")


class _TnPortEgrPortSchedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tnPortEgrPortSchedPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnPortEgrPortSchedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TnPortEgrPortSchedPlcy_Object = MibTableColumn
tnPortEgrPortSchedPlcy = _TnPortEgrPortSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 57),
    _TnPortEgrPortSchedPlcy_Type()
)
tnPortEgrPortSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEgrPortSchedPlcy.setStatus("current")
_TnPortLastClearedTime_Type = TimeStamp
_TnPortLastClearedTime_Object = MibTableColumn
tnPortLastClearedTime = _TnPortLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 58),
    _TnPortLastClearedTime_Type()
)
tnPortLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLastClearedTime.setStatus("current")


class _TnPortEgrHsmdaSchedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tnPortEgrHsmdaSchedPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnPortEgrHsmdaSchedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TnPortEgrHsmdaSchedPlcy_Object = MibTableColumn
tnPortEgrHsmdaSchedPlcy = _TnPortEgrHsmdaSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 59),
    _TnPortEgrHsmdaSchedPlcy_Type()
)
tnPortEgrHsmdaSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEgrHsmdaSchedPlcy.setStatus("current")


class _TnPortIngNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tnPortIngNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnPortIngNamedPoolPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TnPortIngNamedPoolPlcy_Object = MibTableColumn
tnPortIngNamedPoolPlcy = _TnPortIngNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 60),
    _TnPortIngNamedPoolPlcy_Type()
)
tnPortIngNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortIngNamedPoolPlcy.setStatus("current")


class _TnPortEgrNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tnPortEgrNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnPortEgrNamedPoolPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TnPortEgrNamedPoolPlcy_Object = MibTableColumn
tnPortEgrNamedPoolPlcy = _TnPortEgrNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 61),
    _TnPortEgrNamedPoolPlcy_Type()
)
tnPortEgrNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEgrNamedPoolPlcy.setStatus("current")


class _TnPortIngPoolPercentRate_Type(Unsigned32):
    """Custom type tnPortIngPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnPortIngPoolPercentRate_Type.__name__ = "Unsigned32"
_TnPortIngPoolPercentRate_Object = MibTableColumn
tnPortIngPoolPercentRate = _TnPortIngPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 62),
    _TnPortIngPoolPercentRate_Type()
)
tnPortIngPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortIngPoolPercentRate.setStatus("current")


class _TnPortEgrPoolPercentRate_Type(Unsigned32):
    """Custom type tnPortEgrPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnPortEgrPoolPercentRate_Type.__name__ = "Unsigned32"
_TnPortEgrPoolPercentRate_Object = MibTableColumn
tnPortEgrPoolPercentRate = _TnPortEgrPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 63),
    _TnPortEgrPoolPercentRate_Type()
)
tnPortEgrPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEgrPoolPercentRate.setStatus("current")


class _TnPortDDMEventSuppression_Type(TruthValue):
    """Custom type tnPortDDMEventSuppression based on TruthValue"""
    defaultValue = 2


_TnPortDDMEventSuppression_Type.__name__ = "TruthValue"
_TnPortDDMEventSuppression_Object = MibTableColumn
tnPortDDMEventSuppression = _TnPortDDMEventSuppression_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 64),
    _TnPortDDMEventSuppression_Type()
)
tnPortDDMEventSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortDDMEventSuppression.setStatus("current")


class _TnPortSFPStatus_Type(Integer32):
    """Custom type tnPortSFPStatus based on Integer32"""
    defaultValue = 0

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
        *(("not-equipped", 0),
          ("operational", 1),
          ("read-error", 2),
          ("data-corrupt", 3),
          ("ddm-corrupt", 4),
          ("unsupported", 5))
    )


_TnPortSFPStatus_Type.__name__ = "Integer32"
_TnPortSFPStatus_Object = MibTableColumn
tnPortSFPStatus = _TnPortSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 65),
    _TnPortSFPStatus_Type()
)
tnPortSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPStatus.setStatus("current")


class _TnPortReasonDownFlags_Type(Bits):
    """Custom type tnPortReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("linklossFwd", 1),
          ("lagMemberPortStandby", 2),
          ("ethCfmFault", 3),
          ("opticalTuning", 4),
          ("channelOutOfRange", 5),
          ("channelNotConfigured", 6),
          ("crcError", 7),
          ("internalMacTxError", 8),
          ("noServicePort", 9))
    )

_TnPortReasonDownFlags_Type.__name__ = "Bits"
_TnPortReasonDownFlags_Object = MibTableColumn
tnPortReasonDownFlags = _TnPortReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 66),
    _TnPortReasonDownFlags_Type()
)
tnPortReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortReasonDownFlags.setStatus("current")


class _TnPortSSMRxQualityLevel_Type(Integer32):
    """Custom type tnPortSSMRxQualityLevel based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("prs", 1),
          ("stu", 2),
          ("st2", 3),
          ("tnc", 4),
          ("st3e", 5),
          ("st3", 6),
          ("smc", 7),
          ("st4", 8),
          ("dus", 9),
          ("prc", 10),
          ("ssua", 11),
          ("ssub", 12),
          ("sec", 13),
          ("dnu", 14),
          ("inv", 15),
          ("pno", 16),
          ("eec1", 17),
          ("eec2", 18),
          ("failed", 19))
    )


_TnPortSSMRxQualityLevel_Type.__name__ = "Integer32"
_TnPortSSMRxQualityLevel_Object = MibTableColumn
tnPortSSMRxQualityLevel = _TnPortSSMRxQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 67),
    _TnPortSSMRxQualityLevel_Type()
)
tnPortSSMRxQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSSMRxQualityLevel.setStatus("current")


class _TnPortDwdmLaserChannel_Type(Unsigned32):
    """Custom type tnPortDwdmLaserChannel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 61),
        ValueRangeConstraint(170, 610),
    )


_TnPortDwdmLaserChannel_Type.__name__ = "Unsigned32"
_TnPortDwdmLaserChannel_Object = MibTableColumn
tnPortDwdmLaserChannel = _TnPortDwdmLaserChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 68),
    _TnPortDwdmLaserChannel_Type()
)
tnPortDwdmLaserChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortDwdmLaserChannel.setStatus("current")
_TnPortOtuCapable_Type = TruthValue
_TnPortOtuCapable_Object = MibTableColumn
tnPortOtuCapable = _TnPortOtuCapable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 69),
    _TnPortOtuCapable_Type()
)
tnPortOtuCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortOtuCapable.setStatus("current")


class _TnPortHoldTimeUnits_Type(Integer32):
    """Custom type tnPortHoldTimeUnits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 0),
          ("centiseconds", 1))
    )


_TnPortHoldTimeUnits_Type.__name__ = "Integer32"
_TnPortHoldTimeUnits_Object = MibTableColumn
tnPortHoldTimeUnits = _TnPortHoldTimeUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 70),
    _TnPortHoldTimeUnits_Type()
)
tnPortHoldTimeUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortHoldTimeUnits.setStatus("current")


class _TnPortLinkLengthInfo_Type(OctetString):
    """Custom type tnPortLinkLengthInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TnPortLinkLengthInfo_Type.__name__ = "OctetString"
_TnPortLinkLengthInfo_Object = MibTableColumn
tnPortLinkLengthInfo = _TnPortLinkLengthInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 71),
    _TnPortLinkLengthInfo_Type()
)
tnPortLinkLengthInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortLinkLengthInfo.setStatus("current")
_TnPortSFPNumLanes_Type = Unsigned32
_TnPortSFPNumLanes_Object = MibTableColumn
tnPortSFPNumLanes = _TnPortSFPNumLanes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 72),
    _TnPortSFPNumLanes_Type()
)
tnPortSFPNumLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortSFPNumLanes.setStatus("current")
_TnPortPhysStateChangeCount_Type = Counter32
_TnPortPhysStateChangeCount_Object = MibTableColumn
tnPortPhysStateChangeCount = _TnPortPhysStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 73),
    _TnPortPhysStateChangeCount_Type()
)
tnPortPhysStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortPhysStateChangeCount.setStatus("current")
_TnPortPacketSwitchId_Type = Unsigned32
_TnPortPacketSwitchId_Object = MibTableColumn
tnPortPacketSwitchId = _TnPortPacketSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 74),
    _TnPortPacketSwitchId_Type()
)
tnPortPacketSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortPacketSwitchId.setStatus("current")


class _TnPortOtnSignalDegrade_Type(TmnxEnabledDisabled):
    """Custom type tnPortOtnSignalDegrade based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnPortOtnSignalDegrade_Type.__name__ = "TmnxEnabledDisabled"
_TnPortOtnSignalDegrade_Object = MibTableColumn
tnPortOtnSignalDegrade = _TnPortOtnSignalDegrade_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 2, 1, 75),
    _TnPortOtnSignalDegrade_Type()
)
tnPortOtnSignalDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortOtnSignalDegrade.setStatus("current")
_TnPortTestTable_Object = MibTable
tnPortTestTable = _TnPortTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tnPortTestTable.setStatus("current")
_TnPortTestEntry_Object = MibTableRow
tnPortTestEntry = _TnPortTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tnPortTestEntry.setStatus("current")


class _TnPortTestState_Type(Integer32):
    """Custom type tnPortTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInTest", 1),
          ("inTest", 2))
    )


_TnPortTestState_Type.__name__ = "Integer32"
_TnPortTestState_Object = MibTableColumn
tnPortTestState = _TnPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 1),
    _TnPortTestState_Type()
)
tnPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTestState.setStatus("current")


class _TnPortTestMode_Type(Integer32):
    """Custom type tnPortTestMode based on Integer32"""
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
        *(("notApplicable", 0),
          ("loopback1", 1),
          ("loopback2", 2),
          ("loopback3", 3),
          ("singalInsertion", 4))
    )


_TnPortTestMode_Type.__name__ = "Integer32"
_TnPortTestMode_Object = MibTableColumn
tnPortTestMode = _TnPortTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 2),
    _TnPortTestMode_Type()
)
tnPortTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortTestMode.setStatus("current")
_TnPortTestParameter_Type = Unsigned32
_TnPortTestParameter_Object = MibTableColumn
tnPortTestParameter = _TnPortTestParameter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 3),
    _TnPortTestParameter_Type()
)
tnPortTestParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortTestParameter.setStatus("current")


class _TnPortTestLastResult_Type(Integer32):
    """Custom type tnPortTestLastResult based on Integer32"""
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
        *(("notApplicable", 0),
          ("success", 1),
          ("failure", 2),
          ("timeout", 3))
    )


_TnPortTestLastResult_Type.__name__ = "Integer32"
_TnPortTestLastResult_Object = MibTableColumn
tnPortTestLastResult = _TnPortTestLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 4),
    _TnPortTestLastResult_Type()
)
tnPortTestLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTestLastResult.setStatus("current")
_TnPortTestStartTime_Type = DateAndTime
_TnPortTestStartTime_Object = MibTableColumn
tnPortTestStartTime = _TnPortTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 5),
    _TnPortTestStartTime_Type()
)
tnPortTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTestStartTime.setStatus("current")
_TnPortTestEndTime_Type = DateAndTime
_TnPortTestEndTime_Object = MibTableColumn
tnPortTestEndTime = _TnPortTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 6),
    _TnPortTestEndTime_Type()
)
tnPortTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortTestEndTime.setStatus("current")


class _TnPortTestDuration_Type(Integer32):
    """Custom type tnPortTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnPortTestDuration_Type.__name__ = "Integer32"
_TnPortTestDuration_Object = MibTableColumn
tnPortTestDuration = _TnPortTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 7),
    _TnPortTestDuration_Type()
)
tnPortTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortTestDuration.setStatus("current")


class _TnPortTestAction_Type(Integer32):
    """Custom type tnPortTestAction based on Integer32"""
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
          ("startTest", 2),
          ("stopTest", 3))
    )


_TnPortTestAction_Type.__name__ = "Integer32"
_TnPortTestAction_Object = MibTableColumn
tnPortTestAction = _TnPortTestAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 3, 1, 8),
    _TnPortTestAction_Type()
)
tnPortTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortTestAction.setStatus("current")
_TnPortEtherTable_Object = MibTable
tnPortEtherTable = _TnPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnPortEtherTable.setStatus("current")
_TnPortEtherEntry_Object = MibTableRow
tnPortEtherEntry = _TnPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1)
)
tnPortEtherEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
)
if mibBuilder.loadTexts:
    tnPortEtherEntry.setStatus("current")


class _TnPortEtherMTU_Type(Unsigned32):
    """Custom type tnPortEtherMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9612),
    )


_TnPortEtherMTU_Type.__name__ = "Unsigned32"
_TnPortEtherMTU_Object = MibTableColumn
tnPortEtherMTU = _TnPortEtherMTU_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 1),
    _TnPortEtherMTU_Type()
)
tnPortEtherMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherMTU.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherMTU.setUnits("bytes")


class _TnPortEtherDuplex_Type(Integer32):
    """Custom type tnPortEtherDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_TnPortEtherDuplex_Type.__name__ = "Integer32"
_TnPortEtherDuplex_Object = MibTableColumn
tnPortEtherDuplex = _TnPortEtherDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 2),
    _TnPortEtherDuplex_Type()
)
tnPortEtherDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDuplex.setStatus("current")


class _TnPortEtherSpeed_Type(Integer32):
    """Custom type tnPortEtherSpeed based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4),
          ("speed40000", 5),
          ("speed100000", 6),
          ("oduflex", 7),
          ("speed2457", 8),
          ("speed4915", 9),
          ("spped6114", 10),
          ("speed9830", 11),
          ("speed10137", 12),
          ("speed24330", 13),
          ("speed3072", 14),
          ("speed25000", 15))
    )


_TnPortEtherSpeed_Type.__name__ = "Integer32"
_TnPortEtherSpeed_Object = MibTableColumn
tnPortEtherSpeed = _TnPortEtherSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 3),
    _TnPortEtherSpeed_Type()
)
tnPortEtherSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherSpeed.setStatus("current")


class _TnPortEtherAutoNegotiate_Type(Integer32):
    """Custom type tnPortEtherAutoNegotiate based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 0),
          ("true", 1),
          ("false", 2),
          ("limited", 3))
    )


_TnPortEtherAutoNegotiate_Type.__name__ = "Integer32"
_TnPortEtherAutoNegotiate_Object = MibTableColumn
tnPortEtherAutoNegotiate = _TnPortEtherAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 4),
    _TnPortEtherAutoNegotiate_Type()
)
tnPortEtherAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherAutoNegotiate.setStatus("current")


class _TnPortEtherOperDuplex_Type(Integer32):
    """Custom type tnPortEtherOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_TnPortEtherOperDuplex_Type.__name__ = "Integer32"
_TnPortEtherOperDuplex_Object = MibTableColumn
tnPortEtherOperDuplex = _TnPortEtherOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 5),
    _TnPortEtherOperDuplex_Type()
)
tnPortEtherOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherOperDuplex.setStatus("current")
_TnPortEtherOperSpeed_Type = Unsigned32
_TnPortEtherOperSpeed_Object = MibTableColumn
tnPortEtherOperSpeed = _TnPortEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 6),
    _TnPortEtherOperSpeed_Type()
)
tnPortEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherOperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherOperSpeed.setUnits("mega-bits per second")


class _TnPortEtherAcctPolicyId_Type(Unsigned32):
    """Custom type tnPortEtherAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnPortEtherAcctPolicyId_Type.__name__ = "Unsigned32"
_TnPortEtherAcctPolicyId_Object = MibTableColumn
tnPortEtherAcctPolicyId = _TnPortEtherAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 7),
    _TnPortEtherAcctPolicyId_Type()
)
tnPortEtherAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherAcctPolicyId.setStatus("current")


class _TnPortEtherCollectStats_Type(TruthValue):
    """Custom type tnPortEtherCollectStats based on TruthValue"""
    defaultValue = 1


_TnPortEtherCollectStats_Type.__name__ = "TruthValue"
_TnPortEtherCollectStats_Object = MibTableColumn
tnPortEtherCollectStats = _TnPortEtherCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 8),
    _TnPortEtherCollectStats_Type()
)
tnPortEtherCollectStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherCollectStats.setStatus("current")


class _TnPortEtherMDIMDIX_Type(Integer32):
    """Custom type tnPortEtherMDIMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("mdi", 1),
          ("mdix", 2))
    )


_TnPortEtherMDIMDIX_Type.__name__ = "Integer32"
_TnPortEtherMDIMDIX_Object = MibTableColumn
tnPortEtherMDIMDIX = _TnPortEtherMDIMDIX_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 9),
    _TnPortEtherMDIMDIX_Type()
)
tnPortEtherMDIMDIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherMDIMDIX.setStatus("current")


class _TnPortEtherXGigMode_Type(Integer32):
    """Custom type tnPortEtherXGigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("lan", 1),
          ("wan", 2))
    )


_TnPortEtherXGigMode_Type.__name__ = "Integer32"
_TnPortEtherXGigMode_Object = MibTableColumn
tnPortEtherXGigMode = _TnPortEtherXGigMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 10),
    _TnPortEtherXGigMode_Type()
)
tnPortEtherXGigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherXGigMode.setStatus("current")


class _TnPortEtherEgressRate_Type(Integer32):
    """Custom type tnPortEtherEgressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )


_TnPortEtherEgressRate_Type.__name__ = "Integer32"
_TnPortEtherEgressRate_Object = MibTableColumn
tnPortEtherEgressRate = _TnPortEtherEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 11),
    _TnPortEtherEgressRate_Type()
)
tnPortEtherEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherEgressRate.setStatus("current")


class _TnPortEtherDot1qEtype_Type(Unsigned32):
    """Custom type tnPortEtherDot1qEtype based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnPortEtherDot1qEtype_Type.__name__ = "Unsigned32"
_TnPortEtherDot1qEtype_Object = MibTableColumn
tnPortEtherDot1qEtype = _TnPortEtherDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 12),
    _TnPortEtherDot1qEtype_Type()
)
tnPortEtherDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDot1qEtype.setStatus("current")


class _TnPortEtherQinqEtype_Type(Unsigned32):
    """Custom type tnPortEtherQinqEtype based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnPortEtherQinqEtype_Type.__name__ = "Unsigned32"
_TnPortEtherQinqEtype_Object = MibTableColumn
tnPortEtherQinqEtype = _TnPortEtherQinqEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 13),
    _TnPortEtherQinqEtype_Type()
)
tnPortEtherQinqEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherQinqEtype.setStatus("current")


class _TnPortEtherIngressRate_Type(Integer32):
    """Custom type tnPortEtherIngressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_TnPortEtherIngressRate_Type.__name__ = "Integer32"
_TnPortEtherIngressRate_Object = MibTableColumn
tnPortEtherIngressRate = _TnPortEtherIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 14),
    _TnPortEtherIngressRate_Type()
)
tnPortEtherIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherIngressRate.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherIngressRate.setUnits("mega-bits per second")


class _TnPortEtherReportAlarm_Type(TmnxPortEtherReportStatus):
    """Custom type tnPortEtherReportAlarm based on TmnxPortEtherReportStatus"""
    defaultBinValue = "0011"


_TnPortEtherReportAlarm_Type.__name__ = "TmnxPortEtherReportStatus"
_TnPortEtherReportAlarm_Object = MibTableColumn
tnPortEtherReportAlarm = _TnPortEtherReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 15),
    _TnPortEtherReportAlarm_Type()
)
tnPortEtherReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherReportAlarm.setStatus("current")
_TnPortEtherReportAlarmStatus_Type = TmnxPortEtherReportStatus
_TnPortEtherReportAlarmStatus_Object = MibTableColumn
tnPortEtherReportAlarmStatus = _TnPortEtherReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 16),
    _TnPortEtherReportAlarmStatus_Type()
)
tnPortEtherReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherReportAlarmStatus.setStatus("current")
_TnPortEtherPkts1519toMax_Type = Counter32
_TnPortEtherPkts1519toMax_Object = MibTableColumn
tnPortEtherPkts1519toMax = _TnPortEtherPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 17),
    _TnPortEtherPkts1519toMax_Type()
)
tnPortEtherPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherPkts1519toMax.setUnits("Packets")
_TnPortEtherHCOverPkts1519toMax_Type = Counter32
_TnPortEtherHCOverPkts1519toMax_Object = MibTableColumn
tnPortEtherHCOverPkts1519toMax = _TnPortEtherHCOverPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 18),
    _TnPortEtherHCOverPkts1519toMax_Type()
)
tnPortEtherHCOverPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherHCOverPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherHCOverPkts1519toMax.setUnits("Packets")
_TnPortEtherHCPkts1519toMax_Type = Counter64
_TnPortEtherHCPkts1519toMax_Object = MibTableColumn
tnPortEtherHCPkts1519toMax = _TnPortEtherHCPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 19),
    _TnPortEtherHCPkts1519toMax_Type()
)
tnPortEtherHCPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherHCPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherHCPkts1519toMax.setUnits("Packets")


class _TnPortEtherLacpTunnel_Type(TruthValue):
    """Custom type tnPortEtherLacpTunnel based on TruthValue"""
    defaultValue = 2


_TnPortEtherLacpTunnel_Type.__name__ = "TruthValue"
_TnPortEtherLacpTunnel_Object = MibTableColumn
tnPortEtherLacpTunnel = _TnPortEtherLacpTunnel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 20),
    _TnPortEtherLacpTunnel_Type()
)
tnPortEtherLacpTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherLacpTunnel.setStatus("current")


class _TnPortEtherDownWhenLoopedEnabled_Type(TruthValue):
    """Custom type tnPortEtherDownWhenLoopedEnabled based on TruthValue"""
    defaultValue = 2


_TnPortEtherDownWhenLoopedEnabled_Type.__name__ = "TruthValue"
_TnPortEtherDownWhenLoopedEnabled_Object = MibTableColumn
tnPortEtherDownWhenLoopedEnabled = _TnPortEtherDownWhenLoopedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 21),
    _TnPortEtherDownWhenLoopedEnabled_Type()
)
tnPortEtherDownWhenLoopedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedEnabled.setStatus("current")


class _TnPortEtherDownWhenLoopedKeepAlive_Type(Unsigned32):
    """Custom type tnPortEtherDownWhenLoopedKeepAlive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TnPortEtherDownWhenLoopedKeepAlive_Type.__name__ = "Unsigned32"
_TnPortEtherDownWhenLoopedKeepAlive_Object = MibTableColumn
tnPortEtherDownWhenLoopedKeepAlive = _TnPortEtherDownWhenLoopedKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 22),
    _TnPortEtherDownWhenLoopedKeepAlive_Type()
)
tnPortEtherDownWhenLoopedKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedKeepAlive.setUnits("seconds")


class _TnPortEtherDownWhenLoopedRetry_Type(Unsigned32):
    """Custom type tnPortEtherDownWhenLoopedRetry based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 160),
    )


_TnPortEtherDownWhenLoopedRetry_Type.__name__ = "Unsigned32"
_TnPortEtherDownWhenLoopedRetry_Object = MibTableColumn
tnPortEtherDownWhenLoopedRetry = _TnPortEtherDownWhenLoopedRetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 23),
    _TnPortEtherDownWhenLoopedRetry_Type()
)
tnPortEtherDownWhenLoopedRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedRetry.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedRetry.setUnits("seconds")


class _TnPortEtherDownWhenLoopedState_Type(Integer32):
    """Custom type tnPortEtherDownWhenLoopedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLoopDetected", 1),
          ("loopDetected", 2))
    )


_TnPortEtherDownWhenLoopedState_Type.__name__ = "Integer32"
_TnPortEtherDownWhenLoopedState_Object = MibTableColumn
tnPortEtherDownWhenLoopedState = _TnPortEtherDownWhenLoopedState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 24),
    _TnPortEtherDownWhenLoopedState_Type()
)
tnPortEtherDownWhenLoopedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherDownWhenLoopedState.setStatus("current")


class _TnPortEtherPBBEtype_Type(Unsigned32):
    """Custom type tnPortEtherPBBEtype based on Unsigned32"""
    defaultValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnPortEtherPBBEtype_Type.__name__ = "Unsigned32"
_TnPortEtherPBBEtype_Object = MibTableColumn
tnPortEtherPBBEtype = _TnPortEtherPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 25),
    _TnPortEtherPBBEtype_Type()
)
tnPortEtherPBBEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherPBBEtype.setStatus("current")


class _TnPortEtherSingleFiber_Type(TruthValue):
    """Custom type tnPortEtherSingleFiber based on TruthValue"""
    defaultValue = 2


_TnPortEtherSingleFiber_Type.__name__ = "TruthValue"
_TnPortEtherSingleFiber_Object = MibTableColumn
tnPortEtherSingleFiber = _TnPortEtherSingleFiber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 27),
    _TnPortEtherSingleFiber_Type()
)
tnPortEtherSingleFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherSingleFiber.setStatus("current")


class _TnPortEtherSSM_Type(TruthValue):
    """Custom type tnPortEtherSSM based on TruthValue"""
    defaultValue = 2


_TnPortEtherSSM_Type.__name__ = "TruthValue"
_TnPortEtherSSM_Object = MibTableColumn
tnPortEtherSSM = _TnPortEtherSSM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 28),
    _TnPortEtherSSM_Type()
)
tnPortEtherSSM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherSSM.setStatus("current")


class _TnPortEtherDWLUseBroadcastAddr_Type(TruthValue):
    """Custom type tnPortEtherDWLUseBroadcastAddr based on TruthValue"""
    defaultValue = 2


_TnPortEtherDWLUseBroadcastAddr_Type.__name__ = "TruthValue"
_TnPortEtherDWLUseBroadcastAddr_Object = MibTableColumn
tnPortEtherDWLUseBroadcastAddr = _TnPortEtherDWLUseBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 29),
    _TnPortEtherDWLUseBroadcastAddr_Type()
)
tnPortEtherDWLUseBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherDWLUseBroadcastAddr.setStatus("current")


class _TnPortEtherSSMCodeType_Type(Integer32):
    """Custom type tnPortEtherSSMCodeType based on Integer32"""
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
        *(("unknown", 1),
          ("sonet", 2),
          ("sdh", 3))
    )


_TnPortEtherSSMCodeType_Type.__name__ = "Integer32"
_TnPortEtherSSMCodeType_Object = MibTableColumn
tnPortEtherSSMCodeType = _TnPortEtherSSMCodeType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 30),
    _TnPortEtherSSMCodeType_Type()
)
tnPortEtherSSMCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherSSMCodeType.setStatus("current")


class _TnPortEtherSSMTxDus_Type(TruthValue):
    """Custom type tnPortEtherSSMTxDus based on TruthValue"""
    defaultValue = 2


_TnPortEtherSSMTxDus_Type.__name__ = "TruthValue"
_TnPortEtherSSMTxDus_Object = MibTableColumn
tnPortEtherSSMTxDus = _TnPortEtherSSMTxDus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 31),
    _TnPortEtherSSMTxDus_Type()
)
tnPortEtherSSMTxDus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherSSMTxDus.setStatus("current")


class _TnPortEtherSSMRxEsmc_Type(Unsigned32):
    """Custom type tnPortEtherSSMRxEsmc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPortEtherSSMRxEsmc_Type.__name__ = "Unsigned32"
_TnPortEtherSSMRxEsmc_Object = MibTableColumn
tnPortEtherSSMRxEsmc = _TnPortEtherSSMRxEsmc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 32),
    _TnPortEtherSSMRxEsmc_Type()
)
tnPortEtherSSMRxEsmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherSSMRxEsmc.setStatus("current")


class _TnPortEtherSSMTxQualityLevel_Type(Integer32):
    """Custom type tnPortEtherSSMTxQualityLevel based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("prs", 1),
          ("stu", 2),
          ("st2", 3),
          ("tnc", 4),
          ("st3e", 5),
          ("reserved6", 6),
          ("smc", 7),
          ("reserved8", 8),
          ("dus", 9),
          ("prc", 10),
          ("ssua", 11),
          ("ssub", 12),
          ("reserved13", 13),
          ("dnu", 14),
          ("reserved15", 15),
          ("pno", 16),
          ("eec1", 17),
          ("eec2", 18),
          ("reserved19", 19))
    )


_TnPortEtherSSMTxQualityLevel_Type.__name__ = "Integer32"
_TnPortEtherSSMTxQualityLevel_Object = MibTableColumn
tnPortEtherSSMTxQualityLevel = _TnPortEtherSSMTxQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 33),
    _TnPortEtherSSMTxQualityLevel_Type()
)
tnPortEtherSSMTxQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherSSMTxQualityLevel.setStatus("current")
_TnPortEtherQinqEtypelink_Type = Unsigned32
_TnPortEtherQinqEtypelink_Object = MibTableColumn
tnPortEtherQinqEtypelink = _TnPortEtherQinqEtypelink_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 34),
    _TnPortEtherQinqEtypelink_Type()
)
tnPortEtherQinqEtypelink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherQinqEtypelink.setStatus("current")


class _TnPortEtherOperEgressRate_Type(Integer32):
    """Custom type tnPortEtherOperEgressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )


_TnPortEtherOperEgressRate_Type.__name__ = "Integer32"
_TnPortEtherOperEgressRate_Object = MibTableColumn
tnPortEtherOperEgressRate = _TnPortEtherOperEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 4, 1, 35),
    _TnPortEtherOperEgressRate_Type()
)
tnPortEtherOperEgressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortEtherOperEgressRate.setStatus("current")
_TnPortScalarObjs_ObjectIdentity = ObjectIdentity
tnPortScalarObjs = _TnPortScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19)
)
_TnPortScalar1_Type = Unsigned32
_TnPortScalar1_Object = MibScalar
tnPortScalar1 = _TnPortScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 11),
    _TnPortScalar1_Type()
)
tnPortScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar1.setStatus("current")
_TnPortScalar2_Type = Unsigned32
_TnPortScalar2_Object = MibScalar
tnPortScalar2 = _TnPortScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 12),
    _TnPortScalar2_Type()
)
tnPortScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar2.setStatus("current")
_TnPortScalar3_Type = Unsigned32
_TnPortScalar3_Object = MibScalar
tnPortScalar3 = _TnPortScalar3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 13),
    _TnPortScalar3_Type()
)
tnPortScalar3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar3.setStatus("current")
_TnPortScalar4_Type = Unsigned32
_TnPortScalar4_Object = MibScalar
tnPortScalar4 = _TnPortScalar4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 14),
    _TnPortScalar4_Type()
)
tnPortScalar4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar4.setStatus("current")
_TnPortScalar5_Type = Unsigned32
_TnPortScalar5_Object = MibScalar
tnPortScalar5 = _TnPortScalar5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 15),
    _TnPortScalar5_Type()
)
tnPortScalar5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar5.setStatus("current")
_TnPortScalar6_Type = Unsigned32
_TnPortScalar6_Object = MibScalar
tnPortScalar6 = _TnPortScalar6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 16),
    _TnPortScalar6_Type()
)
tnPortScalar6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar6.setStatus("current")
_TnPortScalar7_Type = Unsigned32
_TnPortScalar7_Object = MibScalar
tnPortScalar7 = _TnPortScalar7_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 17),
    _TnPortScalar7_Type()
)
tnPortScalar7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar7.setStatus("current")
_TnPortScalar8_Type = Unsigned32
_TnPortScalar8_Object = MibScalar
tnPortScalar8 = _TnPortScalar8_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 18),
    _TnPortScalar8_Type()
)
tnPortScalar8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar8.setStatus("current")
_TnPortScalar9_Type = Unsigned32
_TnPortScalar9_Object = MibScalar
tnPortScalar9 = _TnPortScalar9_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 19),
    _TnPortScalar9_Type()
)
tnPortScalar9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar9.setStatus("current")
_TnPortScalar10_Type = Unsigned32
_TnPortScalar10_Object = MibScalar
tnPortScalar10 = _TnPortScalar10_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 20),
    _TnPortScalar10_Type()
)
tnPortScalar10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar10.setStatus("current")
_TnPortScalar11_Type = Unsigned32
_TnPortScalar11_Object = MibScalar
tnPortScalar11 = _TnPortScalar11_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 21),
    _TnPortScalar11_Type()
)
tnPortScalar11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar11.setStatus("current")
_TnPortScalar12_Type = Unsigned32
_TnPortScalar12_Object = MibScalar
tnPortScalar12 = _TnPortScalar12_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 22),
    _TnPortScalar12_Type()
)
tnPortScalar12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar12.setStatus("current")
_TnPortScalar13_Type = Unsigned32
_TnPortScalar13_Object = MibScalar
tnPortScalar13 = _TnPortScalar13_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 23),
    _TnPortScalar13_Type()
)
tnPortScalar13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar13.setStatus("current")
_TnPortScalar14_Type = Unsigned32
_TnPortScalar14_Object = MibScalar
tnPortScalar14 = _TnPortScalar14_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 24),
    _TnPortScalar14_Type()
)
tnPortScalar14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar14.setStatus("current")
_TnPortScalar15_Type = Unsigned32
_TnPortScalar15_Object = MibScalar
tnPortScalar15 = _TnPortScalar15_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 25),
    _TnPortScalar15_Type()
)
tnPortScalar15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar15.setStatus("current")
_TnPortScalar16_Type = Unsigned32
_TnPortScalar16_Object = MibScalar
tnPortScalar16 = _TnPortScalar16_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 26),
    _TnPortScalar16_Type()
)
tnPortScalar16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar16.setStatus("current")
_TnPortScalar17_Type = Unsigned32
_TnPortScalar17_Object = MibScalar
tnPortScalar17 = _TnPortScalar17_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 27),
    _TnPortScalar17_Type()
)
tnPortScalar17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar17.setStatus("current")
_TnPortScalar18_Type = Unsigned32
_TnPortScalar18_Object = MibScalar
tnPortScalar18 = _TnPortScalar18_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 28),
    _TnPortScalar18_Type()
)
tnPortScalar18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar18.setStatus("current")
_TnPortScalar19_Type = Unsigned32
_TnPortScalar19_Object = MibScalar
tnPortScalar19 = _TnPortScalar19_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 29),
    _TnPortScalar19_Type()
)
tnPortScalar19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar19.setStatus("current")
_TnPortScalar20_Type = Unsigned32
_TnPortScalar20_Object = MibScalar
tnPortScalar20 = _TnPortScalar20_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 30),
    _TnPortScalar20_Type()
)
tnPortScalar20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar20.setStatus("current")
_TnPortScalar21_Type = Unsigned32
_TnPortScalar21_Object = MibScalar
tnPortScalar21 = _TnPortScalar21_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 31),
    _TnPortScalar21_Type()
)
tnPortScalar21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar21.setStatus("current")
_TnPortScalar22_Type = Unsigned32
_TnPortScalar22_Object = MibScalar
tnPortScalar22 = _TnPortScalar22_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 32),
    _TnPortScalar22_Type()
)
tnPortScalar22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar22.setStatus("current")
_TnPortScalar23_Type = Unsigned32
_TnPortScalar23_Object = MibScalar
tnPortScalar23 = _TnPortScalar23_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 33),
    _TnPortScalar23_Type()
)
tnPortScalar23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar23.setStatus("current")
_TnPortScalar24_Type = Unsigned32
_TnPortScalar24_Object = MibScalar
tnPortScalar24 = _TnPortScalar24_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 34),
    _TnPortScalar24_Type()
)
tnPortScalar24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar24.setStatus("current")
_TnPortScalar25_Type = Unsigned32
_TnPortScalar25_Object = MibScalar
tnPortScalar25 = _TnPortScalar25_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 35),
    _TnPortScalar25_Type()
)
tnPortScalar25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar25.setStatus("current")
_TnPortScalar26_Type = Unsigned32
_TnPortScalar26_Object = MibScalar
tnPortScalar26 = _TnPortScalar26_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 36),
    _TnPortScalar26_Type()
)
tnPortScalar26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar26.setStatus("current")
_TnPortScalar27_Type = Unsigned32
_TnPortScalar27_Object = MibScalar
tnPortScalar27 = _TnPortScalar27_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 37),
    _TnPortScalar27_Type()
)
tnPortScalar27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar27.setStatus("current")
_TnPortScalar28_Type = Unsigned32
_TnPortScalar28_Object = MibScalar
tnPortScalar28 = _TnPortScalar28_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 38),
    _TnPortScalar28_Type()
)
tnPortScalar28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar28.setStatus("current")
_TnPortScalar29_Type = Unsigned32
_TnPortScalar29_Object = MibScalar
tnPortScalar29 = _TnPortScalar29_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 39),
    _TnPortScalar29_Type()
)
tnPortScalar29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar29.setStatus("current")
_TnPortScalar30_Type = Unsigned32
_TnPortScalar30_Object = MibScalar
tnPortScalar30 = _TnPortScalar30_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 19, 40),
    _TnPortScalar30_Type()
)
tnPortScalar30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortScalar30.setStatus("current")
_TnPacketSwitchPortTable_Object = MibTable
tnPacketSwitchPortTable = _TnPacketSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 99)
)
if mibBuilder.loadTexts:
    tnPacketSwitchPortTable.setStatus("current")
_TnPacketSwitchPortEntry_Object = MibTableRow
tnPacketSwitchPortEntry = _TnPacketSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 99, 1)
)
tnPacketSwitchPortEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
)
if mibBuilder.loadTexts:
    tnPacketSwitchPortEntry.setStatus("current")
_TnPacketSwitchPortName_Type = TNamedItemOrEmpty
_TnPacketSwitchPortName_Object = MibTableColumn
tnPacketSwitchPortName = _TnPacketSwitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 99, 1, 1),
    _TnPacketSwitchPortName_Type()
)
tnPacketSwitchPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPacketSwitchPortName.setStatus("current")
_TnEMACTable_Object = MibTable
tnEMACTable = _TnEMACTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 100)
)
if mibBuilder.loadTexts:
    tnEMACTable.setStatus("current")
_TnEMACEntry_Object = MibTableRow
tnEMACEntry = _TnEMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 100, 1)
)
tnEMACEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnEMACID"),
)
if mibBuilder.loadTexts:
    tnEMACEntry.setStatus("current")
_TnEMACID_Type = TmnxPortID
_TnEMACID_Object = MibTableColumn
tnEMACID = _TnEMACID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 100, 1, 1),
    _TnEMACID_Type()
)
tnEMACID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEMACID.setStatus("current")


class _TnEMACAcctPolicyId_Type(Unsigned32):
    """Custom type tnEMACAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnEMACAcctPolicyId_Type.__name__ = "Unsigned32"
_TnEMACAcctPolicyId_Object = MibTableColumn
tnEMACAcctPolicyId = _TnEMACAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 100, 1, 2),
    _TnEMACAcctPolicyId_Type()
)
tnEMACAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEMACAcctPolicyId.setStatus("current")
_TnPMACTable_Object = MibTable
tnPMACTable = _TnPMACTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 101)
)
if mibBuilder.loadTexts:
    tnPMACTable.setStatus("current")
_TnPMACEntry_Object = MibTableRow
tnPMACEntry = _TnPMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 101, 1)
)
tnPMACEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnPMACID"),
)
if mibBuilder.loadTexts:
    tnPMACEntry.setStatus("current")
_TnPMACID_Type = TmnxPortID
_TnPMACID_Object = MibTableColumn
tnPMACID = _TnPMACID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 101, 1, 1),
    _TnPMACID_Type()
)
tnPMACID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPMACID.setStatus("current")


class _TnPMACAcctPolicyId_Type(Unsigned32):
    """Custom type tnPMACAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnPMACAcctPolicyId_Type.__name__ = "Unsigned32"
_TnPMACAcctPolicyId_Object = MibTableColumn
tnPMACAcctPolicyId = _TnPMACAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 101, 1, 2),
    _TnPMACAcctPolicyId_Type()
)
tnPMACAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPMACAcctPolicyId.setStatus("current")
_TnMMACTable_Object = MibTable
tnMMACTable = _TnMMACTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 102)
)
if mibBuilder.loadTexts:
    tnMMACTable.setStatus("current")
_TnMMACEntry_Object = MibTableRow
tnMMACEntry = _TnMMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 102, 1)
)
tnMMACEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnMMACID"),
)
if mibBuilder.loadTexts:
    tnMMACEntry.setStatus("current")
_TnMMACID_Type = TmnxPortID
_TnMMACID_Object = MibTableColumn
tnMMACID = _TnMMACID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 102, 1, 1),
    _TnMMACID_Type()
)
tnMMACID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMMACID.setStatus("current")


class _TnMMACAcctPolicyId_Type(Unsigned32):
    """Custom type tnMMACAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TnMMACAcctPolicyId_Type.__name__ = "Unsigned32"
_TnMMACAcctPolicyId_Object = MibTableColumn
tnMMACAcctPolicyId = _TnMMACAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 4, 102, 1, 2),
    _TnMMACAcctPolicyId_Type()
)
tnMMACAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMMACAcctPolicyId.setStatus("current")
_TnQosAppObjs_ObjectIdentity = ObjectIdentity
tnQosAppObjs = _TnQosAppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10)
)
_TnQosPoolAppTable_Object = MibTable
tnQosPoolAppTable = _TnQosPoolAppTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    tnQosPoolAppTable.setStatus("current")
_TnQosPoolAppEntry_Object = MibTableRow
tnQosPoolAppEntry = _TnQosPoolAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1)
)
tnQosPoolAppEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnObjectType"),
    (0, "TN-PORT-MIB", "tnObjectId"),
    (0, "TN-PORT-MIB", "tnObjectAppType"),
    (0, "TN-PORT-MIB", "tnObjectAppPool"),
)
if mibBuilder.loadTexts:
    tnQosPoolAppEntry.setStatus("current")


class _TnObjectType_Type(Integer32):
    """Custom type tnObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51)
        )
    )
    namedValues = NamedValues(
        *(("mda", 1),
          ("port", 2),
          ("channel", 3),
          ("bundle", 4),
          ("mpointQueues", 51))
    )


_TnObjectType_Type.__name__ = "Integer32"
_TnObjectType_Object = MibTableColumn
tnObjectType = _TnObjectType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 1),
    _TnObjectType_Type()
)
tnObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnObjectType.setStatus("current")
_TnObjectId_Type = TmnxPortID
_TnObjectId_Object = MibTableColumn
tnObjectId = _TnObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 2),
    _TnObjectId_Type()
)
tnObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnObjectId.setStatus("current")


class _TnObjectAppType_Type(Integer32):
    """Custom type tnObjectAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51)
        )
    )
    namedValues = NamedValues(
        *(("accessIngress", 1),
          ("accessEgress", 2),
          ("networkIngress", 3),
          ("networkEgress", 4),
          ("system", 51))
    )


_TnObjectAppType_Type.__name__ = "Integer32"
_TnObjectAppType_Object = MibTableColumn
tnObjectAppType = _TnObjectAppType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 3),
    _TnObjectAppType_Type()
)
tnObjectAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnObjectAppType.setStatus("current")
_TnObjectAppPool_Type = TNamedItem
_TnObjectAppPool_Object = MibTableColumn
tnObjectAppPool = _TnObjectAppPool_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 4),
    _TnObjectAppPool_Type()
)
tnObjectAppPool.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnObjectAppPool.setStatus("current")
_TnObjectAppPoolRowStatus_Type = RowStatus
_TnObjectAppPoolRowStatus_Object = MibTableColumn
tnObjectAppPoolRowStatus = _TnObjectAppPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 5),
    _TnObjectAppPoolRowStatus_Type()
)
tnObjectAppPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnObjectAppPoolRowStatus.setStatus("current")


class _TnObjectAppResvCbs_Type(Integer32):
    """Custom type tnObjectAppResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TnObjectAppResvCbs_Type.__name__ = "Integer32"
_TnObjectAppResvCbs_Object = MibTableColumn
tnObjectAppResvCbs = _TnObjectAppResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 6),
    _TnObjectAppResvCbs_Type()
)
tnObjectAppResvCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnObjectAppResvCbs.setStatus("current")


class _TnObjectAppSlopePolicy_Type(TNamedItem):
    """Custom type tnObjectAppSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TnObjectAppSlopePolicy_Type.__name__ = "TNamedItem"
_TnObjectAppSlopePolicy_Object = MibTableColumn
tnObjectAppSlopePolicy = _TnObjectAppSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 7),
    _TnObjectAppSlopePolicy_Type()
)
tnObjectAppSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnObjectAppSlopePolicy.setStatus("current")


class _TnObjectAppPoolSize_Type(Integer32):
    """Custom type tnObjectAppPoolSize based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TnObjectAppPoolSize_Type.__name__ = "Integer32"
_TnObjectAppPoolSize_Object = MibTableColumn
tnObjectAppPoolSize = _TnObjectAppPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 2, 10, 2, 1, 8),
    _TnObjectAppPoolSize_Type()
)
tnObjectAppPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnObjectAppPoolSize.setStatus("current")
_TnHwNotification_ObjectIdentity = ObjectIdentity
tnHwNotification = _TnHwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 2)
)
_TnPortNotifyPrefix_ObjectIdentity = ObjectIdentity
tnPortNotifyPrefix = _TnPortNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 2, 2)
)
_TnPortNotification_ObjectIdentity = ObjectIdentity
tnPortNotification = _TnPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 2, 2, 0)
)
tnPortEntry.registerAugmentions(
    ("TN-PORT-MIB",
     "tnPortTestEntry")
)
tnPortTestEntry.setIndexNames(*tnPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PORT-MIB",
    **{"TmnxPortOperStatus": TmnxPortOperStatus,
       "TmnxPortEtherReportStatus": TmnxPortEtherReportStatus,
       "TmnxPortClass": TmnxPortClass,
       "TmnxPortConnectorType": TmnxPortConnectorType,
       "TmnxPortState": TmnxPortState,
       "TmnxPortType": TmnxPortType,
       "TmnxAlarmState": TmnxAlarmState,
       "TmnxPortAdminStatus": TmnxPortAdminStatus,
       "tnPortMIBModule": tnPortMIBModule,
       "tnHwObjs": tnHwObjs,
       "tnPortObjs": tnPortObjs,
       "tnPortTableLastChange": tnPortTableLastChange,
       "tnPortTable": tnPortTable,
       "tnPortEntry": tnPortEntry,
       "tnPortPortID": tnPortPortID,
       "tnPortLastChangeTime": tnPortLastChangeTime,
       "tnPortType": tnPortType,
       "tnPortClass": tnPortClass,
       "tnPortDescription": tnPortDescription,
       "tnPortName": tnPortName,
       "tnPortAlias": tnPortAlias,
       "tnPortUserAssignedMac": tnPortUserAssignedMac,
       "tnPortMacAddress": tnPortMacAddress,
       "tnPortHwMacAddress": tnPortHwMacAddress,
       "tnPortMode": tnPortMode,
       "tnPortEncapType": tnPortEncapType,
       "tnPortLagId": tnPortLagId,
       "tnPortHoldTimeUp": tnPortHoldTimeUp,
       "tnPortHoldTimeDown": tnPortHoldTimeDown,
       "tnPortUpProtocols": tnPortUpProtocols,
       "tnPortConnectorType": tnPortConnectorType,
       "tnPortTransceiverType": tnPortTransceiverType,
       "tnPortTransceiverLaserWaveLen": tnPortTransceiverLaserWaveLen,
       "tnPortTransceiverDiagCapable": tnPortTransceiverDiagCapable,
       "tnPortTransceiverModelNumber": tnPortTransceiverModelNumber,
       "tnPortSFPConnectorCode": tnPortSFPConnectorCode,
       "tnPortSFPVendorOUI": tnPortSFPVendorOUI,
       "tnPortSFPVendorManufactureDate": tnPortSFPVendorManufactureDate,
       "tnPortSFPMedia": tnPortSFPMedia,
       "tnPortSFPEquipped": tnPortSFPEquipped,
       "tnPortEquipped": tnPortEquipped,
       "tnPortLinkStatus": tnPortLinkStatus,
       "tnPortAdminStatus": tnPortAdminStatus,
       "tnPortOperStatus": tnPortOperStatus,
       "tnPortState": tnPortState,
       "tnPortPrevState": tnPortPrevState,
       "tnPortNumAlarms": tnPortNumAlarms,
       "tnPortAlarmState": tnPortAlarmState,
       "tnPortLastAlarmEvent": tnPortLastAlarmEvent,
       "tnPortClearAlarms": tnPortClearAlarms,
       "tnPortSFPVendorSerialNum": tnPortSFPVendorSerialNum,
       "tnPortSFPVendorPartNum": tnPortSFPVendorPartNum,
       "tnPortLastStateChanged": tnPortLastStateChanged,
       "tnPortNumChannels": tnPortNumChannels,
       "tnPortNetworkEgrQueues": tnPortNetworkEgrQueues,
       "tnPortBundleNumber": tnPortBundleNumber,
       "tnPortIsLeaf": tnPortIsLeaf,
       "tnPortParentPortID": tnPortParentPortID,
       "tnPortOpticalCompliance": tnPortOpticalCompliance,
       "tnPortLoadBalanceAlgorithm": tnPortLoadBalanceAlgorithm,
       "tnPortEgrPortSchedPlcy": tnPortEgrPortSchedPlcy,
       "tnPortLastClearedTime": tnPortLastClearedTime,
       "tnPortEgrHsmdaSchedPlcy": tnPortEgrHsmdaSchedPlcy,
       "tnPortIngNamedPoolPlcy": tnPortIngNamedPoolPlcy,
       "tnPortEgrNamedPoolPlcy": tnPortEgrNamedPoolPlcy,
       "tnPortIngPoolPercentRate": tnPortIngPoolPercentRate,
       "tnPortEgrPoolPercentRate": tnPortEgrPoolPercentRate,
       "tnPortDDMEventSuppression": tnPortDDMEventSuppression,
       "tnPortSFPStatus": tnPortSFPStatus,
       "tnPortReasonDownFlags": tnPortReasonDownFlags,
       "tnPortSSMRxQualityLevel": tnPortSSMRxQualityLevel,
       "tnPortDwdmLaserChannel": tnPortDwdmLaserChannel,
       "tnPortOtuCapable": tnPortOtuCapable,
       "tnPortHoldTimeUnits": tnPortHoldTimeUnits,
       "tnPortLinkLengthInfo": tnPortLinkLengthInfo,
       "tnPortSFPNumLanes": tnPortSFPNumLanes,
       "tnPortPhysStateChangeCount": tnPortPhysStateChangeCount,
       "tnPortPacketSwitchId": tnPortPacketSwitchId,
       "tnPortOtnSignalDegrade": tnPortOtnSignalDegrade,
       "tnPortTestTable": tnPortTestTable,
       "tnPortTestEntry": tnPortTestEntry,
       "tnPortTestState": tnPortTestState,
       "tnPortTestMode": tnPortTestMode,
       "tnPortTestParameter": tnPortTestParameter,
       "tnPortTestLastResult": tnPortTestLastResult,
       "tnPortTestStartTime": tnPortTestStartTime,
       "tnPortTestEndTime": tnPortTestEndTime,
       "tnPortTestDuration": tnPortTestDuration,
       "tnPortTestAction": tnPortTestAction,
       "tnPortEtherTable": tnPortEtherTable,
       "tnPortEtherEntry": tnPortEtherEntry,
       "tnPortEtherMTU": tnPortEtherMTU,
       "tnPortEtherDuplex": tnPortEtherDuplex,
       "tnPortEtherSpeed": tnPortEtherSpeed,
       "tnPortEtherAutoNegotiate": tnPortEtherAutoNegotiate,
       "tnPortEtherOperDuplex": tnPortEtherOperDuplex,
       "tnPortEtherOperSpeed": tnPortEtherOperSpeed,
       "tnPortEtherAcctPolicyId": tnPortEtherAcctPolicyId,
       "tnPortEtherCollectStats": tnPortEtherCollectStats,
       "tnPortEtherMDIMDIX": tnPortEtherMDIMDIX,
       "tnPortEtherXGigMode": tnPortEtherXGigMode,
       "tnPortEtherEgressRate": tnPortEtherEgressRate,
       "tnPortEtherDot1qEtype": tnPortEtherDot1qEtype,
       "tnPortEtherQinqEtype": tnPortEtherQinqEtype,
       "tnPortEtherIngressRate": tnPortEtherIngressRate,
       "tnPortEtherReportAlarm": tnPortEtherReportAlarm,
       "tnPortEtherReportAlarmStatus": tnPortEtherReportAlarmStatus,
       "tnPortEtherPkts1519toMax": tnPortEtherPkts1519toMax,
       "tnPortEtherHCOverPkts1519toMax": tnPortEtherHCOverPkts1519toMax,
       "tnPortEtherHCPkts1519toMax": tnPortEtherHCPkts1519toMax,
       "tnPortEtherLacpTunnel": tnPortEtherLacpTunnel,
       "tnPortEtherDownWhenLoopedEnabled": tnPortEtherDownWhenLoopedEnabled,
       "tnPortEtherDownWhenLoopedKeepAlive": tnPortEtherDownWhenLoopedKeepAlive,
       "tnPortEtherDownWhenLoopedRetry": tnPortEtherDownWhenLoopedRetry,
       "tnPortEtherDownWhenLoopedState": tnPortEtherDownWhenLoopedState,
       "tnPortEtherPBBEtype": tnPortEtherPBBEtype,
       "tnPortEtherSingleFiber": tnPortEtherSingleFiber,
       "tnPortEtherSSM": tnPortEtherSSM,
       "tnPortEtherDWLUseBroadcastAddr": tnPortEtherDWLUseBroadcastAddr,
       "tnPortEtherSSMCodeType": tnPortEtherSSMCodeType,
       "tnPortEtherSSMTxDus": tnPortEtherSSMTxDus,
       "tnPortEtherSSMRxEsmc": tnPortEtherSSMRxEsmc,
       "tnPortEtherSSMTxQualityLevel": tnPortEtherSSMTxQualityLevel,
       "tnPortEtherQinqEtypelink": tnPortEtherQinqEtypelink,
       "tnPortEtherOperEgressRate": tnPortEtherOperEgressRate,
       "tnPortScalarObjs": tnPortScalarObjs,
       "tnPortScalar1": tnPortScalar1,
       "tnPortScalar2": tnPortScalar2,
       "tnPortScalar3": tnPortScalar3,
       "tnPortScalar4": tnPortScalar4,
       "tnPortScalar5": tnPortScalar5,
       "tnPortScalar6": tnPortScalar6,
       "tnPortScalar7": tnPortScalar7,
       "tnPortScalar8": tnPortScalar8,
       "tnPortScalar9": tnPortScalar9,
       "tnPortScalar10": tnPortScalar10,
       "tnPortScalar11": tnPortScalar11,
       "tnPortScalar12": tnPortScalar12,
       "tnPortScalar13": tnPortScalar13,
       "tnPortScalar14": tnPortScalar14,
       "tnPortScalar15": tnPortScalar15,
       "tnPortScalar16": tnPortScalar16,
       "tnPortScalar17": tnPortScalar17,
       "tnPortScalar18": tnPortScalar18,
       "tnPortScalar19": tnPortScalar19,
       "tnPortScalar20": tnPortScalar20,
       "tnPortScalar21": tnPortScalar21,
       "tnPortScalar22": tnPortScalar22,
       "tnPortScalar23": tnPortScalar23,
       "tnPortScalar24": tnPortScalar24,
       "tnPortScalar25": tnPortScalar25,
       "tnPortScalar26": tnPortScalar26,
       "tnPortScalar27": tnPortScalar27,
       "tnPortScalar28": tnPortScalar28,
       "tnPortScalar29": tnPortScalar29,
       "tnPortScalar30": tnPortScalar30,
       "tnPacketSwitchPortTable": tnPacketSwitchPortTable,
       "tnPacketSwitchPortEntry": tnPacketSwitchPortEntry,
       "tnPacketSwitchPortName": tnPacketSwitchPortName,
       "tnEMACTable": tnEMACTable,
       "tnEMACEntry": tnEMACEntry,
       "tnEMACID": tnEMACID,
       "tnEMACAcctPolicyId": tnEMACAcctPolicyId,
       "tnPMACTable": tnPMACTable,
       "tnPMACEntry": tnPMACEntry,
       "tnPMACID": tnPMACID,
       "tnPMACAcctPolicyId": tnPMACAcctPolicyId,
       "tnMMACTable": tnMMACTable,
       "tnMMACEntry": tnMMACEntry,
       "tnMMACID": tnMMACID,
       "tnMMACAcctPolicyId": tnMMACAcctPolicyId,
       "tnQosAppObjs": tnQosAppObjs,
       "tnQosPoolAppTable": tnQosPoolAppTable,
       "tnQosPoolAppEntry": tnQosPoolAppEntry,
       "tnObjectType": tnObjectType,
       "tnObjectId": tnObjectId,
       "tnObjectAppType": tnObjectAppType,
       "tnObjectAppPool": tnObjectAppPool,
       "tnObjectAppPoolRowStatus": tnObjectAppPoolRowStatus,
       "tnObjectAppResvCbs": tnObjectAppResvCbs,
       "tnObjectAppSlopePolicy": tnObjectAppSlopePolicy,
       "tnObjectAppPoolSize": tnObjectAppPoolSize,
       "tnHwNotification": tnHwNotification,
       "tnPortNotifyPrefix": tnPortNotifyPrefix,
       "tnPortNotification": tnPortNotification}
)
