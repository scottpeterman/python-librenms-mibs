# SNMP MIB module (PEGASUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pegasus\PEGASUS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:37 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pegasusMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2)
)
if mibBuilder.loadTexts:
    pegasusMibModule.setRevisions(
        ("2004-12-17 00:00",
         "2004-06-14 00:00",
         "2004-04-08 00:00",
         "2003-12-11 00:00",
         "2003-10-30 00:00",
         "2003-10-24 00:00",
         "2003-10-02 00:00",
         "2003-03-14 00:00",
         "2003-03-11 00:00",
         "2002-10-09 00:00",
         "2002-09-19 00:00",
         "2002-08-23 00:00",
         "2002-07-16 00:00",
         "2002-07-03 00:00",
         "2002-06-24 00:00",
         "2002-06-20 00:00",
         "2002-06-07 00:00",
         "2002-05-22 00:00",
         "2002-05-10 00:00",
         "2002-04-25 00:00",
         "2002-04-16 00:00",
         "2002-04-03 00:00",
         "2002-03-19 00:00",
         "2002-03-14 00:00",
         "2002-03-01 00:00",
         "2002-02-28 00:00",
         "2002-02-18 00:00",
         "2002-02-14 00:00",
         "2002-01-25 00:00",
         "2002-01-23 00:00",
         "2000-12-21 00:00")
    )


# Types definitions



class AdminStateEnum(Integer32):
    """Custom type AdminStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2),
          ("shutdown", 3))
    )





class OperStateEnum(Integer32):
    """Custom type OperStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )





class CommStateEnum(Integer32):
    """Custom type CommStateEnum based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("init", 2),
          ("identification", 3),
          ("checkHw", 4),
          ("hwAdaption", 5),
          ("checkHwVers", 6),
          ("wrongProgram", 7),
          ("checkConfig", 8),
          ("downloadConfig", 9),
          ("uploadConfig", 10),
          ("statusSynch", 11),
          ("resetting", 12),
          ("inactive", 13),
          ("active", 14))
    )





class DataPortSpeedEnum(Integer32):
    """Custom type DataPortSpeedEnum based on Integer32"""
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
        *(("autoCrossoverAndPortSpeed", 1),
          ("autoNegotiationPortSpeed", 2),
          ("base100TFullDuplex", 3),
          ("base100THalfDuplex", 4),
          ("base10TFullDuplex", 5),
          ("base10THalfDuplex", 6),
          ("unknown", 7))
    )





class DataPortFlowControlEnum(Integer32):
    """Custom type DataPortFlowControlEnum based on Integer32"""
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
        *(("autoNegotiationFlowControl", 1),
          ("onFlowControl", 2),
          ("offFlowControl", 3),
          ("unknown", 4))
    )





class SlotNumber(Integer32):
    """Custom type SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )





class DataCardSlotNumber(Integer32):
    """Custom type DataCardSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )





class V5SlotNumber(Integer32):
    """Custom type V5SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )





class DslSlotNumber(Integer32):
    """Custom type DslSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )





class DslLinkNumber(Integer32):
    """Custom type DslLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )





class TrunkNumber(Integer32):
    """Custom type TrunkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )





class TrunkNumberOrZero(Integer32):
    """Custom type TrunkNumberOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )





class Priority(Integer32):
    """Custom type Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )





class DslLinkLoopEnum(Integer32):
    """Custom type DslLinkLoopEnum based on Integer32"""
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
          ("loop1", 2),
          ("loop2", 3))
    )





class DslLinkPSDMaskEnum(Integer32):
    """Custom type DslLinkPSDMaskEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("symmetric", 1),
          ("asymmetric", 2))
    )





class IadISDNPoweringEnum(Integer32):
    """Custom type IadISDNPoweringEnum based on Integer32"""
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
        *(("off", 1),
          ("normal", 2),
          ("lifeline", 3),
          ("always", 4))
    )





class IadPOTSPoweringEnum(Integer32):
    """Custom type IadPOTSPoweringEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("always", 2))
    )





class DslInterfaceTypeEnum(Integer32):
    """Custom type DslInterfaceTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ltu", 1),
          ("ntu", 2))
    )





class CosClassifierEnum(Integer32):
    """Custom type CosClassifierEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanPriority", 1),
          ("dscpPriority", 2))
    )





class V5ClockModeEnum(Integer32):
    """Custom type V5ClockModeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v5ClockMaster", 1),
          ("v5ClockSlave", 2))
    )





class V5ClockSourceEnum(Integer32):
    """Custom type V5ClockSourceEnum based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("v5ClockExternal", 1),
          ("v5ClockLink1", 2),
          ("v5ClockLink2", 3),
          ("v5ClockLink3", 4),
          ("v5ClockLink4", 5),
          ("v5ClockLink5", 6),
          ("v5ClockLink6", 7),
          ("v5ClockLink7", 8),
          ("v5ClockLink8", 9))
    )





class V5ProtocolVersionEnum(Integer32):
    """Custom type V5ProtocolVersionEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v51", 1),
          ("v52", 2))
    )





class V5LinkNumber(Integer32):
    """Custom type V5LinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )





class V5LinkNumberOrZero(Integer32):
    """Custom type V5LinkNumberOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )





class V5InterfaceNumber(V5LinkNumber):
    """Custom type V5InterfaceNumber based on V5LinkNumber"""




class V5InterfaceNumberOrZero(V5LinkNumberOrZero):
    """Custom type V5InterfaceNumberOrZero based on V5LinkNumberOrZero"""




class V5PccCount(Integer32):
    """Custom type V5PccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )





class V5LinkTypeEnum(Integer32):
    """Custom type V5LinkTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("normal", 3))
    )





class V5LccNumber(Integer32):
    """Custom type V5LccNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )





class V5LccNumberOrZero(Integer32):
    """Custom type V5LccNumberOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )





class V5PccNumberOrZero(Integer32):
    """Custom type V5PccNumberOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )





class V5IsdnPortLoopEnum(Integer32):
    """Custom type V5IsdnPortLoopEnum based on Integer32"""
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
          ("loop1", 2),
          ("loop2", 3))
    )





class V5IsdnPortBlockingStatusEnum(Integer32):
    """Custom type V5IsdnPortBlockingStatusEnum based on Integer32"""
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
          ("local", 2),
          ("remote", 3),
          ("both", 4))
    )





class V5TimeslotNumber(Integer32):
    """Custom type V5TimeslotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
        ValueRangeConstraint(17, 31),
    )





class V5EnvelopeFuncAddress(Integer32):
    """Custom type V5EnvelopeFuncAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8175),
    )





class ConfigPriorityEnum(Integer32):
    """Custom type ConfigPriorityEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("device", 2))
    )





class HWAdaptionPolicyEnum(Integer32):
    """Custom type HWAdaptionPolicyEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("server", 2))
    )





class PerfHistoryType(Integer32):
    """Custom type PerfHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("history15m", 1),
          ("history24h", 2))
    )




# TEXTUAL-CONVENTIONS



class AvailabilityStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("inTest", 0),
          ("failed", 1),
          ("powerOff", 2),
          ("offLine", 3),
          ("offDuty", 4),
          ("dependency", 5),
          ("degraded", 6),
          ("notInstalled", 7),
          ("logFull", 8))
    )


class DslLinkAlarmElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("config", 0),
          ("service", 1))
    )


class DslCardAlarmStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("intercom", 0)
    )


class IadAlarmStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("powerdown", 0),
          ("lifeline", 1),
          ("dcContinuity", 2))
    )


class DslPerformanceStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("att", 0),
          ("losw", 1))
    )


class CosClassmap(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class V5CardFlagSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("noFastAlign", 0),
          ("noLinkId", 1),
          ("autoPortUnblock", 2),
          ("retryAutoPortUnblock", 3),
          ("rejectLinkId", 4),
          ("forcePSTNDL", 5),
          ("slowStart", 6),
          ("deallocBlockedPort", 7))
    )


class V5LinkAlarmStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("v5LinkAlarmLOS", 0),
          ("v5LinkAlarmLFA", 1),
          ("v5LinkAlarmAIS", 2),
          ("v5LinkAlarmBERH", 3),
          ("v5LinkAlarmEXTLOC", 4),
          ("v5LinkAlarmRAI", 5),
          ("v5LinkAlarmIdFailure", 6))
    )


class V5InterfaceAlarmSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("idFailure", 0),
          ("provisioningMismatch", 1))
    )


class V5IsdnPortAlarmStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("l1ActivationFault", 0),
          ("losTref", 1),
          ("losDsig", 2))
    )


class RackAlarmStatusElem(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("psu1Failure", 0),
          ("psu2Failure", 1),
          ("fanFailure", 2),
          ("urgentExt", 3),
          ("nonUrgentExt", 4))
    )


class PerfControlStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("busy", 0),
          ("offline", 1),
          ("data", 2),
          ("marked", 3))
    )


# MIB Managed Objects in the order of their OIDs

_Schmidtelecom_ObjectIdentity = ObjectIdentity
schmidtelecom = _Schmidtelecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368)
)
_Dsl_ObjectIdentity = ObjectIdentity
dsl = _Dsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1)
)
_DslCardTable_Object = MibTable
dslCardTable = _DslCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dslCardTable.setStatus("current")
_DslCardEntry_Object = MibTableRow
dslCardEntry = _DslCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1)
)
dslCardEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dslCardSlotNumber"),
)
if mibBuilder.loadTexts:
    dslCardEntry.setStatus("current")
_DslCardSlotNumber_Type = DslSlotNumber
_DslCardSlotNumber_Object = MibTableColumn
dslCardSlotNumber = _DslCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 1),
    _DslCardSlotNumber_Type()
)
dslCardSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslCardSlotNumber.setStatus("current")
_DslCardAvailabilityStatus_Type = AvailabilityStatusElem
_DslCardAvailabilityStatus_Object = MibTableColumn
dslCardAvailabilityStatus = _DslCardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 2),
    _DslCardAvailabilityStatus_Type()
)
dslCardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardAvailabilityStatus.setStatus("current")


class _DslCardHardwareVersion_Type(DisplayString):
    """Custom type dslCardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardHardwareVersion_Type.__name__ = "DisplayString"
_DslCardHardwareVersion_Object = MibTableColumn
dslCardHardwareVersion = _DslCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 3),
    _DslCardHardwareVersion_Type()
)
dslCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardHardwareVersion.setStatus("current")


class _DslCardManufacturer_Type(DisplayString):
    """Custom type dslCardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardManufacturer_Type.__name__ = "DisplayString"
_DslCardManufacturer_Object = MibTableColumn
dslCardManufacturer = _DslCardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 4),
    _DslCardManufacturer_Type()
)
dslCardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardManufacturer.setStatus("current")


class _DslCardName_Type(DisplayString):
    """Custom type dslCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardName_Type.__name__ = "DisplayString"
_DslCardName_Object = MibTableColumn
dslCardName = _DslCardName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 5),
    _DslCardName_Type()
)
dslCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardName.setStatus("current")
_DslCardOperState_Type = OperStateEnum
_DslCardOperState_Object = MibTableColumn
dslCardOperState = _DslCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 6),
    _DslCardOperState_Type()
)
dslCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardOperState.setStatus("current")


class _DslCardFirmwareVersion_Type(DisplayString):
    """Custom type dslCardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardFirmwareVersion_Type.__name__ = "DisplayString"
_DslCardFirmwareVersion_Object = MibTableColumn
dslCardFirmwareVersion = _DslCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 7),
    _DslCardFirmwareVersion_Type()
)
dslCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardFirmwareVersion.setStatus("current")


class _DslCardSerialNumber_Type(DisplayString):
    """Custom type dslCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardSerialNumber_Type.__name__ = "DisplayString"
_DslCardSerialNumber_Object = MibTableColumn
dslCardSerialNumber = _DslCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 8),
    _DslCardSerialNumber_Type()
)
dslCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardSerialNumber.setStatus("current")
_DslCardCommState_Type = CommStateEnum
_DslCardCommState_Object = MibTableColumn
dslCardCommState = _DslCardCommState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 9),
    _DslCardCommState_Type()
)
dslCardCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardCommState.setStatus("current")
_DslCardAlarmStatus_Type = DslCardAlarmStatus
_DslCardAlarmStatus_Object = MibTableColumn
dslCardAlarmStatus = _DslCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 10),
    _DslCardAlarmStatus_Type()
)
dslCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardAlarmStatus.setStatus("current")


class _DslCardM16FirmwareVersion_Type(DisplayString):
    """Custom type dslCardM16FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslCardM16FirmwareVersion_Type.__name__ = "DisplayString"
_DslCardM16FirmwareVersion_Object = MibTableColumn
dslCardM16FirmwareVersion = _DslCardM16FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 1, 1, 11),
    _DslCardM16FirmwareVersion_Type()
)
dslCardM16FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslCardM16FirmwareVersion.setStatus("current")
_DslLinkTable_Object = MibTable
dslLinkTable = _DslLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dslLinkTable.setStatus("current")
_DslLinkEntry_Object = MibTableRow
dslLinkEntry = _DslLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1)
)
dslLinkEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dslCardSlotNumber"),
    (0, "PEGASUS-MIB", "dslLinkNumber"),
)
if mibBuilder.loadTexts:
    dslLinkEntry.setStatus("current")
_DslLinkNumber_Type = DslLinkNumber
_DslLinkNumber_Object = MibTableColumn
dslLinkNumber = _DslLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 1),
    _DslLinkNumber_Type()
)
dslLinkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslLinkNumber.setStatus("current")
_DslLinkActiveLoop_Type = DslLinkLoopEnum
_DslLinkActiveLoop_Object = MibTableColumn
dslLinkActiveLoop = _DslLinkActiveLoop_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 2),
    _DslLinkActiveLoop_Type()
)
dslLinkActiveLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkActiveLoop.setStatus("current")


class _DslLinkAddress_Type(DisplayString):
    """Custom type dslLinkAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DslLinkAddress_Type.__name__ = "DisplayString"
_DslLinkAddress_Object = MibTableColumn
dslLinkAddress = _DslLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 3),
    _DslLinkAddress_Type()
)
dslLinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkAddress.setStatus("current")
_DslLinkAdminState_Type = AdminStateEnum
_DslLinkAdminState_Object = MibTableColumn
dslLinkAdminState = _DslLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 4),
    _DslLinkAdminState_Type()
)
dslLinkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkAdminState.setStatus("current")
_DslLinkAlarmStatus_Type = DslLinkAlarmElem
_DslLinkAlarmStatus_Object = MibTableColumn
dslLinkAlarmStatus = _DslLinkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 5),
    _DslLinkAlarmStatus_Type()
)
dslLinkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslLinkAlarmStatus.setStatus("current")
_DslLinkAvailabilityStatus_Type = AvailabilityStatusElem
_DslLinkAvailabilityStatus_Object = MibTableColumn
dslLinkAvailabilityStatus = _DslLinkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 6),
    _DslLinkAvailabilityStatus_Type()
)
dslLinkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslLinkAvailabilityStatus.setStatus("current")


class _DslLinkContact_Type(DisplayString):
    """Custom type dslLinkContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DslLinkContact_Type.__name__ = "DisplayString"
_DslLinkContact_Object = MibTableColumn
dslLinkContact = _DslLinkContact_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 7),
    _DslLinkContact_Type()
)
dslLinkContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkContact.setStatus("current")


class _DslLinkCustomerId_Type(DisplayString):
    """Custom type dslLinkCustomerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslLinkCustomerId_Type.__name__ = "DisplayString"
_DslLinkCustomerId_Object = MibTableColumn
dslLinkCustomerId = _DslLinkCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 8),
    _DslLinkCustomerId_Type()
)
dslLinkCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCustomerId.setStatus("current")
_DslLinkDynamicSlotAllocation_Type = TruthValue
_DslLinkDynamicSlotAllocation_Object = MibTableColumn
dslLinkDynamicSlotAllocation = _DslLinkDynamicSlotAllocation_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 9),
    _DslLinkDynamicSlotAllocation_Type()
)
dslLinkDynamicSlotAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkDynamicSlotAllocation.setStatus("current")
_DslLinkIsRemotePower_Type = TruthValue
_DslLinkIsRemotePower_Object = MibTableColumn
dslLinkIsRemotePower = _DslLinkIsRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 10),
    _DslLinkIsRemotePower_Type()
)
dslLinkIsRemotePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkIsRemotePower.setStatus("current")


class _DslLinkLineRate_Type(Integer32):
    """Custom type dslLinkLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 36),
    )


_DslLinkLineRate_Type.__name__ = "Integer32"
_DslLinkLineRate_Object = MibTableColumn
dslLinkLineRate = _DslLinkLineRate_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 11),
    _DslLinkLineRate_Type()
)
dslLinkLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkLineRate.setStatus("current")


class _DslLinkDataRate_Type(Integer32):
    """Custom type dslLinkDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36),
    )


_DslLinkDataRate_Type.__name__ = "Integer32"
_DslLinkDataRate_Object = MibTableColumn
dslLinkDataRate = _DslLinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 12),
    _DslLinkDataRate_Type()
)
dslLinkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkDataRate.setStatus("current")


class _DslLinkName_Type(DisplayString):
    """Custom type dslLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DslLinkName_Type.__name__ = "DisplayString"
_DslLinkName_Object = MibTableColumn
dslLinkName = _DslLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 13),
    _DslLinkName_Type()
)
dslLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkName.setStatus("current")


class _DslLinkNotes_Type(DisplayString):
    """Custom type dslLinkNotes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DslLinkNotes_Type.__name__ = "DisplayString"
_DslLinkNotes_Object = MibTableColumn
dslLinkNotes = _DslLinkNotes_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 14),
    _DslLinkNotes_Type()
)
dslLinkNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkNotes.setStatus("current")


class _DslLinkNumberOfBRA_Type(Integer32):
    """Custom type dslLinkNumberOfBRA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DslLinkNumberOfBRA_Type.__name__ = "Integer32"
_DslLinkNumberOfBRA_Object = MibTableColumn
dslLinkNumberOfBRA = _DslLinkNumberOfBRA_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 15),
    _DslLinkNumberOfBRA_Type()
)
dslLinkNumberOfBRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkNumberOfBRA.setStatus("current")
_DslLinkOperState_Type = OperStateEnum
_DslLinkOperState_Object = MibTableColumn
dslLinkOperState = _DslLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 16),
    _DslLinkOperState_Type()
)
dslLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslLinkOperState.setStatus("current")


class _DslLinkNumberOfZBits_Type(Integer32):
    """Custom type dslLinkNumberOfZBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DslLinkNumberOfZBits_Type.__name__ = "Integer32"
_DslLinkNumberOfZBits_Object = MibTableColumn
dslLinkNumberOfZBits = _DslLinkNumberOfZBits_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 17),
    _DslLinkNumberOfZBits_Type()
)
dslLinkNumberOfZBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkNumberOfZBits.setStatus("current")
_DslLinkPSDMask_Type = DslLinkPSDMaskEnum
_DslLinkPSDMask_Object = MibTableColumn
dslLinkPSDMask = _DslLinkPSDMask_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 18),
    _DslLinkPSDMask_Type()
)
dslLinkPSDMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkPSDMask.setStatus("current")
_DslLinkAssignedTrunk_Type = TrunkNumberOrZero
_DslLinkAssignedTrunk_Object = MibTableColumn
dslLinkAssignedTrunk = _DslLinkAssignedTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 19),
    _DslLinkAssignedTrunk_Type()
)
dslLinkAssignedTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkAssignedTrunk.setStatus("current")
_DslLinkPriority_Type = Priority
_DslLinkPriority_Object = MibTableColumn
dslLinkPriority = _DslLinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 2, 1, 20),
    _DslLinkPriority_Type()
)
dslLinkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkPriority.setStatus("current")
_IadTable_Object = MibTable
iadTable = _IadTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3)
)
if mibBuilder.loadTexts:
    iadTable.setStatus("current")
_IadEntry_Object = MibTableRow
iadEntry = _IadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    iadEntry.setStatus("current")
_IadAvailabilityStatus_Type = AvailabilityStatusElem
_IadAvailabilityStatus_Object = MibTableColumn
iadAvailabilityStatus = _IadAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 1),
    _IadAvailabilityStatus_Type()
)
iadAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadAvailabilityStatus.setStatus("current")


class _IadHardwareVersion_Type(DisplayString):
    """Custom type iadHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IadHardwareVersion_Type.__name__ = "DisplayString"
_IadHardwareVersion_Object = MibTableColumn
iadHardwareVersion = _IadHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 2),
    _IadHardwareVersion_Type()
)
iadHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadHardwareVersion.setStatus("current")


class _IadManufacturer_Type(DisplayString):
    """Custom type iadManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IadManufacturer_Type.__name__ = "DisplayString"
_IadManufacturer_Object = MibTableColumn
iadManufacturer = _IadManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 3),
    _IadManufacturer_Type()
)
iadManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadManufacturer.setStatus("current")


class _IadName_Type(DisplayString):
    """Custom type iadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IadName_Type.__name__ = "DisplayString"
_IadName_Object = MibTableColumn
iadName = _IadName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 4),
    _IadName_Type()
)
iadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadName.setStatus("current")
_IadOperState_Type = OperStateEnum
_IadOperState_Object = MibTableColumn
iadOperState = _IadOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 5),
    _IadOperState_Type()
)
iadOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadOperState.setStatus("current")


class _IadFirmwareVersion_Type(DisplayString):
    """Custom type iadFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IadFirmwareVersion_Type.__name__ = "DisplayString"
_IadFirmwareVersion_Object = MibTableColumn
iadFirmwareVersion = _IadFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 6),
    _IadFirmwareVersion_Type()
)
iadFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadFirmwareVersion.setStatus("current")


class _IadSerialNumber_Type(DisplayString):
    """Custom type iadSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IadSerialNumber_Type.__name__ = "DisplayString"
_IadSerialNumber_Object = MibTableColumn
iadSerialNumber = _IadSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 7),
    _IadSerialNumber_Type()
)
iadSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadSerialNumber.setStatus("current")
_IadAlarmStatus_Type = IadAlarmStatusElem
_IadAlarmStatus_Object = MibTableColumn
iadAlarmStatus = _IadAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 8),
    _IadAlarmStatus_Type()
)
iadAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadAlarmStatus.setStatus("current")
_IadISDNPowering_Type = IadISDNPoweringEnum
_IadISDNPowering_Object = MibTableColumn
iadISDNPowering = _IadISDNPowering_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 9),
    _IadISDNPowering_Type()
)
iadISDNPowering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iadISDNPowering.setStatus("current")
_IadPOTSPowering_Type = IadPOTSPoweringEnum
_IadPOTSPowering_Object = MibTableColumn
iadPOTSPowering = _IadPOTSPowering_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 10),
    _IadPOTSPowering_Type()
)
iadPOTSPowering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iadPOTSPowering.setStatus("current")
_IadEthPortSpeed_Type = DataPortSpeedEnum
_IadEthPortSpeed_Object = MibTableColumn
iadEthPortSpeed = _IadEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 11),
    _IadEthPortSpeed_Type()
)
iadEthPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iadEthPortSpeed.setStatus("current")
_IadEthCurrentPortSpeed_Type = DataPortSpeedEnum
_IadEthCurrentPortSpeed_Object = MibTableColumn
iadEthCurrentPortSpeed = _IadEthCurrentPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 12),
    _IadEthCurrentPortSpeed_Type()
)
iadEthCurrentPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadEthCurrentPortSpeed.setStatus("current")
_IadEthFlowControl_Type = DataPortFlowControlEnum
_IadEthFlowControl_Object = MibTableColumn
iadEthFlowControl = _IadEthFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 13),
    _IadEthFlowControl_Type()
)
iadEthFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iadEthFlowControl.setStatus("current")
_IadEthCurrentFlowControl_Type = DataPortFlowControlEnum
_IadEthCurrentFlowControl_Object = MibTableColumn
iadEthCurrentFlowControl = _IadEthCurrentFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 3, 1, 14),
    _IadEthCurrentFlowControl_Type()
)
iadEthCurrentFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iadEthCurrentFlowControl.setStatus("current")
_DslInterfaceTable_Object = MibTable
dslInterfaceTable = _DslInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4)
)
if mibBuilder.loadTexts:
    dslInterfaceTable.setStatus("current")
_DslInterfaceEntry_Object = MibTableRow
dslInterfaceEntry = _DslInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1)
)
dslInterfaceEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dslCardSlotNumber"),
    (0, "PEGASUS-MIB", "dslLinkNumber"),
    (0, "PEGASUS-MIB", "dslInterfaceType"),
)
if mibBuilder.loadTexts:
    dslInterfaceEntry.setStatus("current")
_DslInterfaceType_Type = DslInterfaceTypeEnum
_DslInterfaceType_Object = MibTableColumn
dslInterfaceType = _DslInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 1),
    _DslInterfaceType_Type()
)
dslInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslInterfaceType.setStatus("current")
_DslInterfaceAvailabilityStatus_Type = AvailabilityStatusElem
_DslInterfaceAvailabilityStatus_Object = MibTableColumn
dslInterfaceAvailabilityStatus = _DslInterfaceAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 2),
    _DslInterfaceAvailabilityStatus_Type()
)
dslInterfaceAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslInterfaceAvailabilityStatus.setStatus("current")
_DslInterfaceOperState_Type = OperStateEnum
_DslInterfaceOperState_Object = MibTableColumn
dslInterfaceOperState = _DslInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 3),
    _DslInterfaceOperState_Type()
)
dslInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslInterfaceOperState.setStatus("current")
_DslInterfacePerformanceStatus_Type = DslPerformanceStatusElem
_DslInterfacePerformanceStatus_Object = MibTableColumn
dslInterfacePerformanceStatus = _DslInterfacePerformanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 4),
    _DslInterfacePerformanceStatus_Type()
)
dslInterfacePerformanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslInterfacePerformanceStatus.setStatus("current")


class _DslInterfacePerfControlIndexOrZero_Type(Integer32):
    """Custom type dslInterfacePerfControlIndexOrZero based on Integer32"""
    defaultValue = 0


_DslInterfacePerfControlIndexOrZero_Type.__name__ = "Integer32"
_DslInterfacePerfControlIndexOrZero_Object = MibTableColumn
dslInterfacePerfControlIndexOrZero = _DslInterfacePerfControlIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 5),
    _DslInterfacePerfControlIndexOrZero_Type()
)
dslInterfacePerfControlIndexOrZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslInterfacePerfControlIndexOrZero.setStatus("current")


class _DslInterfaceSignalQuality_Type(Integer32):
    """Custom type dslInterfaceSignalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_DslInterfaceSignalQuality_Type.__name__ = "Integer32"
_DslInterfaceSignalQuality_Object = MibTableColumn
dslInterfaceSignalQuality = _DslInterfaceSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 6),
    _DslInterfaceSignalQuality_Type()
)
dslInterfaceSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslInterfaceSignalQuality.setStatus("current")
if mibBuilder.loadTexts:
    dslInterfaceSignalQuality.setUnits("dB")


class _DslInterfaceAttenuation_Type(Integer32):
    """Custom type dslInterfaceAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_DslInterfaceAttenuation_Type.__name__ = "Integer32"
_DslInterfaceAttenuation_Object = MibTableColumn
dslInterfaceAttenuation = _DslInterfaceAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 4, 1, 7),
    _DslInterfaceAttenuation_Type()
)
dslInterfaceAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslInterfaceAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    dslInterfaceAttenuation.setUnits("dB")
_DslLinkCosTable_Object = MibTable
dslLinkCosTable = _DslLinkCosTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5)
)
if mibBuilder.loadTexts:
    dslLinkCosTable.setStatus("current")
_DslLinkCosEntry_Object = MibTableRow
dslLinkCosEntry = _DslLinkCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dslLinkCosEntry.setStatus("current")
_DslLinkCosAvailable_Type = TruthValue
_DslLinkCosAvailable_Object = MibTableColumn
dslLinkCosAvailable = _DslLinkCosAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 1),
    _DslLinkCosAvailable_Type()
)
dslLinkCosAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslLinkCosAvailable.setStatus("current")
_DslLinkCosEnabled_Type = TruthValue
_DslLinkCosEnabled_Object = MibTableColumn
dslLinkCosEnabled = _DslLinkCosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 2),
    _DslLinkCosEnabled_Type()
)
dslLinkCosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosEnabled.setStatus("current")
_DslLinkCosClassifier_Type = CosClassifierEnum
_DslLinkCosClassifier_Object = MibTableColumn
dslLinkCosClassifier = _DslLinkCosClassifier_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 3),
    _DslLinkCosClassifier_Type()
)
dslLinkCosClassifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosClassifier.setStatus("current")
_DslLinkCosClassmapEF_Type = CosClassmap
_DslLinkCosClassmapEF_Object = MibTableColumn
dslLinkCosClassmapEF = _DslLinkCosClassmapEF_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 4),
    _DslLinkCosClassmapEF_Type()
)
dslLinkCosClassmapEF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosClassmapEF.setStatus("current")
_DslLinkCosClassmapAF2_Type = CosClassmap
_DslLinkCosClassmapAF2_Object = MibTableColumn
dslLinkCosClassmapAF2 = _DslLinkCosClassmapAF2_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 5),
    _DslLinkCosClassmapAF2_Type()
)
dslLinkCosClassmapAF2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosClassmapAF2.setStatus("current")
_DslLinkCosClassmapAF1_Type = CosClassmap
_DslLinkCosClassmapAF1_Object = MibTableColumn
dslLinkCosClassmapAF1 = _DslLinkCosClassmapAF1_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 6),
    _DslLinkCosClassmapAF1_Type()
)
dslLinkCosClassmapAF1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosClassmapAF1.setStatus("current")


class _DslLinkCosRateLimitEF_Type(Integer32):
    """Custom type dslLinkCosRateLimitEF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2312),
    )


_DslLinkCosRateLimitEF_Type.__name__ = "Integer32"
_DslLinkCosRateLimitEF_Object = MibTableColumn
dslLinkCosRateLimitEF = _DslLinkCosRateLimitEF_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 7),
    _DslLinkCosRateLimitEF_Type()
)
dslLinkCosRateLimitEF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosRateLimitEF.setStatus("current")


class _DslLinkCosRateLimitAF2_Type(Integer32):
    """Custom type dslLinkCosRateLimitAF2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2312),
    )


_DslLinkCosRateLimitAF2_Type.__name__ = "Integer32"
_DslLinkCosRateLimitAF2_Object = MibTableColumn
dslLinkCosRateLimitAF2 = _DslLinkCosRateLimitAF2_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 8),
    _DslLinkCosRateLimitAF2_Type()
)
dslLinkCosRateLimitAF2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosRateLimitAF2.setStatus("current")


class _DslLinkCosRateLimitAF1_Type(Integer32):
    """Custom type dslLinkCosRateLimitAF1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2312),
    )


_DslLinkCosRateLimitAF1_Type.__name__ = "Integer32"
_DslLinkCosRateLimitAF1_Object = MibTableColumn
dslLinkCosRateLimitAF1 = _DslLinkCosRateLimitAF1_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 1, 5, 1, 9),
    _DslLinkCosRateLimitAF1_Type()
)
dslLinkCosRateLimitAF1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslLinkCosRateLimitAF1.setStatus("current")
_V5_ObjectIdentity = ObjectIdentity
v5 = _V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2)
)
_V5CardTable_Object = MibTable
v5CardTable = _V5CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1)
)
if mibBuilder.loadTexts:
    v5CardTable.setStatus("current")
_V5CardEntry_Object = MibTableRow
v5CardEntry = _V5CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1)
)
v5CardEntry.setIndexNames(
    (0, "PEGASUS-MIB", "v5CardSlotNumber"),
)
if mibBuilder.loadTexts:
    v5CardEntry.setStatus("current")
_V5CardSlotNumber_Type = V5SlotNumber
_V5CardSlotNumber_Object = MibTableColumn
v5CardSlotNumber = _V5CardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 1),
    _V5CardSlotNumber_Type()
)
v5CardSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v5CardSlotNumber.setStatus("current")
_V5CardAdminState_Type = AdminStateEnum
_V5CardAdminState_Object = MibTableColumn
v5CardAdminState = _V5CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 2),
    _V5CardAdminState_Type()
)
v5CardAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardAdminState.setStatus("current")
_V5CardAvailabilityStatus_Type = AvailabilityStatusElem
_V5CardAvailabilityStatus_Object = MibTableColumn
v5CardAvailabilityStatus = _V5CardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 3),
    _V5CardAvailabilityStatus_Type()
)
v5CardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardAvailabilityStatus.setStatus("current")


class _V5CardHardwareVersion_Type(DisplayString):
    """Custom type v5CardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V5CardHardwareVersion_Type.__name__ = "DisplayString"
_V5CardHardwareVersion_Object = MibTableColumn
v5CardHardwareVersion = _V5CardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 4),
    _V5CardHardwareVersion_Type()
)
v5CardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardHardwareVersion.setStatus("current")


class _V5CardManufacturer_Type(DisplayString):
    """Custom type v5CardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V5CardManufacturer_Type.__name__ = "DisplayString"
_V5CardManufacturer_Object = MibTableColumn
v5CardManufacturer = _V5CardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 5),
    _V5CardManufacturer_Type()
)
v5CardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardManufacturer.setStatus("current")


class _V5CardName_Type(DisplayString):
    """Custom type v5CardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V5CardName_Type.__name__ = "DisplayString"
_V5CardName_Object = MibTableColumn
v5CardName = _V5CardName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 6),
    _V5CardName_Type()
)
v5CardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardName.setStatus("current")
_V5CardOperState_Type = OperStateEnum
_V5CardOperState_Object = MibTableColumn
v5CardOperState = _V5CardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 7),
    _V5CardOperState_Type()
)
v5CardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardOperState.setStatus("current")


class _V5CardFirmwareVersion_Type(DisplayString):
    """Custom type v5CardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V5CardFirmwareVersion_Type.__name__ = "DisplayString"
_V5CardFirmwareVersion_Object = MibTableColumn
v5CardFirmwareVersion = _V5CardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 8),
    _V5CardFirmwareVersion_Type()
)
v5CardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardFirmwareVersion.setStatus("current")


class _V5CardSerialNumber_Type(DisplayString):
    """Custom type v5CardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V5CardSerialNumber_Type.__name__ = "DisplayString"
_V5CardSerialNumber_Object = MibTableColumn
v5CardSerialNumber = _V5CardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 9),
    _V5CardSerialNumber_Type()
)
v5CardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardSerialNumber.setStatus("current")
_V5CardCommState_Type = CommStateEnum
_V5CardCommState_Object = MibTableColumn
v5CardCommState = _V5CardCommState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 10),
    _V5CardCommState_Type()
)
v5CardCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardCommState.setStatus("current")
_V5CardIsProvisioning_Type = TruthValue
_V5CardIsProvisioning_Object = MibTableColumn
v5CardIsProvisioning = _V5CardIsProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 11),
    _V5CardIsProvisioning_Type()
)
v5CardIsProvisioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5CardIsProvisioning.setStatus("current")
_V5CardClockMode_Type = V5ClockModeEnum
_V5CardClockMode_Object = MibTableColumn
v5CardClockMode = _V5CardClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 12),
    _V5CardClockMode_Type()
)
v5CardClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardClockMode.setStatus("current")
_V5CardClockSource1_Type = V5ClockSourceEnum
_V5CardClockSource1_Object = MibTableColumn
v5CardClockSource1 = _V5CardClockSource1_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 13),
    _V5CardClockSource1_Type()
)
v5CardClockSource1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardClockSource1.setStatus("current")
_V5CardClockSource2_Type = V5ClockSourceEnum
_V5CardClockSource2_Object = MibTableColumn
v5CardClockSource2 = _V5CardClockSource2_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 14),
    _V5CardClockSource2_Type()
)
v5CardClockSource2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardClockSource2.setStatus("current")
_V5CardProtocolVersion_Type = V5ProtocolVersionEnum
_V5CardProtocolVersion_Object = MibTableColumn
v5CardProtocolVersion = _V5CardProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 15),
    _V5CardProtocolVersion_Type()
)
v5CardProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardProtocolVersion.setStatus("current")
_V5CardRowStatus_Type = RowStatus
_V5CardRowStatus_Object = MibTableColumn
v5CardRowStatus = _V5CardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 16),
    _V5CardRowStatus_Type()
)
v5CardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardRowStatus.setStatus("current")
_V5CardFlags_Type = V5CardFlagSet
_V5CardFlags_Object = MibTableColumn
v5CardFlags = _V5CardFlags_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 17),
    _V5CardFlags_Type()
)
v5CardFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardFlags.setStatus("current")


class _V5CardETSIRelease_Type(Integer32):
    """Custom type v5CardETSIRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_V5CardETSIRelease_Type.__name__ = "Integer32"
_V5CardETSIRelease_Object = MibTableColumn
v5CardETSIRelease = _V5CardETSIRelease_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 18),
    _V5CardETSIRelease_Type()
)
v5CardETSIRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardETSIRelease.setStatus("current")


class _V5CardE1LineCode_Type(Integer32):
    """Custom type v5CardE1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdb3", 1),
          ("ami", 2))
    )


_V5CardE1LineCode_Type.__name__ = "Integer32"
_V5CardE1LineCode_Object = MibTableColumn
v5CardE1LineCode = _V5CardE1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 19),
    _V5CardE1LineCode_Type()
)
v5CardE1LineCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardE1LineCode.setStatus("current")


class _V5CardE1FrameFormat_Type(Integer32):
    """Custom type v5CardE1FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crc4", 1),
          ("crc4e", 2),
          ("dff", 3))
    )


_V5CardE1FrameFormat_Type.__name__ = "Integer32"
_V5CardE1FrameFormat_Object = MibTableColumn
v5CardE1FrameFormat = _V5CardE1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 1, 1, 20),
    _V5CardE1FrameFormat_Type()
)
v5CardE1FrameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5CardE1FrameFormat.setStatus("current")
_V5LinkTable_Object = MibTable
v5LinkTable = _V5LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2)
)
if mibBuilder.loadTexts:
    v5LinkTable.setStatus("current")
_V5LinkEntry_Object = MibTableRow
v5LinkEntry = _V5LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1)
)
v5LinkEntry.setIndexNames(
    (0, "PEGASUS-MIB", "v5CardSlotNumber"),
    (0, "PEGASUS-MIB", "v5LinkNumber"),
)
if mibBuilder.loadTexts:
    v5LinkEntry.setStatus("current")
_V5LinkNumber_Type = V5LinkNumber
_V5LinkNumber_Object = MibTableColumn
v5LinkNumber = _V5LinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 1),
    _V5LinkNumber_Type()
)
v5LinkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v5LinkNumber.setStatus("current")
_V5LinkAdminState_Type = AdminStateEnum
_V5LinkAdminState_Object = MibTableColumn
v5LinkAdminState = _V5LinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 2),
    _V5LinkAdminState_Type()
)
v5LinkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkAdminState.setStatus("current")
_V5LinkAvailabilityStatus_Type = AvailabilityStatusElem
_V5LinkAvailabilityStatus_Object = MibTableColumn
v5LinkAvailabilityStatus = _V5LinkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 3),
    _V5LinkAvailabilityStatus_Type()
)
v5LinkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5LinkAvailabilityStatus.setStatus("current")


class _V5LinkId_Type(Integer32):
    """Custom type v5LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_V5LinkId_Type.__name__ = "Integer32"
_V5LinkId_Object = MibTableColumn
v5LinkId = _V5LinkId_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 4),
    _V5LinkId_Type()
)
v5LinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkId.setStatus("current")
_V5LinkOperState_Type = OperStateEnum
_V5LinkOperState_Object = MibTableColumn
v5LinkOperState = _V5LinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 5),
    _V5LinkOperState_Type()
)
v5LinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5LinkOperState.setStatus("current")
_V5LinkInterface_Type = V5InterfaceNumberOrZero
_V5LinkInterface_Object = MibTableColumn
v5LinkInterface = _V5LinkInterface_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 6),
    _V5LinkInterface_Type()
)
v5LinkInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkInterface.setStatus("current")
_V5LinkAlarmStatus_Type = V5LinkAlarmStatusElem
_V5LinkAlarmStatus_Object = MibTableColumn
v5LinkAlarmStatus = _V5LinkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 7),
    _V5LinkAlarmStatus_Type()
)
v5LinkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5LinkAlarmStatus.setStatus("current")
_V5LinkType_Type = V5LinkTypeEnum
_V5LinkType_Object = MibTableColumn
v5LinkType = _V5LinkType_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 8),
    _V5LinkType_Type()
)
v5LinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkType.setStatus("current")
_V5LinkNumberOfPcc_Type = V5PccCount
_V5LinkNumberOfPcc_Object = MibTableColumn
v5LinkNumberOfPcc = _V5LinkNumberOfPcc_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 9),
    _V5LinkNumberOfPcc_Type()
)
v5LinkNumberOfPcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkNumberOfPcc.setStatus("current")
_V5LinkPerfControlIndexOrZero_Type = Integer32
_V5LinkPerfControlIndexOrZero_Object = MibTableColumn
v5LinkPerfControlIndexOrZero = _V5LinkPerfControlIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 10),
    _V5LinkPerfControlIndexOrZero_Type()
)
v5LinkPerfControlIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkPerfControlIndexOrZero.setStatus("current")
_V5LinkRowStatus_Type = RowStatus
_V5LinkRowStatus_Object = MibTableColumn
v5LinkRowStatus = _V5LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 11),
    _V5LinkRowStatus_Type()
)
v5LinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LinkRowStatus.setStatus("current")


class _V5LinkLineIdentifier_Type(DisplayString):
    """Custom type v5LinkLineIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_V5LinkLineIdentifier_Type.__name__ = "DisplayString"
_V5LinkLineIdentifier_Object = MibTableColumn
v5LinkLineIdentifier = _V5LinkLineIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 2, 1, 12),
    _V5LinkLineIdentifier_Type()
)
v5LinkLineIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5LinkLineIdentifier.setStatus("current")
_V5InterfaceTable_Object = MibTable
v5InterfaceTable = _V5InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3)
)
if mibBuilder.loadTexts:
    v5InterfaceTable.setStatus("current")
_V5InterfaceEntry_Object = MibTableRow
v5InterfaceEntry = _V5InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1)
)
v5InterfaceEntry.setIndexNames(
    (0, "PEGASUS-MIB", "v5CardSlotNumber"),
    (0, "PEGASUS-MIB", "v5InterfaceNumber"),
)
if mibBuilder.loadTexts:
    v5InterfaceEntry.setStatus("current")
_V5InterfaceNumber_Type = V5InterfaceNumber
_V5InterfaceNumber_Object = MibTableColumn
v5InterfaceNumber = _V5InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 1),
    _V5InterfaceNumber_Type()
)
v5InterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v5InterfaceNumber.setStatus("current")
_V5InterfaceAdminState_Type = AdminStateEnum
_V5InterfaceAdminState_Object = MibTableColumn
v5InterfaceAdminState = _V5InterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 2),
    _V5InterfaceAdminState_Type()
)
v5InterfaceAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5InterfaceAdminState.setStatus("current")
_V5InterfaceAvailabilityStatus_Type = AvailabilityStatusElem
_V5InterfaceAvailabilityStatus_Object = MibTableColumn
v5InterfaceAvailabilityStatus = _V5InterfaceAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 3),
    _V5InterfaceAvailabilityStatus_Type()
)
v5InterfaceAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5InterfaceAvailabilityStatus.setStatus("current")


class _V5InterfaceId_Type(Integer32):
    """Custom type v5InterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_V5InterfaceId_Type.__name__ = "Integer32"
_V5InterfaceId_Object = MibTableColumn
v5InterfaceId = _V5InterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 4),
    _V5InterfaceId_Type()
)
v5InterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5InterfaceId.setStatus("current")
_V5InterfaceOperState_Type = OperStateEnum
_V5InterfaceOperState_Object = MibTableColumn
v5InterfaceOperState = _V5InterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 5),
    _V5InterfaceOperState_Type()
)
v5InterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5InterfaceOperState.setStatus("current")


class _V5InterfaceVariantId_Type(Integer32):
    """Custom type v5InterfaceVariantId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_V5InterfaceVariantId_Type.__name__ = "Integer32"
_V5InterfaceVariantId_Object = MibTableColumn
v5InterfaceVariantId = _V5InterfaceVariantId_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 6),
    _V5InterfaceVariantId_Type()
)
v5InterfaceVariantId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5InterfaceVariantId.setStatus("current")
_V5InterfaceRowStatus_Type = RowStatus
_V5InterfaceRowStatus_Object = MibTableColumn
v5InterfaceRowStatus = _V5InterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 7),
    _V5InterfaceRowStatus_Type()
)
v5InterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5InterfaceRowStatus.setStatus("current")
_V5InterfaceAlarmStatus_Type = V5InterfaceAlarmSet
_V5InterfaceAlarmStatus_Object = MibTableColumn
v5InterfaceAlarmStatus = _V5InterfaceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 3, 1, 8),
    _V5InterfaceAlarmStatus_Type()
)
v5InterfaceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5InterfaceAlarmStatus.setStatus("current")
_V5LccTable_Object = MibTable
v5LccTable = _V5LccTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4)
)
if mibBuilder.loadTexts:
    v5LccTable.setStatus("current")
_V5LccEntry_Object = MibTableRow
v5LccEntry = _V5LccEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1)
)
v5LccEntry.setIndexNames(
    (0, "PEGASUS-MIB", "v5CardSlotNumber"),
    (0, "PEGASUS-MIB", "v5InterfaceNumber"),
    (0, "PEGASUS-MIB", "v5LccNumber"),
)
if mibBuilder.loadTexts:
    v5LccEntry.setStatus("current")
_V5LccNumber_Type = V5LccNumber
_V5LccNumber_Object = MibTableColumn
v5LccNumber = _V5LccNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 1),
    _V5LccNumber_Type()
)
v5LccNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v5LccNumber.setStatus("current")
_V5LccIsProtected_Type = TruthValue
_V5LccIsProtected_Object = MibTableColumn
v5LccIsProtected = _V5LccIsProtected_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 2),
    _V5LccIsProtected_Type()
)
v5LccIsProtected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LccIsProtected.setStatus("current")
_V5LccId_Type = Integer32
_V5LccId_Object = MibTableColumn
v5LccId = _V5LccId_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 3),
    _V5LccId_Type()
)
v5LccId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LccId.setStatus("current")
_V5LccOperState_Type = OperStateEnum
_V5LccOperState_Object = MibTableColumn
v5LccOperState = _V5LccOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 4),
    _V5LccOperState_Type()
)
v5LccOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5LccOperState.setStatus("current")
_V5LccPccV5LinkNumber_Type = V5LinkNumberOrZero
_V5LccPccV5LinkNumber_Object = MibTableColumn
v5LccPccV5LinkNumber = _V5LccPccV5LinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 5),
    _V5LccPccV5LinkNumber_Type()
)
v5LccPccV5LinkNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LccPccV5LinkNumber.setStatus("current")
_V5LccPccTimeslot_Type = V5PccNumberOrZero
_V5LccPccTimeslot_Object = MibTableColumn
v5LccPccTimeslot = _V5LccPccTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 6),
    _V5LccPccTimeslot_Type()
)
v5LccPccTimeslot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LccPccTimeslot.setStatus("current")
_V5LccRowStatus_Type = RowStatus
_V5LccRowStatus_Object = MibTableColumn
v5LccRowStatus = _V5LccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 4, 1, 7),
    _V5LccRowStatus_Type()
)
v5LccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    v5LccRowStatus.setStatus("current")
_V5IsdnPortTable_Object = MibTable
v5IsdnPortTable = _V5IsdnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5)
)
if mibBuilder.loadTexts:
    v5IsdnPortTable.setStatus("current")
_V5IsdnPortEntry_Object = MibTableRow
v5IsdnPortEntry = _V5IsdnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1)
)
v5IsdnPortEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dslCardSlotNumber"),
    (0, "PEGASUS-MIB", "dslLinkNumber"),
    (0, "PEGASUS-MIB", "v5IsdnPortBRANumber"),
)
if mibBuilder.loadTexts:
    v5IsdnPortEntry.setStatus("current")


class _V5IsdnPortBRANumber_Type(Integer32):
    """Custom type v5IsdnPortBRANumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_V5IsdnPortBRANumber_Type.__name__ = "Integer32"
_V5IsdnPortBRANumber_Object = MibTableColumn
v5IsdnPortBRANumber = _V5IsdnPortBRANumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 3),
    _V5IsdnPortBRANumber_Type()
)
v5IsdnPortBRANumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v5IsdnPortBRANumber.setStatus("current")
_V5IsdnPortAdminState_Type = AdminStateEnum
_V5IsdnPortAdminState_Object = MibTableColumn
v5IsdnPortAdminState = _V5IsdnPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 4),
    _V5IsdnPortAdminState_Type()
)
v5IsdnPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortAdminState.setStatus("current")
_V5IsdnPortOperState_Type = OperStateEnum
_V5IsdnPortOperState_Object = MibTableColumn
v5IsdnPortOperState = _V5IsdnPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 5),
    _V5IsdnPortOperState_Type()
)
v5IsdnPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5IsdnPortOperState.setStatus("current")
_V5IsdnPortBlockingStatus_Type = V5IsdnPortBlockingStatusEnum
_V5IsdnPortBlockingStatus_Object = MibTableColumn
v5IsdnPortBlockingStatus = _V5IsdnPortBlockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 6),
    _V5IsdnPortBlockingStatus_Type()
)
v5IsdnPortBlockingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5IsdnPortBlockingStatus.setStatus("current")
_V5IsdnPortBearer1Timeslot_Type = V5TimeslotNumber
_V5IsdnPortBearer1Timeslot_Object = MibTableColumn
v5IsdnPortBearer1Timeslot = _V5IsdnPortBearer1Timeslot_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 7),
    _V5IsdnPortBearer1Timeslot_Type()
)
v5IsdnPortBearer1Timeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortBearer1Timeslot.setStatus("current")
_V5IsdnPortBearer2Timeslot_Type = V5TimeslotNumber
_V5IsdnPortBearer2Timeslot_Object = MibTableColumn
v5IsdnPortBearer2Timeslot = _V5IsdnPortBearer2Timeslot_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 8),
    _V5IsdnPortBearer2Timeslot_Type()
)
v5IsdnPortBearer2Timeslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortBearer2Timeslot.setStatus("current")
_V5IsdnPortEnvelopeFuncAddress_Type = V5EnvelopeFuncAddress
_V5IsdnPortEnvelopeFuncAddress_Object = MibTableColumn
v5IsdnPortEnvelopeFuncAddress = _V5IsdnPortEnvelopeFuncAddress_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 9),
    _V5IsdnPortEnvelopeFuncAddress_Type()
)
v5IsdnPortEnvelopeFuncAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortEnvelopeFuncAddress.setStatus("current")
_V5IsdnPortIsActivated_Type = TruthValue
_V5IsdnPortIsActivated_Object = MibTableColumn
v5IsdnPortIsActivated = _V5IsdnPortIsActivated_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 10),
    _V5IsdnPortIsActivated_Type()
)
v5IsdnPortIsActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5IsdnPortIsActivated.setStatus("current")
_V5IsdnPortAlarmStatus_Type = V5IsdnPortAlarmStatusElem
_V5IsdnPortAlarmStatus_Object = MibTableColumn
v5IsdnPortAlarmStatus = _V5IsdnPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 11),
    _V5IsdnPortAlarmStatus_Type()
)
v5IsdnPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5IsdnPortAlarmStatus.setStatus("current")
_V5IsdnPortActiveLoop_Type = V5IsdnPortLoopEnum
_V5IsdnPortActiveLoop_Object = MibTableColumn
v5IsdnPortActiveLoop = _V5IsdnPortActiveLoop_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 12),
    _V5IsdnPortActiveLoop_Type()
)
v5IsdnPortActiveLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortActiveLoop.setStatus("obsolete")
_V5IsdnPortV5CardSlotNumber_Type = V5SlotNumber
_V5IsdnPortV5CardSlotNumber_Object = MibTableColumn
v5IsdnPortV5CardSlotNumber = _V5IsdnPortV5CardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 13),
    _V5IsdnPortV5CardSlotNumber_Type()
)
v5IsdnPortV5CardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v5IsdnPortV5CardSlotNumber.setStatus("current")
_V5IsdnPortV5InterfaceNumber_Type = V5InterfaceNumberOrZero
_V5IsdnPortV5InterfaceNumber_Object = MibTableColumn
v5IsdnPortV5InterfaceNumber = _V5IsdnPortV5InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 14),
    _V5IsdnPortV5InterfaceNumber_Type()
)
v5IsdnPortV5InterfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortV5InterfaceNumber.setStatus("current")
_V5IsdnPortDSignallingCommChan_Type = V5LccNumberOrZero
_V5IsdnPortDSignallingCommChan_Object = MibTableColumn
v5IsdnPortDSignallingCommChan = _V5IsdnPortDSignallingCommChan_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 15),
    _V5IsdnPortDSignallingCommChan_Type()
)
v5IsdnPortDSignallingCommChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortDSignallingCommChan.setStatus("current")
_V5IsdnPortFrameCommChan_Type = V5LccNumberOrZero
_V5IsdnPortFrameCommChan_Object = MibTableColumn
v5IsdnPortFrameCommChan = _V5IsdnPortFrameCommChan_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 16),
    _V5IsdnPortFrameCommChan_Type()
)
v5IsdnPortFrameCommChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortFrameCommChan.setStatus("current")
_V5IsdnPortPacketCommChan_Type = V5LccNumberOrZero
_V5IsdnPortPacketCommChan_Object = MibTableColumn
v5IsdnPortPacketCommChan = _V5IsdnPortPacketCommChan_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 17),
    _V5IsdnPortPacketCommChan_Type()
)
v5IsdnPortPacketCommChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortPacketCommChan.setStatus("current")


class _V5IsdnPortLineIdentifier_Type(DisplayString):
    """Custom type v5IsdnPortLineIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_V5IsdnPortLineIdentifier_Type.__name__ = "DisplayString"
_V5IsdnPortLineIdentifier_Object = MibTableColumn
v5IsdnPortLineIdentifier = _V5IsdnPortLineIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 2, 5, 1, 18),
    _V5IsdnPortLineIdentifier_Type()
)
v5IsdnPortLineIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v5IsdnPortLineIdentifier.setStatus("current")
_Data_ObjectIdentity = ObjectIdentity
data = _Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3)
)
_DataCardTable_Object = MibTable
dataCardTable = _DataCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dataCardTable.setStatus("current")
_DataCardEntry_Object = MibTableRow
dataCardEntry = _DataCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1)
)
dataCardEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dataCardSlotNumber"),
)
if mibBuilder.loadTexts:
    dataCardEntry.setStatus("current")
_DataCardSlotNumber_Type = DataCardSlotNumber
_DataCardSlotNumber_Object = MibTableColumn
dataCardSlotNumber = _DataCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 1),
    _DataCardSlotNumber_Type()
)
dataCardSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataCardSlotNumber.setStatus("current")
_DataCardAvailabilityStatus_Type = AvailabilityStatusElem
_DataCardAvailabilityStatus_Object = MibTableColumn
dataCardAvailabilityStatus = _DataCardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 2),
    _DataCardAvailabilityStatus_Type()
)
dataCardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardAvailabilityStatus.setStatus("current")


class _DataCardHardwareVersion_Type(DisplayString):
    """Custom type dataCardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataCardHardwareVersion_Type.__name__ = "DisplayString"
_DataCardHardwareVersion_Object = MibTableColumn
dataCardHardwareVersion = _DataCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 3),
    _DataCardHardwareVersion_Type()
)
dataCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardHardwareVersion.setStatus("current")


class _DataCardManufacturer_Type(DisplayString):
    """Custom type dataCardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataCardManufacturer_Type.__name__ = "DisplayString"
_DataCardManufacturer_Object = MibTableColumn
dataCardManufacturer = _DataCardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 4),
    _DataCardManufacturer_Type()
)
dataCardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardManufacturer.setStatus("current")


class _DataCardName_Type(DisplayString):
    """Custom type dataCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataCardName_Type.__name__ = "DisplayString"
_DataCardName_Object = MibTableColumn
dataCardName = _DataCardName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 5),
    _DataCardName_Type()
)
dataCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardName.setStatus("current")
_DataCardOperState_Type = OperStateEnum
_DataCardOperState_Object = MibTableColumn
dataCardOperState = _DataCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 6),
    _DataCardOperState_Type()
)
dataCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardOperState.setStatus("current")


class _DataCardFirmwareVersion_Type(DisplayString):
    """Custom type dataCardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataCardFirmwareVersion_Type.__name__ = "DisplayString"
_DataCardFirmwareVersion_Object = MibTableColumn
dataCardFirmwareVersion = _DataCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 7),
    _DataCardFirmwareVersion_Type()
)
dataCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardFirmwareVersion.setStatus("current")


class _DataCardSerialNumber_Type(DisplayString):
    """Custom type dataCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DataCardSerialNumber_Type.__name__ = "DisplayString"
_DataCardSerialNumber_Object = MibTableColumn
dataCardSerialNumber = _DataCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 8),
    _DataCardSerialNumber_Type()
)
dataCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardSerialNumber.setStatus("current")
_DataCardCommState_Type = CommStateEnum
_DataCardCommState_Object = MibTableColumn
dataCardCommState = _DataCardCommState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 9),
    _DataCardCommState_Type()
)
dataCardCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCardCommState.setStatus("current")
_DataCardVLANMode_Type = TruthValue
_DataCardVLANMode_Object = MibTableColumn
dataCardVLANMode = _DataCardVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 1, 1, 10),
    _DataCardVLANMode_Type()
)
dataCardVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataCardVLANMode.setStatus("current")
_DataPortTable_Object = MibTable
dataPortTable = _DataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dataPortTable.setStatus("current")
_DataPortEntry_Object = MibTableRow
dataPortEntry = _DataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1)
)
dataPortEntry.setIndexNames(
    (0, "PEGASUS-MIB", "dataCardSlotNumber"),
    (0, "PEGASUS-MIB", "dataPortNumber"),
)
if mibBuilder.loadTexts:
    dataPortEntry.setStatus("current")
_DataPortNumber_Type = TrunkNumber
_DataPortNumber_Object = MibTableColumn
dataPortNumber = _DataPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 1),
    _DataPortNumber_Type()
)
dataPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataPortNumber.setStatus("current")
_DataPortAdminState_Type = AdminStateEnum
_DataPortAdminState_Object = MibTableColumn
dataPortAdminState = _DataPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 2),
    _DataPortAdminState_Type()
)
dataPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAdminState.setStatus("current")
_DataPortOperState_Type = OperStateEnum
_DataPortOperState_Object = MibTableColumn
dataPortOperState = _DataPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 3),
    _DataPortOperState_Type()
)
dataPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortOperState.setStatus("current")
_DataPortAvailabilityStatus_Type = AvailabilityStatusElem
_DataPortAvailabilityStatus_Object = MibTableColumn
dataPortAvailabilityStatus = _DataPortAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 4),
    _DataPortAvailabilityStatus_Type()
)
dataPortAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortAvailabilityStatus.setStatus("current")
_DataPortSpeed_Type = DataPortSpeedEnum
_DataPortSpeed_Object = MibTableColumn
dataPortSpeed = _DataPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 5),
    _DataPortSpeed_Type()
)
dataPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortSpeed.setStatus("current")
_DataPortFlowControl_Type = DataPortFlowControlEnum
_DataPortFlowControl_Object = MibTableColumn
dataPortFlowControl = _DataPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 3, 2, 1, 6),
    _DataPortFlowControl_Type()
)
dataPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortFlowControl.setStatus("current")
_PegasusSystem_ObjectIdentity = ObjectIdentity
pegasusSystem = _PegasusSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4)
)
_AutoPersistDelay_Type = Integer32
_AutoPersistDelay_Object = MibScalar
autoPersistDelay = _AutoPersistDelay_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 1),
    _AutoPersistDelay_Type()
)
autoPersistDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoPersistDelay.setStatus("current")
_AutoPersistEnabled_Type = TruthValue
_AutoPersistEnabled_Object = MibScalar
autoPersistEnabled = _AutoPersistEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 2),
    _AutoPersistEnabled_Type()
)
autoPersistEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoPersistEnabled.setStatus("current")
_ConfigPriority_Type = ConfigPriorityEnum
_ConfigPriority_Object = MibScalar
configPriority = _ConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 3),
    _ConfigPriority_Type()
)
configPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPriority.setStatus("current")
_HwAdaptionPolicy_Type = HWAdaptionPolicyEnum
_HwAdaptionPolicy_Object = MibScalar
hwAdaptionPolicy = _HwAdaptionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 4),
    _HwAdaptionPolicy_Type()
)
hwAdaptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAdaptionPolicy.setStatus("obsolete")
_IpBaseAddress_Type = IpAddress
_IpBaseAddress_Object = MibScalar
ipBaseAddress = _IpBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 5),
    _IpBaseAddress_Type()
)
ipBaseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBaseAddress.setStatus("current")
_JavaRuntimeVersion_Type = DisplayString
_JavaRuntimeVersion_Object = MibScalar
javaRuntimeVersion = _JavaRuntimeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 6),
    _JavaRuntimeVersion_Type()
)
javaRuntimeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    javaRuntimeVersion.setStatus("current")
_JavaVMName_Type = DisplayString
_JavaVMName_Object = MibScalar
javaVMName = _JavaVMName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 7),
    _JavaVMName_Type()
)
javaVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    javaVMName.setStatus("current")
_JavaVMVersion_Type = DisplayString
_JavaVMVersion_Object = MibScalar
javaVMVersion = _JavaVMVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 8),
    _JavaVMVersion_Type()
)
javaVMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    javaVMVersion.setStatus("current")
_MgmtIPAddress_Type = IpAddress
_MgmtIPAddress_Object = MibScalar
mgmtIPAddress = _MgmtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 9),
    _MgmtIPAddress_Type()
)
mgmtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtIPAddress.setStatus("current")
_OsArchitecture_Type = DisplayString
_OsArchitecture_Object = MibScalar
osArchitecture = _OsArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 11),
    _OsArchitecture_Type()
)
osArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osArchitecture.setStatus("current")
_OsNameAndVersion_Type = DisplayString
_OsNameAndVersion_Object = MibScalar
osNameAndVersion = _OsNameAndVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 12),
    _OsNameAndVersion_Type()
)
osNameAndVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osNameAndVersion.setStatus("current")
_PemVersion_Type = DisplayString
_PemVersion_Object = MibScalar
pemVersion = _PemVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 13),
    _PemVersion_Type()
)
pemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemVersion.setStatus("current")
_StartedBy_Type = DisplayString
_StartedBy_Object = MibScalar
startedBy = _StartedBy_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 14),
    _StartedBy_Type()
)
startedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startedBy.setStatus("current")
_SystemNumber_Type = Integer32
_SystemNumber_Object = MibScalar
systemNumber = _SystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 15),
    _SystemNumber_Type()
)
systemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNumber.setStatus("current")


class _MibRevision_Type(DisplayString):
    """Custom type mibRevision based on DisplayString"""
    defaultValue = OctetString("$Workfile: PEGASUS.mib $ $Revision: 48 $ $Date: 12/17/04 1:16p $")


_MibRevision_Type.__name__ = "DisplayString"
_MibRevision_Object = MibScalar
mibRevision = _MibRevision_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 16),
    _MibRevision_Type()
)
mibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibRevision.setStatus("current")


class _ReadCommunity_Type(DisplayString):
    """Custom type readCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ReadCommunity_Type.__name__ = "DisplayString"
_ReadCommunity_Object = MibScalar
readCommunity = _ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 17),
    _ReadCommunity_Type()
)
readCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readCommunity.setStatus("current")


class _WriteCommunity_Type(DisplayString):
    """Custom type writeCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WriteCommunity_Type.__name__ = "DisplayString"
_WriteCommunity_Object = MibScalar
writeCommunity = _WriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 18),
    _WriteCommunity_Type()
)
writeCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeCommunity.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 19),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")


class _TrapDestination_Type(DisplayString):
    """Custom type trapDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TrapDestination_Type.__name__ = "DisplayString"
_TrapDestination_Object = MibScalar
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 20),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestination.setStatus("current")


class _AgentPort_Type(Integer32):
    """Custom type agentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentPort_Type.__name__ = "Integer32"
_AgentPort_Object = MibScalar
agentPort = _AgentPort_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 21),
    _AgentPort_Type()
)
agentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPort.setStatus("current")
_AuthRespEnabled_Type = TruthValue
_AuthRespEnabled_Object = MibScalar
authRespEnabled = _AuthRespEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 22),
    _AuthRespEnabled_Type()
)
authRespEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authRespEnabled.setStatus("obsolete")
_RackAlarmStatus_Type = RackAlarmStatusElem
_RackAlarmStatus_Object = MibScalar
rackAlarmStatus = _RackAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 4, 23),
    _RackAlarmStatus_Type()
)
rackAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackAlarmStatus.setStatus("current")
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7)
)


class _PerfSweepCyclePeriod_Type(Integer32):
    """Custom type perfSweepCyclePeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_PerfSweepCyclePeriod_Type.__name__ = "Integer32"
_PerfSweepCyclePeriod_Object = MibScalar
perfSweepCyclePeriod = _PerfSweepCyclePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 1),
    _PerfSweepCyclePeriod_Type()
)
perfSweepCyclePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfSweepCyclePeriod.setStatus("current")
if mibBuilder.loadTexts:
    perfSweepCyclePeriod.setUnits("Seconds")
_PerfControlTable_Object = MibTable
perfControlTable = _PerfControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2)
)
if mibBuilder.loadTexts:
    perfControlTable.setStatus("current")
_PerfControlEntry_Object = MibTableRow
perfControlEntry = _PerfControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1)
)
perfControlEntry.setIndexNames(
    (0, "PEGASUS-MIB", "perfControlIndex"),
)
if mibBuilder.loadTexts:
    perfControlEntry.setStatus("current")


class _PerfControlIndex_Type(Integer32):
    """Custom type perfControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerfControlIndex_Type.__name__ = "Integer32"
_PerfControlIndex_Object = MibTableColumn
perfControlIndex = _PerfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 1),
    _PerfControlIndex_Type()
)
perfControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfControlIndex.setStatus("current")
_PerfControlStatus_Type = PerfControlStatus
_PerfControlStatus_Object = MibTableColumn
perfControlStatus = _PerfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 2),
    _PerfControlStatus_Type()
)
perfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfControlStatus.setStatus("current")
_PerfControlLinkDescr_Type = DisplayString
_PerfControlLinkDescr_Object = MibTableColumn
perfControlLinkDescr = _PerfControlLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 3),
    _PerfControlLinkDescr_Type()
)
perfControlLinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfControlLinkDescr.setStatus("current")


class _PerfControlUpdatePeriod_Type(Integer32):
    """Custom type perfControlUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_PerfControlUpdatePeriod_Type.__name__ = "Integer32"
_PerfControlUpdatePeriod_Object = MibTableColumn
perfControlUpdatePeriod = _PerfControlUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 4),
    _PerfControlUpdatePeriod_Type()
)
perfControlUpdatePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfControlUpdatePeriod.setStatus("current")


class _PerfControlEffectiveUpdatePeriod_Type(Integer32):
    """Custom type perfControlEffectiveUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_PerfControlEffectiveUpdatePeriod_Type.__name__ = "Integer32"
_PerfControlEffectiveUpdatePeriod_Object = MibTableColumn
perfControlEffectiveUpdatePeriod = _PerfControlEffectiveUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 5),
    _PerfControlEffectiveUpdatePeriod_Type()
)
perfControlEffectiveUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfControlEffectiveUpdatePeriod.setStatus("obsolete")
_PerfControlRowStatus_Type = RowStatus
_PerfControlRowStatus_Object = MibTableColumn
perfControlRowStatus = _PerfControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 2, 1, 6),
    _PerfControlRowStatus_Type()
)
perfControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfControlRowStatus.setStatus("current")
_PerfDataTable_Object = MibTable
perfDataTable = _PerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3)
)
if mibBuilder.loadTexts:
    perfDataTable.setStatus("current")
_PerfDataEntry_Object = MibTableRow
perfDataEntry = _PerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1)
)
perfDataEntry.setIndexNames(
    (0, "PEGASUS-MIB", "perfControlIndex"),
    (0, "PEGASUS-MIB", "perfDataKind"),
    (0, "PEGASUS-MIB", "perfDataIndex"),
)
if mibBuilder.loadTexts:
    perfDataEntry.setStatus("current")
_PerfDataKind_Type = PerfHistoryType
_PerfDataKind_Object = MibTableColumn
perfDataKind = _PerfDataKind_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 1),
    _PerfDataKind_Type()
)
perfDataKind.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfDataKind.setStatus("current")


class _PerfDataIndex_Type(Integer32):
    """Custom type perfDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerfDataIndex_Type.__name__ = "Integer32"
_PerfDataIndex_Object = MibTableColumn
perfDataIndex = _PerfDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 2),
    _PerfDataIndex_Type()
)
perfDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfDataIndex.setStatus("current")
_PerfDataES_Type = Integer32
_PerfDataES_Object = MibTableColumn
perfDataES = _PerfDataES_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 3),
    _PerfDataES_Type()
)
perfDataES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfDataES.setStatus("current")
if mibBuilder.loadTexts:
    perfDataES.setUnits("Seconds")
_PerfDataSES_Type = Integer32
_PerfDataSES_Object = MibTableColumn
perfDataSES = _PerfDataSES_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 4),
    _PerfDataSES_Type()
)
perfDataSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfDataSES.setStatus("current")
if mibBuilder.loadTexts:
    perfDataSES.setUnits("Seconds")
_PerfDataUAS_Type = Integer32
_PerfDataUAS_Object = MibTableColumn
perfDataUAS = _PerfDataUAS_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 5),
    _PerfDataUAS_Type()
)
perfDataUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfDataUAS.setStatus("current")
if mibBuilder.loadTexts:
    perfDataUAS.setUnits("Seconds")
_PerfDataCV_Type = Integer32
_PerfDataCV_Object = MibTableColumn
perfDataCV = _PerfDataCV_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 6),
    _PerfDataCV_Type()
)
perfDataCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfDataCV.setStatus("current")
if mibBuilder.loadTexts:
    perfDataCV.setUnits("Frames with CRC faults")
_PerfDataLOSWS_Type = Integer32
_PerfDataLOSWS_Object = MibTableColumn
perfDataLOSWS = _PerfDataLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 7, 3, 1, 7),
    _PerfDataLOSWS_Type()
)
perfDataLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfDataLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    perfDataLOSWS.setUnits("Seconds")
dslLinkEntry.registerAugmentions(
    ("PEGASUS-MIB",
     "iadEntry")
)
iadEntry.setIndexNames(*dslLinkEntry.getIndexNames())
dslLinkEntry.registerAugmentions(
    ("PEGASUS-MIB",
     "dslLinkCosEntry")
)
dslLinkCosEntry.setIndexNames(*dslLinkEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEGASUS-MIB",
    **{"AdminStateEnum": AdminStateEnum,
       "OperStateEnum": OperStateEnum,
       "AvailabilityStatusElem": AvailabilityStatusElem,
       "CommStateEnum": CommStateEnum,
       "DataPortSpeedEnum": DataPortSpeedEnum,
       "DataPortFlowControlEnum": DataPortFlowControlEnum,
       "SlotNumber": SlotNumber,
       "DataCardSlotNumber": DataCardSlotNumber,
       "V5SlotNumber": V5SlotNumber,
       "DslSlotNumber": DslSlotNumber,
       "DslLinkNumber": DslLinkNumber,
       "TrunkNumber": TrunkNumber,
       "TrunkNumberOrZero": TrunkNumberOrZero,
       "Priority": Priority,
       "DslLinkLoopEnum": DslLinkLoopEnum,
       "DslLinkAlarmElem": DslLinkAlarmElem,
       "DslLinkPSDMaskEnum": DslLinkPSDMaskEnum,
       "DslCardAlarmStatus": DslCardAlarmStatus,
       "IadAlarmStatusElem": IadAlarmStatusElem,
       "IadISDNPoweringEnum": IadISDNPoweringEnum,
       "IadPOTSPoweringEnum": IadPOTSPoweringEnum,
       "DslInterfaceTypeEnum": DslInterfaceTypeEnum,
       "DslPerformanceStatusElem": DslPerformanceStatusElem,
       "CosClassifierEnum": CosClassifierEnum,
       "CosClassmap": CosClassmap,
       "V5ClockModeEnum": V5ClockModeEnum,
       "V5ClockSourceEnum": V5ClockSourceEnum,
       "V5ProtocolVersionEnum": V5ProtocolVersionEnum,
       "V5CardFlagSet": V5CardFlagSet,
       "V5LinkNumber": V5LinkNumber,
       "V5LinkNumberOrZero": V5LinkNumberOrZero,
       "V5InterfaceNumber": V5InterfaceNumber,
       "V5InterfaceNumberOrZero": V5InterfaceNumberOrZero,
       "V5PccCount": V5PccCount,
       "V5LinkAlarmStatusElem": V5LinkAlarmStatusElem,
       "V5LinkTypeEnum": V5LinkTypeEnum,
       "V5InterfaceAlarmSet": V5InterfaceAlarmSet,
       "V5LccNumber": V5LccNumber,
       "V5LccNumberOrZero": V5LccNumberOrZero,
       "V5PccNumberOrZero": V5PccNumberOrZero,
       "V5IsdnPortLoopEnum": V5IsdnPortLoopEnum,
       "V5IsdnPortBlockingStatusEnum": V5IsdnPortBlockingStatusEnum,
       "V5IsdnPortAlarmStatusElem": V5IsdnPortAlarmStatusElem,
       "V5TimeslotNumber": V5TimeslotNumber,
       "V5EnvelopeFuncAddress": V5EnvelopeFuncAddress,
       "ConfigPriorityEnum": ConfigPriorityEnum,
       "HWAdaptionPolicyEnum": HWAdaptionPolicyEnum,
       "RackAlarmStatusElem": RackAlarmStatusElem,
       "PerfControlStatus": PerfControlStatus,
       "PerfHistoryType": PerfHistoryType,
       "schmidtelecom": schmidtelecom,
       "pegasusMibModule": pegasusMibModule,
       "dsl": dsl,
       "dslCardTable": dslCardTable,
       "dslCardEntry": dslCardEntry,
       "dslCardSlotNumber": dslCardSlotNumber,
       "dslCardAvailabilityStatus": dslCardAvailabilityStatus,
       "dslCardHardwareVersion": dslCardHardwareVersion,
       "dslCardManufacturer": dslCardManufacturer,
       "dslCardName": dslCardName,
       "dslCardOperState": dslCardOperState,
       "dslCardFirmwareVersion": dslCardFirmwareVersion,
       "dslCardSerialNumber": dslCardSerialNumber,
       "dslCardCommState": dslCardCommState,
       "dslCardAlarmStatus": dslCardAlarmStatus,
       "dslCardM16FirmwareVersion": dslCardM16FirmwareVersion,
       "dslLinkTable": dslLinkTable,
       "dslLinkEntry": dslLinkEntry,
       "dslLinkNumber": dslLinkNumber,
       "dslLinkActiveLoop": dslLinkActiveLoop,
       "dslLinkAddress": dslLinkAddress,
       "dslLinkAdminState": dslLinkAdminState,
       "dslLinkAlarmStatus": dslLinkAlarmStatus,
       "dslLinkAvailabilityStatus": dslLinkAvailabilityStatus,
       "dslLinkContact": dslLinkContact,
       "dslLinkCustomerId": dslLinkCustomerId,
       "dslLinkDynamicSlotAllocation": dslLinkDynamicSlotAllocation,
       "dslLinkIsRemotePower": dslLinkIsRemotePower,
       "dslLinkLineRate": dslLinkLineRate,
       "dslLinkDataRate": dslLinkDataRate,
       "dslLinkName": dslLinkName,
       "dslLinkNotes": dslLinkNotes,
       "dslLinkNumberOfBRA": dslLinkNumberOfBRA,
       "dslLinkOperState": dslLinkOperState,
       "dslLinkNumberOfZBits": dslLinkNumberOfZBits,
       "dslLinkPSDMask": dslLinkPSDMask,
       "dslLinkAssignedTrunk": dslLinkAssignedTrunk,
       "dslLinkPriority": dslLinkPriority,
       "iadTable": iadTable,
       "iadEntry": iadEntry,
       "iadAvailabilityStatus": iadAvailabilityStatus,
       "iadHardwareVersion": iadHardwareVersion,
       "iadManufacturer": iadManufacturer,
       "iadName": iadName,
       "iadOperState": iadOperState,
       "iadFirmwareVersion": iadFirmwareVersion,
       "iadSerialNumber": iadSerialNumber,
       "iadAlarmStatus": iadAlarmStatus,
       "iadISDNPowering": iadISDNPowering,
       "iadPOTSPowering": iadPOTSPowering,
       "iadEthPortSpeed": iadEthPortSpeed,
       "iadEthCurrentPortSpeed": iadEthCurrentPortSpeed,
       "iadEthFlowControl": iadEthFlowControl,
       "iadEthCurrentFlowControl": iadEthCurrentFlowControl,
       "dslInterfaceTable": dslInterfaceTable,
       "dslInterfaceEntry": dslInterfaceEntry,
       "dslInterfaceType": dslInterfaceType,
       "dslInterfaceAvailabilityStatus": dslInterfaceAvailabilityStatus,
       "dslInterfaceOperState": dslInterfaceOperState,
       "dslInterfacePerformanceStatus": dslInterfacePerformanceStatus,
       "dslInterfacePerfControlIndexOrZero": dslInterfacePerfControlIndexOrZero,
       "dslInterfaceSignalQuality": dslInterfaceSignalQuality,
       "dslInterfaceAttenuation": dslInterfaceAttenuation,
       "dslLinkCosTable": dslLinkCosTable,
       "dslLinkCosEntry": dslLinkCosEntry,
       "dslLinkCosAvailable": dslLinkCosAvailable,
       "dslLinkCosEnabled": dslLinkCosEnabled,
       "dslLinkCosClassifier": dslLinkCosClassifier,
       "dslLinkCosClassmapEF": dslLinkCosClassmapEF,
       "dslLinkCosClassmapAF2": dslLinkCosClassmapAF2,
       "dslLinkCosClassmapAF1": dslLinkCosClassmapAF1,
       "dslLinkCosRateLimitEF": dslLinkCosRateLimitEF,
       "dslLinkCosRateLimitAF2": dslLinkCosRateLimitAF2,
       "dslLinkCosRateLimitAF1": dslLinkCosRateLimitAF1,
       "v5": v5,
       "v5CardTable": v5CardTable,
       "v5CardEntry": v5CardEntry,
       "v5CardSlotNumber": v5CardSlotNumber,
       "v5CardAdminState": v5CardAdminState,
       "v5CardAvailabilityStatus": v5CardAvailabilityStatus,
       "v5CardHardwareVersion": v5CardHardwareVersion,
       "v5CardManufacturer": v5CardManufacturer,
       "v5CardName": v5CardName,
       "v5CardOperState": v5CardOperState,
       "v5CardFirmwareVersion": v5CardFirmwareVersion,
       "v5CardSerialNumber": v5CardSerialNumber,
       "v5CardCommState": v5CardCommState,
       "v5CardIsProvisioning": v5CardIsProvisioning,
       "v5CardClockMode": v5CardClockMode,
       "v5CardClockSource1": v5CardClockSource1,
       "v5CardClockSource2": v5CardClockSource2,
       "v5CardProtocolVersion": v5CardProtocolVersion,
       "v5CardRowStatus": v5CardRowStatus,
       "v5CardFlags": v5CardFlags,
       "v5CardETSIRelease": v5CardETSIRelease,
       "v5CardE1LineCode": v5CardE1LineCode,
       "v5CardE1FrameFormat": v5CardE1FrameFormat,
       "v5LinkTable": v5LinkTable,
       "v5LinkEntry": v5LinkEntry,
       "v5LinkNumber": v5LinkNumber,
       "v5LinkAdminState": v5LinkAdminState,
       "v5LinkAvailabilityStatus": v5LinkAvailabilityStatus,
       "v5LinkId": v5LinkId,
       "v5LinkOperState": v5LinkOperState,
       "v5LinkInterface": v5LinkInterface,
       "v5LinkAlarmStatus": v5LinkAlarmStatus,
       "v5LinkType": v5LinkType,
       "v5LinkNumberOfPcc": v5LinkNumberOfPcc,
       "v5LinkPerfControlIndexOrZero": v5LinkPerfControlIndexOrZero,
       "v5LinkRowStatus": v5LinkRowStatus,
       "v5LinkLineIdentifier": v5LinkLineIdentifier,
       "v5InterfaceTable": v5InterfaceTable,
       "v5InterfaceEntry": v5InterfaceEntry,
       "v5InterfaceNumber": v5InterfaceNumber,
       "v5InterfaceAdminState": v5InterfaceAdminState,
       "v5InterfaceAvailabilityStatus": v5InterfaceAvailabilityStatus,
       "v5InterfaceId": v5InterfaceId,
       "v5InterfaceOperState": v5InterfaceOperState,
       "v5InterfaceVariantId": v5InterfaceVariantId,
       "v5InterfaceRowStatus": v5InterfaceRowStatus,
       "v5InterfaceAlarmStatus": v5InterfaceAlarmStatus,
       "v5LccTable": v5LccTable,
       "v5LccEntry": v5LccEntry,
       "v5LccNumber": v5LccNumber,
       "v5LccIsProtected": v5LccIsProtected,
       "v5LccId": v5LccId,
       "v5LccOperState": v5LccOperState,
       "v5LccPccV5LinkNumber": v5LccPccV5LinkNumber,
       "v5LccPccTimeslot": v5LccPccTimeslot,
       "v5LccRowStatus": v5LccRowStatus,
       "v5IsdnPortTable": v5IsdnPortTable,
       "v5IsdnPortEntry": v5IsdnPortEntry,
       "v5IsdnPortBRANumber": v5IsdnPortBRANumber,
       "v5IsdnPortAdminState": v5IsdnPortAdminState,
       "v5IsdnPortOperState": v5IsdnPortOperState,
       "v5IsdnPortBlockingStatus": v5IsdnPortBlockingStatus,
       "v5IsdnPortBearer1Timeslot": v5IsdnPortBearer1Timeslot,
       "v5IsdnPortBearer2Timeslot": v5IsdnPortBearer2Timeslot,
       "v5IsdnPortEnvelopeFuncAddress": v5IsdnPortEnvelopeFuncAddress,
       "v5IsdnPortIsActivated": v5IsdnPortIsActivated,
       "v5IsdnPortAlarmStatus": v5IsdnPortAlarmStatus,
       "v5IsdnPortActiveLoop": v5IsdnPortActiveLoop,
       "v5IsdnPortV5CardSlotNumber": v5IsdnPortV5CardSlotNumber,
       "v5IsdnPortV5InterfaceNumber": v5IsdnPortV5InterfaceNumber,
       "v5IsdnPortDSignallingCommChan": v5IsdnPortDSignallingCommChan,
       "v5IsdnPortFrameCommChan": v5IsdnPortFrameCommChan,
       "v5IsdnPortPacketCommChan": v5IsdnPortPacketCommChan,
       "v5IsdnPortLineIdentifier": v5IsdnPortLineIdentifier,
       "data": data,
       "dataCardTable": dataCardTable,
       "dataCardEntry": dataCardEntry,
       "dataCardSlotNumber": dataCardSlotNumber,
       "dataCardAvailabilityStatus": dataCardAvailabilityStatus,
       "dataCardHardwareVersion": dataCardHardwareVersion,
       "dataCardManufacturer": dataCardManufacturer,
       "dataCardName": dataCardName,
       "dataCardOperState": dataCardOperState,
       "dataCardFirmwareVersion": dataCardFirmwareVersion,
       "dataCardSerialNumber": dataCardSerialNumber,
       "dataCardCommState": dataCardCommState,
       "dataCardVLANMode": dataCardVLANMode,
       "dataPortTable": dataPortTable,
       "dataPortEntry": dataPortEntry,
       "dataPortNumber": dataPortNumber,
       "dataPortAdminState": dataPortAdminState,
       "dataPortOperState": dataPortOperState,
       "dataPortAvailabilityStatus": dataPortAvailabilityStatus,
       "dataPortSpeed": dataPortSpeed,
       "dataPortFlowControl": dataPortFlowControl,
       "pegasusSystem": pegasusSystem,
       "autoPersistDelay": autoPersistDelay,
       "autoPersistEnabled": autoPersistEnabled,
       "configPriority": configPriority,
       "hwAdaptionPolicy": hwAdaptionPolicy,
       "ipBaseAddress": ipBaseAddress,
       "javaRuntimeVersion": javaRuntimeVersion,
       "javaVMName": javaVMName,
       "javaVMVersion": javaVMVersion,
       "mgmtIPAddress": mgmtIPAddress,
       "osArchitecture": osArchitecture,
       "osNameAndVersion": osNameAndVersion,
       "pemVersion": pemVersion,
       "startedBy": startedBy,
       "systemNumber": systemNumber,
       "mibRevision": mibRevision,
       "readCommunity": readCommunity,
       "writeCommunity": writeCommunity,
       "trapCommunity": trapCommunity,
       "trapDestination": trapDestination,
       "agentPort": agentPort,
       "authRespEnabled": authRespEnabled,
       "rackAlarmStatus": rackAlarmStatus,
       "perf": perf,
       "perfSweepCyclePeriod": perfSweepCyclePeriod,
       "perfControlTable": perfControlTable,
       "perfControlEntry": perfControlEntry,
       "perfControlIndex": perfControlIndex,
       "perfControlStatus": perfControlStatus,
       "perfControlLinkDescr": perfControlLinkDescr,
       "perfControlUpdatePeriod": perfControlUpdatePeriod,
       "perfControlEffectiveUpdatePeriod": perfControlEffectiveUpdatePeriod,
       "perfControlRowStatus": perfControlRowStatus,
       "perfDataTable": perfDataTable,
       "perfDataEntry": perfDataEntry,
       "perfDataKind": perfDataKind,
       "perfDataIndex": perfDataIndex,
       "perfDataES": perfDataES,
       "perfDataSES": perfDataSES,
       "perfDataUAS": perfDataUAS,
       "perfDataCV": perfDataCV,
       "perfDataLOSWS": perfDataLOSWS}
)
