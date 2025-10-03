# SNMP MIB module (NSCRTV-FTTX-GPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\NSCRTV-FTTX-GPON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:57 2025
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
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
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class GponAlarmInstance(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class GponAlarmCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class GponSeverityType(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("clear", 6))
    )



class TAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class GponCardIndex(TextualConvention, Unsigned32):
    status = "current"


class GponPortIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class GponDeviceIndex(TextualConvention, Unsigned32):
    status = "current"


class AutoNegotiationTechAbility(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("tenBaseTFullDuplex", 1),
          ("tenBaseTHalfDuplex", 2),
          ("hundredBaseTFullDuplex", 3),
          ("hundredBaseTHalfDuplex", 4),
          ("thousandBaseTFullDuplex", 5),
          ("thousandBaseTHalfDuplex", 6),
          ("thousandBaseXFullDuplex", 7),
          ("thousandBaseXHalfDuplex", 8),
          ("fdxPause", 9),
          ("fdxApause", 10),
          ("fdxSpause", 11),
          ("fdxBpause", 12))
    )


class GponStats15MinRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )



class GponStats24HourRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class GponStatsThresholdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_NscrtvRoot_ObjectIdentity = ObjectIdentity
nscrtvRoot = _NscrtvRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409)
)
_NscrtvHFCemsTree_ObjectIdentity = ObjectIdentity
nscrtvHFCemsTree = _NscrtvHFCemsTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1)
)
_NscrtvFTTxTree_ObjectIdentity = ObjectIdentity
nscrtvFTTxTree = _NscrtvFTTxTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2)
)
_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2)
)
_GponAlarmTree_ObjectIdentity = ObjectIdentity
gponAlarmTree = _GponAlarmTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12)
)
_GponTrapObjectGroup_ObjectIdentity = ObjectIdentity
gponTrapObjectGroup = _GponTrapObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1)
)
_GponNotifications_ObjectIdentity = ObjectIdentity
gponNotifications = _GponNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 1)
)
_GponTrapObjects_ObjectIdentity = ObjectIdentity
gponTrapObjects = _GponTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2)
)
_GponTrapInstance_Type = GponAlarmInstance
_GponTrapInstance_Object = MibScalar
gponTrapInstance = _GponTrapInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 1),
    _GponTrapInstance_Type()
)
gponTrapInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapInstance.setStatus("current")
_GponTrapCorrelationId_Type = Unsigned32
_GponTrapCorrelationId_Object = MibScalar
gponTrapCorrelationId = _GponTrapCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 2),
    _GponTrapCorrelationId_Type()
)
gponTrapCorrelationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapCorrelationId.setStatus("current")


class _GponTrapAdditionalText_Type(OctetString):
    """Custom type gponTrapAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GponTrapAdditionalText_Type.__name__ = "OctetString"
_GponTrapAdditionalText_Object = MibScalar
gponTrapAdditionalText = _GponTrapAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 3),
    _GponTrapAdditionalText_Type()
)
gponTrapAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapAdditionalText.setStatus("current")
_GponTrapCode_Type = GponAlarmCode
_GponTrapCode_Object = MibScalar
gponTrapCode = _GponTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 4),
    _GponTrapCode_Type()
)
gponTrapCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapCode.setStatus("current")
_GponTrapSeverity_Type = GponSeverityType
_GponTrapSeverity_Object = MibScalar
gponTrapSeverity = _GponTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 5),
    _GponTrapSeverity_Type()
)
gponTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapSeverity.setStatus("current")
_GponTrapOccurTime_Type = DateAndTime
_GponTrapOccurTime_Object = MibScalar
gponTrapOccurTime = _GponTrapOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 6),
    _GponTrapOccurTime_Type()
)
gponTrapOccurTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapOccurTime.setStatus("current")
_GponTrapSequenceNumber_Type = Unsigned32
_GponTrapSequenceNumber_Object = MibScalar
gponTrapSequenceNumber = _GponTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 2, 7),
    _GponTrapSequenceNumber_Type()
)
gponTrapSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gponTrapSequenceNumber.setStatus("current")
_GponAlarmObjGroup_ObjectIdentity = ObjectIdentity
gponAlarmObjGroup = _GponAlarmObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2)
)
_GponActiveAlarmTable_Object = MibTable
gponActiveAlarmTable = _GponActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    gponActiveAlarmTable.setStatus("current")
_GponActiveAlarmEntry_Object = MibTableRow
gponActiveAlarmEntry = _GponActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1)
)
gponActiveAlarmEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponActiveAlarmSeqNum"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponActiveAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    gponActiveAlarmEntry.setStatus("current")
_GponActiveAlarmSeqNum_Type = Unsigned32
_GponActiveAlarmSeqNum_Object = MibTableColumn
gponActiveAlarmSeqNum = _GponActiveAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 1),
    _GponActiveAlarmSeqNum_Type()
)
gponActiveAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponActiveAlarmSeqNum.setStatus("current")
_GponActiveAlarmCode_Type = GponAlarmCode
_GponActiveAlarmCode_Object = MibTableColumn
gponActiveAlarmCode = _GponActiveAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 2),
    _GponActiveAlarmCode_Type()
)
gponActiveAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmCode.setStatus("current")
_GponActiveAlarmInstance_Type = GponAlarmInstance
_GponActiveAlarmInstance_Object = MibTableColumn
gponActiveAlarmInstance = _GponActiveAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 3),
    _GponActiveAlarmInstance_Type()
)
gponActiveAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmInstance.setStatus("current")
_GponActiveAlarmSeverity_Type = GponSeverityType
_GponActiveAlarmSeverity_Object = MibTableColumn
gponActiveAlarmSeverity = _GponActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 4),
    _GponActiveAlarmSeverity_Type()
)
gponActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmSeverity.setStatus("current")
_GponActiveAlarmRaisingNumber_Type = Unsigned32
_GponActiveAlarmRaisingNumber_Object = MibTableColumn
gponActiveAlarmRaisingNumber = _GponActiveAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 5),
    _GponActiveAlarmRaisingNumber_Type()
)
gponActiveAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponActiveAlarmRaisingNumber.setStatus("current")
_GponActiveAlarmFirstOccurTime_Type = DateAndTime
_GponActiveAlarmFirstOccurTime_Object = MibTableColumn
gponActiveAlarmFirstOccurTime = _GponActiveAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 6),
    _GponActiveAlarmFirstOccurTime_Type()
)
gponActiveAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmFirstOccurTime.setStatus("current")
_GponActiveAlarmLastOccurTime_Type = DateAndTime
_GponActiveAlarmLastOccurTime_Object = MibTableColumn
gponActiveAlarmLastOccurTime = _GponActiveAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 7),
    _GponActiveAlarmLastOccurTime_Type()
)
gponActiveAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmLastOccurTime.setStatus("current")
_GponActiveAlarmRepeats_Type = Counter32
_GponActiveAlarmRepeats_Object = MibTableColumn
gponActiveAlarmRepeats = _GponActiveAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 8),
    _GponActiveAlarmRepeats_Type()
)
gponActiveAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmRepeats.setStatus("current")
_GponActiveAlarmConfirm_Type = TruthValue
_GponActiveAlarmConfirm_Object = MibTableColumn
gponActiveAlarmConfirm = _GponActiveAlarmConfirm_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 9),
    _GponActiveAlarmConfirm_Type()
)
gponActiveAlarmConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponActiveAlarmConfirm.setStatus("current")


class _GponActiveAlarmAdditionalText_Type(OctetString):
    """Custom type gponActiveAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GponActiveAlarmAdditionalText_Type.__name__ = "OctetString"
_GponActiveAlarmAdditionalText_Object = MibTableColumn
gponActiveAlarmAdditionalText = _GponActiveAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 1, 1, 10),
    _GponActiveAlarmAdditionalText_Type()
)
gponActiveAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponActiveAlarmAdditionalText.setStatus("current")
_GponHistoryAlarmTable_Object = MibTable
gponHistoryAlarmTable = _GponHistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    gponHistoryAlarmTable.setStatus("current")
_GponHistoryAlarmEntry_Object = MibTableRow
gponHistoryAlarmEntry = _GponHistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1)
)
gponHistoryAlarmEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponHistoryAlarmSeqNum"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponHistoryAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    gponHistoryAlarmEntry.setStatus("current")
_GponHistoryAlarmSeqNum_Type = Unsigned32
_GponHistoryAlarmSeqNum_Object = MibTableColumn
gponHistoryAlarmSeqNum = _GponHistoryAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 1),
    _GponHistoryAlarmSeqNum_Type()
)
gponHistoryAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponHistoryAlarmSeqNum.setStatus("current")
_GponHistoryAlarmCode_Type = GponAlarmCode
_GponHistoryAlarmCode_Object = MibTableColumn
gponHistoryAlarmCode = _GponHistoryAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 2),
    _GponHistoryAlarmCode_Type()
)
gponHistoryAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmCode.setStatus("current")
_GponHistoryAlarmInstance_Type = GponAlarmInstance
_GponHistoryAlarmInstance_Object = MibTableColumn
gponHistoryAlarmInstance = _GponHistoryAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 3),
    _GponHistoryAlarmInstance_Type()
)
gponHistoryAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmInstance.setStatus("current")
_GponHistoryAlarmSeverity_Type = GponSeverityType
_GponHistoryAlarmSeverity_Object = MibTableColumn
gponHistoryAlarmSeverity = _GponHistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 4),
    _GponHistoryAlarmSeverity_Type()
)
gponHistoryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmSeverity.setStatus("current")
_GponHistoryAlarmRaisingNumber_Type = Unsigned32
_GponHistoryAlarmRaisingNumber_Object = MibTableColumn
gponHistoryAlarmRaisingNumber = _GponHistoryAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 5),
    _GponHistoryAlarmRaisingNumber_Type()
)
gponHistoryAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponHistoryAlarmRaisingNumber.setStatus("current")
_GponHistoryAlarmFirstOccurTime_Type = DateAndTime
_GponHistoryAlarmFirstOccurTime_Object = MibTableColumn
gponHistoryAlarmFirstOccurTime = _GponHistoryAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 6),
    _GponHistoryAlarmFirstOccurTime_Type()
)
gponHistoryAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmFirstOccurTime.setStatus("current")
_GponHistoryAlarmLastOccurTime_Type = DateAndTime
_GponHistoryAlarmLastOccurTime_Object = MibTableColumn
gponHistoryAlarmLastOccurTime = _GponHistoryAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 7),
    _GponHistoryAlarmLastOccurTime_Type()
)
gponHistoryAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmLastOccurTime.setStatus("current")
_GponHistoryAlarmRepeats_Type = Counter32
_GponHistoryAlarmRepeats_Object = MibTableColumn
gponHistoryAlarmRepeats = _GponHistoryAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 8),
    _GponHistoryAlarmRepeats_Type()
)
gponHistoryAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmRepeats.setStatus("current")
_GponHistoryAlarmCorrelationId_Type = Unsigned32
_GponHistoryAlarmCorrelationId_Object = MibTableColumn
gponHistoryAlarmCorrelationId = _GponHistoryAlarmCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 9),
    _GponHistoryAlarmCorrelationId_Type()
)
gponHistoryAlarmCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmCorrelationId.setStatus("current")


class _GponHistoryAlarmAdditionalText_Type(OctetString):
    """Custom type gponHistoryAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GponHistoryAlarmAdditionalText_Type.__name__ = "OctetString"
_GponHistoryAlarmAdditionalText_Object = MibTableColumn
gponHistoryAlarmAdditionalText = _GponHistoryAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 10),
    _GponHistoryAlarmAdditionalText_Type()
)
gponHistoryAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmAdditionalText.setStatus("current")
_GponHistoryAlarmClearTime_Type = DateAndTime
_GponHistoryAlarmClearTime_Object = MibTableColumn
gponHistoryAlarmClearTime = _GponHistoryAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 2, 1, 11),
    _GponHistoryAlarmClearTime_Type()
)
gponHistoryAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponHistoryAlarmClearTime.setStatus("current")
_GponEventLogTable_Object = MibTable
gponEventLogTable = _GponEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3)
)
if mibBuilder.loadTexts:
    gponEventLogTable.setStatus("current")
_GponEventLogEntry_Object = MibTableRow
gponEventLogEntry = _GponEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1)
)
gponEventLogEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponEventSeqNum"),
)
if mibBuilder.loadTexts:
    gponEventLogEntry.setStatus("current")
_GponEventSeqNum_Type = Unsigned32
_GponEventSeqNum_Object = MibTableColumn
gponEventSeqNum = _GponEventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1, 1),
    _GponEventSeqNum_Type()
)
gponEventSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponEventSeqNum.setStatus("current")
_GponEventCode_Type = GponAlarmCode
_GponEventCode_Object = MibTableColumn
gponEventCode = _GponEventCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1, 2),
    _GponEventCode_Type()
)
gponEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponEventCode.setStatus("current")
_GponEventInstance_Type = GponAlarmInstance
_GponEventInstance_Object = MibTableColumn
gponEventInstance = _GponEventInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1, 3),
    _GponEventInstance_Type()
)
gponEventInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponEventInstance.setStatus("current")
_GponEventOccurTime_Type = DateAndTime
_GponEventOccurTime_Object = MibTableColumn
gponEventOccurTime = _GponEventOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1, 4),
    _GponEventOccurTime_Type()
)
gponEventOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponEventOccurTime.setStatus("current")


class _GponEventAdditionalText_Type(OctetString):
    """Custom type gponEventAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GponEventAdditionalText_Type.__name__ = "OctetString"
_GponEventAdditionalText_Object = MibTableColumn
gponEventAdditionalText = _GponEventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 2, 3, 1, 5),
    _GponEventAdditionalText_Type()
)
gponEventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponEventAdditionalText.setStatus("current")
_GponManagementObjGroup_ObjectIdentity = ObjectIdentity
gponManagementObjGroup = _GponManagementObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3)
)
_GponManagementAddrTable_Object = MibTable
gponManagementAddrTable = _GponManagementAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    gponManagementAddrTable.setStatus("current")
_GponManagementAddrEntry_Object = MibTableRow
gponManagementAddrEntry = _GponManagementAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1, 1)
)
gponManagementAddrEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponManagementAddrName"),
)
if mibBuilder.loadTexts:
    gponManagementAddrEntry.setStatus("current")


class _GponManagementAddrName_Type(OctetString):
    """Custom type gponManagementAddrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GponManagementAddrName_Type.__name__ = "OctetString"
_GponManagementAddrName_Object = MibTableColumn
gponManagementAddrName = _GponManagementAddrName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1, 1, 1),
    _GponManagementAddrName_Type()
)
gponManagementAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponManagementAddrName.setStatus("current")
_GponManagementAddrTAddress_Type = TAddress
_GponManagementAddrTAddress_Object = MibTableColumn
gponManagementAddrTAddress = _GponManagementAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1, 1, 2),
    _GponManagementAddrTAddress_Type()
)
gponManagementAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrTAddress.setStatus("current")


class _GponManagementAddrCommunity_Type(OctetString):
    """Custom type gponManagementAddrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GponManagementAddrCommunity_Type.__name__ = "OctetString"
_GponManagementAddrCommunity_Object = MibTableColumn
gponManagementAddrCommunity = _GponManagementAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1, 1, 3),
    _GponManagementAddrCommunity_Type()
)
gponManagementAddrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrCommunity.setStatus("current")
_GponManagementAddrRowStatus_Type = RowStatus
_GponManagementAddrRowStatus_Object = MibTableColumn
gponManagementAddrRowStatus = _GponManagementAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 3, 1, 1, 4),
    _GponManagementAddrRowStatus_Type()
)
gponManagementAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponManagementAddrRowStatus.setStatus("current")
_GponTree_ObjectIdentity = ObjectIdentity
gponTree = _GponTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8)
)
_GponPonPortObjects_ObjectIdentity = ObjectIdentity
gponPonPortObjects = _GponPonPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3)
)
_GponOnuAuthenticationModeTable_Object = MibTable
gponOnuAuthenticationModeTable = _GponOnuAuthenticationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    gponOnuAuthenticationModeTable.setStatus("current")
_GponOnuAuthenticationModeEntry_Object = MibTableRow
gponOnuAuthenticationModeEntry = _GponOnuAuthenticationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1)
)
gponOnuAuthenticationModeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponAuthenDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponAuthenCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponAuthenPortIndex"),
)
if mibBuilder.loadTexts:
    gponOnuAuthenticationModeEntry.setStatus("current")
_GponAuthenDeviceIndex_Type = Integer32
_GponAuthenDeviceIndex_Object = MibTableColumn
gponAuthenDeviceIndex = _GponAuthenDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1, 1),
    _GponAuthenDeviceIndex_Type()
)
gponAuthenDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponAuthenDeviceIndex.setStatus("current")
_GponAuthenCardIndex_Type = GponCardIndex
_GponAuthenCardIndex_Object = MibTableColumn
gponAuthenCardIndex = _GponAuthenCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1, 2),
    _GponAuthenCardIndex_Type()
)
gponAuthenCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponAuthenCardIndex.setStatus("current")
_GponAuthenPortIndex_Type = GponPortIndex
_GponAuthenPortIndex_Object = MibTableColumn
gponAuthenPortIndex = _GponAuthenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1, 3),
    _GponAuthenPortIndex_Type()
)
gponAuthenPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponAuthenPortIndex.setStatus("current")


class _GponOnuAuthenMode_Type(Integer32):
    """Custom type gponOnuAuthenMode based on Integer32"""
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
        *(("sn", 1),
          ("sn-pwd", 2),
          ("loid", 3),
          ("loid-pwd", 4),
          ("pwd", 5),
          ("auto", 6))
    )


_GponOnuAuthenMode_Type.__name__ = "Integer32"
_GponOnuAuthenMode_Object = MibTableColumn
gponOnuAuthenMode = _GponOnuAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1, 4),
    _GponOnuAuthenMode_Type()
)
gponOnuAuthenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponOnuAuthenMode.setStatus("current")


class _GponAutoFindEnable_Type(Integer32):
    """Custom type gponAutoFindEnable based on Integer32"""
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


_GponAutoFindEnable_Type.__name__ = "Integer32"
_GponAutoFindEnable_Object = MibTableColumn
gponAutoFindEnable = _GponAutoFindEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 3, 4, 1, 5),
    _GponAutoFindEnable_Type()
)
gponAutoFindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponAutoFindEnable.setStatus("current")
_GponOnuObjects_ObjectIdentity = ObjectIdentity
gponOnuObjects = _GponOnuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4)
)
_GponOnuInfoTable_Object = MibTable
gponOnuInfoTable = _GponOnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    gponOnuInfoTable.setStatus("current")
_GponOnuInfoEntry_Object = MibTableRow
gponOnuInfoEntry = _GponOnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1)
)
gponOnuInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuDeviceIndex"),
)
if mibBuilder.loadTexts:
    gponOnuInfoEntry.setStatus("current")
_OnuDeviceIndex_Type = GponDeviceIndex
_OnuDeviceIndex_Object = MibTableColumn
onuDeviceIndex = _OnuDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 1),
    _OnuDeviceIndex_Type()
)
onuDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuDeviceIndex.setStatus("current")
_OnuName_Type = DisplayString
_OnuName_Object = MibTableColumn
onuName = _OnuName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 2),
    _OnuName_Type()
)
onuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuName.setStatus("current")


class _OnuSerialNum_Type(OctetString):
    """Custom type onuSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OnuSerialNum_Type.__name__ = "OctetString"
_OnuSerialNum_Object = MibTableColumn
onuSerialNum = _OnuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 3),
    _OnuSerialNum_Type()
)
onuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSerialNum.setStatus("current")


class _OnuType_Type(Integer32):
    """Custom type onuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("chassisBased", 2))
    )


_OnuType_Type.__name__ = "Integer32"
_OnuType_Object = MibTableColumn
onuType = _OnuType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 4),
    _OnuType_Type()
)
onuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuType.setStatus("current")


class _OnuVendorID_Type(OctetString):
    """Custom type onuVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_OnuVendorID_Type.__name__ = "OctetString"
_OnuVendorID_Object = MibTableColumn
onuVendorID = _OnuVendorID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 5),
    _OnuVendorID_Type()
)
onuVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVendorID.setStatus("current")


class _OnuEquipmentID_Type(OctetString):
    """Custom type onuEquipmentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_OnuEquipmentID_Type.__name__ = "OctetString"
_OnuEquipmentID_Object = MibTableColumn
onuEquipmentID = _OnuEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 6),
    _OnuEquipmentID_Type()
)
onuEquipmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuEquipmentID.setStatus("current")


class _OnuOperationStatus_Type(Integer32):
    """Custom type onuOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OnuOperationStatus_Type.__name__ = "Integer32"
_OnuOperationStatus_Object = MibTableColumn
onuOperationStatus = _OnuOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 7),
    _OnuOperationStatus_Type()
)
onuOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuOperationStatus.setStatus("current")


class _OnuAdminStatus_Type(Integer32):
    """Custom type onuAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OnuAdminStatus_Type.__name__ = "Integer32"
_OnuAdminStatus_Object = MibTableColumn
onuAdminStatus = _OnuAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 8),
    _OnuAdminStatus_Type()
)
onuAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAdminStatus.setStatus("current")
_OnuTestDistance_Type = Integer32
_OnuTestDistance_Object = MibTableColumn
onuTestDistance = _OnuTestDistance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 9),
    _OnuTestDistance_Type()
)
onuTestDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTestDistance.setStatus("current")
if mibBuilder.loadTexts:
    onuTestDistance.setUnits("Meter")


class _ResetONU_Type(Integer32):
    """Custom type resetONU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetONU_Type.__name__ = "Integer32"
_ResetONU_Object = MibTableColumn
resetONU = _ResetONU_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 10),
    _ResetONU_Type()
)
resetONU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetONU.setStatus("current")


class _OnuDeactive_Type(Integer32):
    """Custom type onuDeactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactive", 2))
    )


_OnuDeactive_Type.__name__ = "Integer32"
_OnuDeactive_Object = MibTableColumn
onuDeactive = _OnuDeactive_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 11),
    _OnuDeactive_Type()
)
onuDeactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuDeactive.setStatus("current")
_OnuTimeSinceLastRegister_Type = Counter32
_OnuTimeSinceLastRegister_Object = MibTableColumn
onuTimeSinceLastRegister = _OnuTimeSinceLastRegister_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 12),
    _OnuTimeSinceLastRegister_Type()
)
onuTimeSinceLastRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTimeSinceLastRegister.setStatus("current")
if mibBuilder.loadTexts:
    onuTimeSinceLastRegister.setUnits("second")
_OnuSysUpTime_Type = Counter32
_OnuSysUpTime_Object = MibTableColumn
onuSysUpTime = _OnuSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 13),
    _OnuSysUpTime_Type()
)
onuSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    onuSysUpTime.setUnits("second")
_OnuHardwareVersion_Type = DisplayString
_OnuHardwareVersion_Object = MibTableColumn
onuHardwareVersion = _OnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 14),
    _OnuHardwareVersion_Type()
)
onuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuHardwareVersion.setStatus("current")
_OnuPerfStats15minuteEnable_Type = TruthValue
_OnuPerfStats15minuteEnable_Object = MibTableColumn
onuPerfStats15minuteEnable = _OnuPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 15),
    _OnuPerfStats15minuteEnable_Type()
)
onuPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPerfStats15minuteEnable.setStatus("current")
_OnuPerfStats24hourEnable_Type = TruthValue
_OnuPerfStats24hourEnable_Object = MibTableColumn
onuPerfStats24hourEnable = _OnuPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 1, 1, 16),
    _OnuPerfStats24hourEnable_Type()
)
onuPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPerfStats24hourEnable.setStatus("current")
_OnuInfoSoftwareTable_Object = MibTable
onuInfoSoftwareTable = _OnuInfoSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2)
)
if mibBuilder.loadTexts:
    onuInfoSoftwareTable.setStatus("current")
_OnuInfoSoftwareEntry_Object = MibTableRow
onuInfoSoftwareEntry = _OnuInfoSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1)
)
onuInfoSoftwareEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuSoftwareDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuInfoSoftwareEntry.setStatus("current")
_OnuSoftwareDeviceIndex_Type = Integer32
_OnuSoftwareDeviceIndex_Object = MibTableColumn
onuSoftwareDeviceIndex = _OnuSoftwareDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 1),
    _OnuSoftwareDeviceIndex_Type()
)
onuSoftwareDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuSoftwareDeviceIndex.setStatus("current")
_OnuSoftware0Version_Type = DisplayString
_OnuSoftware0Version_Object = MibTableColumn
onuSoftware0Version = _OnuSoftware0Version_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 2),
    _OnuSoftware0Version_Type()
)
onuSoftware0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSoftware0Version.setStatus("current")


class _OnuSoftware0Valid_Type(Integer32):
    """Custom type onuSoftware0Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_OnuSoftware0Valid_Type.__name__ = "Integer32"
_OnuSoftware0Valid_Object = MibTableColumn
onuSoftware0Valid = _OnuSoftware0Valid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 3),
    _OnuSoftware0Valid_Type()
)
onuSoftware0Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSoftware0Valid.setStatus("current")


class _OnuSoftware0Active_Type(Integer32):
    """Custom type onuSoftware0Active based on Integer32"""
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


_OnuSoftware0Active_Type.__name__ = "Integer32"
_OnuSoftware0Active_Object = MibTableColumn
onuSoftware0Active = _OnuSoftware0Active_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 4),
    _OnuSoftware0Active_Type()
)
onuSoftware0Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSoftware0Active.setStatus("current")


class _OnuSoftware0Commited_Type(Integer32):
    """Custom type onuSoftware0Commited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncommitted", 0),
          ("committed", 1))
    )


_OnuSoftware0Commited_Type.__name__ = "Integer32"
_OnuSoftware0Commited_Object = MibTableColumn
onuSoftware0Commited = _OnuSoftware0Commited_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 5),
    _OnuSoftware0Commited_Type()
)
onuSoftware0Commited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSoftware0Commited.setStatus("current")
_OnuSoftware1Version_Type = DisplayString
_OnuSoftware1Version_Object = MibTableColumn
onuSoftware1Version = _OnuSoftware1Version_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 6),
    _OnuSoftware1Version_Type()
)
onuSoftware1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSoftware1Version.setStatus("current")


class _OnuSoftware1Valid_Type(Integer32):
    """Custom type onuSoftware1Valid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_OnuSoftware1Valid_Type.__name__ = "Integer32"
_OnuSoftware1Valid_Object = MibTableColumn
onuSoftware1Valid = _OnuSoftware1Valid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 7),
    _OnuSoftware1Valid_Type()
)
onuSoftware1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSoftware1Valid.setStatus("current")


class _OnuSoftware1Active_Type(Integer32):
    """Custom type onuSoftware1Active based on Integer32"""
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


_OnuSoftware1Active_Type.__name__ = "Integer32"
_OnuSoftware1Active_Object = MibTableColumn
onuSoftware1Active = _OnuSoftware1Active_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 8),
    _OnuSoftware1Active_Type()
)
onuSoftware1Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSoftware1Active.setStatus("current")


class _OnuSoftware1Commited_Type(Integer32):
    """Custom type onuSoftware1Commited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uncommitted", 0),
          ("committed", 1))
    )


_OnuSoftware1Commited_Type.__name__ = "Integer32"
_OnuSoftware1Commited_Object = MibTableColumn
onuSoftware1Commited = _OnuSoftware1Commited_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 2, 1, 9),
    _OnuSoftware1Commited_Type()
)
onuSoftware1Commited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSoftware1Commited.setStatus("current")
_OnuIpHostTable_Object = MibTable
onuIpHostTable = _OnuIpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3)
)
if mibBuilder.loadTexts:
    onuIpHostTable.setStatus("current")
_OnuIpHostEntry_Object = MibTableRow
onuIpHostEntry = _OnuIpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1)
)
onuIpHostEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuIpHostDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuIpHostIndex"),
)
if mibBuilder.loadTexts:
    onuIpHostEntry.setStatus("current")
_OnuIpHostDeviceIndex_Type = Integer32
_OnuIpHostDeviceIndex_Object = MibTableColumn
onuIpHostDeviceIndex = _OnuIpHostDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 1),
    _OnuIpHostDeviceIndex_Type()
)
onuIpHostDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIpHostDeviceIndex.setStatus("current")


class _OnuIpHostIndex_Type(Integer32):
    """Custom type onuIpHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OnuIpHostIndex_Type.__name__ = "Integer32"
_OnuIpHostIndex_Object = MibTableColumn
onuIpHostIndex = _OnuIpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 2),
    _OnuIpHostIndex_Type()
)
onuIpHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIpHostIndex.setStatus("current")


class _OnuIpHostAddressConfigMode_Type(Integer32):
    """Custom type onuIpHostAddressConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_OnuIpHostAddressConfigMode_Type.__name__ = "Integer32"
_OnuIpHostAddressConfigMode_Object = MibTableColumn
onuIpHostAddressConfigMode = _OnuIpHostAddressConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 3),
    _OnuIpHostAddressConfigMode_Type()
)
onuIpHostAddressConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostAddressConfigMode.setStatus("current")
_OnuIpHostAddress_Type = IpAddress
_OnuIpHostAddress_Object = MibTableColumn
onuIpHostAddress = _OnuIpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 4),
    _OnuIpHostAddress_Type()
)
onuIpHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostAddress.setStatus("current")
_OnuIpHostSubnetMask_Type = IpAddress
_OnuIpHostSubnetMask_Object = MibTableColumn
onuIpHostSubnetMask = _OnuIpHostSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 5),
    _OnuIpHostSubnetMask_Type()
)
onuIpHostSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostSubnetMask.setStatus("current")
_OnuIpHostGateway_Type = IpAddress
_OnuIpHostGateway_Object = MibTableColumn
onuIpHostGateway = _OnuIpHostGateway_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 6),
    _OnuIpHostGateway_Type()
)
onuIpHostGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostGateway.setStatus("current")
_OnuIpHostPrimaryDNS_Type = IpAddress
_OnuIpHostPrimaryDNS_Object = MibTableColumn
onuIpHostPrimaryDNS = _OnuIpHostPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 7),
    _OnuIpHostPrimaryDNS_Type()
)
onuIpHostPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostPrimaryDNS.setStatus("current")
_OnuIpHostSecondaryDNS_Type = IpAddress
_OnuIpHostSecondaryDNS_Object = MibTableColumn
onuIpHostSecondaryDNS = _OnuIpHostSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 8),
    _OnuIpHostSecondaryDNS_Type()
)
onuIpHostSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostSecondaryDNS.setStatus("current")


class _OnuIpHostVlanTagPriority_Type(Integer32):
    """Custom type onuIpHostVlanTagPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OnuIpHostVlanTagPriority_Type.__name__ = "Integer32"
_OnuIpHostVlanTagPriority_Object = MibTableColumn
onuIpHostVlanTagPriority = _OnuIpHostVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 9),
    _OnuIpHostVlanTagPriority_Type()
)
onuIpHostVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostVlanTagPriority.setStatus("current")


class _OnuIpHostVlanPvid_Type(Integer32):
    """Custom type onuIpHostVlanPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OnuIpHostVlanPvid_Type.__name__ = "Integer32"
_OnuIpHostVlanPvid_Object = MibTableColumn
onuIpHostVlanPvid = _OnuIpHostVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 10),
    _OnuIpHostVlanPvid_Type()
)
onuIpHostVlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpHostVlanPvid.setStatus("current")
_OnuIpHostMacAddress_Type = MacAddress
_OnuIpHostMacAddress_Object = MibTableColumn
onuIpHostMacAddress = _OnuIpHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 11),
    _OnuIpHostMacAddress_Type()
)
onuIpHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIpHostMacAddress.setStatus("current")
_OnuIpHostRowStatus_Type = RowStatus
_OnuIpHostRowStatus_Object = MibTableColumn
onuIpHostRowStatus = _OnuIpHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 3, 1, 12),
    _OnuIpHostRowStatus_Type()
)
onuIpHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuIpHostRowStatus.setStatus("current")
_GponOnuPonPortOpticalTransmissionPropertyTable_Object = MibTable
gponOnuPonPortOpticalTransmissionPropertyTable = _GponOnuPonPortOpticalTransmissionPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4)
)
if mibBuilder.loadTexts:
    gponOnuPonPortOpticalTransmissionPropertyTable.setStatus("current")
_GponOnuPonPortOpticalTransmissionPropertyEntry_Object = MibTableRow
gponOnuPonPortOpticalTransmissionPropertyEntry = _GponOnuPonPortOpticalTransmissionPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1)
)
gponOnuPonPortOpticalTransmissionPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuPonPortOpticalTransmissionPropertyDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuPonPortOpticalTransmissionPropertyCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuPonPortOpticalTransmissionPropertyPortIndex"),
)
if mibBuilder.loadTexts:
    gponOnuPonPortOpticalTransmissionPropertyEntry.setStatus("current")
_OnuPonPortOpticalTransmissionPropertyDeviceIndex_Type = GponDeviceIndex
_OnuPonPortOpticalTransmissionPropertyDeviceIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyDeviceIndex = _OnuPonPortOpticalTransmissionPropertyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 1),
    _OnuPonPortOpticalTransmissionPropertyDeviceIndex_Type()
)
onuPonPortOpticalTransmissionPropertyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyDeviceIndex.setStatus("current")
_OnuPonPortOpticalTransmissionPropertyCardIndex_Type = Integer32
_OnuPonPortOpticalTransmissionPropertyCardIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyCardIndex = _OnuPonPortOpticalTransmissionPropertyCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 2),
    _OnuPonPortOpticalTransmissionPropertyCardIndex_Type()
)
onuPonPortOpticalTransmissionPropertyCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyCardIndex.setStatus("current")
_OnuPonPortOpticalTransmissionPropertyPortIndex_Type = Integer32
_OnuPonPortOpticalTransmissionPropertyPortIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyPortIndex = _OnuPonPortOpticalTransmissionPropertyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 3),
    _OnuPonPortOpticalTransmissionPropertyPortIndex_Type()
)
onuPonPortOpticalTransmissionPropertyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyPortIndex.setStatus("current")
_OnuReceivedOpticalPower_Type = Integer32
_OnuReceivedOpticalPower_Object = MibTableColumn
onuReceivedOpticalPower = _OnuReceivedOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 4),
    _OnuReceivedOpticalPower_Type()
)
onuReceivedOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReceivedOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    onuReceivedOpticalPower.setUnits("centi-dBm")
_OnuTramsmittedOpticalPower_Type = Integer32
_OnuTramsmittedOpticalPower_Object = MibTableColumn
onuTramsmittedOpticalPower = _OnuTramsmittedOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 5),
    _OnuTramsmittedOpticalPower_Type()
)
onuTramsmittedOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTramsmittedOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    onuTramsmittedOpticalPower.setUnits("centi-dBm")
_OnuBiasCurrent_Type = Integer32
_OnuBiasCurrent_Object = MibTableColumn
onuBiasCurrent = _OnuBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 6),
    _OnuBiasCurrent_Type()
)
onuBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    onuBiasCurrent.setUnits("centi-mA")
_OnuWorkingVoltage_Type = Integer32
_OnuWorkingVoltage_Object = MibTableColumn
onuWorkingVoltage = _OnuWorkingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 7),
    _OnuWorkingVoltage_Type()
)
onuWorkingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuWorkingVoltage.setStatus("current")
if mibBuilder.loadTexts:
    onuWorkingVoltage.setUnits("centi-mV")
_OnuWorkingTemperature_Type = Integer32
_OnuWorkingTemperature_Object = MibTableColumn
onuWorkingTemperature = _OnuWorkingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 4, 1, 8),
    _OnuWorkingTemperature_Type()
)
onuWorkingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuWorkingTemperature.setStatus("current")
if mibBuilder.loadTexts:
    onuWorkingTemperature.setUnits("Centi-degree centigrade")
_OnuCapabilityTable_Object = MibTable
onuCapabilityTable = _OnuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5)
)
if mibBuilder.loadTexts:
    onuCapabilityTable.setStatus("current")
_OnuCapabilityEntry_Object = MibTableRow
onuCapabilityEntry = _OnuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1)
)
onuCapabilityEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuCapabilityDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuCapabilityEntry.setStatus("current")
_OnuCapabilityDeviceIndex_Type = GponDeviceIndex
_OnuCapabilityDeviceIndex_Object = MibTableColumn
onuCapabilityDeviceIndex = _OnuCapabilityDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 1),
    _OnuCapabilityDeviceIndex_Type()
)
onuCapabilityDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuCapabilityDeviceIndex.setStatus("current")
_OnuOMCCVersion_Type = Integer32
_OnuOMCCVersion_Object = MibTableColumn
onuOMCCVersion = _OnuOMCCVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 2),
    _OnuOMCCVersion_Type()
)
onuOMCCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuOMCCVersion.setStatus("current")
_OnuTotalEthNum_Type = Integer32
_OnuTotalEthNum_Object = MibTableColumn
onuTotalEthNum = _OnuTotalEthNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 3),
    _OnuTotalEthNum_Type()
)
onuTotalEthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalEthNum.setStatus("current")
_OnuTotalWlanNum_Type = Integer32
_OnuTotalWlanNum_Object = MibTableColumn
onuTotalWlanNum = _OnuTotalWlanNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 4),
    _OnuTotalWlanNum_Type()
)
onuTotalWlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalWlanNum.setStatus("current")
_OnuTotalCatvNum_Type = Integer32
_OnuTotalCatvNum_Object = MibTableColumn
onuTotalCatvNum = _OnuTotalCatvNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 5),
    _OnuTotalCatvNum_Type()
)
onuTotalCatvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalCatvNum.setStatus("current")
_OnuTotalVeipNum_Type = Integer32
_OnuTotalVeipNum_Object = MibTableColumn
onuTotalVeipNum = _OnuTotalVeipNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 6),
    _OnuTotalVeipNum_Type()
)
onuTotalVeipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalVeipNum.setStatus("current")
_OnuIpHostNum_Type = Integer32
_OnuIpHostNum_Object = MibTableColumn
onuIpHostNum = _OnuIpHostNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 7),
    _OnuIpHostNum_Type()
)
onuIpHostNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIpHostNum.setStatus("current")
_OnuTrafficMgmtOption_Type = Integer32
_OnuTrafficMgmtOption_Object = MibTableColumn
onuTrafficMgmtOption = _OnuTrafficMgmtOption_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 8),
    _OnuTrafficMgmtOption_Type()
)
onuTrafficMgmtOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTrafficMgmtOption.setStatus("current")
_OnuTotalGEMPortNum_Type = Integer32
_OnuTotalGEMPortNum_Object = MibTableColumn
onuTotalGEMPortNum = _OnuTotalGEMPortNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 9),
    _OnuTotalGEMPortNum_Type()
)
onuTotalGEMPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalGEMPortNum.setStatus("current")
_OnuTotalTContNum_Type = Integer32
_OnuTotalTContNum_Object = MibTableColumn
onuTotalTContNum = _OnuTotalTContNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 10),
    _OnuTotalTContNum_Type()
)
onuTotalTContNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTotalTContNum.setStatus("current")


class _OnuConnectCapbility_Type(Bits):
    """Custom type onuConnectCapbility based on Bits"""
    namedValues = NamedValues(
        *(("nto1", 0),
          ("ntom", 3),
          ("ntop", 5),
          ("ntomp", 6))
    )

_OnuConnectCapbility_Type.__name__ = "Bits"
_OnuConnectCapbility_Object = MibTableColumn
onuConnectCapbility = _OnuConnectCapbility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 11),
    _OnuConnectCapbility_Type()
)
onuConnectCapbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuConnectCapbility.setStatus("current")


class _OnuQosFlexibility_Type(Bits):
    """Custom type onuQosFlexibility based on Bits"""
    namedValues = NamedValues(
        ("priorityQueueME", 1)
    )

_OnuQosFlexibility_Type.__name__ = "Bits"
_OnuQosFlexibility_Object = MibTableColumn
onuQosFlexibility = _OnuQosFlexibility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 5, 1, 12),
    _OnuQosFlexibility_Type()
)
onuQosFlexibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuQosFlexibility.setStatus("current")
_OnuAuthenticationManagement_ObjectIdentity = ObjectIdentity
onuAuthenticationManagement = _OnuAuthenticationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6)
)
if mibBuilder.loadTexts:
    onuAuthenticationManagement.setStatus("current")
_OnuAuthenticationConfigTable_Object = MibTable
onuAuthenticationConfigTable = _OnuAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1)
)
if mibBuilder.loadTexts:
    onuAuthenticationConfigTable.setStatus("current")
_OnuAuthenticationConfigEntry_Object = MibTableRow
onuAuthenticationConfigEntry = _OnuAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1)
)
onuAuthenticationConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuAuthenOnuId"),
)
if mibBuilder.loadTexts:
    onuAuthenticationConfigEntry.setStatus("current")
_OnuAuthenOnuId_Type = Integer32
_OnuAuthenOnuId_Object = MibTableColumn
onuAuthenOnuId = _OnuAuthenOnuId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 1),
    _OnuAuthenOnuId_Type()
)
onuAuthenOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAuthenOnuId.setStatus("current")


class _OnuAuthenSN_Type(OctetString):
    """Custom type onuAuthenSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OnuAuthenSN_Type.__name__ = "OctetString"
_OnuAuthenSN_Object = MibTableColumn
onuAuthenSN = _OnuAuthenSN_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 2),
    _OnuAuthenSN_Type()
)
onuAuthenSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenSN.setStatus("current")
_OnuAuthenPassword_Type = DisplayString
_OnuAuthenPassword_Object = MibTableColumn
onuAuthenPassword = _OnuAuthenPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 3),
    _OnuAuthenPassword_Type()
)
onuAuthenPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenPassword.setStatus("current")
_OnuAuthenLoid_Type = DisplayString
_OnuAuthenLoid_Object = MibTableColumn
onuAuthenLoid = _OnuAuthenLoid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 4),
    _OnuAuthenLoid_Type()
)
onuAuthenLoid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenLoid.setStatus("current")
_OnuAuthenLoidPassword_Type = DisplayString
_OnuAuthenLoidPassword_Object = MibTableColumn
onuAuthenLoidPassword = _OnuAuthenLoidPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 5),
    _OnuAuthenLoidPassword_Type()
)
onuAuthenLoidPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenLoidPassword.setStatus("current")
_OnuAuthenLineProfileId_Type = Integer32
_OnuAuthenLineProfileId_Object = MibTableColumn
onuAuthenLineProfileId = _OnuAuthenLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 6),
    _OnuAuthenLineProfileId_Type()
)
onuAuthenLineProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenLineProfileId.setStatus("current")
_OnuAuthenSrvProfileId_Type = Integer32
_OnuAuthenSrvProfileId_Object = MibTableColumn
onuAuthenSrvProfileId = _OnuAuthenSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 7),
    _OnuAuthenSrvProfileId_Type()
)
onuAuthenSrvProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenSrvProfileId.setStatus("current")
_OnuAuthenRowStatus_Type = RowStatus
_OnuAuthenRowStatus_Object = MibTableColumn
onuAuthenRowStatus = _OnuAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 6, 1, 1, 8),
    _OnuAuthenRowStatus_Type()
)
onuAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenRowStatus.setStatus("current")
_OnuAutoFindTable_Object = MibTable
onuAutoFindTable = _OnuAutoFindTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7)
)
if mibBuilder.loadTexts:
    onuAutoFindTable.setStatus("current")
_OnuAutoFindEntry_Object = MibTableRow
onuAutoFindEntry = _OnuAutoFindEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1)
)
onuAutoFindEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuAutoFindOnuIndex"),
)
if mibBuilder.loadTexts:
    onuAutoFindEntry.setStatus("current")
_OnuAutoFindOnuIndex_Type = Integer32
_OnuAutoFindOnuIndex_Object = MibTableColumn
onuAutoFindOnuIndex = _OnuAutoFindOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 1),
    _OnuAutoFindOnuIndex_Type()
)
onuAutoFindOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAutoFindOnuIndex.setStatus("current")
_OnuAutoFindOnuType_Type = DisplayString
_OnuAutoFindOnuType_Object = MibTableColumn
onuAutoFindOnuType = _OnuAutoFindOnuType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 2),
    _OnuAutoFindOnuType_Type()
)
onuAutoFindOnuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindOnuType.setStatus("current")
_OnuAutoFindSerialNumber_Type = DisplayString
_OnuAutoFindSerialNumber_Object = MibTableColumn
onuAutoFindSerialNumber = _OnuAutoFindSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 3),
    _OnuAutoFindSerialNumber_Type()
)
onuAutoFindSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindSerialNumber.setStatus("current")
_OnuAutoFindPassword_Type = DisplayString
_OnuAutoFindPassword_Object = MibTableColumn
onuAutoFindPassword = _OnuAutoFindPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 4),
    _OnuAutoFindPassword_Type()
)
onuAutoFindPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindPassword.setStatus("current")
_OnuAutoFindLoid_Type = DisplayString
_OnuAutoFindLoid_Object = MibTableColumn
onuAutoFindLoid = _OnuAutoFindLoid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 5),
    _OnuAutoFindLoid_Type()
)
onuAutoFindLoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindLoid.setStatus("current")
_OnuAutoFindLoidPassword_Type = DisplayString
_OnuAutoFindLoidPassword_Object = MibTableColumn
onuAutoFindLoidPassword = _OnuAutoFindLoidPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 6),
    _OnuAutoFindLoidPassword_Type()
)
onuAutoFindLoidPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindLoidPassword.setStatus("current")
_OnuAutoFindTime_Type = DateAndTime
_OnuAutoFindTime_Object = MibTableColumn
onuAutoFindTime = _OnuAutoFindTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 7),
    _OnuAutoFindTime_Type()
)
onuAutoFindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindTime.setStatus("current")
_OnuAutoFindSoftwareVersion_Type = DisplayString
_OnuAutoFindSoftwareVersion_Object = MibTableColumn
onuAutoFindSoftwareVersion = _OnuAutoFindSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 8),
    _OnuAutoFindSoftwareVersion_Type()
)
onuAutoFindSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindSoftwareVersion.setStatus("current")
_OnuAutoFindHardwareVersion_Type = DisplayString
_OnuAutoFindHardwareVersion_Object = MibTableColumn
onuAutoFindHardwareVersion = _OnuAutoFindHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 7, 1, 9),
    _OnuAutoFindHardwareVersion_Type()
)
onuAutoFindHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindHardwareVersion.setStatus("current")
_OnuAutoAuthenticationTable_Object = MibTable
onuAutoAuthenticationTable = _OnuAutoAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8)
)
if mibBuilder.loadTexts:
    onuAutoAuthenticationTable.setStatus("current")
_OnuAutoAuthenticationEntry_Object = MibTableRow
onuAutoAuthenticationEntry = _OnuAutoAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1)
)
onuAutoAuthenticationEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuAutoAuthenIndex"),
)
if mibBuilder.loadTexts:
    onuAutoAuthenticationEntry.setStatus("current")
_OnuAutoAuthenIndex_Type = Integer32
_OnuAutoAuthenIndex_Object = MibTableColumn
onuAutoAuthenIndex = _OnuAutoAuthenIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 1),
    _OnuAutoAuthenIndex_Type()
)
onuAutoAuthenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAutoAuthenIndex.setStatus("current")
_OnuAutoAuthenPortlist_Type = DisplayString
_OnuAutoAuthenPortlist_Object = MibTableColumn
onuAutoAuthenPortlist = _OnuAutoAuthenPortlist_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 2),
    _OnuAutoAuthenPortlist_Type()
)
onuAutoAuthenPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenPortlist.setStatus("current")
_OnuAutoAuthenOnuType_Type = DisplayString
_OnuAutoAuthenOnuType_Object = MibTableColumn
onuAutoAuthenOnuType = _OnuAutoAuthenOnuType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 3),
    _OnuAutoAuthenOnuType_Type()
)
onuAutoAuthenOnuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenOnuType.setStatus("current")
_OnuAutoAuthenEthNum_Type = Integer32
_OnuAutoAuthenEthNum_Object = MibTableColumn
onuAutoAuthenEthNum = _OnuAutoAuthenEthNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 4),
    _OnuAutoAuthenEthNum_Type()
)
onuAutoAuthenEthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenEthNum.setStatus("current")
_OnuAutoAuthenWlanNum_Type = Integer32
_OnuAutoAuthenWlanNum_Object = MibTableColumn
onuAutoAuthenWlanNum = _OnuAutoAuthenWlanNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 5),
    _OnuAutoAuthenWlanNum_Type()
)
onuAutoAuthenWlanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenWlanNum.setStatus("current")
_OnuAutoAuthenCatvNum_Type = Integer32
_OnuAutoAuthenCatvNum_Object = MibTableColumn
onuAutoAuthenCatvNum = _OnuAutoAuthenCatvNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 6),
    _OnuAutoAuthenCatvNum_Type()
)
onuAutoAuthenCatvNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenCatvNum.setStatus("current")
_OnuAutoAuthenVeipNum_Type = Integer32
_OnuAutoAuthenVeipNum_Object = MibTableColumn
onuAutoAuthenVeipNum = _OnuAutoAuthenVeipNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 7),
    _OnuAutoAuthenVeipNum_Type()
)
onuAutoAuthenVeipNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenVeipNum.setStatus("current")
_OnuAutoAuthenLineProfileId_Type = Integer32
_OnuAutoAuthenLineProfileId_Object = MibTableColumn
onuAutoAuthenLineProfileId = _OnuAutoAuthenLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 8),
    _OnuAutoAuthenLineProfileId_Type()
)
onuAutoAuthenLineProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenLineProfileId.setStatus("current")
_OnuAutoAuthenSrvProfileId_Type = Integer32
_OnuAutoAuthenSrvProfileId_Object = MibTableColumn
onuAutoAuthenSrvProfileId = _OnuAutoAuthenSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 9),
    _OnuAutoAuthenSrvProfileId_Type()
)
onuAutoAuthenSrvProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAutoAuthenSrvProfileId.setStatus("current")
_OnuAutoAuthenRowStatus_Type = RowStatus
_OnuAutoAuthenRowStatus_Object = MibTableColumn
onuAutoAuthenRowStatus = _OnuAutoAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 4, 8, 1, 10),
    _OnuAutoAuthenRowStatus_Type()
)
onuAutoAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAutoAuthenRowStatus.setStatus("current")
_GponUniObjects_ObjectIdentity = ObjectIdentity
gponUniObjects = _GponUniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5)
)
_EthAttributeTable_Object = MibTable
ethAttributeTable = _EthAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1)
)
if mibBuilder.loadTexts:
    ethAttributeTable.setStatus("current")
_EthAttributeEntry_Object = MibTableRow
ethAttributeEntry = _EthAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1)
)
ethAttributeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "ethAttributeDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "ethAttributeCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "ethAttributePortIndex"),
)
if mibBuilder.loadTexts:
    ethAttributeEntry.setStatus("current")
_EthAttributeDeviceIndex_Type = GponDeviceIndex
_EthAttributeDeviceIndex_Object = MibTableColumn
ethAttributeDeviceIndex = _EthAttributeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 1),
    _EthAttributeDeviceIndex_Type()
)
ethAttributeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethAttributeDeviceIndex.setStatus("current")
_EthAttributeCardIndex_Type = GponCardIndex
_EthAttributeCardIndex_Object = MibTableColumn
ethAttributeCardIndex = _EthAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 2),
    _EthAttributeCardIndex_Type()
)
ethAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethAttributeCardIndex.setStatus("current")
_EthAttributePortIndex_Type = GponPortIndex
_EthAttributePortIndex_Object = MibTableColumn
ethAttributePortIndex = _EthAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 3),
    _EthAttributePortIndex_Type()
)
ethAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethAttributePortIndex.setStatus("current")


class _EthAdminStatus_Type(Integer32):
    """Custom type ethAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_EthAdminStatus_Type.__name__ = "Integer32"
_EthAdminStatus_Object = MibTableColumn
ethAdminStatus = _EthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 4),
    _EthAdminStatus_Type()
)
ethAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAdminStatus.setStatus("current")


class _EthOperationStatus_Type(Integer32):
    """Custom type ethOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_EthOperationStatus_Type.__name__ = "Integer32"
_EthOperationStatus_Object = MibTableColumn
ethOperationStatus = _EthOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 5),
    _EthOperationStatus_Type()
)
ethOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOperationStatus.setStatus("current")
_EthDuplexRate_Type = Integer32
_EthDuplexRate_Object = MibTableColumn
ethDuplexRate = _EthDuplexRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 6),
    _EthDuplexRate_Type()
)
ethDuplexRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDuplexRate.setStatus("current")
_EthPerfStats15minuteEnable_Type = TruthValue
_EthPerfStats15minuteEnable_Object = MibTableColumn
ethPerfStats15minuteEnable = _EthPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 7),
    _EthPerfStats15minuteEnable_Type()
)
ethPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPerfStats15minuteEnable.setStatus("current")
_EthPerfStats24hourEnable_Type = TruthValue
_EthPerfStats24hourEnable_Object = MibTableColumn
ethPerfStats24hourEnable = _EthPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 5, 1, 1, 8),
    _EthPerfStats24hourEnable_Type()
)
ethPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPerfStats24hourEnable.setStatus("current")
_GponIgmpManagementObjects_ObjectIdentity = ObjectIdentity
gponIgmpManagementObjects = _GponIgmpManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6)
)
_GponOnuIgmpProfile_ObjectIdentity = ObjectIdentity
gponOnuIgmpProfile = _GponOnuIgmpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4)
)
if mibBuilder.loadTexts:
    gponOnuIgmpProfile.setStatus("current")
_GponOnuIgmpProfileTable_Object = MibTable
gponOnuIgmpProfileTable = _GponOnuIgmpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1)
)
if mibBuilder.loadTexts:
    gponOnuIgmpProfileTable.setStatus("current")
_GponOnuIgmpProfileEntry_Object = MibTableRow
gponOnuIgmpProfileEntry = _GponOnuIgmpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1)
)
gponOnuIgmpProfileEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponOnuIgmpProfileIndex"),
)
if mibBuilder.loadTexts:
    gponOnuIgmpProfileEntry.setStatus("current")
_GponOnuIgmpProfileIndex_Type = Integer32
_GponOnuIgmpProfileIndex_Object = MibTableColumn
gponOnuIgmpProfileIndex = _GponOnuIgmpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 1),
    _GponOnuIgmpProfileIndex_Type()
)
gponOnuIgmpProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuIgmpProfileIndex.setStatus("current")
_GponOnuIgmpProfileName_Type = DisplayString
_GponOnuIgmpProfileName_Object = MibTableColumn
gponOnuIgmpProfileName = _GponOnuIgmpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 2),
    _GponOnuIgmpProfileName_Type()
)
gponOnuIgmpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponOnuIgmpProfileName.setStatus("current")


class _GponOnuIgmpVersion_Type(Integer32):
    """Custom type gponOnuIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmp-v1", 1),
          ("igmp-v2", 2),
          ("igmp-v3", 3))
    )


_GponOnuIgmpVersion_Type.__name__ = "Integer32"
_GponOnuIgmpVersion_Object = MibTableColumn
gponOnuIgmpVersion = _GponOnuIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 3),
    _GponOnuIgmpVersion_Type()
)
gponOnuIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpVersion.setStatus("current")


class _GponOnuIgmpFunction_Type(Integer32):
    """Custom type gponOnuIgmpFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snooping", 1),
          ("spr", 2),
          ("proxy", 3))
    )


_GponOnuIgmpFunction_Type.__name__ = "Integer32"
_GponOnuIgmpFunction_Object = MibTableColumn
gponOnuIgmpFunction = _GponOnuIgmpFunction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 4),
    _GponOnuIgmpFunction_Type()
)
gponOnuIgmpFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpFunction.setStatus("current")


class _GponOnuIgmpImmediateLeave_Type(Integer32):
    """Custom type gponOnuIgmpImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_GponOnuIgmpImmediateLeave_Type.__name__ = "Integer32"
_GponOnuIgmpImmediateLeave_Object = MibTableColumn
gponOnuIgmpImmediateLeave = _GponOnuIgmpImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 5),
    _GponOnuIgmpImmediateLeave_Type()
)
gponOnuIgmpImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpImmediateLeave.setStatus("current")


class _GponOnuIgmpUpstreamProtoTCI_Type(Integer32):
    """Custom type gponOnuIgmpUpstreamProtoTCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GponOnuIgmpUpstreamProtoTCI_Type.__name__ = "Integer32"
_GponOnuIgmpUpstreamProtoTCI_Object = MibTableColumn
gponOnuIgmpUpstreamProtoTCI = _GponOnuIgmpUpstreamProtoTCI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 6),
    _GponOnuIgmpUpstreamProtoTCI_Type()
)
gponOnuIgmpUpstreamProtoTCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpUpstreamProtoTCI.setStatus("current")


class _GponOnuIgmpUpstreamProtoTagControl_Type(Integer32):
    """Custom type gponOnuIgmpUpstreamProtoTagControl based on Integer32"""
    defaultValue = 1

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
        *(("pass-through", 1),
          ("add-vlan", 2),
          ("replace-tci", 3),
          ("replace-vlan", 4))
    )


_GponOnuIgmpUpstreamProtoTagControl_Type.__name__ = "Integer32"
_GponOnuIgmpUpstreamProtoTagControl_Object = MibTableColumn
gponOnuIgmpUpstreamProtoTagControl = _GponOnuIgmpUpstreamProtoTagControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 7),
    _GponOnuIgmpUpstreamProtoTagControl_Type()
)
gponOnuIgmpUpstreamProtoTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpUpstreamProtoTagControl.setStatus("current")


class _GponOnuIgmpUpstreamProtoRate_Type(Integer32):
    """Custom type gponOnuIgmpUpstreamProtoRate based on Integer32"""
    defaultValue = 0


_GponOnuIgmpUpstreamProtoRate_Type.__name__ = "Integer32"
_GponOnuIgmpUpstreamProtoRate_Object = MibTableColumn
gponOnuIgmpUpstreamProtoRate = _GponOnuIgmpUpstreamProtoRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 8),
    _GponOnuIgmpUpstreamProtoRate_Type()
)
gponOnuIgmpUpstreamProtoRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpUpstreamProtoRate.setStatus("current")
if mibBuilder.loadTexts:
    gponOnuIgmpUpstreamProtoRate.setUnits("pps")
_GponOnuIgmpDynamicACL_Type = Integer32
_GponOnuIgmpDynamicACL_Object = MibTableColumn
gponOnuIgmpDynamicACL = _GponOnuIgmpDynamicACL_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 9),
    _GponOnuIgmpDynamicACL_Type()
)
gponOnuIgmpDynamicACL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpDynamicACL.setStatus("current")


class _GponOnuIgmpStaticACL_Type(Integer32):
    """Custom type gponOnuIgmpStaticACL based on Integer32"""
    defaultValue = 0


_GponOnuIgmpStaticACL_Type.__name__ = "Integer32"
_GponOnuIgmpStaticACL_Object = MibTableColumn
gponOnuIgmpStaticACL = _GponOnuIgmpStaticACL_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 10),
    _GponOnuIgmpStaticACL_Type()
)
gponOnuIgmpStaticACL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpStaticACL.setStatus("current")


class _GponOnuIgmpRobustness_Type(Integer32):
    """Custom type gponOnuIgmpRobustness based on Integer32"""
    defaultValue = 0


_GponOnuIgmpRobustness_Type.__name__ = "Integer32"
_GponOnuIgmpRobustness_Object = MibTableColumn
gponOnuIgmpRobustness = _GponOnuIgmpRobustness_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 11),
    _GponOnuIgmpRobustness_Type()
)
gponOnuIgmpRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpRobustness.setStatus("current")


class _GponOnuIgmpQueryInterval_Type(Integer32):
    """Custom type gponOnuIgmpQueryInterval based on Integer32"""
    defaultValue = 125


_GponOnuIgmpQueryInterval_Type.__name__ = "Integer32"
_GponOnuIgmpQueryInterval_Object = MibTableColumn
gponOnuIgmpQueryInterval = _GponOnuIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 12),
    _GponOnuIgmpQueryInterval_Type()
)
gponOnuIgmpQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    gponOnuIgmpQueryInterval.setUnits("seconds")


class _GponOnuIgmpQueryMaxResponseTime_Type(Integer32):
    """Custom type gponOnuIgmpQueryMaxResponseTime based on Integer32"""
    defaultValue = 100


_GponOnuIgmpQueryMaxResponseTime_Type.__name__ = "Integer32"
_GponOnuIgmpQueryMaxResponseTime_Object = MibTableColumn
gponOnuIgmpQueryMaxResponseTime = _GponOnuIgmpQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 13),
    _GponOnuIgmpQueryMaxResponseTime_Type()
)
gponOnuIgmpQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    gponOnuIgmpQueryMaxResponseTime.setUnits("0.1 seconds")


class _GponOnuIgmpLastMemberQueryInterval_Type(Integer32):
    """Custom type gponOnuIgmpLastMemberQueryInterval based on Integer32"""
    defaultValue = 10


_GponOnuIgmpLastMemberQueryInterval_Type.__name__ = "Integer32"
_GponOnuIgmpLastMemberQueryInterval_Object = MibTableColumn
gponOnuIgmpLastMemberQueryInterval = _GponOnuIgmpLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 14),
    _GponOnuIgmpLastMemberQueryInterval_Type()
)
gponOnuIgmpLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    gponOnuIgmpLastMemberQueryInterval.setUnits("0.1 seconds")


class _GponOnuIgmpUnautherizedJoin_Type(Integer32):
    """Custom type gponOnuIgmpUnautherizedJoin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_GponOnuIgmpUnautherizedJoin_Type.__name__ = "Integer32"
_GponOnuIgmpUnautherizedJoin_Object = MibTableColumn
gponOnuIgmpUnautherizedJoin = _GponOnuIgmpUnautherizedJoin_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 15),
    _GponOnuIgmpUnautherizedJoin_Type()
)
gponOnuIgmpUnautherizedJoin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpUnautherizedJoin.setStatus("current")


class _GponOnuIgmpDownstreamTCI_Type(Integer32):
    """Custom type gponOnuIgmpDownstreamTCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GponOnuIgmpDownstreamTCI_Type.__name__ = "Integer32"
_GponOnuIgmpDownstreamTCI_Object = MibTableColumn
gponOnuIgmpDownstreamTCI = _GponOnuIgmpDownstreamTCI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 16),
    _GponOnuIgmpDownstreamTCI_Type()
)
gponOnuIgmpDownstreamTCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpDownstreamTCI.setStatus("current")


class _GponOnuIgmpDownstreamTagControl_Type(Integer32):
    """Custom type gponOnuIgmpDownstreamTagControl based on Integer32"""
    defaultValue = 1

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
        *(("pass-through", 1),
          ("strip-vlan", 2),
          ("add-vlan", 3),
          ("replace-tci", 4),
          ("replace-vlan", 5))
    )


_GponOnuIgmpDownstreamTagControl_Type.__name__ = "Integer32"
_GponOnuIgmpDownstreamTagControl_Object = MibTableColumn
gponOnuIgmpDownstreamTagControl = _GponOnuIgmpDownstreamTagControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 17),
    _GponOnuIgmpDownstreamTagControl_Type()
)
gponOnuIgmpDownstreamTagControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpDownstreamTagControl.setStatus("current")


class _GponOnuIgmpMaxRequestChannelNum_Type(Integer32):
    """Custom type gponOnuIgmpMaxRequestChannelNum based on Integer32"""
    defaultValue = 0


_GponOnuIgmpMaxRequestChannelNum_Type.__name__ = "Integer32"
_GponOnuIgmpMaxRequestChannelNum_Object = MibTableColumn
gponOnuIgmpMaxRequestChannelNum = _GponOnuIgmpMaxRequestChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 18),
    _GponOnuIgmpMaxRequestChannelNum_Type()
)
gponOnuIgmpMaxRequestChannelNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpMaxRequestChannelNum.setStatus("current")


class _GponOnuIgmpGlobalBW_Type(Integer32):
    """Custom type gponOnuIgmpGlobalBW based on Integer32"""
    defaultValue = 0


_GponOnuIgmpGlobalBW_Type.__name__ = "Integer32"
_GponOnuIgmpGlobalBW_Object = MibTableColumn
gponOnuIgmpGlobalBW = _GponOnuIgmpGlobalBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 19),
    _GponOnuIgmpGlobalBW_Type()
)
gponOnuIgmpGlobalBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpGlobalBW.setStatus("current")
if mibBuilder.loadTexts:
    gponOnuIgmpGlobalBW.setUnits("Bps")
_GponOnuIgmpRowStatus_Type = RowStatus
_GponOnuIgmpRowStatus_Object = MibTableColumn
gponOnuIgmpRowStatus = _GponOnuIgmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 1, 1, 20),
    _GponOnuIgmpRowStatus_Type()
)
gponOnuIgmpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponOnuIgmpRowStatus.setStatus("current")
_GponOnuMulticastACLTable_Object = MibTable
gponOnuMulticastACLTable = _GponOnuMulticastACLTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gponOnuMulticastACLTable.setStatus("current")
_GponOnuMulticastACLEntry_Object = MibTableRow
gponOnuMulticastACLEntry = _GponOnuMulticastACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1)
)
gponOnuMulticastACLEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "multicastACLIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "multicastACLIndex"),
)
if mibBuilder.loadTexts:
    gponOnuMulticastACLEntry.setStatus("current")
_MulticastACLIndex_Type = Integer32
_MulticastACLIndex_Object = MibTableColumn
multicastACLIndex = _MulticastACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 1),
    _MulticastACLIndex_Type()
)
multicastACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastACLIndex.setStatus("current")
_MulticastACLRuleIndex_Type = Integer32
_MulticastACLRuleIndex_Object = MibTableColumn
multicastACLRuleIndex = _MulticastACLRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 2),
    _MulticastACLRuleIndex_Type()
)
multicastACLRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastACLRuleIndex.setStatus("current")
_MulticastACLRuleName_Type = DisplayString
_MulticastACLRuleName_Object = MibTableColumn
multicastACLRuleName = _MulticastACLRuleName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 3),
    _MulticastACLRuleName_Type()
)
multicastACLRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastACLRuleName.setStatus("current")


class _VlanID_Type(Integer32):
    """Custom type vlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanID_Type.__name__ = "Integer32"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 4),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_SourceIpAddress_Type = IpAddress
_SourceIpAddress_Object = MibTableColumn
sourceIpAddress = _SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 5),
    _SourceIpAddress_Type()
)
sourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sourceIpAddress.setStatus("current")
_DestinationIpAddressStart_Type = IpAddress
_DestinationIpAddressStart_Object = MibTableColumn
destinationIpAddressStart = _DestinationIpAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 6),
    _DestinationIpAddressStart_Type()
)
destinationIpAddressStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    destinationIpAddressStart.setStatus("current")
_DestinationIpAddressEnd_Type = IpAddress
_DestinationIpAddressEnd_Object = MibTableColumn
destinationIpAddressEnd = _DestinationIpAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 7),
    _DestinationIpAddressEnd_Type()
)
destinationIpAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    destinationIpAddressEnd.setStatus("current")
_PreviewLenAndAuthority_Type = Integer32
_PreviewLenAndAuthority_Object = MibTableColumn
previewLenAndAuthority = _PreviewLenAndAuthority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 8),
    _PreviewLenAndAuthority_Type()
)
previewLenAndAuthority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewLenAndAuthority.setStatus("current")
if mibBuilder.loadTexts:
    previewLenAndAuthority.setUnits("seconds")
_PreviewRepeatTime_Type = Integer32
_PreviewRepeatTime_Object = MibTableColumn
previewRepeatTime = _PreviewRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 9),
    _PreviewRepeatTime_Type()
)
previewRepeatTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewRepeatTime.setStatus("current")
if mibBuilder.loadTexts:
    previewRepeatTime.setUnits("seconds")


class _PreviewResetTime_Type(Integer32):
    """Custom type previewResetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PreviewResetTime_Type.__name__ = "Integer32"
_PreviewResetTime_Object = MibTableColumn
previewResetTime = _PreviewResetTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 10),
    _PreviewResetTime_Type()
)
previewResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewResetTime.setStatus("current")
_PreviewCount_Type = Integer32
_PreviewCount_Object = MibTableColumn
previewCount = _PreviewCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 11),
    _PreviewCount_Type()
)
previewCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewCount.setStatus("current")
_ImputedGroupBandwidth_Type = Integer32
_ImputedGroupBandwidth_Object = MibTableColumn
imputedGroupBandwidth = _ImputedGroupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 12),
    _ImputedGroupBandwidth_Type()
)
imputedGroupBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imputedGroupBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    imputedGroupBandwidth.setUnits("Bps")
_MulticastACLRuleStatus_Type = RowStatus
_MulticastACLRuleStatus_Object = MibTableColumn
multicastACLRuleStatus = _MulticastACLRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 4, 2, 1, 13),
    _MulticastACLRuleStatus_Type()
)
multicastACLRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastACLRuleStatus.setStatus("current")
_GponIgmpOnuUniTable_Object = MibTable
gponIgmpOnuUniTable = _GponIgmpOnuUniTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5)
)
if mibBuilder.loadTexts:
    gponIgmpOnuUniTable.setStatus("current")
_GponIgmpOnuUniEntry_Object = MibTableRow
gponIgmpOnuUniEntry = _GponIgmpOnuUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1)
)
gponIgmpOnuUniEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponUniDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponUniCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponUniPortIndex"),
)
if mibBuilder.loadTexts:
    gponIgmpOnuUniEntry.setStatus("current")
_GponUniDeviceIndex_Type = GponDeviceIndex
_GponUniDeviceIndex_Object = MibTableColumn
gponUniDeviceIndex = _GponUniDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1, 1),
    _GponUniDeviceIndex_Type()
)
gponUniDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponUniDeviceIndex.setStatus("current")
_GponUniCardIndex_Type = GponCardIndex
_GponUniCardIndex_Object = MibTableColumn
gponUniCardIndex = _GponUniCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1, 2),
    _GponUniCardIndex_Type()
)
gponUniCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponUniCardIndex.setStatus("current")
_GponUniPortIndex_Type = GponPortIndex
_GponUniPortIndex_Object = MibTableColumn
gponUniPortIndex = _GponUniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1, 3),
    _GponUniPortIndex_Type()
)
gponUniPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponUniPortIndex.setStatus("current")
_GponUniIgmpProfileIndex_Type = Integer32
_GponUniIgmpProfileIndex_Object = MibTableColumn
gponUniIgmpProfileIndex = _GponUniIgmpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1, 4),
    _GponUniIgmpProfileIndex_Type()
)
gponUniIgmpProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponUniIgmpProfileIndex.setStatus("current")
_GponUniRowstatus_Type = RowStatus
_GponUniRowstatus_Object = MibTableColumn
gponUniRowstatus = _GponUniRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 5, 1, 5),
    _GponUniRowstatus_Type()
)
gponUniRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponUniRowstatus.setStatus("current")
_IgmpOnuMulticastInfoTable_Object = MibTable
igmpOnuMulticastInfoTable = _IgmpOnuMulticastInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6)
)
if mibBuilder.loadTexts:
    igmpOnuMulticastInfoTable.setStatus("current")
_IgmpOnuMulticastInfoEntry_Object = MibTableRow
igmpOnuMulticastInfoEntry = _IgmpOnuMulticastInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1)
)
igmpOnuMulticastInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "onuMcInfoDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuMcInfoCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuMcInfoPortIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "onuMcInfoIndex"),
)
if mibBuilder.loadTexts:
    igmpOnuMulticastInfoEntry.setStatus("current")
_OnuMcInfoDeviceIndex_Type = GponDeviceIndex
_OnuMcInfoDeviceIndex_Object = MibTableColumn
onuMcInfoDeviceIndex = _OnuMcInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 1),
    _OnuMcInfoDeviceIndex_Type()
)
onuMcInfoDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuMcInfoDeviceIndex.setStatus("current")
_OnuMcInfoCardIndex_Type = GponCardIndex
_OnuMcInfoCardIndex_Object = MibTableColumn
onuMcInfoCardIndex = _OnuMcInfoCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 2),
    _OnuMcInfoCardIndex_Type()
)
onuMcInfoCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuMcInfoCardIndex.setStatus("current")
_OnuMcInfoPortIndex_Type = GponPortIndex
_OnuMcInfoPortIndex_Object = MibTableColumn
onuMcInfoPortIndex = _OnuMcInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 3),
    _OnuMcInfoPortIndex_Type()
)
onuMcInfoPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoPortIndex.setStatus("current")
_OnuMcInfoIndex_Type = Integer32
_OnuMcInfoIndex_Object = MibTableColumn
onuMcInfoIndex = _OnuMcInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 4),
    _OnuMcInfoIndex_Type()
)
onuMcInfoIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoIndex.setStatus("current")
_OnuMcInfoSrcIp_Type = IpAddress
_OnuMcInfoSrcIp_Object = MibTableColumn
onuMcInfoSrcIp = _OnuMcInfoSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 5),
    _OnuMcInfoSrcIp_Type()
)
onuMcInfoSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoSrcIp.setStatus("current")
_OnuMcInfoMcDstIp_Type = IpAddress
_OnuMcInfoMcDstIp_Object = MibTableColumn
onuMcInfoMcDstIp = _OnuMcInfoMcDstIp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 6),
    _OnuMcInfoMcDstIp_Type()
)
onuMcInfoMcDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoMcDstIp.setStatus("current")


class _OnuMcInfoMvlanVid_Type(Integer32):
    """Custom type onuMcInfoMvlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_OnuMcInfoMvlanVid_Type.__name__ = "Integer32"
_OnuMcInfoMvlanVid_Object = MibTableColumn
onuMcInfoMvlanVid = _OnuMcInfoMvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 7),
    _OnuMcInfoMvlanVid_Type()
)
onuMcInfoMvlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoMvlanVid.setStatus("current")
_OnuMcInfoClientIp_Type = IpAddress
_OnuMcInfoClientIp_Object = MibTableColumn
onuMcInfoClientIp = _OnuMcInfoClientIp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 6, 6, 1, 8),
    _OnuMcInfoClientIp_Type()
)
onuMcInfoClientIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuMcInfoClientIp.setStatus("current")
_GponPerformanceStatisticObjects_ObjectIdentity = ObjectIdentity
gponPerformanceStatisticObjects = _GponPerformanceStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10)
)
_GponPerfStatsThresholdTable_Object = MibTable
gponPerfStatsThresholdTable = _GponPerfStatsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5)
)
if mibBuilder.loadTexts:
    gponPerfStatsThresholdTable.setStatus("current")
_GponPerfStatsThresholdEntry_Object = MibTableRow
gponPerfStatsThresholdEntry = _GponPerfStatsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1)
)
gponPerfStatsThresholdEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponPerfStatsThresholdDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponPerfStatsThresholdCardIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponPerfStatsThresholdPortIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponPerfStatsThresholdTypeIndex"),
)
if mibBuilder.loadTexts:
    gponPerfStatsThresholdEntry.setStatus("current")
_GponPerfStatsThresholdDeviceIndex_Type = GponDeviceIndex
_GponPerfStatsThresholdDeviceIndex_Object = MibTableColumn
gponPerfStatsThresholdDeviceIndex = _GponPerfStatsThresholdDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 1),
    _GponPerfStatsThresholdDeviceIndex_Type()
)
gponPerfStatsThresholdDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdDeviceIndex.setStatus("current")
_GponPerfStatsThresholdCardIndex_Type = GponCardIndex
_GponPerfStatsThresholdCardIndex_Object = MibTableColumn
gponPerfStatsThresholdCardIndex = _GponPerfStatsThresholdCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 2),
    _GponPerfStatsThresholdCardIndex_Type()
)
gponPerfStatsThresholdCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdCardIndex.setStatus("current")
_GponPerfStatsThresholdPortIndex_Type = GponPortIndex
_GponPerfStatsThresholdPortIndex_Object = MibTableColumn
gponPerfStatsThresholdPortIndex = _GponPerfStatsThresholdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 3),
    _GponPerfStatsThresholdPortIndex_Type()
)
gponPerfStatsThresholdPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdPortIndex.setStatus("current")
_GponPerfStatsThresholdTypeIndex_Type = GponStatsThresholdType
_GponPerfStatsThresholdTypeIndex_Object = MibTableColumn
gponPerfStatsThresholdTypeIndex = _GponPerfStatsThresholdTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 4),
    _GponPerfStatsThresholdTypeIndex_Type()
)
gponPerfStatsThresholdTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdTypeIndex.setStatus("current")
_GponPerfStatsThresholdUpper_Type = Counter64
_GponPerfStatsThresholdUpper_Object = MibTableColumn
gponPerfStatsThresholdUpper = _GponPerfStatsThresholdUpper_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 5),
    _GponPerfStatsThresholdUpper_Type()
)
gponPerfStatsThresholdUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdUpper.setStatus("current")
_GponPerfStatsThresholdLower_Type = Counter64
_GponPerfStatsThresholdLower_Object = MibTableColumn
gponPerfStatsThresholdLower = _GponPerfStatsThresholdLower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 6),
    _GponPerfStatsThresholdLower_Type()
)
gponPerfStatsThresholdLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdLower.setStatus("current")
_GponPerfStatsThresholdRowStatus_Type = RowStatus
_GponPerfStatsThresholdRowStatus_Object = MibTableColumn
gponPerfStatsThresholdRowStatus = _GponPerfStatsThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 5, 1, 7),
    _GponPerfStatsThresholdRowStatus_Type()
)
gponPerfStatsThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponPerfStatsThresholdRowStatus.setStatus("current")
_CurStatsGemPortTable_Object = MibTable
curStatsGemPortTable = _CurStatsGemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6)
)
if mibBuilder.loadTexts:
    curStatsGemPortTable.setStatus("current")
_CurStatsGemPortEntry_Object = MibTableRow
curStatsGemPortEntry = _CurStatsGemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1)
)
curStatsGemPortEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "curStatsGemPortDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "curStatsGemPortIndex"),
)
if mibBuilder.loadTexts:
    curStatsGemPortEntry.setStatus("current")
_CurStatsGemPortDeviceIndex_Type = GponDeviceIndex
_CurStatsGemPortDeviceIndex_Object = MibTableColumn
curStatsGemPortDeviceIndex = _CurStatsGemPortDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 1),
    _CurStatsGemPortDeviceIndex_Type()
)
curStatsGemPortDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsGemPortDeviceIndex.setStatus("current")
_CurStatsGemPortIndex_Type = Integer32
_CurStatsGemPortIndex_Object = MibTableColumn
curStatsGemPortIndex = _CurStatsGemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 2),
    _CurStatsGemPortIndex_Type()
)
curStatsGemPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsGemPortIndex.setStatus("current")
_CurStatsGemPortOutGemFrames_Type = Counter64
_CurStatsGemPortOutGemFrames_Object = MibTableColumn
curStatsGemPortOutGemFrames = _CurStatsGemPortOutGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 3),
    _CurStatsGemPortOutGemFrames_Type()
)
curStatsGemPortOutGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsGemPortOutGemFrames.setStatus("current")
_CurStatsGemPortInGemFrames_Type = Counter64
_CurStatsGemPortInGemFrames_Object = MibTableColumn
curStatsGemPortInGemFrames = _CurStatsGemPortInGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 4),
    _CurStatsGemPortInGemFrames_Type()
)
curStatsGemPortInGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsGemPortInGemFrames.setStatus("current")
_CurStatsGemPortOutBytes_Type = Counter64
_CurStatsGemPortOutBytes_Object = MibTableColumn
curStatsGemPortOutBytes = _CurStatsGemPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 5),
    _CurStatsGemPortOutBytes_Type()
)
curStatsGemPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsGemPortOutBytes.setStatus("current")
_CurStatsGemPortInBytes_Type = Counter64
_CurStatsGemPortInBytes_Object = MibTableColumn
curStatsGemPortInBytes = _CurStatsGemPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 6),
    _CurStatsGemPortInBytes_Type()
)
curStatsGemPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsGemPortInBytes.setStatus("current")


class _CurStatsGemPortStatusAndAction_Type(Integer32):
    """Custom type curStatsGemPortStatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cleandata", 2))
    )


_CurStatsGemPortStatusAndAction_Type.__name__ = "Integer32"
_CurStatsGemPortStatusAndAction_Object = MibTableColumn
curStatsGemPortStatusAndAction = _CurStatsGemPortStatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 6, 1, 7),
    _CurStatsGemPortStatusAndAction_Type()
)
curStatsGemPortStatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curStatsGemPortStatusAndAction.setStatus("current")
_Stats15GemPortTable_Object = MibTable
stats15GemPortTable = _Stats15GemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7)
)
if mibBuilder.loadTexts:
    stats15GemPortTable.setStatus("current")
_Stats15GemPortEntry_Object = MibTableRow
stats15GemPortEntry = _Stats15GemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1)
)
stats15GemPortEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "stats15GemPortDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "stats15GemPortIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "stats15GemPortStatIndex"),
)
if mibBuilder.loadTexts:
    stats15GemPortEntry.setStatus("current")
_Stats15GemPortDeviceIndex_Type = GponDeviceIndex
_Stats15GemPortDeviceIndex_Object = MibTableColumn
stats15GemPortDeviceIndex = _Stats15GemPortDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 1),
    _Stats15GemPortDeviceIndex_Type()
)
stats15GemPortDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15GemPortDeviceIndex.setStatus("current")
_Stats15GemPortIndex_Type = Integer32
_Stats15GemPortIndex_Object = MibTableColumn
stats15GemPortIndex = _Stats15GemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 2),
    _Stats15GemPortIndex_Type()
)
stats15GemPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15GemPortIndex.setStatus("current")
_Stats15GemPortStatIndex_Type = GponStats15MinRecordType
_Stats15GemPortStatIndex_Object = MibTableColumn
stats15GemPortStatIndex = _Stats15GemPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 3),
    _Stats15GemPortStatIndex_Type()
)
stats15GemPortStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15GemPortStatIndex.setStatus("current")
_Stats15GemPortOutGemFrames_Type = Counter64
_Stats15GemPortOutGemFrames_Object = MibTableColumn
stats15GemPortOutGemFrames = _Stats15GemPortOutGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 4),
    _Stats15GemPortOutGemFrames_Type()
)
stats15GemPortOutGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortOutGemFrames.setStatus("current")
_Stats15GemPortInGemFrames_Type = Counter64
_Stats15GemPortInGemFrames_Object = MibTableColumn
stats15GemPortInGemFrames = _Stats15GemPortInGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 5),
    _Stats15GemPortInGemFrames_Type()
)
stats15GemPortInGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortInGemFrames.setStatus("current")
_Stats15GemPortOutBytes_Type = Counter64
_Stats15GemPortOutBytes_Object = MibTableColumn
stats15GemPortOutBytes = _Stats15GemPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 6),
    _Stats15GemPortOutBytes_Type()
)
stats15GemPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortOutBytes.setStatus("current")
_Stats15GemPortInBytes_Type = Counter64
_Stats15GemPortInBytes_Object = MibTableColumn
stats15GemPortInBytes = _Stats15GemPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 7),
    _Stats15GemPortInBytes_Type()
)
stats15GemPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortInBytes.setStatus("current")


class _Stats15GemPortStatusAndAction_Type(Integer32):
    """Custom type stats15GemPortStatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cleandata", 2))
    )


_Stats15GemPortStatusAndAction_Type.__name__ = "Integer32"
_Stats15GemPortStatusAndAction_Object = MibTableColumn
stats15GemPortStatusAndAction = _Stats15GemPortStatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 8),
    _Stats15GemPortStatusAndAction_Type()
)
stats15GemPortStatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats15GemPortStatusAndAction.setStatus("current")
_Stats15GemPortValidityTag_Type = TruthValue
_Stats15GemPortValidityTag_Object = MibTableColumn
stats15GemPortValidityTag = _Stats15GemPortValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 9),
    _Stats15GemPortValidityTag_Type()
)
stats15GemPortValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortValidityTag.setStatus("current")
_Stats15GemPortElapsedTime_Type = Counter32
_Stats15GemPortElapsedTime_Object = MibTableColumn
stats15GemPortElapsedTime = _Stats15GemPortElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 10),
    _Stats15GemPortElapsedTime_Type()
)
stats15GemPortElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats15GemPortElapsedTime.setUnits("seconds")
_Stats15GemPortEndTime_Type = DateAndTime
_Stats15GemPortEndTime_Object = MibTableColumn
stats15GemPortEndTime = _Stats15GemPortEndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 7, 1, 11),
    _Stats15GemPortEndTime_Type()
)
stats15GemPortEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15GemPortEndTime.setStatus("current")
_Stats24GemPortTable_Object = MibTable
stats24GemPortTable = _Stats24GemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8)
)
if mibBuilder.loadTexts:
    stats24GemPortTable.setStatus("current")
_Stats24GemPortEntry_Object = MibTableRow
stats24GemPortEntry = _Stats24GemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1)
)
stats24GemPortEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "stats24GemPortDeviceIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "stats24GemPortIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "stats24GemPortStatIndex"),
)
if mibBuilder.loadTexts:
    stats24GemPortEntry.setStatus("current")
_Stats24GemPortDeviceIndex_Type = GponDeviceIndex
_Stats24GemPortDeviceIndex_Object = MibTableColumn
stats24GemPortDeviceIndex = _Stats24GemPortDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 1),
    _Stats24GemPortDeviceIndex_Type()
)
stats24GemPortDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24GemPortDeviceIndex.setStatus("current")
_Stats24GemPortIndex_Type = Integer32
_Stats24GemPortIndex_Object = MibTableColumn
stats24GemPortIndex = _Stats24GemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 2),
    _Stats24GemPortIndex_Type()
)
stats24GemPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24GemPortIndex.setStatus("current")
_Stats24GemPortStatIndex_Type = GponStats24HourRecordType
_Stats24GemPortStatIndex_Object = MibTableColumn
stats24GemPortStatIndex = _Stats24GemPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 3),
    _Stats24GemPortStatIndex_Type()
)
stats24GemPortStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24GemPortStatIndex.setStatus("current")
_Stats24GemPortOutGemFrames_Type = Counter64
_Stats24GemPortOutGemFrames_Object = MibTableColumn
stats24GemPortOutGemFrames = _Stats24GemPortOutGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 4),
    _Stats24GemPortOutGemFrames_Type()
)
stats24GemPortOutGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortOutGemFrames.setStatus("current")
_Stats24GemPortInGemFrames_Type = Counter64
_Stats24GemPortInGemFrames_Object = MibTableColumn
stats24GemPortInGemFrames = _Stats24GemPortInGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 5),
    _Stats24GemPortInGemFrames_Type()
)
stats24GemPortInGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortInGemFrames.setStatus("current")
_Stats24GemPortOutBytes_Type = Counter64
_Stats24GemPortOutBytes_Object = MibTableColumn
stats24GemPortOutBytes = _Stats24GemPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 6),
    _Stats24GemPortOutBytes_Type()
)
stats24GemPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortOutBytes.setStatus("current")
_Stats24GemPortInBytes_Type = Counter64
_Stats24GemPortInBytes_Object = MibTableColumn
stats24GemPortInBytes = _Stats24GemPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 7),
    _Stats24GemPortInBytes_Type()
)
stats24GemPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortInBytes.setStatus("current")


class _Stats24GemPortStatusAndAction_Type(Integer32):
    """Custom type stats24GemPortStatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cleandata", 2))
    )


_Stats24GemPortStatusAndAction_Type.__name__ = "Integer32"
_Stats24GemPortStatusAndAction_Object = MibTableColumn
stats24GemPortStatusAndAction = _Stats24GemPortStatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 8),
    _Stats24GemPortStatusAndAction_Type()
)
stats24GemPortStatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats24GemPortStatusAndAction.setStatus("current")
_Stats24GemPortValidityTag_Type = TruthValue
_Stats24GemPortValidityTag_Object = MibTableColumn
stats24GemPortValidityTag = _Stats24GemPortValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 9),
    _Stats24GemPortValidityTag_Type()
)
stats24GemPortValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortValidityTag.setStatus("current")
_Stats24GemPortElapsedTime_Type = Counter32
_Stats24GemPortElapsedTime_Object = MibTableColumn
stats24GemPortElapsedTime = _Stats24GemPortElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 10),
    _Stats24GemPortElapsedTime_Type()
)
stats24GemPortElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats24GemPortElapsedTime.setUnits("seconds")
_Stats24GemPortEndTime_Type = DateAndTime
_Stats24GemPortEndTime_Object = MibTableColumn
stats24GemPortEndTime = _Stats24GemPortEndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 10, 8, 1, 11),
    _Stats24GemPortEndTime_Type()
)
stats24GemPortEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24GemPortEndTime.setStatus("current")
_GponProfileObjects_ObjectIdentity = ObjectIdentity
gponProfileObjects = _GponProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11)
)
_GponDbaProfileObjects_ObjectIdentity = ObjectIdentity
gponDbaProfileObjects = _GponDbaProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1)
)
_GponDbaProfileInfoTable_Object = MibTable
gponDbaProfileInfoTable = _GponDbaProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1)
)
if mibBuilder.loadTexts:
    gponDbaProfileInfoTable.setStatus("current")
_GponDbaProfileInfoEntry_Object = MibTableRow
gponDbaProfileInfoEntry = _GponDbaProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1)
)
gponDbaProfileInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponDbaProfileId"),
)
if mibBuilder.loadTexts:
    gponDbaProfileInfoEntry.setStatus("current")
_GponDbaProfileId_Type = Integer32
_GponDbaProfileId_Object = MibTableColumn
gponDbaProfileId = _GponDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 1),
    _GponDbaProfileId_Type()
)
gponDbaProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponDbaProfileId.setStatus("current")
_GponDbaProfileName_Type = DisplayString
_GponDbaProfileName_Object = MibTableColumn
gponDbaProfileName = _GponDbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 2),
    _GponDbaProfileName_Type()
)
gponDbaProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileName.setStatus("current")


class _GponDbaProfileType_Type(Integer32):
    """Custom type gponDbaProfileType based on Integer32"""
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
        *(("fix", 1),
          ("assure", 2),
          ("assureAndMax", 3),
          ("max", 4),
          ("fixAndAssureAndMax", 5))
    )


_GponDbaProfileType_Type.__name__ = "Integer32"
_GponDbaProfileType_Object = MibTableColumn
gponDbaProfileType = _GponDbaProfileType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 3),
    _GponDbaProfileType_Type()
)
gponDbaProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileType.setStatus("current")
_GponDbaProfileFixRate_Type = Integer32
_GponDbaProfileFixRate_Object = MibTableColumn
gponDbaProfileFixRate = _GponDbaProfileFixRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 4),
    _GponDbaProfileFixRate_Type()
)
gponDbaProfileFixRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileFixRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileFixRate.setUnits("kbit/s")
_GponDbaProfileAssureRate_Type = Integer32
_GponDbaProfileAssureRate_Object = MibTableColumn
gponDbaProfileAssureRate = _GponDbaProfileAssureRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 5),
    _GponDbaProfileAssureRate_Type()
)
gponDbaProfileAssureRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileAssureRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileAssureRate.setUnits("kbit/s")
_GponDbaProfileMaxRate_Type = Integer32
_GponDbaProfileMaxRate_Object = MibTableColumn
gponDbaProfileMaxRate = _GponDbaProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 6),
    _GponDbaProfileMaxRate_Type()
)
gponDbaProfileMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponDbaProfileMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    gponDbaProfileMaxRate.setUnits("kbit/s")
_GponDbaProfileBindNum_Type = Integer32
_GponDbaProfileBindNum_Object = MibTableColumn
gponDbaProfileBindNum = _GponDbaProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 7),
    _GponDbaProfileBindNum_Type()
)
gponDbaProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponDbaProfileBindNum.setStatus("current")
_GponDbaProfileRowStatus_Type = RowStatus
_GponDbaProfileRowStatus_Object = MibTableColumn
gponDbaProfileRowStatus = _GponDbaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 1, 1, 1, 8),
    _GponDbaProfileRowStatus_Type()
)
gponDbaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponDbaProfileRowStatus.setStatus("current")
_GponLineProfileObjects_ObjectIdentity = ObjectIdentity
gponLineProfileObjects = _GponLineProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2)
)
_GponLineProfileInfoTable_Object = MibTable
gponLineProfileInfoTable = _GponLineProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1)
)
if mibBuilder.loadTexts:
    gponLineProfileInfoTable.setStatus("current")
_GponLineProfileInfoEntry_Object = MibTableRow
gponLineProfileInfoEntry = _GponLineProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1)
)
gponLineProfileInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileId"),
)
if mibBuilder.loadTexts:
    gponLineProfileInfoEntry.setStatus("current")
_GponLineProfileId_Type = Integer32
_GponLineProfileId_Object = MibTableColumn
gponLineProfileId = _GponLineProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 1),
    _GponLineProfileId_Type()
)
gponLineProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileId.setStatus("current")
_GponLineProfileName_Type = DisplayString
_GponLineProfileName_Object = MibTableColumn
gponLineProfileName = _GponLineProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 2),
    _GponLineProfileName_Type()
)
gponLineProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileName.setStatus("current")


class _GponLineProfileUpstreamFECMode_Type(Integer32):
    """Custom type gponLineProfileUpstreamFECMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_GponLineProfileUpstreamFECMode_Type.__name__ = "Integer32"
_GponLineProfileUpstreamFECMode_Object = MibTableColumn
gponLineProfileUpstreamFECMode = _GponLineProfileUpstreamFECMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 3),
    _GponLineProfileUpstreamFECMode_Type()
)
gponLineProfileUpstreamFECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileUpstreamFECMode.setStatus("current")


class _GponLineProfileMappingMode_Type(Integer32):
    """Custom type gponLineProfileMappingMode based on Integer32"""
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
        *(("vlan", 1),
          ("priority", 2),
          ("vlan-priority", 3),
          ("port", 4))
    )


_GponLineProfileMappingMode_Type.__name__ = "Integer32"
_GponLineProfileMappingMode_Object = MibTableColumn
gponLineProfileMappingMode = _GponLineProfileMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 4),
    _GponLineProfileMappingMode_Type()
)
gponLineProfileMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileMappingMode.setStatus("current")
_GponLineProfileTcontNum_Type = Integer32
_GponLineProfileTcontNum_Object = MibTableColumn
gponLineProfileTcontNum = _GponLineProfileTcontNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 5),
    _GponLineProfileTcontNum_Type()
)
gponLineProfileTcontNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileTcontNum.setStatus("current")
_GponLineProfileGemNum_Type = Integer32
_GponLineProfileGemNum_Object = MibTableColumn
gponLineProfileGemNum = _GponLineProfileGemNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 6),
    _GponLineProfileGemNum_Type()
)
gponLineProfileGemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileGemNum.setStatus("current")
_GponLineProfileBindNum_Type = Integer32
_GponLineProfileBindNum_Object = MibTableColumn
gponLineProfileBindNum = _GponLineProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 7),
    _GponLineProfileBindNum_Type()
)
gponLineProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileBindNum.setStatus("current")
_GponLineProfileRowStatus_Type = RowStatus
_GponLineProfileRowStatus_Object = MibTableColumn
gponLineProfileRowStatus = _GponLineProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 1, 1, 8),
    _GponLineProfileRowStatus_Type()
)
gponLineProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileRowStatus.setStatus("current")
_GponLineProfileTcontTable_Object = MibTable
gponLineProfileTcontTable = _GponLineProfileTcontTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2)
)
if mibBuilder.loadTexts:
    gponLineProfileTcontTable.setStatus("current")
_GponLineProfileTcontEntry_Object = MibTableRow
gponLineProfileTcontEntry = _GponLineProfileTcontEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2, 1)
)
gponLineProfileTcontEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileTcontProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileTcontIndex"),
)
if mibBuilder.loadTexts:
    gponLineProfileTcontEntry.setStatus("current")
_GponLineProfileTcontProfileIndex_Type = Integer32
_GponLineProfileTcontProfileIndex_Object = MibTableColumn
gponLineProfileTcontProfileIndex = _GponLineProfileTcontProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2, 1, 1),
    _GponLineProfileTcontProfileIndex_Type()
)
gponLineProfileTcontProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileTcontProfileIndex.setStatus("current")
_GponLineProfileTcontIndex_Type = Integer32
_GponLineProfileTcontIndex_Object = MibTableColumn
gponLineProfileTcontIndex = _GponLineProfileTcontIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2, 1, 2),
    _GponLineProfileTcontIndex_Type()
)
gponLineProfileTcontIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileTcontIndex.setStatus("current")
_GponLineProfileTcontDbaProfileId_Type = Integer32
_GponLineProfileTcontDbaProfileId_Object = MibTableColumn
gponLineProfileTcontDbaProfileId = _GponLineProfileTcontDbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2, 1, 3),
    _GponLineProfileTcontDbaProfileId_Type()
)
gponLineProfileTcontDbaProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileTcontDbaProfileId.setStatus("current")
_GponLineProfileTcontRowStatus_Type = RowStatus
_GponLineProfileTcontRowStatus_Object = MibTableColumn
gponLineProfileTcontRowStatus = _GponLineProfileTcontRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 2, 1, 4),
    _GponLineProfileTcontRowStatus_Type()
)
gponLineProfileTcontRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileTcontRowStatus.setStatus("current")
_GponLineProfileGemTable_Object = MibTable
gponLineProfileGemTable = _GponLineProfileGemTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3)
)
if mibBuilder.loadTexts:
    gponLineProfileGemTable.setStatus("current")
_GponLineProfileGemEntry_Object = MibTableRow
gponLineProfileGemEntry = _GponLineProfileGemEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1)
)
gponLineProfileGemEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileGemProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileGemIndex"),
)
if mibBuilder.loadTexts:
    gponLineProfileGemEntry.setStatus("current")
_GponLineProfileGemProfileIndex_Type = Integer32
_GponLineProfileGemProfileIndex_Object = MibTableColumn
gponLineProfileGemProfileIndex = _GponLineProfileGemProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 1),
    _GponLineProfileGemProfileIndex_Type()
)
gponLineProfileGemProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemProfileIndex.setStatus("current")
_GponLineProfileGemIndex_Type = Integer32
_GponLineProfileGemIndex_Object = MibTableColumn
gponLineProfileGemIndex = _GponLineProfileGemIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 2),
    _GponLineProfileGemIndex_Type()
)
gponLineProfileGemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemIndex.setStatus("current")


class _GponLineProfileGemEncrypt_Type(Integer32):
    """Custom type gponLineProfileGemEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconcern", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GponLineProfileGemEncrypt_Type.__name__ = "Integer32"
_GponLineProfileGemEncrypt_Object = MibTableColumn
gponLineProfileGemEncrypt = _GponLineProfileGemEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 3),
    _GponLineProfileGemEncrypt_Type()
)
gponLineProfileGemEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemEncrypt.setStatus("current")
_GponLineProfileGemTcontId_Type = Integer32
_GponLineProfileGemTcontId_Object = MibTableColumn
gponLineProfileGemTcontId = _GponLineProfileGemTcontId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 4),
    _GponLineProfileGemTcontId_Type()
)
gponLineProfileGemTcontId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemTcontId.setStatus("current")


class _GponLineProfileGemQueuePri_Type(Integer32):
    """Custom type gponLineProfileGemQueuePri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GponLineProfileGemQueuePri_Type.__name__ = "Integer32"
_GponLineProfileGemQueuePri_Object = MibTableColumn
gponLineProfileGemQueuePri = _GponLineProfileGemQueuePri_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 5),
    _GponLineProfileGemQueuePri_Type()
)
gponLineProfileGemQueuePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemQueuePri.setStatus("current")


class _GponLineProfileGemUpCar_Type(Integer32):
    """Custom type gponLineProfileGemUpCar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_GponLineProfileGemUpCar_Type.__name__ = "Integer32"
_GponLineProfileGemUpCar_Object = MibTableColumn
gponLineProfileGemUpCar = _GponLineProfileGemUpCar_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 6),
    _GponLineProfileGemUpCar_Type()
)
gponLineProfileGemUpCar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemUpCar.setStatus("current")


class _GponLineProfileGemDownCar_Type(Integer32):
    """Custom type gponLineProfileGemDownCar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1024),
    )


_GponLineProfileGemDownCar_Type.__name__ = "Integer32"
_GponLineProfileGemDownCar_Object = MibTableColumn
gponLineProfileGemDownCar = _GponLineProfileGemDownCar_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 7),
    _GponLineProfileGemDownCar_Type()
)
gponLineProfileGemDownCar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemDownCar.setStatus("current")
_GponLineProfileGemMapNum_Type = Integer32
_GponLineProfileGemMapNum_Object = MibTableColumn
gponLineProfileGemMapNum = _GponLineProfileGemMapNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 8),
    _GponLineProfileGemMapNum_Type()
)
gponLineProfileGemMapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLineProfileGemMapNum.setStatus("current")
_GponLineProfileGemRowStatus_Type = RowStatus
_GponLineProfileGemRowStatus_Object = MibTableColumn
gponLineProfileGemRowStatus = _GponLineProfileGemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 3, 1, 9),
    _GponLineProfileGemRowStatus_Type()
)
gponLineProfileGemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemRowStatus.setStatus("current")
_GponLineProfileGemMapTable_Object = MibTable
gponLineProfileGemMapTable = _GponLineProfileGemMapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4)
)
if mibBuilder.loadTexts:
    gponLineProfileGemMapTable.setStatus("current")
_GponLineProfileGemMapEntry_Object = MibTableRow
gponLineProfileGemMapEntry = _GponLineProfileGemMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1)
)
gponLineProfileGemMapEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileGemMapProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileGemMapGemIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponLineProfileGemMapIndex"),
)
if mibBuilder.loadTexts:
    gponLineProfileGemMapEntry.setStatus("current")
_GponLineProfileGemMapProfileIndex_Type = Integer32
_GponLineProfileGemMapProfileIndex_Object = MibTableColumn
gponLineProfileGemMapProfileIndex = _GponLineProfileGemMapProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 1),
    _GponLineProfileGemMapProfileIndex_Type()
)
gponLineProfileGemMapProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemMapProfileIndex.setStatus("current")
_GponLineProfileGemMapGemIndex_Type = Integer32
_GponLineProfileGemMapGemIndex_Object = MibTableColumn
gponLineProfileGemMapGemIndex = _GponLineProfileGemMapGemIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 2),
    _GponLineProfileGemMapGemIndex_Type()
)
gponLineProfileGemMapGemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemMapGemIndex.setStatus("current")
_GponLineProfileGemMapIndex_Type = Integer32
_GponLineProfileGemMapIndex_Object = MibTableColumn
gponLineProfileGemMapIndex = _GponLineProfileGemMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 3),
    _GponLineProfileGemMapIndex_Type()
)
gponLineProfileGemMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponLineProfileGemMapIndex.setStatus("current")
_GponLineProfileGemMapVlan_Type = Integer32
_GponLineProfileGemMapVlan_Object = MibTableColumn
gponLineProfileGemMapVlan = _GponLineProfileGemMapVlan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 4),
    _GponLineProfileGemMapVlan_Type()
)
gponLineProfileGemMapVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapVlan.setStatus("current")
_GponLineProfileGemMapPriority_Type = Integer32
_GponLineProfileGemMapPriority_Object = MibTableColumn
gponLineProfileGemMapPriority = _GponLineProfileGemMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 5),
    _GponLineProfileGemMapPriority_Type()
)
gponLineProfileGemMapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapPriority.setStatus("current")


class _GponLineProfileGemMapPortType_Type(Integer32):
    """Custom type gponLineProfileGemMapPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 1),
          ("iphost", 2))
    )


_GponLineProfileGemMapPortType_Type.__name__ = "Integer32"
_GponLineProfileGemMapPortType_Object = MibTableColumn
gponLineProfileGemMapPortType = _GponLineProfileGemMapPortType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 6),
    _GponLineProfileGemMapPortType_Type()
)
gponLineProfileGemMapPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponLineProfileGemMapPortType.setStatus("current")
_GponLineProfileGemMapPortId_Type = Integer32
_GponLineProfileGemMapPortId_Object = MibTableColumn
gponLineProfileGemMapPortId = _GponLineProfileGemMapPortId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 7),
    _GponLineProfileGemMapPortId_Type()
)
gponLineProfileGemMapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapPortId.setStatus("current")
_GponLineProfileGemMapRowStatus_Type = RowStatus
_GponLineProfileGemMapRowStatus_Object = MibTableColumn
gponLineProfileGemMapRowStatus = _GponLineProfileGemMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 2, 4, 1, 8),
    _GponLineProfileGemMapRowStatus_Type()
)
gponLineProfileGemMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponLineProfileGemMapRowStatus.setStatus("current")
_GponSrvProfileObjects_ObjectIdentity = ObjectIdentity
gponSrvProfileObjects = _GponSrvProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3)
)
_GponSrvProfileInfoTable_Object = MibTable
gponSrvProfileInfoTable = _GponSrvProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gponSrvProfileInfoTable.setStatus("current")
_GponSrvProfileInfoEntry_Object = MibTableRow
gponSrvProfileInfoEntry = _GponSrvProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1, 1)
)
gponSrvProfileInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfileId"),
)
if mibBuilder.loadTexts:
    gponSrvProfileInfoEntry.setStatus("current")
_GponSrvProfileId_Type = Integer32
_GponSrvProfileId_Object = MibTableColumn
gponSrvProfileId = _GponSrvProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1, 1, 1),
    _GponSrvProfileId_Type()
)
gponSrvProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfileId.setStatus("current")
_GponSrvProfileName_Type = DisplayString
_GponSrvProfileName_Object = MibTableColumn
gponSrvProfileName = _GponSrvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1, 1, 2),
    _GponSrvProfileName_Type()
)
gponSrvProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileName.setStatus("current")
_GponSrvProfileBindNum_Type = Integer32
_GponSrvProfileBindNum_Object = MibTableColumn
gponSrvProfileBindNum = _GponSrvProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1, 1, 3),
    _GponSrvProfileBindNum_Type()
)
gponSrvProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponSrvProfileBindNum.setStatus("current")
_GponSrvProfileRowStatus_Type = RowStatus
_GponSrvProfileRowStatus_Object = MibTableColumn
gponSrvProfileRowStatus = _GponSrvProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 1, 1, 4),
    _GponSrvProfileRowStatus_Type()
)
gponSrvProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfileRowStatus.setStatus("current")
_GponSrvProfileCfgTable_Object = MibTable
gponSrvProfileCfgTable = _GponSrvProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gponSrvProfileCfgTable.setStatus("current")
_GponSrvProfileCfgEntry_Object = MibTableRow
gponSrvProfileCfgEntry = _GponSrvProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2, 1)
)
gponSrvProfileCfgEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfileIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfileCfgEntry.setStatus("current")
_GponSrvProfileIndex_Type = Integer32
_GponSrvProfileIndex_Object = MibTableColumn
gponSrvProfileIndex = _GponSrvProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2, 1, 1),
    _GponSrvProfileIndex_Type()
)
gponSrvProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfileIndex.setStatus("current")


class _GponSrvProfileMacLearning_Type(Integer32):
    """Custom type gponSrvProfileMacLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconcern", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GponSrvProfileMacLearning_Type.__name__ = "Integer32"
_GponSrvProfileMacLearning_Object = MibTableColumn
gponSrvProfileMacLearning = _GponSrvProfileMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2, 1, 2),
    _GponSrvProfileMacLearning_Type()
)
gponSrvProfileMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileMacLearning.setStatus("current")


class _GponSrvProfileMacAgeSeconds_Type(Integer32):
    """Custom type gponSrvProfileMacAgeSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_GponSrvProfileMacAgeSeconds_Type.__name__ = "Integer32"
_GponSrvProfileMacAgeSeconds_Object = MibTableColumn
gponSrvProfileMacAgeSeconds = _GponSrvProfileMacAgeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2, 1, 3),
    _GponSrvProfileMacAgeSeconds_Type()
)
gponSrvProfileMacAgeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileMacAgeSeconds.setStatus("current")
if mibBuilder.loadTexts:
    gponSrvProfileMacAgeSeconds.setUnits("second")


class _GponSrvProfileLoopbackDetectCheck_Type(Integer32):
    """Custom type gponSrvProfileLoopbackDetectCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconcern", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GponSrvProfileLoopbackDetectCheck_Type.__name__ = "Integer32"
_GponSrvProfileLoopbackDetectCheck_Object = MibTableColumn
gponSrvProfileLoopbackDetectCheck = _GponSrvProfileLoopbackDetectCheck_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 2, 1, 4),
    _GponSrvProfileLoopbackDetectCheck_Type()
)
gponSrvProfileLoopbackDetectCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileLoopbackDetectCheck.setStatus("current")
_GponSrvProfilePortNumTable_Object = MibTable
gponSrvProfilePortNumTable = _GponSrvProfilePortNumTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortNumTable.setStatus("current")
_GponSrvProfilePortNumEntry_Object = MibTableRow
gponSrvProfilePortNumEntry = _GponSrvProfilePortNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1)
)
gponSrvProfilePortNumEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortNumProfileIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortNumEntry.setStatus("current")
_GponSrvProfilePortNumProfileIndex_Type = Integer32
_GponSrvProfilePortNumProfileIndex_Object = MibTableColumn
gponSrvProfilePortNumProfileIndex = _GponSrvProfilePortNumProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1, 1),
    _GponSrvProfilePortNumProfileIndex_Type()
)
gponSrvProfilePortNumProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortNumProfileIndex.setStatus("current")


class _GponSrvProfileEthNum_Type(Integer32):
    """Custom type gponSrvProfileEthNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 24),
    )


_GponSrvProfileEthNum_Type.__name__ = "Integer32"
_GponSrvProfileEthNum_Object = MibTableColumn
gponSrvProfileEthNum = _GponSrvProfileEthNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1, 2),
    _GponSrvProfileEthNum_Type()
)
gponSrvProfileEthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthNum.setStatus("current")


class _GponSrvProfileCatvNum_Type(Integer32):
    """Custom type gponSrvProfileCatvNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2),
    )


_GponSrvProfileCatvNum_Type.__name__ = "Integer32"
_GponSrvProfileCatvNum_Object = MibTableColumn
gponSrvProfileCatvNum = _GponSrvProfileCatvNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1, 3),
    _GponSrvProfileCatvNum_Type()
)
gponSrvProfileCatvNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileCatvNum.setStatus("current")


class _GponSrvProfileWlanNum_Type(Integer32):
    """Custom type gponSrvProfileWlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2),
    )


_GponSrvProfileWlanNum_Type.__name__ = "Integer32"
_GponSrvProfileWlanNum_Object = MibTableColumn
gponSrvProfileWlanNum = _GponSrvProfileWlanNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1, 4),
    _GponSrvProfileWlanNum_Type()
)
gponSrvProfileWlanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileWlanNum.setStatus("current")


class _GponSrvProfileVeipNum_Type(Integer32):
    """Custom type gponSrvProfileVeipNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8),
    )


_GponSrvProfileVeipNum_Type.__name__ = "Integer32"
_GponSrvProfileVeipNum_Object = MibTableColumn
gponSrvProfileVeipNum = _GponSrvProfileVeipNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 3, 1, 5),
    _GponSrvProfileVeipNum_Type()
)
gponSrvProfileVeipNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileVeipNum.setStatus("current")
_GponSrvProfileEthPortConfigTable_Object = MibTable
gponSrvProfileEthPortConfigTable = _GponSrvProfileEthPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4)
)
if mibBuilder.loadTexts:
    gponSrvProfileEthPortConfigTable.setStatus("current")
_GponSrvProfileEthPortConfigEntry_Object = MibTableRow
gponSrvProfileEthPortConfigEntry = _GponSrvProfileEthPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1)
)
gponSrvProfileEthPortConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfileEthPortProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfileEthPortIdIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfileEthPortConfigEntry.setStatus("current")
_GponSrvProfileEthPortProfileIndex_Type = Integer32
_GponSrvProfileEthPortProfileIndex_Object = MibTableColumn
gponSrvProfileEthPortProfileIndex = _GponSrvProfileEthPortProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 1),
    _GponSrvProfileEthPortProfileIndex_Type()
)
gponSrvProfileEthPortProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortProfileIndex.setStatus("current")
_GponSrvProfileEthPortIdIndex_Type = Integer32
_GponSrvProfileEthPortIdIndex_Object = MibTableColumn
gponSrvProfileEthPortIdIndex = _GponSrvProfileEthPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 2),
    _GponSrvProfileEthPortIdIndex_Type()
)
gponSrvProfileEthPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortIdIndex.setStatus("current")


class _GponSrvProfileEthPortMacLimited_Type(Integer32):
    """Custom type gponSrvProfileEthPortMacLimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_GponSrvProfileEthPortMacLimited_Type.__name__ = "Integer32"
_GponSrvProfileEthPortMacLimited_Object = MibTableColumn
gponSrvProfileEthPortMacLimited = _GponSrvProfileEthPortMacLimited_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 3),
    _GponSrvProfileEthPortMacLimited_Type()
)
gponSrvProfileEthPortMacLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortMacLimited.setStatus("current")


class _GponSrvProfileEthPortMtu_Type(Integer32):
    """Custom type gponSrvProfileEthPortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1518, 2000),
    )


_GponSrvProfileEthPortMtu_Type.__name__ = "Integer32"
_GponSrvProfileEthPortMtu_Object = MibTableColumn
gponSrvProfileEthPortMtu = _GponSrvProfileEthPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 4),
    _GponSrvProfileEthPortMtu_Type()
)
gponSrvProfileEthPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortMtu.setStatus("current")


class _GponSrvProfileEthPortFlowCtrl_Type(Integer32):
    """Custom type gponSrvProfileEthPortFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconcern", 0),
          ("enable", 1),
          ("disable", 2))
    )


_GponSrvProfileEthPortFlowCtrl_Type.__name__ = "Integer32"
_GponSrvProfileEthPortFlowCtrl_Object = MibTableColumn
gponSrvProfileEthPortFlowCtrl = _GponSrvProfileEthPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 5),
    _GponSrvProfileEthPortFlowCtrl_Type()
)
gponSrvProfileEthPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortFlowCtrl.setStatus("current")


class _GponSrvProfileEthPortInTrafficProfileId_Type(Integer32):
    """Custom type gponSrvProfileEthPortInTrafficProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GponSrvProfileEthPortInTrafficProfileId_Type.__name__ = "Integer32"
_GponSrvProfileEthPortInTrafficProfileId_Object = MibTableColumn
gponSrvProfileEthPortInTrafficProfileId = _GponSrvProfileEthPortInTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 6),
    _GponSrvProfileEthPortInTrafficProfileId_Type()
)
gponSrvProfileEthPortInTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortInTrafficProfileId.setStatus("current")


class _GponSrvProfileEthPortOutTrafficProfileId_Type(Integer32):
    """Custom type gponSrvProfileEthPortOutTrafficProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GponSrvProfileEthPortOutTrafficProfileId_Type.__name__ = "Integer32"
_GponSrvProfileEthPortOutTrafficProfileId_Object = MibTableColumn
gponSrvProfileEthPortOutTrafficProfileId = _GponSrvProfileEthPortOutTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 4, 1, 7),
    _GponSrvProfileEthPortOutTrafficProfileId_Type()
)
gponSrvProfileEthPortOutTrafficProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfileEthPortOutTrafficProfileId.setStatus("current")
_GponSrvProfilePortVlanObjects_ObjectIdentity = ObjectIdentity
gponSrvProfilePortVlanObjects = _GponSrvProfilePortVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5)
)
_GponSrvProfilePortVlanCfgTable_Object = MibTable
gponSrvProfilePortVlanCfgTable = _GponSrvProfilePortVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanCfgTable.setStatus("current")
_GponSrvProfilePortVlanCfgEntry_Object = MibTableRow
gponSrvProfilePortVlanCfgEntry = _GponSrvProfilePortVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1)
)
gponSrvProfilePortVlanCfgEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanPortTypeIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanPortIdIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanCfgEntry.setStatus("current")
_GponSrvProfilePortVlanProfileIndex_Type = Integer32
_GponSrvProfilePortVlanProfileIndex_Object = MibTableColumn
gponSrvProfilePortVlanProfileIndex = _GponSrvProfilePortVlanProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 1),
    _GponSrvProfilePortVlanProfileIndex_Type()
)
gponSrvProfilePortVlanProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanProfileIndex.setStatus("current")


class _GponSrvProfilePortVlanPortTypeIndex_Type(Integer32):
    """Custom type gponSrvProfilePortVlanPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("wlan", 1),
          ("catv", 2))
    )


_GponSrvProfilePortVlanPortTypeIndex_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanPortTypeIndex_Object = MibTableColumn
gponSrvProfilePortVlanPortTypeIndex = _GponSrvProfilePortVlanPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 2),
    _GponSrvProfilePortVlanPortTypeIndex_Type()
)
gponSrvProfilePortVlanPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanPortTypeIndex.setStatus("current")
_GponSrvProfilePortVlanPortIdIndex_Type = Integer32
_GponSrvProfilePortVlanPortIdIndex_Object = MibTableColumn
gponSrvProfilePortVlanPortIdIndex = _GponSrvProfilePortVlanPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 3),
    _GponSrvProfilePortVlanPortIdIndex_Type()
)
gponSrvProfilePortVlanPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanPortIdIndex.setStatus("current")


class _GponSrvProfilePortVlanPvid_Type(Integer32):
    """Custom type gponSrvProfilePortVlanPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_GponSrvProfilePortVlanPvid_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanPvid_Object = MibTableColumn
gponSrvProfilePortVlanPvid = _GponSrvProfilePortVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 4),
    _GponSrvProfilePortVlanPvid_Type()
)
gponSrvProfilePortVlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanPvid.setStatus("current")


class _GponSrvProfilePortVlanPvidPri_Type(Integer32):
    """Custom type gponSrvProfilePortVlanPvidPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GponSrvProfilePortVlanPvidPri_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanPvidPri_Object = MibTableColumn
gponSrvProfilePortVlanPvidPri = _GponSrvProfilePortVlanPvidPri_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 5),
    _GponSrvProfilePortVlanPvidPri_Type()
)
gponSrvProfilePortVlanPvidPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanPvidPri.setStatus("current")


class _GponSrvProfilePortVlanMode_Type(Integer32):
    """Custom type gponSrvProfilePortVlanMode based on Integer32"""
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
        *(("transparent", 0),
          ("tag", 1),
          ("translate", 2),
          ("aggregation", 3),
          ("trunk", 4))
    )


_GponSrvProfilePortVlanMode_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanMode_Object = MibTableColumn
gponSrvProfilePortVlanMode = _GponSrvProfilePortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 1, 1, 6),
    _GponSrvProfilePortVlanMode_Type()
)
gponSrvProfilePortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanMode.setStatus("current")
_GponSrvProfilePortVlanTranslationTable_Object = MibTable
gponSrvProfilePortVlanTranslationTable = _GponSrvProfilePortVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTranslationTable.setStatus("current")
_GponSrvProfilePortVlanTranslationEntry_Object = MibTableRow
gponSrvProfilePortVlanTranslationEntry = _GponSrvProfilePortVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1)
)
gponSrvProfilePortVlanTranslationEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTransProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTransPortTypeIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTransPortIdIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTransVlanIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTranslationEntry.setStatus("current")
_GponSrvProfilePortVlanTransProfileIndex_Type = Integer32
_GponSrvProfilePortVlanTransProfileIndex_Object = MibTableColumn
gponSrvProfilePortVlanTransProfileIndex = _GponSrvProfilePortVlanTransProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 1),
    _GponSrvProfilePortVlanTransProfileIndex_Type()
)
gponSrvProfilePortVlanTransProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransProfileIndex.setStatus("current")


class _GponSrvProfilePortVlanTransPortTypeIndex_Type(Integer32):
    """Custom type gponSrvProfilePortVlanTransPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("wlan", 1),
          ("catv", 2))
    )


_GponSrvProfilePortVlanTransPortTypeIndex_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanTransPortTypeIndex_Object = MibTableColumn
gponSrvProfilePortVlanTransPortTypeIndex = _GponSrvProfilePortVlanTransPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 2),
    _GponSrvProfilePortVlanTransPortTypeIndex_Type()
)
gponSrvProfilePortVlanTransPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransPortTypeIndex.setStatus("current")
_GponSrvProfilePortVlanTransPortIdIndex_Type = Integer32
_GponSrvProfilePortVlanTransPortIdIndex_Object = MibTableColumn
gponSrvProfilePortVlanTransPortIdIndex = _GponSrvProfilePortVlanTransPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 3),
    _GponSrvProfilePortVlanTransPortIdIndex_Type()
)
gponSrvProfilePortVlanTransPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransPortIdIndex.setStatus("current")
_GponSrvProfilePortVlanTransVlanIndex_Type = Integer32
_GponSrvProfilePortVlanTransVlanIndex_Object = MibTableColumn
gponSrvProfilePortVlanTransVlanIndex = _GponSrvProfilePortVlanTransVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 4),
    _GponSrvProfilePortVlanTransVlanIndex_Type()
)
gponSrvProfilePortVlanTransVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransVlanIndex.setStatus("current")
_GponSrvProfilePortVlanTransNewVlan_Type = Integer32
_GponSrvProfilePortVlanTransNewVlan_Object = MibTableColumn
gponSrvProfilePortVlanTransNewVlan = _GponSrvProfilePortVlanTransNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 5),
    _GponSrvProfilePortVlanTransNewVlan_Type()
)
gponSrvProfilePortVlanTransNewVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransNewVlan.setStatus("current")
_GponSrvProfilePortVlanTransRowStatus_Type = RowStatus
_GponSrvProfilePortVlanTransRowStatus_Object = MibTableColumn
gponSrvProfilePortVlanTransRowStatus = _GponSrvProfilePortVlanTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 2, 1, 6),
    _GponSrvProfilePortVlanTransRowStatus_Type()
)
gponSrvProfilePortVlanTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTransRowStatus.setStatus("current")
_GponSrvProfilePortVlanAggregationTable_Object = MibTable
gponSrvProfilePortVlanAggregationTable = _GponSrvProfilePortVlanAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggregationTable.setStatus("current")
_GponSrvProfilePortVlanAggregationEntry_Object = MibTableRow
gponSrvProfilePortVlanAggregationEntry = _GponSrvProfilePortVlanAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1)
)
gponSrvProfilePortVlanAggregationEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanAggrProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanAggrPortTypeIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanAggrPortIdIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanAggrVlanIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggregationEntry.setStatus("current")
_GponSrvProfilePortVlanAggrProfileIndex_Type = Integer32
_GponSrvProfilePortVlanAggrProfileIndex_Object = MibTableColumn
gponSrvProfilePortVlanAggrProfileIndex = _GponSrvProfilePortVlanAggrProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 1),
    _GponSrvProfilePortVlanAggrProfileIndex_Type()
)
gponSrvProfilePortVlanAggrProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrProfileIndex.setStatus("current")


class _GponSrvProfilePortVlanAggrPortTypeIndex_Type(Integer32):
    """Custom type gponSrvProfilePortVlanAggrPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("wlan", 1),
          ("catv", 2))
    )


_GponSrvProfilePortVlanAggrPortTypeIndex_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanAggrPortTypeIndex_Object = MibTableColumn
gponSrvProfilePortVlanAggrPortTypeIndex = _GponSrvProfilePortVlanAggrPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 2),
    _GponSrvProfilePortVlanAggrPortTypeIndex_Type()
)
gponSrvProfilePortVlanAggrPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrPortTypeIndex.setStatus("current")
_GponSrvProfilePortVlanAggrPortIdIndex_Type = Integer32
_GponSrvProfilePortVlanAggrPortIdIndex_Object = MibTableColumn
gponSrvProfilePortVlanAggrPortIdIndex = _GponSrvProfilePortVlanAggrPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 3),
    _GponSrvProfilePortVlanAggrPortIdIndex_Type()
)
gponSrvProfilePortVlanAggrPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrPortIdIndex.setStatus("current")
_GponSrvProfilePortVlanAggrVlanIndex_Type = Integer32
_GponSrvProfilePortVlanAggrVlanIndex_Object = MibTableColumn
gponSrvProfilePortVlanAggrVlanIndex = _GponSrvProfilePortVlanAggrVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 4),
    _GponSrvProfilePortVlanAggrVlanIndex_Type()
)
gponSrvProfilePortVlanAggrVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrVlanIndex.setStatus("current")


class _GponSrvProfilePortVlanAggrVlanList_Type(OctetString):
    """Custom type gponSrvProfilePortVlanAggrVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GponSrvProfilePortVlanAggrVlanList_Type.__name__ = "OctetString"
_GponSrvProfilePortVlanAggrVlanList_Object = MibTableColumn
gponSrvProfilePortVlanAggrVlanList = _GponSrvProfilePortVlanAggrVlanList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 5),
    _GponSrvProfilePortVlanAggrVlanList_Type()
)
gponSrvProfilePortVlanAggrVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrVlanList.setStatus("current")
_GponSrvProfilePortVlanAggrRowStatus_Type = RowStatus
_GponSrvProfilePortVlanAggrRowStatus_Object = MibTableColumn
gponSrvProfilePortVlanAggrRowStatus = _GponSrvProfilePortVlanAggrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 3, 1, 6),
    _GponSrvProfilePortVlanAggrRowStatus_Type()
)
gponSrvProfilePortVlanAggrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanAggrRowStatus.setStatus("current")
_GponSrvProfilePortVlanTrunkTable_Object = MibTable
gponSrvProfilePortVlanTrunkTable = _GponSrvProfilePortVlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4)
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkTable.setStatus("current")
_GponSrvProfilePortVlanTrunkEntry_Object = MibTableRow
gponSrvProfilePortVlanTrunkEntry = _GponSrvProfilePortVlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1)
)
gponSrvProfilePortVlanTrunkEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTrunkProfileIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTrunkPortTypeIndex"),
    (0, "NSCRTV-FTTX-GPON-MIB", "gponSrvProfilePortVlanTrunkPortIdIndex"),
)
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkEntry.setStatus("current")
_GponSrvProfilePortVlanTrunkProfileIndex_Type = Integer32
_GponSrvProfilePortVlanTrunkProfileIndex_Object = MibTableColumn
gponSrvProfilePortVlanTrunkProfileIndex = _GponSrvProfilePortVlanTrunkProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1, 1),
    _GponSrvProfilePortVlanTrunkProfileIndex_Type()
)
gponSrvProfilePortVlanTrunkProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkProfileIndex.setStatus("current")


class _GponSrvProfilePortVlanTrunkPortTypeIndex_Type(Integer32):
    """Custom type gponSrvProfilePortVlanTrunkPortTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("wlan", 1),
          ("catv", 2))
    )


_GponSrvProfilePortVlanTrunkPortTypeIndex_Type.__name__ = "Integer32"
_GponSrvProfilePortVlanTrunkPortTypeIndex_Object = MibTableColumn
gponSrvProfilePortVlanTrunkPortTypeIndex = _GponSrvProfilePortVlanTrunkPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1, 2),
    _GponSrvProfilePortVlanTrunkPortTypeIndex_Type()
)
gponSrvProfilePortVlanTrunkPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkPortTypeIndex.setStatus("current")
_GponSrvProfilePortVlanTrunkPortIdIndex_Type = Integer32
_GponSrvProfilePortVlanTrunkPortIdIndex_Object = MibTableColumn
gponSrvProfilePortVlanTrunkPortIdIndex = _GponSrvProfilePortVlanTrunkPortIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1, 3),
    _GponSrvProfilePortVlanTrunkPortIdIndex_Type()
)
gponSrvProfilePortVlanTrunkPortIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkPortIdIndex.setStatus("current")


class _GponSrvProfilePortVlanTrunkVlanList_Type(OctetString):
    """Custom type gponSrvProfilePortVlanTrunkVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GponSrvProfilePortVlanTrunkVlanList_Type.__name__ = "OctetString"
_GponSrvProfilePortVlanTrunkVlanList_Object = MibTableColumn
gponSrvProfilePortVlanTrunkVlanList = _GponSrvProfilePortVlanTrunkVlanList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1, 4),
    _GponSrvProfilePortVlanTrunkVlanList_Type()
)
gponSrvProfilePortVlanTrunkVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkVlanList.setStatus("current")
_GponSrvProfilePortVlanTrunkRowStatus_Type = RowStatus
_GponSrvProfilePortVlanTrunkRowStatus_Object = MibTableColumn
gponSrvProfilePortVlanTrunkRowStatus = _GponSrvProfilePortVlanTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 3, 5, 4, 1, 5),
    _GponSrvProfilePortVlanTrunkRowStatus_Type()
)
gponSrvProfilePortVlanTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponSrvProfilePortVlanTrunkRowStatus.setStatus("current")
_GponTrafficProfileObjects_ObjectIdentity = ObjectIdentity
gponTrafficProfileObjects = _GponTrafficProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4)
)
_GponTrafficProfileInfoTable_Object = MibTable
gponTrafficProfileInfoTable = _GponTrafficProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1)
)
if mibBuilder.loadTexts:
    gponTrafficProfileInfoTable.setStatus("current")
_GponTrafficProfileInfoEntry_Object = MibTableRow
gponTrafficProfileInfoEntry = _GponTrafficProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1)
)
gponTrafficProfileInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-GPON-MIB", "gponTrafficProfileId"),
)
if mibBuilder.loadTexts:
    gponTrafficProfileInfoEntry.setStatus("current")
_GponTrafficProfileId_Type = Integer32
_GponTrafficProfileId_Object = MibTableColumn
gponTrafficProfileId = _GponTrafficProfileId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 1),
    _GponTrafficProfileId_Type()
)
gponTrafficProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponTrafficProfileId.setStatus("current")
_GponTrafficProfileName_Type = DisplayString
_GponTrafficProfileName_Object = MibTableColumn
gponTrafficProfileName = _GponTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 2),
    _GponTrafficProfileName_Type()
)
gponTrafficProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileName.setStatus("current")
_GponTrafficProfileCfgCir_Type = Integer32
_GponTrafficProfileCfgCir_Object = MibTableColumn
gponTrafficProfileCfgCir = _GponTrafficProfileCfgCir_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 3),
    _GponTrafficProfileCfgCir_Type()
)
gponTrafficProfileCfgCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCir.setStatus("current")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCir.setUnits("kbit/s")
_GponTrafficProfileCfgPir_Type = Integer32
_GponTrafficProfileCfgPir_Object = MibTableColumn
gponTrafficProfileCfgPir = _GponTrafficProfileCfgPir_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 4),
    _GponTrafficProfileCfgPir_Type()
)
gponTrafficProfileCfgPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPir.setStatus("current")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPir.setUnits("kbit/s")
_GponTrafficProfileCfgCbs_Type = Integer32
_GponTrafficProfileCfgCbs_Object = MibTableColumn
gponTrafficProfileCfgCbs = _GponTrafficProfileCfgCbs_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 5),
    _GponTrafficProfileCfgCbs_Type()
)
gponTrafficProfileCfgCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCbs.setStatus("current")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgCbs.setUnits("byte")
_GponTrafficProfileCfgPbs_Type = Integer32
_GponTrafficProfileCfgPbs_Object = MibTableColumn
gponTrafficProfileCfgPbs = _GponTrafficProfileCfgPbs_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 6),
    _GponTrafficProfileCfgPbs_Type()
)
gponTrafficProfileCfgPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPbs.setStatus("current")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPbs.setUnits("byte")


class _GponTrafficProfileCfgPriority_Type(Integer32):
    """Custom type gponTrafficProfileCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GponTrafficProfileCfgPriority_Type.__name__ = "Integer32"
_GponTrafficProfileCfgPriority_Object = MibTableColumn
gponTrafficProfileCfgPriority = _GponTrafficProfileCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 7),
    _GponTrafficProfileCfgPriority_Type()
)
gponTrafficProfileCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gponTrafficProfileCfgPriority.setStatus("current")
_GponTrafficProfileBindNum_Type = Integer32
_GponTrafficProfileBindNum_Object = MibTableColumn
gponTrafficProfileBindNum = _GponTrafficProfileBindNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 8),
    _GponTrafficProfileBindNum_Type()
)
gponTrafficProfileBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTrafficProfileBindNum.setStatus("current")
_GponTrafficProfileRowStatus_Type = RowStatus
_GponTrafficProfileRowStatus_Object = MibTableColumn
gponTrafficProfileRowStatus = _GponTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 8, 11, 4, 1, 1, 9),
    _GponTrafficProfileRowStatus_Type()
)
gponTrafficProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gponTrafficProfileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

gponAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 1, 1)
)
gponAlarmNotification.setObjects(
      *(("NSCRTV-FTTX-GPON-MIB", "gponTrapSequenceNumber"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapOccurTime"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapCode"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapInstance"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapSeverity"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapCorrelationId"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    gponAlarmNotification.setStatus(
        "current"
    )

gponEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 12, 1, 1, 2)
)
gponEventNotification.setObjects(
      *(("NSCRTV-FTTX-GPON-MIB", "gponTrapSequenceNumber"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapOccurTime"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapCode"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapInstance"),
        ("NSCRTV-FTTX-GPON-MIB", "gponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    gponEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-FTTX-GPON-MIB",
    **{"GponAlarmInstance": GponAlarmInstance,
       "GponAlarmCode": GponAlarmCode,
       "GponSeverityType": GponSeverityType,
       "TAddress": TAddress,
       "GponCardIndex": GponCardIndex,
       "GponPortIndex": GponPortIndex,
       "GponDeviceIndex": GponDeviceIndex,
       "AutoNegotiationTechAbility": AutoNegotiationTechAbility,
       "GponStats15MinRecordType": GponStats15MinRecordType,
       "GponStats24HourRecordType": GponStats24HourRecordType,
       "GponStatsThresholdType": GponStatsThresholdType,
       "nscrtvRoot": nscrtvRoot,
       "nscrtvHFCemsTree": nscrtvHFCemsTree,
       "nscrtvFTTxTree": nscrtvFTTxTree,
       "propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "gponAlarmTree": gponAlarmTree,
       "gponTrapObjectGroup": gponTrapObjectGroup,
       "gponNotifications": gponNotifications,
       "gponAlarmNotification": gponAlarmNotification,
       "gponEventNotification": gponEventNotification,
       "gponTrapObjects": gponTrapObjects,
       "gponTrapInstance": gponTrapInstance,
       "gponTrapCorrelationId": gponTrapCorrelationId,
       "gponTrapAdditionalText": gponTrapAdditionalText,
       "gponTrapCode": gponTrapCode,
       "gponTrapSeverity": gponTrapSeverity,
       "gponTrapOccurTime": gponTrapOccurTime,
       "gponTrapSequenceNumber": gponTrapSequenceNumber,
       "gponAlarmObjGroup": gponAlarmObjGroup,
       "gponActiveAlarmTable": gponActiveAlarmTable,
       "gponActiveAlarmEntry": gponActiveAlarmEntry,
       "gponActiveAlarmSeqNum": gponActiveAlarmSeqNum,
       "gponActiveAlarmCode": gponActiveAlarmCode,
       "gponActiveAlarmInstance": gponActiveAlarmInstance,
       "gponActiveAlarmSeverity": gponActiveAlarmSeverity,
       "gponActiveAlarmRaisingNumber": gponActiveAlarmRaisingNumber,
       "gponActiveAlarmFirstOccurTime": gponActiveAlarmFirstOccurTime,
       "gponActiveAlarmLastOccurTime": gponActiveAlarmLastOccurTime,
       "gponActiveAlarmRepeats": gponActiveAlarmRepeats,
       "gponActiveAlarmConfirm": gponActiveAlarmConfirm,
       "gponActiveAlarmAdditionalText": gponActiveAlarmAdditionalText,
       "gponHistoryAlarmTable": gponHistoryAlarmTable,
       "gponHistoryAlarmEntry": gponHistoryAlarmEntry,
       "gponHistoryAlarmSeqNum": gponHistoryAlarmSeqNum,
       "gponHistoryAlarmCode": gponHistoryAlarmCode,
       "gponHistoryAlarmInstance": gponHistoryAlarmInstance,
       "gponHistoryAlarmSeverity": gponHistoryAlarmSeverity,
       "gponHistoryAlarmRaisingNumber": gponHistoryAlarmRaisingNumber,
       "gponHistoryAlarmFirstOccurTime": gponHistoryAlarmFirstOccurTime,
       "gponHistoryAlarmLastOccurTime": gponHistoryAlarmLastOccurTime,
       "gponHistoryAlarmRepeats": gponHistoryAlarmRepeats,
       "gponHistoryAlarmCorrelationId": gponHistoryAlarmCorrelationId,
       "gponHistoryAlarmAdditionalText": gponHistoryAlarmAdditionalText,
       "gponHistoryAlarmClearTime": gponHistoryAlarmClearTime,
       "gponEventLogTable": gponEventLogTable,
       "gponEventLogEntry": gponEventLogEntry,
       "gponEventSeqNum": gponEventSeqNum,
       "gponEventCode": gponEventCode,
       "gponEventInstance": gponEventInstance,
       "gponEventOccurTime": gponEventOccurTime,
       "gponEventAdditionalText": gponEventAdditionalText,
       "gponManagementObjGroup": gponManagementObjGroup,
       "gponManagementAddrTable": gponManagementAddrTable,
       "gponManagementAddrEntry": gponManagementAddrEntry,
       "gponManagementAddrName": gponManagementAddrName,
       "gponManagementAddrTAddress": gponManagementAddrTAddress,
       "gponManagementAddrCommunity": gponManagementAddrCommunity,
       "gponManagementAddrRowStatus": gponManagementAddrRowStatus,
       "gponTree": gponTree,
       "gponPonPortObjects": gponPonPortObjects,
       "gponOnuAuthenticationModeTable": gponOnuAuthenticationModeTable,
       "gponOnuAuthenticationModeEntry": gponOnuAuthenticationModeEntry,
       "gponAuthenDeviceIndex": gponAuthenDeviceIndex,
       "gponAuthenCardIndex": gponAuthenCardIndex,
       "gponAuthenPortIndex": gponAuthenPortIndex,
       "gponOnuAuthenMode": gponOnuAuthenMode,
       "gponAutoFindEnable": gponAutoFindEnable,
       "gponOnuObjects": gponOnuObjects,
       "gponOnuInfoTable": gponOnuInfoTable,
       "gponOnuInfoEntry": gponOnuInfoEntry,
       "onuDeviceIndex": onuDeviceIndex,
       "onuName": onuName,
       "onuSerialNum": onuSerialNum,
       "onuType": onuType,
       "onuVendorID": onuVendorID,
       "onuEquipmentID": onuEquipmentID,
       "onuOperationStatus": onuOperationStatus,
       "onuAdminStatus": onuAdminStatus,
       "onuTestDistance": onuTestDistance,
       "resetONU": resetONU,
       "onuDeactive": onuDeactive,
       "onuTimeSinceLastRegister": onuTimeSinceLastRegister,
       "onuSysUpTime": onuSysUpTime,
       "onuHardwareVersion": onuHardwareVersion,
       "onuPerfStats15minuteEnable": onuPerfStats15minuteEnable,
       "onuPerfStats24hourEnable": onuPerfStats24hourEnable,
       "onuInfoSoftwareTable": onuInfoSoftwareTable,
       "onuInfoSoftwareEntry": onuInfoSoftwareEntry,
       "onuSoftwareDeviceIndex": onuSoftwareDeviceIndex,
       "onuSoftware0Version": onuSoftware0Version,
       "onuSoftware0Valid": onuSoftware0Valid,
       "onuSoftware0Active": onuSoftware0Active,
       "onuSoftware0Commited": onuSoftware0Commited,
       "onuSoftware1Version": onuSoftware1Version,
       "onuSoftware1Valid": onuSoftware1Valid,
       "onuSoftware1Active": onuSoftware1Active,
       "onuSoftware1Commited": onuSoftware1Commited,
       "onuIpHostTable": onuIpHostTable,
       "onuIpHostEntry": onuIpHostEntry,
       "onuIpHostDeviceIndex": onuIpHostDeviceIndex,
       "onuIpHostIndex": onuIpHostIndex,
       "onuIpHostAddressConfigMode": onuIpHostAddressConfigMode,
       "onuIpHostAddress": onuIpHostAddress,
       "onuIpHostSubnetMask": onuIpHostSubnetMask,
       "onuIpHostGateway": onuIpHostGateway,
       "onuIpHostPrimaryDNS": onuIpHostPrimaryDNS,
       "onuIpHostSecondaryDNS": onuIpHostSecondaryDNS,
       "onuIpHostVlanTagPriority": onuIpHostVlanTagPriority,
       "onuIpHostVlanPvid": onuIpHostVlanPvid,
       "onuIpHostMacAddress": onuIpHostMacAddress,
       "onuIpHostRowStatus": onuIpHostRowStatus,
       "gponOnuPonPortOpticalTransmissionPropertyTable": gponOnuPonPortOpticalTransmissionPropertyTable,
       "gponOnuPonPortOpticalTransmissionPropertyEntry": gponOnuPonPortOpticalTransmissionPropertyEntry,
       "onuPonPortOpticalTransmissionPropertyDeviceIndex": onuPonPortOpticalTransmissionPropertyDeviceIndex,
       "onuPonPortOpticalTransmissionPropertyCardIndex": onuPonPortOpticalTransmissionPropertyCardIndex,
       "onuPonPortOpticalTransmissionPropertyPortIndex": onuPonPortOpticalTransmissionPropertyPortIndex,
       "onuReceivedOpticalPower": onuReceivedOpticalPower,
       "onuTramsmittedOpticalPower": onuTramsmittedOpticalPower,
       "onuBiasCurrent": onuBiasCurrent,
       "onuWorkingVoltage": onuWorkingVoltage,
       "onuWorkingTemperature": onuWorkingTemperature,
       "onuCapabilityTable": onuCapabilityTable,
       "onuCapabilityEntry": onuCapabilityEntry,
       "onuCapabilityDeviceIndex": onuCapabilityDeviceIndex,
       "onuOMCCVersion": onuOMCCVersion,
       "onuTotalEthNum": onuTotalEthNum,
       "onuTotalWlanNum": onuTotalWlanNum,
       "onuTotalCatvNum": onuTotalCatvNum,
       "onuTotalVeipNum": onuTotalVeipNum,
       "onuIpHostNum": onuIpHostNum,
       "onuTrafficMgmtOption": onuTrafficMgmtOption,
       "onuTotalGEMPortNum": onuTotalGEMPortNum,
       "onuTotalTContNum": onuTotalTContNum,
       "onuConnectCapbility": onuConnectCapbility,
       "onuQosFlexibility": onuQosFlexibility,
       "onuAuthenticationManagement": onuAuthenticationManagement,
       "onuAuthenticationConfigTable": onuAuthenticationConfigTable,
       "onuAuthenticationConfigEntry": onuAuthenticationConfigEntry,
       "onuAuthenOnuId": onuAuthenOnuId,
       "onuAuthenSN": onuAuthenSN,
       "onuAuthenPassword": onuAuthenPassword,
       "onuAuthenLoid": onuAuthenLoid,
       "onuAuthenLoidPassword": onuAuthenLoidPassword,
       "onuAuthenLineProfileId": onuAuthenLineProfileId,
       "onuAuthenSrvProfileId": onuAuthenSrvProfileId,
       "onuAuthenRowStatus": onuAuthenRowStatus,
       "onuAutoFindTable": onuAutoFindTable,
       "onuAutoFindEntry": onuAutoFindEntry,
       "onuAutoFindOnuIndex": onuAutoFindOnuIndex,
       "onuAutoFindOnuType": onuAutoFindOnuType,
       "onuAutoFindSerialNumber": onuAutoFindSerialNumber,
       "onuAutoFindPassword": onuAutoFindPassword,
       "onuAutoFindLoid": onuAutoFindLoid,
       "onuAutoFindLoidPassword": onuAutoFindLoidPassword,
       "onuAutoFindTime": onuAutoFindTime,
       "onuAutoFindSoftwareVersion": onuAutoFindSoftwareVersion,
       "onuAutoFindHardwareVersion": onuAutoFindHardwareVersion,
       "onuAutoAuthenticationTable": onuAutoAuthenticationTable,
       "onuAutoAuthenticationEntry": onuAutoAuthenticationEntry,
       "onuAutoAuthenIndex": onuAutoAuthenIndex,
       "onuAutoAuthenPortlist": onuAutoAuthenPortlist,
       "onuAutoAuthenOnuType": onuAutoAuthenOnuType,
       "onuAutoAuthenEthNum": onuAutoAuthenEthNum,
       "onuAutoAuthenWlanNum": onuAutoAuthenWlanNum,
       "onuAutoAuthenCatvNum": onuAutoAuthenCatvNum,
       "onuAutoAuthenVeipNum": onuAutoAuthenVeipNum,
       "onuAutoAuthenLineProfileId": onuAutoAuthenLineProfileId,
       "onuAutoAuthenSrvProfileId": onuAutoAuthenSrvProfileId,
       "onuAutoAuthenRowStatus": onuAutoAuthenRowStatus,
       "gponUniObjects": gponUniObjects,
       "ethAttributeTable": ethAttributeTable,
       "ethAttributeEntry": ethAttributeEntry,
       "ethAttributeDeviceIndex": ethAttributeDeviceIndex,
       "ethAttributeCardIndex": ethAttributeCardIndex,
       "ethAttributePortIndex": ethAttributePortIndex,
       "ethAdminStatus": ethAdminStatus,
       "ethOperationStatus": ethOperationStatus,
       "ethDuplexRate": ethDuplexRate,
       "ethPerfStats15minuteEnable": ethPerfStats15minuteEnable,
       "ethPerfStats24hourEnable": ethPerfStats24hourEnable,
       "gponIgmpManagementObjects": gponIgmpManagementObjects,
       "gponOnuIgmpProfile": gponOnuIgmpProfile,
       "gponOnuIgmpProfileTable": gponOnuIgmpProfileTable,
       "gponOnuIgmpProfileEntry": gponOnuIgmpProfileEntry,
       "gponOnuIgmpProfileIndex": gponOnuIgmpProfileIndex,
       "gponOnuIgmpProfileName": gponOnuIgmpProfileName,
       "gponOnuIgmpVersion": gponOnuIgmpVersion,
       "gponOnuIgmpFunction": gponOnuIgmpFunction,
       "gponOnuIgmpImmediateLeave": gponOnuIgmpImmediateLeave,
       "gponOnuIgmpUpstreamProtoTCI": gponOnuIgmpUpstreamProtoTCI,
       "gponOnuIgmpUpstreamProtoTagControl": gponOnuIgmpUpstreamProtoTagControl,
       "gponOnuIgmpUpstreamProtoRate": gponOnuIgmpUpstreamProtoRate,
       "gponOnuIgmpDynamicACL": gponOnuIgmpDynamicACL,
       "gponOnuIgmpStaticACL": gponOnuIgmpStaticACL,
       "gponOnuIgmpRobustness": gponOnuIgmpRobustness,
       "gponOnuIgmpQueryInterval": gponOnuIgmpQueryInterval,
       "gponOnuIgmpQueryMaxResponseTime": gponOnuIgmpQueryMaxResponseTime,
       "gponOnuIgmpLastMemberQueryInterval": gponOnuIgmpLastMemberQueryInterval,
       "gponOnuIgmpUnautherizedJoin": gponOnuIgmpUnautherizedJoin,
       "gponOnuIgmpDownstreamTCI": gponOnuIgmpDownstreamTCI,
       "gponOnuIgmpDownstreamTagControl": gponOnuIgmpDownstreamTagControl,
       "gponOnuIgmpMaxRequestChannelNum": gponOnuIgmpMaxRequestChannelNum,
       "gponOnuIgmpGlobalBW": gponOnuIgmpGlobalBW,
       "gponOnuIgmpRowStatus": gponOnuIgmpRowStatus,
       "gponOnuMulticastACLTable": gponOnuMulticastACLTable,
       "gponOnuMulticastACLEntry": gponOnuMulticastACLEntry,
       "multicastACLIndex": multicastACLIndex,
       "multicastACLRuleIndex": multicastACLRuleIndex,
       "multicastACLRuleName": multicastACLRuleName,
       "vlanID": vlanID,
       "sourceIpAddress": sourceIpAddress,
       "destinationIpAddressStart": destinationIpAddressStart,
       "destinationIpAddressEnd": destinationIpAddressEnd,
       "previewLenAndAuthority": previewLenAndAuthority,
       "previewRepeatTime": previewRepeatTime,
       "previewResetTime": previewResetTime,
       "previewCount": previewCount,
       "imputedGroupBandwidth": imputedGroupBandwidth,
       "multicastACLRuleStatus": multicastACLRuleStatus,
       "gponIgmpOnuUniTable": gponIgmpOnuUniTable,
       "gponIgmpOnuUniEntry": gponIgmpOnuUniEntry,
       "gponUniDeviceIndex": gponUniDeviceIndex,
       "gponUniCardIndex": gponUniCardIndex,
       "gponUniPortIndex": gponUniPortIndex,
       "gponUniIgmpProfileIndex": gponUniIgmpProfileIndex,
       "gponUniRowstatus": gponUniRowstatus,
       "igmpOnuMulticastInfoTable": igmpOnuMulticastInfoTable,
       "igmpOnuMulticastInfoEntry": igmpOnuMulticastInfoEntry,
       "onuMcInfoDeviceIndex": onuMcInfoDeviceIndex,
       "onuMcInfoCardIndex": onuMcInfoCardIndex,
       "onuMcInfoPortIndex": onuMcInfoPortIndex,
       "onuMcInfoIndex": onuMcInfoIndex,
       "onuMcInfoSrcIp": onuMcInfoSrcIp,
       "onuMcInfoMcDstIp": onuMcInfoMcDstIp,
       "onuMcInfoMvlanVid": onuMcInfoMvlanVid,
       "onuMcInfoClientIp": onuMcInfoClientIp,
       "gponPerformanceStatisticObjects": gponPerformanceStatisticObjects,
       "gponPerfStatsThresholdTable": gponPerfStatsThresholdTable,
       "gponPerfStatsThresholdEntry": gponPerfStatsThresholdEntry,
       "gponPerfStatsThresholdDeviceIndex": gponPerfStatsThresholdDeviceIndex,
       "gponPerfStatsThresholdCardIndex": gponPerfStatsThresholdCardIndex,
       "gponPerfStatsThresholdPortIndex": gponPerfStatsThresholdPortIndex,
       "gponPerfStatsThresholdTypeIndex": gponPerfStatsThresholdTypeIndex,
       "gponPerfStatsThresholdUpper": gponPerfStatsThresholdUpper,
       "gponPerfStatsThresholdLower": gponPerfStatsThresholdLower,
       "gponPerfStatsThresholdRowStatus": gponPerfStatsThresholdRowStatus,
       "curStatsGemPortTable": curStatsGemPortTable,
       "curStatsGemPortEntry": curStatsGemPortEntry,
       "curStatsGemPortDeviceIndex": curStatsGemPortDeviceIndex,
       "curStatsGemPortIndex": curStatsGemPortIndex,
       "curStatsGemPortOutGemFrames": curStatsGemPortOutGemFrames,
       "curStatsGemPortInGemFrames": curStatsGemPortInGemFrames,
       "curStatsGemPortOutBytes": curStatsGemPortOutBytes,
       "curStatsGemPortInBytes": curStatsGemPortInBytes,
       "curStatsGemPortStatusAndAction": curStatsGemPortStatusAndAction,
       "stats15GemPortTable": stats15GemPortTable,
       "stats15GemPortEntry": stats15GemPortEntry,
       "stats15GemPortDeviceIndex": stats15GemPortDeviceIndex,
       "stats15GemPortIndex": stats15GemPortIndex,
       "stats15GemPortStatIndex": stats15GemPortStatIndex,
       "stats15GemPortOutGemFrames": stats15GemPortOutGemFrames,
       "stats15GemPortInGemFrames": stats15GemPortInGemFrames,
       "stats15GemPortOutBytes": stats15GemPortOutBytes,
       "stats15GemPortInBytes": stats15GemPortInBytes,
       "stats15GemPortStatusAndAction": stats15GemPortStatusAndAction,
       "stats15GemPortValidityTag": stats15GemPortValidityTag,
       "stats15GemPortElapsedTime": stats15GemPortElapsedTime,
       "stats15GemPortEndTime": stats15GemPortEndTime,
       "stats24GemPortTable": stats24GemPortTable,
       "stats24GemPortEntry": stats24GemPortEntry,
       "stats24GemPortDeviceIndex": stats24GemPortDeviceIndex,
       "stats24GemPortIndex": stats24GemPortIndex,
       "stats24GemPortStatIndex": stats24GemPortStatIndex,
       "stats24GemPortOutGemFrames": stats24GemPortOutGemFrames,
       "stats24GemPortInGemFrames": stats24GemPortInGemFrames,
       "stats24GemPortOutBytes": stats24GemPortOutBytes,
       "stats24GemPortInBytes": stats24GemPortInBytes,
       "stats24GemPortStatusAndAction": stats24GemPortStatusAndAction,
       "stats24GemPortValidityTag": stats24GemPortValidityTag,
       "stats24GemPortElapsedTime": stats24GemPortElapsedTime,
       "stats24GemPortEndTime": stats24GemPortEndTime,
       "gponProfileObjects": gponProfileObjects,
       "gponDbaProfileObjects": gponDbaProfileObjects,
       "gponDbaProfileInfoTable": gponDbaProfileInfoTable,
       "gponDbaProfileInfoEntry": gponDbaProfileInfoEntry,
       "gponDbaProfileId": gponDbaProfileId,
       "gponDbaProfileName": gponDbaProfileName,
       "gponDbaProfileType": gponDbaProfileType,
       "gponDbaProfileFixRate": gponDbaProfileFixRate,
       "gponDbaProfileAssureRate": gponDbaProfileAssureRate,
       "gponDbaProfileMaxRate": gponDbaProfileMaxRate,
       "gponDbaProfileBindNum": gponDbaProfileBindNum,
       "gponDbaProfileRowStatus": gponDbaProfileRowStatus,
       "gponLineProfileObjects": gponLineProfileObjects,
       "gponLineProfileInfoTable": gponLineProfileInfoTable,
       "gponLineProfileInfoEntry": gponLineProfileInfoEntry,
       "gponLineProfileId": gponLineProfileId,
       "gponLineProfileName": gponLineProfileName,
       "gponLineProfileUpstreamFECMode": gponLineProfileUpstreamFECMode,
       "gponLineProfileMappingMode": gponLineProfileMappingMode,
       "gponLineProfileTcontNum": gponLineProfileTcontNum,
       "gponLineProfileGemNum": gponLineProfileGemNum,
       "gponLineProfileBindNum": gponLineProfileBindNum,
       "gponLineProfileRowStatus": gponLineProfileRowStatus,
       "gponLineProfileTcontTable": gponLineProfileTcontTable,
       "gponLineProfileTcontEntry": gponLineProfileTcontEntry,
       "gponLineProfileTcontProfileIndex": gponLineProfileTcontProfileIndex,
       "gponLineProfileTcontIndex": gponLineProfileTcontIndex,
       "gponLineProfileTcontDbaProfileId": gponLineProfileTcontDbaProfileId,
       "gponLineProfileTcontRowStatus": gponLineProfileTcontRowStatus,
       "gponLineProfileGemTable": gponLineProfileGemTable,
       "gponLineProfileGemEntry": gponLineProfileGemEntry,
       "gponLineProfileGemProfileIndex": gponLineProfileGemProfileIndex,
       "gponLineProfileGemIndex": gponLineProfileGemIndex,
       "gponLineProfileGemEncrypt": gponLineProfileGemEncrypt,
       "gponLineProfileGemTcontId": gponLineProfileGemTcontId,
       "gponLineProfileGemQueuePri": gponLineProfileGemQueuePri,
       "gponLineProfileGemUpCar": gponLineProfileGemUpCar,
       "gponLineProfileGemDownCar": gponLineProfileGemDownCar,
       "gponLineProfileGemMapNum": gponLineProfileGemMapNum,
       "gponLineProfileGemRowStatus": gponLineProfileGemRowStatus,
       "gponLineProfileGemMapTable": gponLineProfileGemMapTable,
       "gponLineProfileGemMapEntry": gponLineProfileGemMapEntry,
       "gponLineProfileGemMapProfileIndex": gponLineProfileGemMapProfileIndex,
       "gponLineProfileGemMapGemIndex": gponLineProfileGemMapGemIndex,
       "gponLineProfileGemMapIndex": gponLineProfileGemMapIndex,
       "gponLineProfileGemMapVlan": gponLineProfileGemMapVlan,
       "gponLineProfileGemMapPriority": gponLineProfileGemMapPriority,
       "gponLineProfileGemMapPortType": gponLineProfileGemMapPortType,
       "gponLineProfileGemMapPortId": gponLineProfileGemMapPortId,
       "gponLineProfileGemMapRowStatus": gponLineProfileGemMapRowStatus,
       "gponSrvProfileObjects": gponSrvProfileObjects,
       "gponSrvProfileInfoTable": gponSrvProfileInfoTable,
       "gponSrvProfileInfoEntry": gponSrvProfileInfoEntry,
       "gponSrvProfileId": gponSrvProfileId,
       "gponSrvProfileName": gponSrvProfileName,
       "gponSrvProfileBindNum": gponSrvProfileBindNum,
       "gponSrvProfileRowStatus": gponSrvProfileRowStatus,
       "gponSrvProfileCfgTable": gponSrvProfileCfgTable,
       "gponSrvProfileCfgEntry": gponSrvProfileCfgEntry,
       "gponSrvProfileIndex": gponSrvProfileIndex,
       "gponSrvProfileMacLearning": gponSrvProfileMacLearning,
       "gponSrvProfileMacAgeSeconds": gponSrvProfileMacAgeSeconds,
       "gponSrvProfileLoopbackDetectCheck": gponSrvProfileLoopbackDetectCheck,
       "gponSrvProfilePortNumTable": gponSrvProfilePortNumTable,
       "gponSrvProfilePortNumEntry": gponSrvProfilePortNumEntry,
       "gponSrvProfilePortNumProfileIndex": gponSrvProfilePortNumProfileIndex,
       "gponSrvProfileEthNum": gponSrvProfileEthNum,
       "gponSrvProfileCatvNum": gponSrvProfileCatvNum,
       "gponSrvProfileWlanNum": gponSrvProfileWlanNum,
       "gponSrvProfileVeipNum": gponSrvProfileVeipNum,
       "gponSrvProfileEthPortConfigTable": gponSrvProfileEthPortConfigTable,
       "gponSrvProfileEthPortConfigEntry": gponSrvProfileEthPortConfigEntry,
       "gponSrvProfileEthPortProfileIndex": gponSrvProfileEthPortProfileIndex,
       "gponSrvProfileEthPortIdIndex": gponSrvProfileEthPortIdIndex,
       "gponSrvProfileEthPortMacLimited": gponSrvProfileEthPortMacLimited,
       "gponSrvProfileEthPortMtu": gponSrvProfileEthPortMtu,
       "gponSrvProfileEthPortFlowCtrl": gponSrvProfileEthPortFlowCtrl,
       "gponSrvProfileEthPortInTrafficProfileId": gponSrvProfileEthPortInTrafficProfileId,
       "gponSrvProfileEthPortOutTrafficProfileId": gponSrvProfileEthPortOutTrafficProfileId,
       "gponSrvProfilePortVlanObjects": gponSrvProfilePortVlanObjects,
       "gponSrvProfilePortVlanCfgTable": gponSrvProfilePortVlanCfgTable,
       "gponSrvProfilePortVlanCfgEntry": gponSrvProfilePortVlanCfgEntry,
       "gponSrvProfilePortVlanProfileIndex": gponSrvProfilePortVlanProfileIndex,
       "gponSrvProfilePortVlanPortTypeIndex": gponSrvProfilePortVlanPortTypeIndex,
       "gponSrvProfilePortVlanPortIdIndex": gponSrvProfilePortVlanPortIdIndex,
       "gponSrvProfilePortVlanPvid": gponSrvProfilePortVlanPvid,
       "gponSrvProfilePortVlanPvidPri": gponSrvProfilePortVlanPvidPri,
       "gponSrvProfilePortVlanMode": gponSrvProfilePortVlanMode,
       "gponSrvProfilePortVlanTranslationTable": gponSrvProfilePortVlanTranslationTable,
       "gponSrvProfilePortVlanTranslationEntry": gponSrvProfilePortVlanTranslationEntry,
       "gponSrvProfilePortVlanTransProfileIndex": gponSrvProfilePortVlanTransProfileIndex,
       "gponSrvProfilePortVlanTransPortTypeIndex": gponSrvProfilePortVlanTransPortTypeIndex,
       "gponSrvProfilePortVlanTransPortIdIndex": gponSrvProfilePortVlanTransPortIdIndex,
       "gponSrvProfilePortVlanTransVlanIndex": gponSrvProfilePortVlanTransVlanIndex,
       "gponSrvProfilePortVlanTransNewVlan": gponSrvProfilePortVlanTransNewVlan,
       "gponSrvProfilePortVlanTransRowStatus": gponSrvProfilePortVlanTransRowStatus,
       "gponSrvProfilePortVlanAggregationTable": gponSrvProfilePortVlanAggregationTable,
       "gponSrvProfilePortVlanAggregationEntry": gponSrvProfilePortVlanAggregationEntry,
       "gponSrvProfilePortVlanAggrProfileIndex": gponSrvProfilePortVlanAggrProfileIndex,
       "gponSrvProfilePortVlanAggrPortTypeIndex": gponSrvProfilePortVlanAggrPortTypeIndex,
       "gponSrvProfilePortVlanAggrPortIdIndex": gponSrvProfilePortVlanAggrPortIdIndex,
       "gponSrvProfilePortVlanAggrVlanIndex": gponSrvProfilePortVlanAggrVlanIndex,
       "gponSrvProfilePortVlanAggrVlanList": gponSrvProfilePortVlanAggrVlanList,
       "gponSrvProfilePortVlanAggrRowStatus": gponSrvProfilePortVlanAggrRowStatus,
       "gponSrvProfilePortVlanTrunkTable": gponSrvProfilePortVlanTrunkTable,
       "gponSrvProfilePortVlanTrunkEntry": gponSrvProfilePortVlanTrunkEntry,
       "gponSrvProfilePortVlanTrunkProfileIndex": gponSrvProfilePortVlanTrunkProfileIndex,
       "gponSrvProfilePortVlanTrunkPortTypeIndex": gponSrvProfilePortVlanTrunkPortTypeIndex,
       "gponSrvProfilePortVlanTrunkPortIdIndex": gponSrvProfilePortVlanTrunkPortIdIndex,
       "gponSrvProfilePortVlanTrunkVlanList": gponSrvProfilePortVlanTrunkVlanList,
       "gponSrvProfilePortVlanTrunkRowStatus": gponSrvProfilePortVlanTrunkRowStatus,
       "gponTrafficProfileObjects": gponTrafficProfileObjects,
       "gponTrafficProfileInfoTable": gponTrafficProfileInfoTable,
       "gponTrafficProfileInfoEntry": gponTrafficProfileInfoEntry,
       "gponTrafficProfileId": gponTrafficProfileId,
       "gponTrafficProfileName": gponTrafficProfileName,
       "gponTrafficProfileCfgCir": gponTrafficProfileCfgCir,
       "gponTrafficProfileCfgPir": gponTrafficProfileCfgPir,
       "gponTrafficProfileCfgCbs": gponTrafficProfileCfgCbs,
       "gponTrafficProfileCfgPbs": gponTrafficProfileCfgPbs,
       "gponTrafficProfileCfgPriority": gponTrafficProfileCfgPriority,
       "gponTrafficProfileBindNum": gponTrafficProfileBindNum,
       "gponTrafficProfileRowStatus": gponTrafficProfileRowStatus}
)
