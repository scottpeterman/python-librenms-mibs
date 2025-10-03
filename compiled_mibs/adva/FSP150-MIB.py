# SNMP MIB module (FSP150-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\FSP150-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:02 2025
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

(ArcState,
 Counter64String,
 ServiceImpairment,
 TrapAlarmSeverity,
 fsp150,
 neEventLogIdentityTranslation,
 neEventLogTimeStamp) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "ArcState",
    "Counter64String",
    "ServiceImpairment",
    "TrapAlarmSeverity",
    "fsp150",
    "neEventLogIdentityTranslation",
    "neEventLogTimeStamp")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsp150MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fsp150MIB.setRevisions(
        ("2007-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Fsp150ProvAssignmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("unassigned", 2))
    )



class Fsp150ProvEquipmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 2))
    )



class Fsp150ProvRequestType(TextualConvention, Integer32):
    status = "current"
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
          ("accept", 2),
          ("delete", 3))
    )



class Fsp150ChassisType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fsp150CP10100", 2),
          ("fsp150CPGIGABIT", 3),
          ("fsp150MO", 5),
          ("fsp150ME", 6),
          ("fsp150CPGIGREV2", 7),
          ("fsp150MG", 8),
          ("fsp150CX", 9))
    )



class Fsp150AlarmType(TextualConvention, Integer32):
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109)
        )
    )
    namedValues = NamedValues(
        *(("voltageTooLow", 1),
          ("voltageTooHigh", 2),
          ("tempTooHigh", 3),
          ("psuFailure", 4),
          ("fanFailure", 5),
          ("localChassisMissing", 6),
          ("localChassisMismatch", 7),
          ("configFailed", 8),
          ("configuring", 9),
          ("lossOfSignal", 101),
          ("lowOIP", 102),
          ("txFailure", 103),
          ("lossOfLink", 104),
          ("eqMismatch", 105),
          ("remChassisMissing", 106),
          ("remChassisMismatch", 107),
          ("loopback", 108),
          ("sfpMissing", 109))
    )



class Fsp150ProtectionType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("l2WithoutST", 2),
          ("l2WithST", 3),
          ("l3", 4),
          ("pointToPoint", 5),
          ("forceA", 6),
          ("forceB", 7),
          ("detecting", 8),
          ("linkAggregate", 9),
          ("none", 10))
    )



class Fsp150IngressDepartureConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("single", 2))
    )



class Fsp150EgressArrivalConfig(TextualConvention, Integer32):
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
        *(("both", 1),
          ("network1", 2),
          ("network2", 3),
          ("aps", 4))
    )



class Fsp150AddressFilter(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("addr00", 0),
          ("addr01", 1),
          ("addr02", 2))
    )


class Fsp150PreferredNetwork(TextualConvention, Integer32):
    status = "current"
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
          ("network1", 2),
          ("network2", 3))
    )



class Fsp150MulticastProtectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sameAsUnicast", 0),
          ("l2WithoutST", 1),
          ("l3", 2),
          ("pointToPoint", 3),
          ("forceA", 4),
          ("forceB", 5),
          ("linkAggregate", 6))
    )



class Fsp150NEMIModeType(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("notFitted", 2),
          ("master", 3),
          ("slave", 4))
    )



class Fsp150IngressDepartureStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("single", 2),
          ("tandem", 3))
    )



class Fsp150EgressArrivalStatus(TextualConvention, Integer32):
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
        *(("both", 1),
          ("network1", 2),
          ("network2", 3),
          ("tandem", 4))
    )



class Fsp150AdminStatusType(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("forcedLinkDown", 4))
    )



class Fsp150TechnologyAbility(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tech10BaseT", 1),
          ("tech10BaseTfullDuplex", 2),
          ("tech100BaseT4", 3),
          ("tech100BaseTX", 4),
          ("tech100BaseTXfullDuplex", 5),
          ("techPAUSE", 8),
          ("techAsymmetricPAUSE", 9),
          ("tech1000BaseTfullDuplex", 15))
    )


class Fsp150AutoNegStatus(TextualConvention, Integer32):
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
        *(("other", 1),
          ("configuring", 2),
          ("completed", 3),
          ("disabled", 4),
          ("parallelDetectFail", 5),
          ("unknown", 6))
    )



class Fsp150FanStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )



class Fsp150PSUStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2))
    )



class Fsp150OAMLoopbackCommandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("startRemoteLoopback", 2),
          ("stopRemoteLoopback", 3),
          ("startLoopback", 6),
          ("stopLoopback", 7),
          ("startLocalLoopback", 8),
          ("stopLocalLoopback", 9),
          ("startTerminalLoopback", 10),
          ("stopTerminalLoopback", 11))
    )



class Fsp150OAMLoopbackStatusType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("initiatingLoopback", 2),
          ("remoteLoopback", 3),
          ("terminatingLoopback", 4),
          ("loopback", 5),
          ("unknown", 6),
          ("localTailLoopback", 7))
    )



class Fsp150AccessPortForwardMode(TextualConvention, Integer32):
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
        *(("both", 1),
          ("network1", 2),
          ("network2", 3),
          ("tandem", 4))
    )



class Fsp150AccessPortTagMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("branch", 1),
          ("leaf", 2))
    )



class Fsp150PriorityType(TextualConvention, Integer32):
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
        *(("default", 0),
          ("force", 1),
          ("copy", 2))
    )



class Fsp150DataRates(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rate10Mbps", 0),
          ("rate100Mbps", 1),
          ("rate1000Mbps", 2),
          ("rateMaxSpeed", 5))
    )


class Fsp150TxModes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1))
    )


class Fsp150AutoNegSupp(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


class Fsp150MulticastIGMPConfig(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unmodified", 1),
          ("multicastVLAN", 2),
          ("both", 3))
    )



class Fsp150TMPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Fsp150VID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Fsp150VIDctrl(TextualConvention, Integer32):
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
        *(("qBridge", 1),
          ("force", 2),
          ("qInQ", 3),
          ("translate", 4))
    )



class Fsp150VLANfilter(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("onlyTagged", 2),
          ("onlyUntagged", 3))
    )



class Fsp150TMPortMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2),
          ("port3", 3))
    )


class Fsp150TrafficClassIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Fsp150TMColour(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )



class Fsp150ColourMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blind", 1),
          ("aware", 2))
    )



class Fsp150ConfigMgmtCommandType(TextualConvention, Integer32):
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
          ("save", 2),
          ("backup", 3),
          ("activate", 4),
          ("reset", 5),
          ("factory", 6))
    )



class Fsp150ConfigMgmtFileStatusType(TextualConvention, Integer32):
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
        *(("undefined", 1),
          ("upToDate", 2),
          ("notUpToDate", 3),
          ("rstPend", 4))
    )



class Fsp150TTPayloadType(TextualConvention, Integer32):
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
        *(("all0", 1),
          ("all1", 2),
          ("incr", 3),
          ("random", 4))
    )



class Fsp150TTStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )



class Fsp150TTActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("drop", 2))
    )



class Fsp150UpgradeState(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("downloading", 1),
          ("downloaded", 2),
          ("downloadFailed", 3),
          ("erasing", 4),
          ("installing", 5),
          ("installed", 6),
          ("verifying", 7),
          ("failed", 8),
          ("done", 9),
          ("fileNotFound", 10))
    )



class Fsp150UpgradeRequestCmd(TextualConvention, Integer32):
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
        *(("none", 0),
          ("upgrade", 1),
          ("reset", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Fsp150Products_ObjectIdentity = ObjectIdentity
fsp150Products = _Fsp150Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 1)
)
_Fsp150CP_ObjectIdentity = ObjectIdentity
fsp150CP = _Fsp150CP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    fsp150CP.setStatus("current")
_Fsp150Mx_ObjectIdentity = ObjectIdentity
fsp150Mx = _Fsp150Mx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    fsp150Mx.setStatus("current")
_Fsp150TopologyMIB_ObjectIdentity = ObjectIdentity
fsp150TopologyMIB = _Fsp150TopologyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1)
)
_Fsp150LocalChassisTable_Object = MibTable
fsp150LocalChassisTable = _Fsp150LocalChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsp150LocalChassisTable.setStatus("current")
_Fsp150LocalChassisEntry_Object = MibTableRow
fsp150LocalChassisEntry = _Fsp150LocalChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1)
)
fsp150LocalChassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150LocalChassisEntry.setStatus("current")
_Fsp150LocalChassisProvAssignmentState_Type = Fsp150ProvAssignmentType
_Fsp150LocalChassisProvAssignmentState_Object = MibTableColumn
fsp150LocalChassisProvAssignmentState = _Fsp150LocalChassisProvAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1, 1),
    _Fsp150LocalChassisProvAssignmentState_Type()
)
fsp150LocalChassisProvAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150LocalChassisProvAssignmentState.setStatus("current")
_Fsp150LocalChassisProvEquipmentState_Type = Fsp150ProvEquipmentType
_Fsp150LocalChassisProvEquipmentState_Object = MibTableColumn
fsp150LocalChassisProvEquipmentState = _Fsp150LocalChassisProvEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1, 2),
    _Fsp150LocalChassisProvEquipmentState_Type()
)
fsp150LocalChassisProvEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150LocalChassisProvEquipmentState.setStatus("current")
_Fsp150LocalChassisProvRequest_Type = Fsp150ProvRequestType
_Fsp150LocalChassisProvRequest_Object = MibTableColumn
fsp150LocalChassisProvRequest = _Fsp150LocalChassisProvRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1, 3),
    _Fsp150LocalChassisProvRequest_Type()
)
fsp150LocalChassisProvRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150LocalChassisProvRequest.setStatus("current")
_Fsp150LocalChassisAgentAddr_Type = IpAddress
_Fsp150LocalChassisAgentAddr_Object = MibTableColumn
fsp150LocalChassisAgentAddr = _Fsp150LocalChassisAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1, 4),
    _Fsp150LocalChassisAgentAddr_Type()
)
fsp150LocalChassisAgentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150LocalChassisAgentAddr.setStatus("current")


class _Fsp150LocalChassisAgentPort_Type(Integer32):
    """Custom type fsp150LocalChassisAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150LocalChassisAgentPort_Type.__name__ = "Integer32"
_Fsp150LocalChassisAgentPort_Object = MibTableColumn
fsp150LocalChassisAgentPort = _Fsp150LocalChassisAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 1, 1, 5),
    _Fsp150LocalChassisAgentPort_Type()
)
fsp150LocalChassisAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150LocalChassisAgentPort.setStatus("current")
_Fsp150PortIDTranslationTable_Object = MibTable
fsp150PortIDTranslationTable = _Fsp150PortIDTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fsp150PortIDTranslationTable.setStatus("current")
_Fsp150PortIDTranslationEntry_Object = MibTableRow
fsp150PortIDTranslationEntry = _Fsp150PortIDTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 2, 1)
)
fsp150PortIDTranslationEntry.setIndexNames(
    (0, "FSP150-MIB", "fsp150PortIDTranslationDevID"),
    (0, "FSP150-MIB", "fsp150PortIDTranslationPortNum"),
)
if mibBuilder.loadTexts:
    fsp150PortIDTranslationEntry.setStatus("current")
_Fsp150PortIDTranslationDevID_Type = MacAddress
_Fsp150PortIDTranslationDevID_Object = MibTableColumn
fsp150PortIDTranslationDevID = _Fsp150PortIDTranslationDevID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 2, 1, 1),
    _Fsp150PortIDTranslationDevID_Type()
)
fsp150PortIDTranslationDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150PortIDTranslationDevID.setStatus("current")


class _Fsp150PortIDTranslationPortNum_Type(Integer32):
    """Custom type fsp150PortIDTranslationPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150PortIDTranslationPortNum_Type.__name__ = "Integer32"
_Fsp150PortIDTranslationPortNum_Object = MibTableColumn
fsp150PortIDTranslationPortNum = _Fsp150PortIDTranslationPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 2, 1, 2),
    _Fsp150PortIDTranslationPortNum_Type()
)
fsp150PortIDTranslationPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150PortIDTranslationPortNum.setStatus("current")
_Fsp150PortIDTranslationIndex_Type = InterfaceIndex
_Fsp150PortIDTranslationIndex_Object = MibTableColumn
fsp150PortIDTranslationIndex = _Fsp150PortIDTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 2, 1, 3),
    _Fsp150PortIDTranslationIndex_Type()
)
fsp150PortIDTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150PortIDTranslationIndex.setStatus("current")
_Fsp150ChassisIDTranslationTable_Object = MibTable
fsp150ChassisIDTranslationTable = _Fsp150ChassisIDTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fsp150ChassisIDTranslationTable.setStatus("current")
_Fsp150ChassisIDTranslationEntry_Object = MibTableRow
fsp150ChassisIDTranslationEntry = _Fsp150ChassisIDTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 3, 1)
)
fsp150ChassisIDTranslationEntry.setIndexNames(
    (0, "FSP150-MIB", "fsp150ChassisIDTranslationDevID"),
)
if mibBuilder.loadTexts:
    fsp150ChassisIDTranslationEntry.setStatus("current")
_Fsp150ChassisIDTranslationDevID_Type = MacAddress
_Fsp150ChassisIDTranslationDevID_Object = MibTableColumn
fsp150ChassisIDTranslationDevID = _Fsp150ChassisIDTranslationDevID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 3, 1, 1),
    _Fsp150ChassisIDTranslationDevID_Type()
)
fsp150ChassisIDTranslationDevID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150ChassisIDTranslationDevID.setStatus("current")
_Fsp150ChassisIDTranslationIndex_Type = PhysicalIndex
_Fsp150ChassisIDTranslationIndex_Object = MibTableColumn
fsp150ChassisIDTranslationIndex = _Fsp150ChassisIDTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 3, 1, 2),
    _Fsp150ChassisIDTranslationIndex_Type()
)
fsp150ChassisIDTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisIDTranslationIndex.setStatus("current")
_Fsp150TopologyTable_Object = MibTable
fsp150TopologyTable = _Fsp150TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    fsp150TopologyTable.setStatus("current")
_Fsp150TopologyEntry_Object = MibTableRow
fsp150TopologyEntry = _Fsp150TopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1)
)
fsp150TopologyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150TopologyEntry.setStatus("current")
_Fsp150TopologyProvAssignmentState_Type = Fsp150ProvAssignmentType
_Fsp150TopologyProvAssignmentState_Object = MibTableColumn
fsp150TopologyProvAssignmentState = _Fsp150TopologyProvAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 1),
    _Fsp150TopologyProvAssignmentState_Type()
)
fsp150TopologyProvAssignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyProvAssignmentState.setStatus("current")
_Fsp150TopologyProvEquipmentState_Type = Fsp150ProvEquipmentType
_Fsp150TopologyProvEquipmentState_Object = MibTableColumn
fsp150TopologyProvEquipmentState = _Fsp150TopologyProvEquipmentState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 2),
    _Fsp150TopologyProvEquipmentState_Type()
)
fsp150TopologyProvEquipmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyProvEquipmentState.setStatus("current")
_Fsp150TopologyProvRequest_Type = Fsp150ProvRequestType
_Fsp150TopologyProvRequest_Object = MibTableColumn
fsp150TopologyProvRequest = _Fsp150TopologyProvRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 3),
    _Fsp150TopologyProvRequest_Type()
)
fsp150TopologyProvRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150TopologyProvRequest.setStatus("current")
_Fsp150TopologyRemAgentAddr_Type = IpAddress
_Fsp150TopologyRemAgentAddr_Object = MibTableColumn
fsp150TopologyRemAgentAddr = _Fsp150TopologyRemAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 4),
    _Fsp150TopologyRemAgentAddr_Type()
)
fsp150TopologyRemAgentAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemAgentAddr.setStatus("current")


class _Fsp150TopologyRemAgentPort_Type(Integer32):
    """Custom type fsp150TopologyRemAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TopologyRemAgentPort_Type.__name__ = "Integer32"
_Fsp150TopologyRemAgentPort_Object = MibTableColumn
fsp150TopologyRemAgentPort = _Fsp150TopologyRemAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 5),
    _Fsp150TopologyRemAgentPort_Type()
)
fsp150TopologyRemAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemAgentPort.setStatus("current")
_Fsp150TopologyRemChassisType_Type = Fsp150ChassisType
_Fsp150TopologyRemChassisType_Object = MibTableColumn
fsp150TopologyRemChassisType = _Fsp150TopologyRemChassisType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 6),
    _Fsp150TopologyRemChassisType_Type()
)
fsp150TopologyRemChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemChassisType.setStatus("current")
_Fsp150TopologyRemDevID_Type = MacAddress
_Fsp150TopologyRemDevID_Object = MibTableColumn
fsp150TopologyRemDevID = _Fsp150TopologyRemDevID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 7),
    _Fsp150TopologyRemDevID_Type()
)
fsp150TopologyRemDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemDevID.setStatus("current")


class _Fsp150TopologyRemPortNum_Type(Integer32):
    """Custom type fsp150TopologyRemPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TopologyRemPortNum_Type.__name__ = "Integer32"
_Fsp150TopologyRemPortNum_Object = MibTableColumn
fsp150TopologyRemPortNum = _Fsp150TopologyRemPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 8),
    _Fsp150TopologyRemPortNum_Type()
)
fsp150TopologyRemPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemPortNum.setStatus("current")
_Fsp150TopologyRemChassisIndex_Type = PhysicalIndex
_Fsp150TopologyRemChassisIndex_Object = MibTableColumn
fsp150TopologyRemChassisIndex = _Fsp150TopologyRemChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 9),
    _Fsp150TopologyRemChassisIndex_Type()
)
fsp150TopologyRemChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemChassisIndex.setStatus("current")
_Fsp150TopologyRemPortIndex_Type = InterfaceIndex
_Fsp150TopologyRemPortIndex_Object = MibTableColumn
fsp150TopologyRemPortIndex = _Fsp150TopologyRemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 10),
    _Fsp150TopologyRemPortIndex_Type()
)
fsp150TopologyRemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyRemPortIndex.setStatus("current")
_Fsp150TopologyPhysRemChassisType_Type = Fsp150ChassisType
_Fsp150TopologyPhysRemChassisType_Object = MibTableColumn
fsp150TopologyPhysRemChassisType = _Fsp150TopologyPhysRemChassisType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 11),
    _Fsp150TopologyPhysRemChassisType_Type()
)
fsp150TopologyPhysRemChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyPhysRemChassisType.setStatus("current")
_Fsp150TopologyPhysRemDevID_Type = MacAddress
_Fsp150TopologyPhysRemDevID_Object = MibTableColumn
fsp150TopologyPhysRemDevID = _Fsp150TopologyPhysRemDevID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 12),
    _Fsp150TopologyPhysRemDevID_Type()
)
fsp150TopologyPhysRemDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyPhysRemDevID.setStatus("current")


class _Fsp150TopologyPhysRemPortNum_Type(Integer32):
    """Custom type fsp150TopologyPhysRemPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TopologyPhysRemPortNum_Type.__name__ = "Integer32"
_Fsp150TopologyPhysRemPortNum_Object = MibTableColumn
fsp150TopologyPhysRemPortNum = _Fsp150TopologyPhysRemPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 1, 4, 1, 13),
    _Fsp150TopologyPhysRemPortNum_Type()
)
fsp150TopologyPhysRemPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TopologyPhysRemPortNum.setStatus("current")
_Fsp150AlarmMIB_ObjectIdentity = ObjectIdentity
fsp150AlarmMIB = _Fsp150AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2)
)
_Fsp150AlarmFilters_ObjectIdentity = ObjectIdentity
fsp150AlarmFilters = _Fsp150AlarmFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1)
)
_Fsp150EquipmentAlarmReportControlTable_Object = MibTable
fsp150EquipmentAlarmReportControlTable = _Fsp150EquipmentAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsp150EquipmentAlarmReportControlTable.setStatus("current")
_Fsp150EquipmentAlarmReportControlEntry_Object = MibTableRow
fsp150EquipmentAlarmReportControlEntry = _Fsp150EquipmentAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 1, 1)
)
fsp150EquipmentAlarmReportControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150EquipmentAlarmReportControlEntry.setStatus("current")
_Fsp150EquipmentAlarmReportControlState_Type = ArcState
_Fsp150EquipmentAlarmReportControlState_Object = MibTableColumn
fsp150EquipmentAlarmReportControlState = _Fsp150EquipmentAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 1, 1, 1),
    _Fsp150EquipmentAlarmReportControlState_Type()
)
fsp150EquipmentAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EquipmentAlarmReportControlState.setStatus("current")
_Fsp150InterfaceAlarmReportControlTable_Object = MibTable
fsp150InterfaceAlarmReportControlTable = _Fsp150InterfaceAlarmReportControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fsp150InterfaceAlarmReportControlTable.setStatus("current")
_Fsp150InterfaceAlarmReportControlEntry_Object = MibTableRow
fsp150InterfaceAlarmReportControlEntry = _Fsp150InterfaceAlarmReportControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 2, 1)
)
fsp150InterfaceAlarmReportControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150InterfaceAlarmReportControlEntry.setStatus("current")
_Fsp150InterfaceAlarmReportControlState_Type = ArcState
_Fsp150InterfaceAlarmReportControlState_Object = MibTableColumn
fsp150InterfaceAlarmReportControlState = _Fsp150InterfaceAlarmReportControlState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 2, 1, 1),
    _Fsp150InterfaceAlarmReportControlState_Type()
)
fsp150InterfaceAlarmReportControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150InterfaceAlarmReportControlState.setStatus("current")
_Fsp150AlarmSeverityTable_Object = MibTable
fsp150AlarmSeverityTable = _Fsp150AlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fsp150AlarmSeverityTable.setStatus("current")
_Fsp150AlarmSeverityEntry_Object = MibTableRow
fsp150AlarmSeverityEntry = _Fsp150AlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 3, 1)
)
fsp150AlarmSeverityEntry.setIndexNames(
    (0, "FSP150-MIB", "fsp150AlarmSeverityType"),
)
if mibBuilder.loadTexts:
    fsp150AlarmSeverityEntry.setStatus("current")
_Fsp150AlarmSeverityType_Type = Fsp150AlarmType
_Fsp150AlarmSeverityType_Object = MibTableColumn
fsp150AlarmSeverityType = _Fsp150AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 3, 1, 1),
    _Fsp150AlarmSeverityType_Type()
)
fsp150AlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150AlarmSeverityType.setStatus("current")
_Fsp150AlarmSeverityValue_Type = TrapAlarmSeverity
_Fsp150AlarmSeverityValue_Object = MibTableColumn
fsp150AlarmSeverityValue = _Fsp150AlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 1, 3, 1, 2),
    _Fsp150AlarmSeverityValue_Type()
)
fsp150AlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AlarmSeverityValue.setStatus("current")
_Fsp150CurrentAlarms_ObjectIdentity = ObjectIdentity
fsp150CurrentAlarms = _Fsp150CurrentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2)
)
_Fsp150EquipmentCurrentAlarmTable_Object = MibTable
fsp150EquipmentCurrentAlarmTable = _Fsp150EquipmentCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsp150EquipmentCurrentAlarmTable.setStatus("current")
_Fsp150EquipmentCurrentAlarmEntry_Object = MibTableRow
fsp150EquipmentCurrentAlarmEntry = _Fsp150EquipmentCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 1, 1)
)
fsp150EquipmentCurrentAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150EquipmentCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    fsp150EquipmentCurrentAlarmEntry.setStatus("current")
_Fsp150EquipmentCurrentAlarmType_Type = Fsp150AlarmType
_Fsp150EquipmentCurrentAlarmType_Object = MibTableColumn
fsp150EquipmentCurrentAlarmType = _Fsp150EquipmentCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 1, 1, 1),
    _Fsp150EquipmentCurrentAlarmType_Type()
)
fsp150EquipmentCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150EquipmentCurrentAlarmType.setStatus("current")
_Fsp150EquipmentCurrentAlarmSeverity_Type = TrapAlarmSeverity
_Fsp150EquipmentCurrentAlarmSeverity_Object = MibTableColumn
fsp150EquipmentCurrentAlarmSeverity = _Fsp150EquipmentCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 1, 1, 2),
    _Fsp150EquipmentCurrentAlarmSeverity_Type()
)
fsp150EquipmentCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EquipmentCurrentAlarmSeverity.setStatus("current")
_Fsp150EquipmentCurrentAlarmImpairment_Type = ServiceImpairment
_Fsp150EquipmentCurrentAlarmImpairment_Object = MibTableColumn
fsp150EquipmentCurrentAlarmImpairment = _Fsp150EquipmentCurrentAlarmImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 1, 1, 3),
    _Fsp150EquipmentCurrentAlarmImpairment_Type()
)
fsp150EquipmentCurrentAlarmImpairment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EquipmentCurrentAlarmImpairment.setStatus("current")
_Fsp150InterfaceCurrentAlarmTable_Object = MibTable
fsp150InterfaceCurrentAlarmTable = _Fsp150InterfaceCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fsp150InterfaceCurrentAlarmTable.setStatus("current")
_Fsp150InterfaceCurrentAlarmEntry_Object = MibTableRow
fsp150InterfaceCurrentAlarmEntry = _Fsp150InterfaceCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 2, 1)
)
fsp150InterfaceCurrentAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP150-MIB", "fsp150InterfaceCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    fsp150InterfaceCurrentAlarmEntry.setStatus("current")
_Fsp150InterfaceCurrentAlarmType_Type = Fsp150AlarmType
_Fsp150InterfaceCurrentAlarmType_Object = MibTableColumn
fsp150InterfaceCurrentAlarmType = _Fsp150InterfaceCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 2, 1, 1),
    _Fsp150InterfaceCurrentAlarmType_Type()
)
fsp150InterfaceCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150InterfaceCurrentAlarmType.setStatus("current")
_Fsp150InterfaceCurrentAlarmSeverity_Type = TrapAlarmSeverity
_Fsp150InterfaceCurrentAlarmSeverity_Object = MibTableColumn
fsp150InterfaceCurrentAlarmSeverity = _Fsp150InterfaceCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 2, 1, 2),
    _Fsp150InterfaceCurrentAlarmSeverity_Type()
)
fsp150InterfaceCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150InterfaceCurrentAlarmSeverity.setStatus("current")
_Fsp150InterfaceCurrentAlarmImpairment_Type = ServiceImpairment
_Fsp150InterfaceCurrentAlarmImpairment_Object = MibTableColumn
fsp150InterfaceCurrentAlarmImpairment = _Fsp150InterfaceCurrentAlarmImpairment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 2, 2, 1, 3),
    _Fsp150InterfaceCurrentAlarmImpairment_Type()
)
fsp150InterfaceCurrentAlarmImpairment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150InterfaceCurrentAlarmImpairment.setStatus("current")


class _Fsp150AlarmDelayRaise_Type(Integer32):
    """Custom type fsp150AlarmDelayRaise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150AlarmDelayRaise_Type.__name__ = "Integer32"
_Fsp150AlarmDelayRaise_Object = MibScalar
fsp150AlarmDelayRaise = _Fsp150AlarmDelayRaise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 3),
    _Fsp150AlarmDelayRaise_Type()
)
fsp150AlarmDelayRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AlarmDelayRaise.setStatus("current")


class _Fsp150AlarmDelayClear_Type(Integer32):
    """Custom type fsp150AlarmDelayClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150AlarmDelayClear_Type.__name__ = "Integer32"
_Fsp150AlarmDelayClear_Object = MibScalar
fsp150AlarmDelayClear = _Fsp150AlarmDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 2, 4),
    _Fsp150AlarmDelayClear_Type()
)
fsp150AlarmDelayClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AlarmDelayClear.setStatus("current")
_Fsp150ConfigAndStatus_ObjectIdentity = ObjectIdentity
fsp150ConfigAndStatus = _Fsp150ConfigAndStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3)
)
_Fsp150ChassisConfigTable_Object = MibTable
fsp150ChassisConfigTable = _Fsp150ChassisConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fsp150ChassisConfigTable.setStatus("current")
_Fsp150ChassisConfigEntry_Object = MibTableRow
fsp150ChassisConfigEntry = _Fsp150ChassisConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1)
)
fsp150ChassisConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150ChassisConfigEntry.setStatus("current")
_Fsp150ChassisConfigNetAIndex_Type = InterfaceIndex
_Fsp150ChassisConfigNetAIndex_Object = MibTableColumn
fsp150ChassisConfigNetAIndex = _Fsp150ChassisConfigNetAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 2),
    _Fsp150ChassisConfigNetAIndex_Type()
)
fsp150ChassisConfigNetAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisConfigNetAIndex.setStatus("current")
_Fsp150ChassisConfigNetBIndex_Type = InterfaceIndex
_Fsp150ChassisConfigNetBIndex_Object = MibTableColumn
fsp150ChassisConfigNetBIndex = _Fsp150ChassisConfigNetBIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 3),
    _Fsp150ChassisConfigNetBIndex_Type()
)
fsp150ChassisConfigNetBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisConfigNetBIndex.setStatus("current")
_Fsp150ChassisConfigProtType_Type = Fsp150ProtectionType
_Fsp150ChassisConfigProtType_Object = MibTableColumn
fsp150ChassisConfigProtType = _Fsp150ChassisConfigProtType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 4),
    _Fsp150ChassisConfigProtType_Type()
)
fsp150ChassisConfigProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigProtType.setStatus("current")


class _Fsp150ChassisConfigUserString1_Type(DisplayString):
    """Custom type fsp150ChassisConfigUserString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Fsp150ChassisConfigUserString1_Type.__name__ = "DisplayString"
_Fsp150ChassisConfigUserString1_Object = MibTableColumn
fsp150ChassisConfigUserString1 = _Fsp150ChassisConfigUserString1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 5),
    _Fsp150ChassisConfigUserString1_Type()
)
fsp150ChassisConfigUserString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigUserString1.setStatus("current")


class _Fsp150ChassisConfigUserString2_Type(DisplayString):
    """Custom type fsp150ChassisConfigUserString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Fsp150ChassisConfigUserString2_Type.__name__ = "DisplayString"
_Fsp150ChassisConfigUserString2_Object = MibTableColumn
fsp150ChassisConfigUserString2 = _Fsp150ChassisConfigUserString2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 6),
    _Fsp150ChassisConfigUserString2_Type()
)
fsp150ChassisConfigUserString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigUserString2.setStatus("current")


class _Fsp150ChassisConfigUserString3_Type(DisplayString):
    """Custom type fsp150ChassisConfigUserString3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Fsp150ChassisConfigUserString3_Type.__name__ = "DisplayString"
_Fsp150ChassisConfigUserString3_Object = MibTableColumn
fsp150ChassisConfigUserString3 = _Fsp150ChassisConfigUserString3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 7),
    _Fsp150ChassisConfigUserString3_Type()
)
fsp150ChassisConfigUserString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigUserString3.setStatus("current")


class _Fsp150ChassisConfigLowVoltageThreshold_Type(Integer32):
    """Custom type fsp150ChassisConfigLowVoltageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisConfigLowVoltageThreshold_Type.__name__ = "Integer32"
_Fsp150ChassisConfigLowVoltageThreshold_Object = MibTableColumn
fsp150ChassisConfigLowVoltageThreshold = _Fsp150ChassisConfigLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 8),
    _Fsp150ChassisConfigLowVoltageThreshold_Type()
)
fsp150ChassisConfigLowVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigLowVoltageThreshold.setStatus("current")


class _Fsp150ChassisConfigHighVoltageThreshold_Type(Integer32):
    """Custom type fsp150ChassisConfigHighVoltageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisConfigHighVoltageThreshold_Type.__name__ = "Integer32"
_Fsp150ChassisConfigHighVoltageThreshold_Object = MibTableColumn
fsp150ChassisConfigHighVoltageThreshold = _Fsp150ChassisConfigHighVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 9),
    _Fsp150ChassisConfigHighVoltageThreshold_Type()
)
fsp150ChassisConfigHighVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigHighVoltageThreshold.setStatus("current")


class _Fsp150ChassisConfigHighTempThreshold_Type(Integer32):
    """Custom type fsp150ChassisConfigHighTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150ChassisConfigHighTempThreshold_Type.__name__ = "Integer32"
_Fsp150ChassisConfigHighTempThreshold_Object = MibTableColumn
fsp150ChassisConfigHighTempThreshold = _Fsp150ChassisConfigHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 10),
    _Fsp150ChassisConfigHighTempThreshold_Type()
)
fsp150ChassisConfigHighTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigHighTempThreshold.setStatus("current")
_Fsp150ChassisConfigForwardHSRP_Type = TruthValue
_Fsp150ChassisConfigForwardHSRP_Object = MibTableColumn
fsp150ChassisConfigForwardHSRP = _Fsp150ChassisConfigForwardHSRP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 11),
    _Fsp150ChassisConfigForwardHSRP_Type()
)
fsp150ChassisConfigForwardHSRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigForwardHSRP.setStatus("current")
_Fsp150ChassisConfigForwardVRRP_Type = TruthValue
_Fsp150ChassisConfigForwardVRRP_Object = MibTableColumn
fsp150ChassisConfigForwardVRRP = _Fsp150ChassisConfigForwardVRRP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 12),
    _Fsp150ChassisConfigForwardVRRP_Type()
)
fsp150ChassisConfigForwardVRRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigForwardVRRP.setStatus("current")


class _Fsp150ChassisConfigBPDUInflation_Type(Integer32):
    """Custom type fsp150ChassisConfigBPDUInflation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150ChassisConfigBPDUInflation_Type.__name__ = "Integer32"
_Fsp150ChassisConfigBPDUInflation_Object = MibTableColumn
fsp150ChassisConfigBPDUInflation = _Fsp150ChassisConfigBPDUInflation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 13),
    _Fsp150ChassisConfigBPDUInflation_Type()
)
fsp150ChassisConfigBPDUInflation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigBPDUInflation.setStatus("current")
_Fsp150ChassisConfigIngressDepartureConfig_Type = Fsp150IngressDepartureConfig
_Fsp150ChassisConfigIngressDepartureConfig_Object = MibTableColumn
fsp150ChassisConfigIngressDepartureConfig = _Fsp150ChassisConfigIngressDepartureConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 14),
    _Fsp150ChassisConfigIngressDepartureConfig_Type()
)
fsp150ChassisConfigIngressDepartureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigIngressDepartureConfig.setStatus("current")
_Fsp150ChassisConfigEgressArrivalConfig_Type = Fsp150EgressArrivalConfig
_Fsp150ChassisConfigEgressArrivalConfig_Object = MibTableColumn
fsp150ChassisConfigEgressArrivalConfig = _Fsp150ChassisConfigEgressArrivalConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 15),
    _Fsp150ChassisConfigEgressArrivalConfig_Type()
)
fsp150ChassisConfigEgressArrivalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigEgressArrivalConfig.setStatus("current")
_Fsp150ChassisConfigLinkLossFwd_Type = TruthValue
_Fsp150ChassisConfigLinkLossFwd_Object = MibTableColumn
fsp150ChassisConfigLinkLossFwd = _Fsp150ChassisConfigLinkLossFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 16),
    _Fsp150ChassisConfigLinkLossFwd_Type()
)
fsp150ChassisConfigLinkLossFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigLinkLossFwd.setStatus("current")
_Fsp150ChassisConfigPointToPointMode_Type = TruthValue
_Fsp150ChassisConfigPointToPointMode_Object = MibTableColumn
fsp150ChassisConfigPointToPointMode = _Fsp150ChassisConfigPointToPointMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 17),
    _Fsp150ChassisConfigPointToPointMode_Type()
)
fsp150ChassisConfigPointToPointMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigPointToPointMode.setStatus("current")


class _Fsp150ChassisConfigTagProtocolId_Type(Integer32):
    """Custom type fsp150ChassisConfigTagProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisConfigTagProtocolId_Type.__name__ = "Integer32"
_Fsp150ChassisConfigTagProtocolId_Object = MibTableColumn
fsp150ChassisConfigTagProtocolId = _Fsp150ChassisConfigTagProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 18),
    _Fsp150ChassisConfigTagProtocolId_Type()
)
fsp150ChassisConfigTagProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigTagProtocolId.setStatus("current")
_Fsp150ChassisConfigTrafficMgmtClassification_Type = TruthValue
_Fsp150ChassisConfigTrafficMgmtClassification_Object = MibTableColumn
fsp150ChassisConfigTrafficMgmtClassification = _Fsp150ChassisConfigTrafficMgmtClassification_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 19),
    _Fsp150ChassisConfigTrafficMgmtClassification_Type()
)
fsp150ChassisConfigTrafficMgmtClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigTrafficMgmtClassification.setStatus("current")
_Fsp150ChassisConfigJumboFrame_Type = TruthValue
_Fsp150ChassisConfigJumboFrame_Object = MibTableColumn
fsp150ChassisConfigJumboFrame = _Fsp150ChassisConfigJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 20),
    _Fsp150ChassisConfigJumboFrame_Type()
)
fsp150ChassisConfigJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigJumboFrame.setStatus("current")
_Fsp150ChassisConfigTandemMode_Type = TruthValue
_Fsp150ChassisConfigTandemMode_Object = MibTableColumn
fsp150ChassisConfigTandemMode = _Fsp150ChassisConfigTandemMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 21),
    _Fsp150ChassisConfigTandemMode_Type()
)
fsp150ChassisConfigTandemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigTandemMode.setStatus("current")


class _Fsp150ChassisConfigRingId_Type(Integer32):
    """Custom type fsp150ChassisConfigRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisConfigRingId_Type.__name__ = "Integer32"
_Fsp150ChassisConfigRingId_Object = MibTableColumn
fsp150ChassisConfigRingId = _Fsp150ChassisConfigRingId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 22),
    _Fsp150ChassisConfigRingId_Type()
)
fsp150ChassisConfigRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigRingId.setStatus("current")
_Fsp150ChassisConfigPauseEnable_Type = TruthValue
_Fsp150ChassisConfigPauseEnable_Object = MibTableColumn
fsp150ChassisConfigPauseEnable = _Fsp150ChassisConfigPauseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 23),
    _Fsp150ChassisConfigPauseEnable_Type()
)
fsp150ChassisConfigPauseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigPauseEnable.setStatus("current")
_Fsp150ChassisConfigBpduFilter_Type = Fsp150AddressFilter
_Fsp150ChassisConfigBpduFilter_Object = MibTableColumn
fsp150ChassisConfigBpduFilter = _Fsp150ChassisConfigBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 24),
    _Fsp150ChassisConfigBpduFilter_Type()
)
fsp150ChassisConfigBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigBpduFilter.setStatus("current")
_Fsp150ChassisConfigTmSupp_Type = TruthValue
_Fsp150ChassisConfigTmSupp_Object = MibTableColumn
fsp150ChassisConfigTmSupp = _Fsp150ChassisConfigTmSupp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 25),
    _Fsp150ChassisConfigTmSupp_Type()
)
fsp150ChassisConfigTmSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisConfigTmSupp.setStatus("current")
_Fsp150ChassisConfigPreferredNet_Type = Fsp150PreferredNetwork
_Fsp150ChassisConfigPreferredNet_Object = MibTableColumn
fsp150ChassisConfigPreferredNet = _Fsp150ChassisConfigPreferredNet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 26),
    _Fsp150ChassisConfigPreferredNet_Type()
)
fsp150ChassisConfigPreferredNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigPreferredNet.setStatus("current")


class _Fsp150ChassisConfigSwSyncRequest_Type(Integer32):
    """Custom type fsp150ChassisConfigSwSyncRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150ChassisConfigSwSyncRequest_Type.__name__ = "Integer32"
_Fsp150ChassisConfigSwSyncRequest_Object = MibTableColumn
fsp150ChassisConfigSwSyncRequest = _Fsp150ChassisConfigSwSyncRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 27),
    _Fsp150ChassisConfigSwSyncRequest_Type()
)
fsp150ChassisConfigSwSyncRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigSwSyncRequest.setStatus("current")
_Fsp150ChassisConfigMACAddressLearning_Type = TruthValue
_Fsp150ChassisConfigMACAddressLearning_Object = MibTableColumn
fsp150ChassisConfigMACAddressLearning = _Fsp150ChassisConfigMACAddressLearning_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 28),
    _Fsp150ChassisConfigMACAddressLearning_Type()
)
fsp150ChassisConfigMACAddressLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigMACAddressLearning.setStatus("current")
_Fsp150ChassisConfigUnitEgressMulticastCIR_Type = Unsigned32
_Fsp150ChassisConfigUnitEgressMulticastCIR_Object = MibTableColumn
fsp150ChassisConfigUnitEgressMulticastCIR = _Fsp150ChassisConfigUnitEgressMulticastCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 29),
    _Fsp150ChassisConfigUnitEgressMulticastCIR_Type()
)
fsp150ChassisConfigUnitEgressMulticastCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigUnitEgressMulticastCIR.setStatus("current")
_Fsp150ChassisConfigUnitEgressMulticastCBS_Type = Unsigned32
_Fsp150ChassisConfigUnitEgressMulticastCBS_Object = MibTableColumn
fsp150ChassisConfigUnitEgressMulticastCBS = _Fsp150ChassisConfigUnitEgressMulticastCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 30),
    _Fsp150ChassisConfigUnitEgressMulticastCBS_Type()
)
fsp150ChassisConfigUnitEgressMulticastCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigUnitEgressMulticastCBS.setStatus("current")
_Fsp150ChassisConfigMulticastProtType_Type = Fsp150MulticastProtectionType
_Fsp150ChassisConfigMulticastProtType_Object = MibTableColumn
fsp150ChassisConfigMulticastProtType = _Fsp150ChassisConfigMulticastProtType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 1, 1, 31),
    _Fsp150ChassisConfigMulticastProtType_Type()
)
fsp150ChassisConfigMulticastProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ChassisConfigMulticastProtType.setStatus("current")
_Fsp150ChassisStatusTable_Object = MibTable
fsp150ChassisStatusTable = _Fsp150ChassisStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fsp150ChassisStatusTable.setStatus("current")
_Fsp150ChassisStatusEntry_Object = MibTableRow
fsp150ChassisStatusEntry = _Fsp150ChassisStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1)
)
fsp150ChassisStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150ChassisStatusEntry.setStatus("current")
_Fsp150ChassisStatusProtState_Type = Fsp150ProtectionType
_Fsp150ChassisStatusProtState_Object = MibTableColumn
fsp150ChassisStatusProtState = _Fsp150ChassisStatusProtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 1),
    _Fsp150ChassisStatusProtState_Type()
)
fsp150ChassisStatusProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusProtState.setStatus("current")


class _Fsp150ChassisStatusTemperature_Type(Integer32):
    """Custom type fsp150ChassisStatusTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150ChassisStatusTemperature_Type.__name__ = "Integer32"
_Fsp150ChassisStatusTemperature_Object = MibTableColumn
fsp150ChassisStatusTemperature = _Fsp150ChassisStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 2),
    _Fsp150ChassisStatusTemperature_Type()
)
fsp150ChassisStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusTemperature.setStatus("current")


class _Fsp150ChassisStatusRailVoltage_Type(Integer32):
    """Custom type fsp150ChassisStatusRailVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisStatusRailVoltage_Type.__name__ = "Integer32"
_Fsp150ChassisStatusRailVoltage_Object = MibTableColumn
fsp150ChassisStatusRailVoltage = _Fsp150ChassisStatusRailVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 3),
    _Fsp150ChassisStatusRailVoltage_Type()
)
fsp150ChassisStatusRailVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusRailVoltage.setStatus("current")
_Fsp150ChassisStatusNEMIMode_Type = Fsp150NEMIModeType
_Fsp150ChassisStatusNEMIMode_Object = MibTableColumn
fsp150ChassisStatusNEMIMode = _Fsp150ChassisStatusNEMIMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 4),
    _Fsp150ChassisStatusNEMIMode_Type()
)
fsp150ChassisStatusNEMIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusNEMIMode.setStatus("current")


class _Fsp150ChassisStatusActiveNetwork_Type(Integer32):
    """Custom type fsp150ChassisStatusActiveNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisStatusActiveNetwork_Type.__name__ = "Integer32"
_Fsp150ChassisStatusActiveNetwork_Object = MibTableColumn
fsp150ChassisStatusActiveNetwork = _Fsp150ChassisStatusActiveNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 5),
    _Fsp150ChassisStatusActiveNetwork_Type()
)
fsp150ChassisStatusActiveNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusActiveNetwork.setStatus("current")
_Fsp150ChassisStatusBootTimer_Type = Unsigned32
_Fsp150ChassisStatusBootTimer_Object = MibTableColumn
fsp150ChassisStatusBootTimer = _Fsp150ChassisStatusBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 6),
    _Fsp150ChassisStatusBootTimer_Type()
)
fsp150ChassisStatusBootTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusBootTimer.setStatus("current")
_Fsp150ChassisStatusIngressDepartureStatus_Type = Fsp150IngressDepartureStatus
_Fsp150ChassisStatusIngressDepartureStatus_Object = MibTableColumn
fsp150ChassisStatusIngressDepartureStatus = _Fsp150ChassisStatusIngressDepartureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 7),
    _Fsp150ChassisStatusIngressDepartureStatus_Type()
)
fsp150ChassisStatusIngressDepartureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusIngressDepartureStatus.setStatus("current")
_Fsp150ChassisStatusEgressArrivalStatus_Type = Fsp150EgressArrivalStatus
_Fsp150ChassisStatusEgressArrivalStatus_Object = MibTableColumn
fsp150ChassisStatusEgressArrivalStatus = _Fsp150ChassisStatusEgressArrivalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 8),
    _Fsp150ChassisStatusEgressArrivalStatus_Type()
)
fsp150ChassisStatusEgressArrivalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusEgressArrivalStatus.setStatus("current")
_Fsp150ChassisStatusPreferredNet_Type = Fsp150PreferredNetwork
_Fsp150ChassisStatusPreferredNet_Object = MibTableColumn
fsp150ChassisStatusPreferredNet = _Fsp150ChassisStatusPreferredNet_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 9),
    _Fsp150ChassisStatusPreferredNet_Type()
)
fsp150ChassisStatusPreferredNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusPreferredNet.setStatus("current")


class _Fsp150ChassisStatusMulticastActiveNetwork_Type(Integer32):
    """Custom type fsp150ChassisStatusMulticastActiveNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ChassisStatusMulticastActiveNetwork_Type.__name__ = "Integer32"
_Fsp150ChassisStatusMulticastActiveNetwork_Object = MibTableColumn
fsp150ChassisStatusMulticastActiveNetwork = _Fsp150ChassisStatusMulticastActiveNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 2, 1, 10),
    _Fsp150ChassisStatusMulticastActiveNetwork_Type()
)
fsp150ChassisStatusMulticastActiveNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ChassisStatusMulticastActiveNetwork.setStatus("current")
_Fsp150IfConfigTable_Object = MibTable
fsp150IfConfigTable = _Fsp150IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3)
)
if mibBuilder.loadTexts:
    fsp150IfConfigTable.setStatus("current")
_Fsp150IfConfigEntry_Object = MibTableRow
fsp150IfConfigEntry = _Fsp150IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1)
)
fsp150IfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfConfigEntry.setStatus("current")


class _Fsp150IfConfigUserString_Type(DisplayString):
    """Custom type fsp150IfConfigUserString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Fsp150IfConfigUserString_Type.__name__ = "DisplayString"
_Fsp150IfConfigUserString_Object = MibTableColumn
fsp150IfConfigUserString = _Fsp150IfConfigUserString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 1),
    _Fsp150IfConfigUserString_Type()
)
fsp150IfConfigUserString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigUserString.setStatus("current")
_Fsp150IfConfigLinkLossFwd_Type = TruthValue
_Fsp150IfConfigLinkLossFwd_Object = MibTableColumn
fsp150IfConfigLinkLossFwd = _Fsp150IfConfigLinkLossFwd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 2),
    _Fsp150IfConfigLinkLossFwd_Type()
)
fsp150IfConfigLinkLossFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigLinkLossFwd.setStatus("current")
_Fsp150IfConfigAutoNeg_Type = TruthValue
_Fsp150IfConfigAutoNeg_Object = MibTableColumn
fsp150IfConfigAutoNeg = _Fsp150IfConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 3),
    _Fsp150IfConfigAutoNeg_Type()
)
fsp150IfConfigAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigAutoNeg.setStatus("current")


class _Fsp150IfConfigDataRate_Type(Integer32):
    """Custom type fsp150IfConfigDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IfConfigDataRate_Type.__name__ = "Integer32"
_Fsp150IfConfigDataRate_Object = MibTableColumn
fsp150IfConfigDataRate = _Fsp150IfConfigDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 4),
    _Fsp150IfConfigDataRate_Type()
)
fsp150IfConfigDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigDataRate.setStatus("current")
_Fsp150IfConfigAdminStatus_Type = Fsp150AdminStatusType
_Fsp150IfConfigAdminStatus_Object = MibTableColumn
fsp150IfConfigAdminStatus = _Fsp150IfConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 5),
    _Fsp150IfConfigAdminStatus_Type()
)
fsp150IfConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigAdminStatus.setStatus("current")
_Fsp150IfConfigRingController_Type = TruthValue
_Fsp150IfConfigRingController_Object = MibTableColumn
fsp150IfConfigRingController = _Fsp150IfConfigRingController_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 6),
    _Fsp150IfConfigRingController_Type()
)
fsp150IfConfigRingController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigRingController.setStatus("current")
_Fsp150IfConfigDasaSwapping_Type = TruthValue
_Fsp150IfConfigDasaSwapping_Object = MibTableColumn
fsp150IfConfigDasaSwapping = _Fsp150IfConfigDasaSwapping_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 7),
    _Fsp150IfConfigDasaSwapping_Type()
)
fsp150IfConfigDasaSwapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigDasaSwapping.setStatus("current")
_Fsp150IfConfigTerminalLoopback_Type = TruthValue
_Fsp150IfConfigTerminalLoopback_Object = MibTableColumn
fsp150IfConfigTerminalLoopback = _Fsp150IfConfigTerminalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 3, 1, 8),
    _Fsp150IfConfigTerminalLoopback_Type()
)
fsp150IfConfigTerminalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfConfigTerminalLoopback.setStatus("current")
_Fsp150IfTable_Object = MibTable
fsp150IfTable = _Fsp150IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 4)
)
if mibBuilder.loadTexts:
    fsp150IfTable.setStatus("current")
_Fsp150IfEntry_Object = MibTableRow
fsp150IfEntry = _Fsp150IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 4, 1)
)
fsp150IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfEntry.setStatus("current")
_Fsp150IfConnectorType_Type = SnmpAdminString
_Fsp150IfConnectorType_Object = MibTableColumn
fsp150IfConnectorType = _Fsp150IfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 4, 1, 1),
    _Fsp150IfConnectorType_Type()
)
fsp150IfConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfConnectorType.setStatus("current")
_Fsp150IfLinkLossFwdActive_Type = TruthValue
_Fsp150IfLinkLossFwdActive_Object = MibTableColumn
fsp150IfLinkLossFwdActive = _Fsp150IfLinkLossFwdActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 4, 1, 2),
    _Fsp150IfLinkLossFwdActive_Type()
)
fsp150IfLinkLossFwdActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfLinkLossFwdActive.setStatus("current")


class _Fsp150IfDataRate_Type(Integer32):
    """Custom type fsp150IfDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IfDataRate_Type.__name__ = "Integer32"
_Fsp150IfDataRate_Object = MibTableColumn
fsp150IfDataRate = _Fsp150IfDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 4, 1, 3),
    _Fsp150IfDataRate_Type()
)
fsp150IfDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfDataRate.setStatus("current")
_Fsp150OpticalIfConfigTable_Object = MibTable
fsp150OpticalIfConfigTable = _Fsp150OpticalIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 5)
)
if mibBuilder.loadTexts:
    fsp150OpticalIfConfigTable.setStatus("current")
_Fsp150OpticalIfConfigEntry_Object = MibTableRow
fsp150OpticalIfConfigEntry = _Fsp150OpticalIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 5, 1)
)
fsp150OpticalIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150OpticalIfConfigEntry.setStatus("current")


class _Fsp150OpticalIfConfigLowOIPThreshold_Type(Integer32):
    """Custom type fsp150OpticalIfConfigLowOIPThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150OpticalIfConfigLowOIPThreshold_Type.__name__ = "Integer32"
_Fsp150OpticalIfConfigLowOIPThreshold_Object = MibTableColumn
fsp150OpticalIfConfigLowOIPThreshold = _Fsp150OpticalIfConfigLowOIPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 5, 1, 1),
    _Fsp150OpticalIfConfigLowOIPThreshold_Type()
)
fsp150OpticalIfConfigLowOIPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150OpticalIfConfigLowOIPThreshold.setStatus("current")
_Fsp150OpticalIfTable_Object = MibTable
fsp150OpticalIfTable = _Fsp150OpticalIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6)
)
if mibBuilder.loadTexts:
    fsp150OpticalIfTable.setStatus("current")
_Fsp150OpticalIfEntry_Object = MibTableRow
fsp150OpticalIfEntry = _Fsp150OpticalIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1)
)
fsp150OpticalIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150OpticalIfEntry.setStatus("current")


class _Fsp150OpticalIfLinkLength9um_Type(Integer32):
    """Custom type fsp150OpticalIfLinkLength9um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150OpticalIfLinkLength9um_Type.__name__ = "Integer32"
_Fsp150OpticalIfLinkLength9um_Object = MibTableColumn
fsp150OpticalIfLinkLength9um = _Fsp150OpticalIfLinkLength9um_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1, 1),
    _Fsp150OpticalIfLinkLength9um_Type()
)
fsp150OpticalIfLinkLength9um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfLinkLength9um.setStatus("current")


class _Fsp150OpticalIfLinkLength50um_Type(Integer32):
    """Custom type fsp150OpticalIfLinkLength50um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150OpticalIfLinkLength50um_Type.__name__ = "Integer32"
_Fsp150OpticalIfLinkLength50um_Object = MibTableColumn
fsp150OpticalIfLinkLength50um = _Fsp150OpticalIfLinkLength50um_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1, 2),
    _Fsp150OpticalIfLinkLength50um_Type()
)
fsp150OpticalIfLinkLength50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfLinkLength50um.setStatus("current")


class _Fsp150OpticalIfLinkLength62d5um_Type(Integer32):
    """Custom type fsp150OpticalIfLinkLength62d5um based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150OpticalIfLinkLength62d5um_Type.__name__ = "Integer32"
_Fsp150OpticalIfLinkLength62d5um_Object = MibTableColumn
fsp150OpticalIfLinkLength62d5um = _Fsp150OpticalIfLinkLength62d5um_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1, 3),
    _Fsp150OpticalIfLinkLength62d5um_Type()
)
fsp150OpticalIfLinkLength62d5um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfLinkLength62d5um.setStatus("current")


class _Fsp150OpticalIfLinkLengthCopper_Type(Integer32):
    """Custom type fsp150OpticalIfLinkLengthCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150OpticalIfLinkLengthCopper_Type.__name__ = "Integer32"
_Fsp150OpticalIfLinkLengthCopper_Object = MibTableColumn
fsp150OpticalIfLinkLengthCopper = _Fsp150OpticalIfLinkLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1, 4),
    _Fsp150OpticalIfLinkLengthCopper_Type()
)
fsp150OpticalIfLinkLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfLinkLengthCopper.setStatus("current")


class _Fsp150OpticalIfWavelength_Type(Integer32):
    """Custom type fsp150OpticalIfWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150OpticalIfWavelength_Type.__name__ = "Integer32"
_Fsp150OpticalIfWavelength_Object = MibTableColumn
fsp150OpticalIfWavelength = _Fsp150OpticalIfWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 6, 1, 5),
    _Fsp150OpticalIfWavelength_Type()
)
fsp150OpticalIfWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfWavelength.setStatus("current")
_Fsp150OpticalIfStatusTable_Object = MibTable
fsp150OpticalIfStatusTable = _Fsp150OpticalIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7)
)
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusTable.setStatus("current")
_Fsp150OpticalIfStatusEntry_Object = MibTableRow
fsp150OpticalIfStatusEntry = _Fsp150OpticalIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7, 1)
)
fsp150OpticalIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusEntry.setStatus("current")


class _Fsp150OpticalIfStatusLaserBias_Type(Integer32):
    """Custom type fsp150OpticalIfStatusLaserBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150OpticalIfStatusLaserBias_Type.__name__ = "Integer32"
_Fsp150OpticalIfStatusLaserBias_Object = MibTableColumn
fsp150OpticalIfStatusLaserBias = _Fsp150OpticalIfStatusLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7, 1, 1),
    _Fsp150OpticalIfStatusLaserBias_Type()
)
fsp150OpticalIfStatusLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusLaserBias.setStatus("current")


class _Fsp150OpticalIfStatusTxPower_Type(Integer32):
    """Custom type fsp150OpticalIfStatusTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150OpticalIfStatusTxPower_Type.__name__ = "Integer32"
_Fsp150OpticalIfStatusTxPower_Object = MibTableColumn
fsp150OpticalIfStatusTxPower = _Fsp150OpticalIfStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7, 1, 2),
    _Fsp150OpticalIfStatusTxPower_Type()
)
fsp150OpticalIfStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusTxPower.setStatus("current")


class _Fsp150OpticalIfStatusRxPower_Type(Integer32):
    """Custom type fsp150OpticalIfStatusRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150OpticalIfStatusRxPower_Type.__name__ = "Integer32"
_Fsp150OpticalIfStatusRxPower_Object = MibTableColumn
fsp150OpticalIfStatusRxPower = _Fsp150OpticalIfStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7, 1, 3),
    _Fsp150OpticalIfStatusRxPower_Type()
)
fsp150OpticalIfStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusRxPower.setStatus("current")


class _Fsp150OpticalIfStatusLaserTemp_Type(Integer32):
    """Custom type fsp150OpticalIfStatusLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150OpticalIfStatusLaserTemp_Type.__name__ = "Integer32"
_Fsp150OpticalIfStatusLaserTemp_Object = MibTableColumn
fsp150OpticalIfStatusLaserTemp = _Fsp150OpticalIfStatusLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 7, 1, 4),
    _Fsp150OpticalIfStatusLaserTemp_Type()
)
fsp150OpticalIfStatusLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150OpticalIfStatusLaserTemp.setStatus("current")
_Fsp150ElectricalIfConfigTable_Object = MibTable
fsp150ElectricalIfConfigTable = _Fsp150ElectricalIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 8)
)
if mibBuilder.loadTexts:
    fsp150ElectricalIfConfigTable.setStatus("current")
_Fsp150ElectricalIfConfigEntry_Object = MibTableRow
fsp150ElectricalIfConfigEntry = _Fsp150ElectricalIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 8, 1)
)
fsp150ElectricalIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150ElectricalIfConfigEntry.setStatus("current")
_Fsp150ElectricalIfConfigFullDuplex_Type = TruthValue
_Fsp150ElectricalIfConfigFullDuplex_Object = MibTableColumn
fsp150ElectricalIfConfigFullDuplex = _Fsp150ElectricalIfConfigFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 8, 1, 1),
    _Fsp150ElectricalIfConfigFullDuplex_Type()
)
fsp150ElectricalIfConfigFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ElectricalIfConfigFullDuplex.setStatus("current")
_Fsp150IfAutoNegConfigTable_Object = MibTable
fsp150IfAutoNegConfigTable = _Fsp150IfAutoNegConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 9)
)
if mibBuilder.loadTexts:
    fsp150IfAutoNegConfigTable.setStatus("current")
_Fsp150IfAutoNegConfigEntry_Object = MibTableRow
fsp150IfAutoNegConfigEntry = _Fsp150IfAutoNegConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 9, 1)
)
fsp150IfAutoNegConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfAutoNegConfigEntry.setStatus("current")
_Fsp150IfAutoNegConfigAdvertisedTechnologyAbility_Type = Fsp150TechnologyAbility
_Fsp150IfAutoNegConfigAdvertisedTechnologyAbility_Object = MibTableColumn
fsp150IfAutoNegConfigAdvertisedTechnologyAbility = _Fsp150IfAutoNegConfigAdvertisedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 9, 1, 1),
    _Fsp150IfAutoNegConfigAdvertisedTechnologyAbility_Type()
)
fsp150IfAutoNegConfigAdvertisedTechnologyAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfAutoNegConfigAdvertisedTechnologyAbility.setStatus("current")
_Fsp150IfAutoNegStatusTable_Object = MibTable
fsp150IfAutoNegStatusTable = _Fsp150IfAutoNegStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10)
)
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusTable.setStatus("current")
_Fsp150IfAutoNegStatusEntry_Object = MibTableRow
fsp150IfAutoNegStatusEntry = _Fsp150IfAutoNegStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10, 1)
)
fsp150IfAutoNegStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusEntry.setStatus("current")
_Fsp150IfAutoNegStatusRemSignallingDetected_Type = TruthValue
_Fsp150IfAutoNegStatusRemSignallingDetected_Object = MibTableColumn
fsp150IfAutoNegStatusRemSignallingDetected = _Fsp150IfAutoNegStatusRemSignallingDetected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10, 1, 1),
    _Fsp150IfAutoNegStatusRemSignallingDetected_Type()
)
fsp150IfAutoNegStatusRemSignallingDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusRemSignallingDetected.setStatus("current")
_Fsp150IfAutoNegStatusStatus_Type = Fsp150AutoNegStatus
_Fsp150IfAutoNegStatusStatus_Object = MibTableColumn
fsp150IfAutoNegStatusStatus = _Fsp150IfAutoNegStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10, 1, 2),
    _Fsp150IfAutoNegStatusStatus_Type()
)
fsp150IfAutoNegStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusStatus.setStatus("current")
_Fsp150IfAutoNegStatusLocalTechnologyAbility_Type = Fsp150TechnologyAbility
_Fsp150IfAutoNegStatusLocalTechnologyAbility_Object = MibTableColumn
fsp150IfAutoNegStatusLocalTechnologyAbility = _Fsp150IfAutoNegStatusLocalTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10, 1, 3),
    _Fsp150IfAutoNegStatusLocalTechnologyAbility_Type()
)
fsp150IfAutoNegStatusLocalTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusLocalTechnologyAbility.setStatus("current")
_Fsp150IfAutoNegStatusReceivedTechnologyAbility_Type = Fsp150TechnologyAbility
_Fsp150IfAutoNegStatusReceivedTechnologyAbility_Object = MibTableColumn
fsp150IfAutoNegStatusReceivedTechnologyAbility = _Fsp150IfAutoNegStatusReceivedTechnologyAbility_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 10, 1, 4),
    _Fsp150IfAutoNegStatusReceivedTechnologyAbility_Type()
)
fsp150IfAutoNegStatusReceivedTechnologyAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfAutoNegStatusReceivedTechnologyAbility.setStatus("current")
_Fsp150FanTable_Object = MibTable
fsp150FanTable = _Fsp150FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 11)
)
if mibBuilder.loadTexts:
    fsp150FanTable.setStatus("current")
_Fsp150FanEntry_Object = MibTableRow
fsp150FanEntry = _Fsp150FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 11, 1)
)
fsp150FanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150FanEntry.setStatus("current")
_Fsp150FanStatus_Type = Fsp150FanStatus
_Fsp150FanStatus_Object = MibTableColumn
fsp150FanStatus = _Fsp150FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 11, 1, 1),
    _Fsp150FanStatus_Type()
)
fsp150FanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150FanStatus.setStatus("current")
_Fsp150PSUTable_Object = MibTable
fsp150PSUTable = _Fsp150PSUTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 12)
)
if mibBuilder.loadTexts:
    fsp150PSUTable.setStatus("current")
_Fsp150PSUEntry_Object = MibTableRow
fsp150PSUEntry = _Fsp150PSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 12, 1)
)
fsp150PSUEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150PSUEntry.setStatus("current")
_Fsp150PSUType_Type = SnmpAdminString
_Fsp150PSUType_Object = MibTableColumn
fsp150PSUType = _Fsp150PSUType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 12, 1, 1),
    _Fsp150PSUType_Type()
)
fsp150PSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150PSUType.setStatus("current")
_Fsp150PSUStatus_Type = Fsp150PSUStatus
_Fsp150PSUStatus_Object = MibTableColumn
fsp150PSUStatus = _Fsp150PSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 12, 1, 2),
    _Fsp150PSUStatus_Type()
)
fsp150PSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150PSUStatus.setStatus("current")


class _Fsp150PSUVoltage_Type(Integer32):
    """Custom type fsp150PSUVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150PSUVoltage_Type.__name__ = "Integer32"
_Fsp150PSUVoltage_Object = MibTableColumn
fsp150PSUVoltage = _Fsp150PSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 12, 1, 3),
    _Fsp150PSUVoltage_Type()
)
fsp150PSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150PSUVoltage.setStatus("current")
_Fsp150IfOAMConfigTable_Object = MibTable
fsp150IfOAMConfigTable = _Fsp150IfOAMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13)
)
if mibBuilder.loadTexts:
    fsp150IfOAMConfigTable.setStatus("current")
_Fsp150IfOAMConfigEntry_Object = MibTableRow
fsp150IfOAMConfigEntry = _Fsp150IfOAMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1)
)
fsp150IfOAMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfOAMConfigEntry.setStatus("current")
_Fsp150IfOAMConfigOAMEnable_Type = TruthValue
_Fsp150IfOAMConfigOAMEnable_Object = MibTableColumn
fsp150IfOAMConfigOAMEnable = _Fsp150IfOAMConfigOAMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 1),
    _Fsp150IfOAMConfigOAMEnable_Type()
)
fsp150IfOAMConfigOAMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigOAMEnable.setStatus("current")
_Fsp150IfOAMConfigLoopbackCommand_Type = Fsp150OAMLoopbackCommandType
_Fsp150IfOAMConfigLoopbackCommand_Object = MibTableColumn
fsp150IfOAMConfigLoopbackCommand = _Fsp150IfOAMConfigLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 2),
    _Fsp150IfOAMConfigLoopbackCommand_Type()
)
fsp150IfOAMConfigLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigLoopbackCommand.setStatus("current")
_Fsp150IfOAMConfigLoopbackStatus_Type = Fsp150OAMLoopbackStatusType
_Fsp150IfOAMConfigLoopbackStatus_Object = MibTableColumn
fsp150IfOAMConfigLoopbackStatus = _Fsp150IfOAMConfigLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 3),
    _Fsp150IfOAMConfigLoopbackStatus_Type()
)
fsp150IfOAMConfigLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigLoopbackStatus.setStatus("current")
_Fsp150IfOAMConfigOAMActive_Type = TruthValue
_Fsp150IfOAMConfigOAMActive_Object = MibTableColumn
fsp150IfOAMConfigOAMActive = _Fsp150IfOAMConfigOAMActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 4),
    _Fsp150IfOAMConfigOAMActive_Type()
)
fsp150IfOAMConfigOAMActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigOAMActive.setStatus("current")
_Fsp150IfOAMConfigOAMInfoEnable_Type = TruthValue
_Fsp150IfOAMConfigOAMInfoEnable_Object = MibTableColumn
fsp150IfOAMConfigOAMInfoEnable = _Fsp150IfOAMConfigOAMInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 5),
    _Fsp150IfOAMConfigOAMInfoEnable_Type()
)
fsp150IfOAMConfigOAMInfoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigOAMInfoEnable.setStatus("current")


class _Fsp150IfOAMConfigLoopbacktimer_Type(Integer32):
    """Custom type fsp150IfOAMConfigLoopbacktimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IfOAMConfigLoopbacktimer_Type.__name__ = "Integer32"
_Fsp150IfOAMConfigLoopbacktimer_Object = MibTableColumn
fsp150IfOAMConfigLoopbacktimer = _Fsp150IfOAMConfigLoopbacktimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 6),
    _Fsp150IfOAMConfigLoopbacktimer_Type()
)
fsp150IfOAMConfigLoopbacktimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigLoopbacktimer.setStatus("current")
_Fsp150IfOAMConfigTestTrafficEnable_Type = TruthValue
_Fsp150IfOAMConfigTestTrafficEnable_Object = MibTableColumn
fsp150IfOAMConfigTestTrafficEnable = _Fsp150IfOAMConfigTestTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 7),
    _Fsp150IfOAMConfigTestTrafficEnable_Type()
)
fsp150IfOAMConfigTestTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigTestTrafficEnable.setStatus("current")
_Fsp150IfOAMConfigResetCounters_Type = TruthValue
_Fsp150IfOAMConfigResetCounters_Object = MibTableColumn
fsp150IfOAMConfigResetCounters = _Fsp150IfOAMConfigResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 8),
    _Fsp150IfOAMConfigResetCounters_Type()
)
fsp150IfOAMConfigResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigResetCounters.setStatus("current")
_Fsp150IfOAMConfigDaSaSwapping_Type = TruthValue
_Fsp150IfOAMConfigDaSaSwapping_Object = MibTableColumn
fsp150IfOAMConfigDaSaSwapping = _Fsp150IfOAMConfigDaSaSwapping_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 13, 1, 9),
    _Fsp150IfOAMConfigDaSaSwapping_Type()
)
fsp150IfOAMConfigDaSaSwapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IfOAMConfigDaSaSwapping.setStatus("current")
_Fsp150AccessIfConfigTable_Object = MibTable
fsp150AccessIfConfigTable = _Fsp150AccessIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14)
)
if mibBuilder.loadTexts:
    fsp150AccessIfConfigTable.setStatus("current")
_Fsp150AccessIfConfigEntry_Object = MibTableRow
fsp150AccessIfConfigEntry = _Fsp150AccessIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1)
)
fsp150AccessIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEntry.setStatus("current")
_Fsp150AccessIfConfigForwardMode_Type = Fsp150AccessPortForwardMode
_Fsp150AccessIfConfigForwardMode_Object = MibTableColumn
fsp150AccessIfConfigForwardMode = _Fsp150AccessIfConfigForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 1),
    _Fsp150AccessIfConfigForwardMode_Type()
)
fsp150AccessIfConfigForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigForwardMode.setStatus("current")
_Fsp150AccessIfConfigTagMode_Type = Fsp150AccessPortTagMode
_Fsp150AccessIfConfigTagMode_Object = MibTableColumn
fsp150AccessIfConfigTagMode = _Fsp150AccessIfConfigTagMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 2),
    _Fsp150AccessIfConfigTagMode_Type()
)
fsp150AccessIfConfigTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigTagMode.setStatus("current")


class _Fsp150AccessIfConfigEgressCirLow_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCirLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCirLow_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCirLow_Object = MibTableColumn
fsp150AccessIfConfigEgressCirLow = _Fsp150AccessIfConfigEgressCirLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 3),
    _Fsp150AccessIfConfigEgressCirLow_Type()
)
fsp150AccessIfConfigEgressCirLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCirLow.setStatus("current")


class _Fsp150AccessIfConfigEgressCbsLow_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCbsLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCbsLow_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCbsLow_Object = MibTableColumn
fsp150AccessIfConfigEgressCbsLow = _Fsp150AccessIfConfigEgressCbsLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 4),
    _Fsp150AccessIfConfigEgressCbsLow_Type()
)
fsp150AccessIfConfigEgressCbsLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCbsLow.setStatus("current")


class _Fsp150AccessIfConfigEgressCirMed_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCirMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCirMed_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCirMed_Object = MibTableColumn
fsp150AccessIfConfigEgressCirMed = _Fsp150AccessIfConfigEgressCirMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 5),
    _Fsp150AccessIfConfigEgressCirMed_Type()
)
fsp150AccessIfConfigEgressCirMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCirMed.setStatus("current")


class _Fsp150AccessIfConfigEgressCbsMed_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCbsMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCbsMed_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCbsMed_Object = MibTableColumn
fsp150AccessIfConfigEgressCbsMed = _Fsp150AccessIfConfigEgressCbsMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 6),
    _Fsp150AccessIfConfigEgressCbsMed_Type()
)
fsp150AccessIfConfigEgressCbsMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCbsMed.setStatus("current")


class _Fsp150AccessIfConfigEgressCirHigh_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCirHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCirHigh_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCirHigh_Object = MibTableColumn
fsp150AccessIfConfigEgressCirHigh = _Fsp150AccessIfConfigEgressCirHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 7),
    _Fsp150AccessIfConfigEgressCirHigh_Type()
)
fsp150AccessIfConfigEgressCirHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCirHigh.setStatus("current")


class _Fsp150AccessIfConfigEgressCbsHigh_Type(Integer32):
    """Custom type fsp150AccessIfConfigEgressCbsHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigEgressCbsHigh_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigEgressCbsHigh_Object = MibTableColumn
fsp150AccessIfConfigEgressCbsHigh = _Fsp150AccessIfConfigEgressCbsHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 8),
    _Fsp150AccessIfConfigEgressCbsHigh_Type()
)
fsp150AccessIfConfigEgressCbsHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigEgressCbsHigh.setStatus("current")


class _Fsp150AccessIfConfigIngressCirLow_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCirLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCirLow_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCirLow_Object = MibTableColumn
fsp150AccessIfConfigIngressCirLow = _Fsp150AccessIfConfigIngressCirLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 9),
    _Fsp150AccessIfConfigIngressCirLow_Type()
)
fsp150AccessIfConfigIngressCirLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCirLow.setStatus("current")


class _Fsp150AccessIfConfigIngressCbsLow_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCbsLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCbsLow_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCbsLow_Object = MibTableColumn
fsp150AccessIfConfigIngressCbsLow = _Fsp150AccessIfConfigIngressCbsLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 10),
    _Fsp150AccessIfConfigIngressCbsLow_Type()
)
fsp150AccessIfConfigIngressCbsLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCbsLow.setStatus("current")


class _Fsp150AccessIfConfigIngressCirMed_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCirMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCirMed_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCirMed_Object = MibTableColumn
fsp150AccessIfConfigIngressCirMed = _Fsp150AccessIfConfigIngressCirMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 11),
    _Fsp150AccessIfConfigIngressCirMed_Type()
)
fsp150AccessIfConfigIngressCirMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCirMed.setStatus("current")


class _Fsp150AccessIfConfigIngressCbsMed_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCbsMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCbsMed_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCbsMed_Object = MibTableColumn
fsp150AccessIfConfigIngressCbsMed = _Fsp150AccessIfConfigIngressCbsMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 12),
    _Fsp150AccessIfConfigIngressCbsMed_Type()
)
fsp150AccessIfConfigIngressCbsMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCbsMed.setStatus("current")


class _Fsp150AccessIfConfigIngressCirHigh_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCirHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCirHigh_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCirHigh_Object = MibTableColumn
fsp150AccessIfConfigIngressCirHigh = _Fsp150AccessIfConfigIngressCirHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 13),
    _Fsp150AccessIfConfigIngressCirHigh_Type()
)
fsp150AccessIfConfigIngressCirHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCirHigh.setStatus("current")


class _Fsp150AccessIfConfigIngressCbsHigh_Type(Integer32):
    """Custom type fsp150AccessIfConfigIngressCbsHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150AccessIfConfigIngressCbsHigh_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigIngressCbsHigh_Object = MibTableColumn
fsp150AccessIfConfigIngressCbsHigh = _Fsp150AccessIfConfigIngressCbsHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 14),
    _Fsp150AccessIfConfigIngressCbsHigh_Type()
)
fsp150AccessIfConfigIngressCbsHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigIngressCbsHigh.setStatus("current")
_Fsp150AccessIfConfigPriorityType_Type = Fsp150PriorityType
_Fsp150AccessIfConfigPriorityType_Object = MibTableColumn
fsp150AccessIfConfigPriorityType = _Fsp150AccessIfConfigPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 15),
    _Fsp150AccessIfConfigPriorityType_Type()
)
fsp150AccessIfConfigPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigPriorityType.setStatus("current")


class _Fsp150AccessIfConfigPriorityValue_Type(Integer32):
    """Custom type fsp150AccessIfConfigPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150AccessIfConfigPriorityValue_Type.__name__ = "Integer32"
_Fsp150AccessIfConfigPriorityValue_Object = MibTableColumn
fsp150AccessIfConfigPriorityValue = _Fsp150AccessIfConfigPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 14, 1, 16),
    _Fsp150AccessIfConfigPriorityValue_Type()
)
fsp150AccessIfConfigPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessIfConfigPriorityValue.setStatus("current")
_Fsp150AccessIfStatusTable_Object = MibTable
fsp150AccessIfStatusTable = _Fsp150AccessIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15)
)
if mibBuilder.loadTexts:
    fsp150AccessIfStatusTable.setStatus("current")
_Fsp150AccessIfStatusEntry_Object = MibTableRow
fsp150AccessIfStatusEntry = _Fsp150AccessIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1)
)
fsp150AccessIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150AccessIfStatusEntry.setStatus("current")
_Fsp150AccessIfStatusForwardMode_Type = Fsp150AccessPortForwardMode
_Fsp150AccessIfStatusForwardMode_Object = MibTableColumn
fsp150AccessIfStatusForwardMode = _Fsp150AccessIfStatusForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 1),
    _Fsp150AccessIfStatusForwardMode_Type()
)
fsp150AccessIfStatusForwardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusForwardMode.setStatus("current")
_Fsp150AccessIfStatusEgressRegulatorOverflowLow_Type = Counter64String
_Fsp150AccessIfStatusEgressRegulatorOverflowLow_Object = MibTableColumn
fsp150AccessIfStatusEgressRegulatorOverflowLow = _Fsp150AccessIfStatusEgressRegulatorOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 2),
    _Fsp150AccessIfStatusEgressRegulatorOverflowLow_Type()
)
fsp150AccessIfStatusEgressRegulatorOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusEgressRegulatorOverflowLow.setStatus("current")
_Fsp150AccessIfStatusEgressRegulatorOverflowMed_Type = Counter64String
_Fsp150AccessIfStatusEgressRegulatorOverflowMed_Object = MibTableColumn
fsp150AccessIfStatusEgressRegulatorOverflowMed = _Fsp150AccessIfStatusEgressRegulatorOverflowMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 3),
    _Fsp150AccessIfStatusEgressRegulatorOverflowMed_Type()
)
fsp150AccessIfStatusEgressRegulatorOverflowMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusEgressRegulatorOverflowMed.setStatus("current")
_Fsp150AccessIfStatusEgressRegulatorOverflowHigh_Type = Counter64String
_Fsp150AccessIfStatusEgressRegulatorOverflowHigh_Object = MibTableColumn
fsp150AccessIfStatusEgressRegulatorOverflowHigh = _Fsp150AccessIfStatusEgressRegulatorOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 4),
    _Fsp150AccessIfStatusEgressRegulatorOverflowHigh_Type()
)
fsp150AccessIfStatusEgressRegulatorOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusEgressRegulatorOverflowHigh.setStatus("current")
_Fsp150AccessIfStatusIngressRegulatorOverflowLow_Type = Counter64String
_Fsp150AccessIfStatusIngressRegulatorOverflowLow_Object = MibTableColumn
fsp150AccessIfStatusIngressRegulatorOverflowLow = _Fsp150AccessIfStatusIngressRegulatorOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 5),
    _Fsp150AccessIfStatusIngressRegulatorOverflowLow_Type()
)
fsp150AccessIfStatusIngressRegulatorOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusIngressRegulatorOverflowLow.setStatus("current")
_Fsp150AccessIfStatusIngressRegulatorOverflowMed_Type = Counter64String
_Fsp150AccessIfStatusIngressRegulatorOverflowMed_Object = MibTableColumn
fsp150AccessIfStatusIngressRegulatorOverflowMed = _Fsp150AccessIfStatusIngressRegulatorOverflowMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 6),
    _Fsp150AccessIfStatusIngressRegulatorOverflowMed_Type()
)
fsp150AccessIfStatusIngressRegulatorOverflowMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusIngressRegulatorOverflowMed.setStatus("current")
_Fsp150AccessIfStatusIngressRegulatorOverflowHigh_Type = Counter64String
_Fsp150AccessIfStatusIngressRegulatorOverflowHigh_Object = MibTableColumn
fsp150AccessIfStatusIngressRegulatorOverflowHigh = _Fsp150AccessIfStatusIngressRegulatorOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 15, 1, 7),
    _Fsp150AccessIfStatusIngressRegulatorOverflowHigh_Type()
)
fsp150AccessIfStatusIngressRegulatorOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150AccessIfStatusIngressRegulatorOverflowHigh.setStatus("current")
_Fsp150IfCapsTable_Object = MibTable
fsp150IfCapsTable = _Fsp150IfCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 16)
)
if mibBuilder.loadTexts:
    fsp150IfCapsTable.setStatus("current")
_Fsp150IfCapsEntry_Object = MibTableRow
fsp150IfCapsEntry = _Fsp150IfCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 16, 1)
)
fsp150IfCapsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfCapsEntry.setStatus("current")
_Fsp150IfCapsSuppRates_Type = Fsp150DataRates
_Fsp150IfCapsSuppRates_Object = MibTableColumn
fsp150IfCapsSuppRates = _Fsp150IfCapsSuppRates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 16, 1, 1),
    _Fsp150IfCapsSuppRates_Type()
)
fsp150IfCapsSuppRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfCapsSuppRates.setStatus("current")
_Fsp150IfCapsSuppTxModes_Type = Fsp150TxModes
_Fsp150IfCapsSuppTxModes_Object = MibTableColumn
fsp150IfCapsSuppTxModes = _Fsp150IfCapsSuppTxModes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 16, 1, 2),
    _Fsp150IfCapsSuppTxModes_Type()
)
fsp150IfCapsSuppTxModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfCapsSuppTxModes.setStatus("current")
_Fsp150IfCapsSuppAutoNeg_Type = Fsp150AutoNegSupp
_Fsp150IfCapsSuppAutoNeg_Object = MibTableColumn
fsp150IfCapsSuppAutoNeg = _Fsp150IfCapsSuppAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 16, 1, 3),
    _Fsp150IfCapsSuppAutoNeg_Type()
)
fsp150IfCapsSuppAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfCapsSuppAutoNeg.setStatus("current")
_Fsp150NetworkIfConfigTable_Object = MibTable
fsp150NetworkIfConfigTable = _Fsp150NetworkIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 17)
)
if mibBuilder.loadTexts:
    fsp150NetworkIfConfigTable.setStatus("current")
_Fsp150NetworkIfConfigEntry_Object = MibTableRow
fsp150NetworkIfConfigEntry = _Fsp150NetworkIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 17, 1)
)
fsp150NetworkIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150NetworkIfConfigEntry.setStatus("current")


class _Fsp150NetworkIfConfigTransmitAc_Type(Integer32):
    """Custom type fsp150NetworkIfConfigTransmitAc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150NetworkIfConfigTransmitAc_Type.__name__ = "Integer32"
_Fsp150NetworkIfConfigTransmitAc_Object = MibTableColumn
fsp150NetworkIfConfigTransmitAc = _Fsp150NetworkIfConfigTransmitAc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 17, 1, 1),
    _Fsp150NetworkIfConfigTransmitAc_Type()
)
fsp150NetworkIfConfigTransmitAc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150NetworkIfConfigTransmitAc.setStatus("current")


class _Fsp150NetworkIfConfigTransmitAbs_Type(Integer32):
    """Custom type fsp150NetworkIfConfigTransmitAbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150NetworkIfConfigTransmitAbs_Type.__name__ = "Integer32"
_Fsp150NetworkIfConfigTransmitAbs_Object = MibTableColumn
fsp150NetworkIfConfigTransmitAbs = _Fsp150NetworkIfConfigTransmitAbs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 17, 1, 2),
    _Fsp150NetworkIfConfigTransmitAbs_Type()
)
fsp150NetworkIfConfigTransmitAbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150NetworkIfConfigTransmitAbs.setStatus("current")
_Fsp150NetworkIfConfigTranslation_Type = TruthValue
_Fsp150NetworkIfConfigTranslation_Object = MibTableColumn
fsp150NetworkIfConfigTranslation = _Fsp150NetworkIfConfigTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 17, 1, 3),
    _Fsp150NetworkIfConfigTranslation_Type()
)
fsp150NetworkIfConfigTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150NetworkIfConfigTranslation.setStatus("current")
_Fsp150TrafficManagementMIB_ObjectIdentity = ObjectIdentity
fsp150TrafficManagementMIB = _Fsp150TrafficManagementMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18)
)
_Fsp150TMBaseTable_Object = MibTable
fsp150TMBaseTable = _Fsp150TMBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1)
)
if mibBuilder.loadTexts:
    fsp150TMBaseTable.setStatus("current")
_Fsp150TMBaseEntry_Object = MibTableRow
fsp150TMBaseEntry = _Fsp150TMBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1)
)
fsp150TMBaseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150TMBaseEntry.setStatus("current")


class _Fsp150TMBaseMaxClassRules_Type(Integer32):
    """Custom type fsp150TMBaseMaxClassRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TMBaseMaxClassRules_Type.__name__ = "Integer32"
_Fsp150TMBaseMaxClassRules_Object = MibTableColumn
fsp150TMBaseMaxClassRules = _Fsp150TMBaseMaxClassRules_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1, 1),
    _Fsp150TMBaseMaxClassRules_Type()
)
fsp150TMBaseMaxClassRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMBaseMaxClassRules.setStatus("current")


class _Fsp150TMBaseMaxClasses_Type(Integer32):
    """Custom type fsp150TMBaseMaxClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TMBaseMaxClasses_Type.__name__ = "Integer32"
_Fsp150TMBaseMaxClasses_Object = MibTableColumn
fsp150TMBaseMaxClasses = _Fsp150TMBaseMaxClasses_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1, 2),
    _Fsp150TMBaseMaxClasses_Type()
)
fsp150TMBaseMaxClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMBaseMaxClasses.setStatus("current")


class _Fsp150TMBaseMaxMeters_Type(Integer32):
    """Custom type fsp150TMBaseMaxMeters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TMBaseMaxMeters_Type.__name__ = "Integer32"
_Fsp150TMBaseMaxMeters_Object = MibTableColumn
fsp150TMBaseMaxMeters = _Fsp150TMBaseMaxMeters_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1, 3),
    _Fsp150TMBaseMaxMeters_Type()
)
fsp150TMBaseMaxMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMBaseMaxMeters.setStatus("current")


class _Fsp150TMBaseMaxQueues_Type(Integer32):
    """Custom type fsp150TMBaseMaxQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TMBaseMaxQueues_Type.__name__ = "Integer32"
_Fsp150TMBaseMaxQueues_Object = MibTableColumn
fsp150TMBaseMaxQueues = _Fsp150TMBaseMaxQueues_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1, 4),
    _Fsp150TMBaseMaxQueues_Type()
)
fsp150TMBaseMaxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMBaseMaxQueues.setStatus("current")
_Fsp150TMBaseLastChangeTime_Type = TimeStamp
_Fsp150TMBaseLastChangeTime_Object = MibTableColumn
fsp150TMBaseLastChangeTime = _Fsp150TMBaseLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 1, 1, 5),
    _Fsp150TMBaseLastChangeTime_Type()
)
fsp150TMBaseLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMBaseLastChangeTime.setStatus("current")
_Fsp150TMPortTable_Object = MibTable
fsp150TMPortTable = _Fsp150TMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 2)
)
if mibBuilder.loadTexts:
    fsp150TMPortTable.setStatus("current")
_Fsp150TMPortEntry_Object = MibTableRow
fsp150TMPortEntry = _Fsp150TMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 2, 1)
)
fsp150TMPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150TMPortEntry.setStatus("current")
_Fsp150TMPortPortNo_Type = Fsp150TMPort
_Fsp150TMPortPortNo_Object = MibTableColumn
fsp150TMPortPortNo = _Fsp150TMPortPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 2, 1, 1),
    _Fsp150TMPortPortNo_Type()
)
fsp150TMPortPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150TMPortPortNo.setStatus("current")
_Fsp150TMPortConfigTable_Object = MibTable
fsp150TMPortConfigTable = _Fsp150TMPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3)
)
if mibBuilder.loadTexts:
    fsp150TMPortConfigTable.setStatus("current")
_Fsp150TMPortConfigEntry_Object = MibTableRow
fsp150TMPortConfigEntry = _Fsp150TMPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1)
)
fsp150TMPortConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150TMPortConfigPortNo"),
)
if mibBuilder.loadTexts:
    fsp150TMPortConfigEntry.setStatus("current")
_Fsp150TMPortConfigPortNo_Type = Fsp150TMPort
_Fsp150TMPortConfigPortNo_Object = MibTableColumn
fsp150TMPortConfigPortNo = _Fsp150TMPortConfigPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1, 1),
    _Fsp150TMPortConfigPortNo_Type()
)
fsp150TMPortConfigPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150TMPortConfigPortNo.setStatus("current")
_Fsp150TMPortConfigPVID_Type = Fsp150VID
_Fsp150TMPortConfigPVID_Object = MibTableColumn
fsp150TMPortConfigPVID = _Fsp150TMPortConfigPVID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1, 2),
    _Fsp150TMPortConfigPVID_Type()
)
fsp150TMPortConfigPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150TMPortConfigPVID.setStatus("current")
_Fsp150TMPortConfigPVIDctrl_Type = Fsp150VIDctrl
_Fsp150TMPortConfigPVIDctrl_Object = MibTableColumn
fsp150TMPortConfigPVIDctrl = _Fsp150TMPortConfigPVIDctrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1, 3),
    _Fsp150TMPortConfigPVIDctrl_Type()
)
fsp150TMPortConfigPVIDctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150TMPortConfigPVIDctrl.setStatus("current")


class _Fsp150TMPortConfigTPID_Type(Integer32):
    """Custom type fsp150TMPortConfigTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150TMPortConfigTPID_Type.__name__ = "Integer32"
_Fsp150TMPortConfigTPID_Object = MibTableColumn
fsp150TMPortConfigTPID = _Fsp150TMPortConfigTPID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1, 4),
    _Fsp150TMPortConfigTPID_Type()
)
fsp150TMPortConfigTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150TMPortConfigTPID.setStatus("current")
_Fsp150TMPortConfigVLANfilter_Type = Fsp150VLANfilter
_Fsp150TMPortConfigVLANfilter_Object = MibTableColumn
fsp150TMPortConfigVLANfilter = _Fsp150TMPortConfigVLANfilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 3, 1, 5),
    _Fsp150TMPortConfigVLANfilter_Type()
)
fsp150TMPortConfigVLANfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150TMPortConfigVLANfilter.setStatus("current")
_Fsp150VIDtranslationTable_Object = MibTable
fsp150VIDtranslationTable = _Fsp150VIDtranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4)
)
if mibBuilder.loadTexts:
    fsp150VIDtranslationTable.setStatus("current")
_Fsp150VIDtranslationEntry_Object = MibTableRow
fsp150VIDtranslationEntry = _Fsp150VIDtranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4, 1)
)
fsp150VIDtranslationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150VIDtranslationPortNo"),
    (0, "FSP150-MIB", "fsp150VIDtranslationInternal"),
)
if mibBuilder.loadTexts:
    fsp150VIDtranslationEntry.setStatus("current")
_Fsp150VIDtranslationPortNo_Type = Fsp150TMPort
_Fsp150VIDtranslationPortNo_Object = MibTableColumn
fsp150VIDtranslationPortNo = _Fsp150VIDtranslationPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4, 1, 1),
    _Fsp150VIDtranslationPortNo_Type()
)
fsp150VIDtranslationPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150VIDtranslationPortNo.setStatus("current")
_Fsp150VIDtranslationInternal_Type = Fsp150VID
_Fsp150VIDtranslationInternal_Object = MibTableColumn
fsp150VIDtranslationInternal = _Fsp150VIDtranslationInternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4, 1, 2),
    _Fsp150VIDtranslationInternal_Type()
)
fsp150VIDtranslationInternal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150VIDtranslationInternal.setStatus("current")
_Fsp150VIDtranslationExternal_Type = Fsp150VID
_Fsp150VIDtranslationExternal_Object = MibTableColumn
fsp150VIDtranslationExternal = _Fsp150VIDtranslationExternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4, 1, 3),
    _Fsp150VIDtranslationExternal_Type()
)
fsp150VIDtranslationExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150VIDtranslationExternal.setStatus("current")
_Fsp150VIDtranslationRowStatus_Type = RowStatus
_Fsp150VIDtranslationRowStatus_Object = MibTableColumn
fsp150VIDtranslationRowStatus = _Fsp150VIDtranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 4, 1, 4),
    _Fsp150VIDtranslationRowStatus_Type()
)
fsp150VIDtranslationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150VIDtranslationRowStatus.setStatus("current")
_Fsp150FilteringTable_Object = MibTable
fsp150FilteringTable = _Fsp150FilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5)
)
if mibBuilder.loadTexts:
    fsp150FilteringTable.setStatus("current")
_Fsp150FilteringEntry_Object = MibTableRow
fsp150FilteringEntry = _Fsp150FilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5, 1)
)
fsp150FilteringEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150FilteringVlanId"),
)
if mibBuilder.loadTexts:
    fsp150FilteringEntry.setStatus("current")
_Fsp150FilteringVlanId_Type = Fsp150VID
_Fsp150FilteringVlanId_Object = MibTableColumn
fsp150FilteringVlanId = _Fsp150FilteringVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5, 1, 1),
    _Fsp150FilteringVlanId_Type()
)
fsp150FilteringVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150FilteringVlanId.setStatus("current")
_Fsp150FilteringMembers_Type = Fsp150TMPortMap
_Fsp150FilteringMembers_Object = MibTableColumn
fsp150FilteringMembers = _Fsp150FilteringMembers_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5, 1, 3),
    _Fsp150FilteringMembers_Type()
)
fsp150FilteringMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FilteringMembers.setStatus("current")
_Fsp150FilteringTrunkMode_Type = Fsp150TMPortMap
_Fsp150FilteringTrunkMode_Object = MibTableColumn
fsp150FilteringTrunkMode = _Fsp150FilteringTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5, 1, 4),
    _Fsp150FilteringTrunkMode_Type()
)
fsp150FilteringTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FilteringTrunkMode.setStatus("current")
_Fsp150FilteringRowStatus_Type = RowStatus
_Fsp150FilteringRowStatus_Object = MibTableColumn
fsp150FilteringRowStatus = _Fsp150FilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 5, 1, 5),
    _Fsp150FilteringRowStatus_Type()
)
fsp150FilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FilteringRowStatus.setStatus("current")
_Fsp150ClassificationTable_Object = MibTable
fsp150ClassificationTable = _Fsp150ClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6)
)
if mibBuilder.loadTexts:
    fsp150ClassificationTable.setStatus("current")
_Fsp150ClassificationEntry_Object = MibTableRow
fsp150ClassificationEntry = _Fsp150ClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1)
)
fsp150ClassificationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150ClassificationPriority"),
)
if mibBuilder.loadTexts:
    fsp150ClassificationEntry.setStatus("current")


class _Fsp150ClassificationPriority_Type(Integer32):
    """Custom type fsp150ClassificationPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ClassificationPriority_Type.__name__ = "Integer32"
_Fsp150ClassificationPriority_Object = MibTableColumn
fsp150ClassificationPriority = _Fsp150ClassificationPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 1),
    _Fsp150ClassificationPriority_Type()
)
fsp150ClassificationPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150ClassificationPriority.setStatus("current")
_Fsp150ClassificationArrivalPortMask_Type = Fsp150TMPortMap
_Fsp150ClassificationArrivalPortMask_Object = MibTableColumn
fsp150ClassificationArrivalPortMask = _Fsp150ClassificationArrivalPortMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 2),
    _Fsp150ClassificationArrivalPortMask_Type()
)
fsp150ClassificationArrivalPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationArrivalPortMask.setStatus("current")
_Fsp150ClassificationInVID_Type = Fsp150VID
_Fsp150ClassificationInVID_Object = MibTableColumn
fsp150ClassificationInVID = _Fsp150ClassificationInVID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 3),
    _Fsp150ClassificationInVID_Type()
)
fsp150ClassificationInVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationInVID.setStatus("current")


class _Fsp150ClassificationInPCP_Type(Integer32):
    """Custom type fsp150ClassificationInPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ClassificationInPCP_Type.__name__ = "Integer32"
_Fsp150ClassificationInPCP_Object = MibTableColumn
fsp150ClassificationInPCP = _Fsp150ClassificationInPCP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 4),
    _Fsp150ClassificationInPCP_Type()
)
fsp150ClassificationInPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationInPCP.setStatus("current")


class _Fsp150ClassificationInDE_Type(Integer32):
    """Custom type fsp150ClassificationInDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ClassificationInDE_Type.__name__ = "Integer32"
_Fsp150ClassificationInDE_Object = MibTableColumn
fsp150ClassificationInDE = _Fsp150ClassificationInDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 5),
    _Fsp150ClassificationInDE_Type()
)
fsp150ClassificationInDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationInDE.setStatus("current")


class _Fsp150ClassificationInDSCP_Type(Integer32):
    """Custom type fsp150ClassificationInDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ClassificationInDSCP_Type.__name__ = "Integer32"
_Fsp150ClassificationInDSCP_Object = MibTableColumn
fsp150ClassificationInDSCP = _Fsp150ClassificationInDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 6),
    _Fsp150ClassificationInDSCP_Type()
)
fsp150ClassificationInDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationInDSCP.setStatus("current")
_Fsp150ClassificationOutTrafficClass_Type = Fsp150TrafficClassIndex
_Fsp150ClassificationOutTrafficClass_Object = MibTableColumn
fsp150ClassificationOutTrafficClass = _Fsp150ClassificationOutTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 7),
    _Fsp150ClassificationOutTrafficClass_Type()
)
fsp150ClassificationOutTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationOutTrafficClass.setStatus("current")
_Fsp150ClassificationOutColour_Type = Fsp150TMColour
_Fsp150ClassificationOutColour_Object = MibTableColumn
fsp150ClassificationOutColour = _Fsp150ClassificationOutColour_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 8),
    _Fsp150ClassificationOutColour_Type()
)
fsp150ClassificationOutColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationOutColour.setStatus("current")
_Fsp150ClassificationRowStatus_Type = RowStatus
_Fsp150ClassificationRowStatus_Object = MibTableColumn
fsp150ClassificationRowStatus = _Fsp150ClassificationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 6, 1, 9),
    _Fsp150ClassificationRowStatus_Type()
)
fsp150ClassificationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ClassificationRowStatus.setStatus("current")
_Fsp150ClassificationStatisticsTable_Object = MibTable
fsp150ClassificationStatisticsTable = _Fsp150ClassificationStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 7)
)
if mibBuilder.loadTexts:
    fsp150ClassificationStatisticsTable.setStatus("current")
_Fsp150ClassificationStatisticsEntry_Object = MibTableRow
fsp150ClassificationStatisticsEntry = _Fsp150ClassificationStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 7, 1)
)
fsp150ClassificationStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150ClassificationStatisticsPriority"),
)
if mibBuilder.loadTexts:
    fsp150ClassificationStatisticsEntry.setStatus("current")


class _Fsp150ClassificationStatisticsPriority_Type(Integer32):
    """Custom type fsp150ClassificationStatisticsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ClassificationStatisticsPriority_Type.__name__ = "Integer32"
_Fsp150ClassificationStatisticsPriority_Object = MibTableColumn
fsp150ClassificationStatisticsPriority = _Fsp150ClassificationStatisticsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 7, 1, 1),
    _Fsp150ClassificationStatisticsPriority_Type()
)
fsp150ClassificationStatisticsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150ClassificationStatisticsPriority.setStatus("current")
_Fsp150ClassificationStatisticsClassified_Type = Counter32
_Fsp150ClassificationStatisticsClassified_Object = MibTableColumn
fsp150ClassificationStatisticsClassified = _Fsp150ClassificationStatisticsClassified_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 7, 1, 2),
    _Fsp150ClassificationStatisticsClassified_Type()
)
fsp150ClassificationStatisticsClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150ClassificationStatisticsClassified.setStatus("current")
_Fsp150MeterAllocationTable_Object = MibTable
fsp150MeterAllocationTable = _Fsp150MeterAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 8)
)
if mibBuilder.loadTexts:
    fsp150MeterAllocationTable.setStatus("current")
_Fsp150MeterAllocationEntry_Object = MibTableRow
fsp150MeterAllocationEntry = _Fsp150MeterAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 8, 1)
)
fsp150MeterAllocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150MeterAllocationTrafficClass"),
)
if mibBuilder.loadTexts:
    fsp150MeterAllocationEntry.setStatus("current")
_Fsp150MeterAllocationTrafficClass_Type = Fsp150TrafficClassIndex
_Fsp150MeterAllocationTrafficClass_Object = MibTableColumn
fsp150MeterAllocationTrafficClass = _Fsp150MeterAllocationTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 8, 1, 1),
    _Fsp150MeterAllocationTrafficClass_Type()
)
fsp150MeterAllocationTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150MeterAllocationTrafficClass.setStatus("current")


class _Fsp150MeterAllocationMeterIndex_Type(Integer32):
    """Custom type fsp150MeterAllocationMeterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150MeterAllocationMeterIndex_Type.__name__ = "Integer32"
_Fsp150MeterAllocationMeterIndex_Object = MibTableColumn
fsp150MeterAllocationMeterIndex = _Fsp150MeterAllocationMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 8, 1, 2),
    _Fsp150MeterAllocationMeterIndex_Type()
)
fsp150MeterAllocationMeterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterAllocationMeterIndex.setStatus("current")
_Fsp150MeterAllocationRowStatus_Type = RowStatus
_Fsp150MeterAllocationRowStatus_Object = MibTableColumn
fsp150MeterAllocationRowStatus = _Fsp150MeterAllocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 8, 1, 3),
    _Fsp150MeterAllocationRowStatus_Type()
)
fsp150MeterAllocationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterAllocationRowStatus.setStatus("current")
_Fsp150MeterTable_Object = MibTable
fsp150MeterTable = _Fsp150MeterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9)
)
if mibBuilder.loadTexts:
    fsp150MeterTable.setStatus("current")
_Fsp150MeterEntry_Object = MibTableRow
fsp150MeterEntry = _Fsp150MeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1)
)
fsp150MeterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150MeterMeterIndex"),
)
if mibBuilder.loadTexts:
    fsp150MeterEntry.setStatus("current")


class _Fsp150MeterMeterIndex_Type(Integer32):
    """Custom type fsp150MeterMeterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150MeterMeterIndex_Type.__name__ = "Integer32"
_Fsp150MeterMeterIndex_Object = MibTableColumn
fsp150MeterMeterIndex = _Fsp150MeterMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 1),
    _Fsp150MeterMeterIndex_Type()
)
fsp150MeterMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150MeterMeterIndex.setStatus("current")
_Fsp150MeterCIR_Type = Unsigned32
_Fsp150MeterCIR_Object = MibTableColumn
fsp150MeterCIR = _Fsp150MeterCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 2),
    _Fsp150MeterCIR_Type()
)
fsp150MeterCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterCIR.setStatus("current")
_Fsp150MeterCBS_Type = Unsigned32
_Fsp150MeterCBS_Object = MibTableColumn
fsp150MeterCBS = _Fsp150MeterCBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 3),
    _Fsp150MeterCBS_Type()
)
fsp150MeterCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterCBS.setStatus("current")
_Fsp150MeterEIR_Type = Unsigned32
_Fsp150MeterEIR_Object = MibTableColumn
fsp150MeterEIR = _Fsp150MeterEIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 4),
    _Fsp150MeterEIR_Type()
)
fsp150MeterEIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterEIR.setStatus("current")
_Fsp150MeterEBS_Type = Unsigned32
_Fsp150MeterEBS_Object = MibTableColumn
fsp150MeterEBS = _Fsp150MeterEBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 5),
    _Fsp150MeterEBS_Type()
)
fsp150MeterEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterEBS.setStatus("current")
_Fsp150MeterCM_Type = Fsp150ColourMode
_Fsp150MeterCM_Object = MibTableColumn
fsp150MeterCM = _Fsp150MeterCM_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 6),
    _Fsp150MeterCM_Type()
)
fsp150MeterCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterCM.setStatus("current")
_Fsp150MeterCF_Type = TruthValue
_Fsp150MeterCF_Object = MibTableColumn
fsp150MeterCF = _Fsp150MeterCF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 9, 1, 7),
    _Fsp150MeterCF_Type()
)
fsp150MeterCF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150MeterCF.setStatus("current")
_Fsp150MeterStatisticsTable_Object = MibTable
fsp150MeterStatisticsTable = _Fsp150MeterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10)
)
if mibBuilder.loadTexts:
    fsp150MeterStatisticsTable.setStatus("current")
_Fsp150MeterStatisticsEntry_Object = MibTableRow
fsp150MeterStatisticsEntry = _Fsp150MeterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10, 1)
)
fsp150MeterStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150MeterStatisticsMeterIndex"),
)
if mibBuilder.loadTexts:
    fsp150MeterStatisticsEntry.setStatus("current")


class _Fsp150MeterStatisticsMeterIndex_Type(Integer32):
    """Custom type fsp150MeterStatisticsMeterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150MeterStatisticsMeterIndex_Type.__name__ = "Integer32"
_Fsp150MeterStatisticsMeterIndex_Object = MibTableColumn
fsp150MeterStatisticsMeterIndex = _Fsp150MeterStatisticsMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10, 1, 1),
    _Fsp150MeterStatisticsMeterIndex_Type()
)
fsp150MeterStatisticsMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150MeterStatisticsMeterIndex.setStatus("current")
_Fsp150MeterStatisticsUnchanged_Type = Counter32
_Fsp150MeterStatisticsUnchanged_Object = MibTableColumn
fsp150MeterStatisticsUnchanged = _Fsp150MeterStatisticsUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10, 1, 2),
    _Fsp150MeterStatisticsUnchanged_Type()
)
fsp150MeterStatisticsUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150MeterStatisticsUnchanged.setStatus("current")
_Fsp150MeterStatisticsReMarked_Type = Counter32
_Fsp150MeterStatisticsReMarked_Object = MibTableColumn
fsp150MeterStatisticsReMarked = _Fsp150MeterStatisticsReMarked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10, 1, 3),
    _Fsp150MeterStatisticsReMarked_Type()
)
fsp150MeterStatisticsReMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150MeterStatisticsReMarked.setStatus("current")
_Fsp150MeterStatisticsDropped_Type = Counter32
_Fsp150MeterStatisticsDropped_Object = MibTableColumn
fsp150MeterStatisticsDropped = _Fsp150MeterStatisticsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 10, 1, 4),
    _Fsp150MeterStatisticsDropped_Type()
)
fsp150MeterStatisticsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150MeterStatisticsDropped.setStatus("current")
_Fsp150QueueMappingTable_Object = MibTable
fsp150QueueMappingTable = _Fsp150QueueMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11)
)
if mibBuilder.loadTexts:
    fsp150QueueMappingTable.setStatus("current")
_Fsp150QueueMappingEntry_Object = MibTableRow
fsp150QueueMappingEntry = _Fsp150QueueMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11, 1)
)
fsp150QueueMappingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150QueueMappingPortNo"),
    (0, "FSP150-MIB", "fsp150QueueMappingTrafficClass"),
)
if mibBuilder.loadTexts:
    fsp150QueueMappingEntry.setStatus("current")
_Fsp150QueueMappingPortNo_Type = Fsp150TMPort
_Fsp150QueueMappingPortNo_Object = MibTableColumn
fsp150QueueMappingPortNo = _Fsp150QueueMappingPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11, 1, 1),
    _Fsp150QueueMappingPortNo_Type()
)
fsp150QueueMappingPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150QueueMappingPortNo.setStatus("current")
_Fsp150QueueMappingTrafficClass_Type = Fsp150TrafficClassIndex
_Fsp150QueueMappingTrafficClass_Object = MibTableColumn
fsp150QueueMappingTrafficClass = _Fsp150QueueMappingTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11, 1, 2),
    _Fsp150QueueMappingTrafficClass_Type()
)
fsp150QueueMappingTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150QueueMappingTrafficClass.setStatus("current")


class _Fsp150QueueMappingOutQueueIndex_Type(Integer32):
    """Custom type fsp150QueueMappingOutQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150QueueMappingOutQueueIndex_Type.__name__ = "Integer32"
_Fsp150QueueMappingOutQueueIndex_Object = MibTableColumn
fsp150QueueMappingOutQueueIndex = _Fsp150QueueMappingOutQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11, 1, 3),
    _Fsp150QueueMappingOutQueueIndex_Type()
)
fsp150QueueMappingOutQueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150QueueMappingOutQueueIndex.setStatus("current")
_Fsp150QueueMappingRowStatus_Type = RowStatus
_Fsp150QueueMappingRowStatus_Object = MibTableColumn
fsp150QueueMappingRowStatus = _Fsp150QueueMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 11, 1, 4),
    _Fsp150QueueMappingRowStatus_Type()
)
fsp150QueueMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150QueueMappingRowStatus.setStatus("current")
_Fsp150ShaperTable_Object = MibTable
fsp150ShaperTable = _Fsp150ShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12)
)
if mibBuilder.loadTexts:
    fsp150ShaperTable.setStatus("current")
_Fsp150ShaperEntry_Object = MibTableRow
fsp150ShaperEntry = _Fsp150ShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12, 1)
)
fsp150ShaperEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150ShaperPortNo"),
    (0, "FSP150-MIB", "fsp150ShaperQueueIndex"),
)
if mibBuilder.loadTexts:
    fsp150ShaperEntry.setStatus("current")
_Fsp150ShaperPortNo_Type = Fsp150TMPort
_Fsp150ShaperPortNo_Object = MibTableColumn
fsp150ShaperPortNo = _Fsp150ShaperPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12, 1, 1),
    _Fsp150ShaperPortNo_Type()
)
fsp150ShaperPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150ShaperPortNo.setStatus("current")


class _Fsp150ShaperQueueIndex_Type(Integer32):
    """Custom type fsp150ShaperQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150ShaperQueueIndex_Type.__name__ = "Integer32"
_Fsp150ShaperQueueIndex_Object = MibTableColumn
fsp150ShaperQueueIndex = _Fsp150ShaperQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12, 1, 2),
    _Fsp150ShaperQueueIndex_Type()
)
fsp150ShaperQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150ShaperQueueIndex.setStatus("current")
_Fsp150ShaperAC_Type = Unsigned32
_Fsp150ShaperAC_Object = MibTableColumn
fsp150ShaperAC = _Fsp150ShaperAC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12, 1, 3),
    _Fsp150ShaperAC_Type()
)
fsp150ShaperAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ShaperAC.setStatus("current")
_Fsp150ShaperABS_Type = Unsigned32
_Fsp150ShaperABS_Object = MibTableColumn
fsp150ShaperABS = _Fsp150ShaperABS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 12, 1, 4),
    _Fsp150ShaperABS_Type()
)
fsp150ShaperABS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150ShaperABS.setStatus("current")
_Fsp150FrameModificationTable_Object = MibTable
fsp150FrameModificationTable = _Fsp150FrameModificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13)
)
if mibBuilder.loadTexts:
    fsp150FrameModificationTable.setStatus("current")
_Fsp150FrameModificationEntry_Object = MibTableRow
fsp150FrameModificationEntry = _Fsp150FrameModificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1)
)
fsp150FrameModificationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150FrameModificationDeparturePort"),
    (0, "FSP150-MIB", "fsp150FrameModificationTrafficClass"),
)
if mibBuilder.loadTexts:
    fsp150FrameModificationEntry.setStatus("current")
_Fsp150FrameModificationDeparturePort_Type = Fsp150TMPort
_Fsp150FrameModificationDeparturePort_Object = MibTableColumn
fsp150FrameModificationDeparturePort = _Fsp150FrameModificationDeparturePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 1),
    _Fsp150FrameModificationDeparturePort_Type()
)
fsp150FrameModificationDeparturePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150FrameModificationDeparturePort.setStatus("current")
_Fsp150FrameModificationTrafficClass_Type = Fsp150TrafficClassIndex
_Fsp150FrameModificationTrafficClass_Object = MibTableColumn
fsp150FrameModificationTrafficClass = _Fsp150FrameModificationTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 2),
    _Fsp150FrameModificationTrafficClass_Type()
)
fsp150FrameModificationTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150FrameModificationTrafficClass.setStatus("current")


class _Fsp150FrameModificationOutGreenPCP_Type(Integer32):
    """Custom type fsp150FrameModificationOutGreenPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150FrameModificationOutGreenPCP_Type.__name__ = "Integer32"
_Fsp150FrameModificationOutGreenPCP_Object = MibTableColumn
fsp150FrameModificationOutGreenPCP = _Fsp150FrameModificationOutGreenPCP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 4),
    _Fsp150FrameModificationOutGreenPCP_Type()
)
fsp150FrameModificationOutGreenPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FrameModificationOutGreenPCP.setStatus("current")


class _Fsp150FrameModificationOutGreenDE_Type(Integer32):
    """Custom type fsp150FrameModificationOutGreenDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150FrameModificationOutGreenDE_Type.__name__ = "Integer32"
_Fsp150FrameModificationOutGreenDE_Object = MibTableColumn
fsp150FrameModificationOutGreenDE = _Fsp150FrameModificationOutGreenDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 5),
    _Fsp150FrameModificationOutGreenDE_Type()
)
fsp150FrameModificationOutGreenDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FrameModificationOutGreenDE.setStatus("current")


class _Fsp150FrameModificationOutYellowPCP_Type(Integer32):
    """Custom type fsp150FrameModificationOutYellowPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150FrameModificationOutYellowPCP_Type.__name__ = "Integer32"
_Fsp150FrameModificationOutYellowPCP_Object = MibTableColumn
fsp150FrameModificationOutYellowPCP = _Fsp150FrameModificationOutYellowPCP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 6),
    _Fsp150FrameModificationOutYellowPCP_Type()
)
fsp150FrameModificationOutYellowPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FrameModificationOutYellowPCP.setStatus("current")


class _Fsp150FrameModificationOutYellowDE_Type(Integer32):
    """Custom type fsp150FrameModificationOutYellowDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150FrameModificationOutYellowDE_Type.__name__ = "Integer32"
_Fsp150FrameModificationOutYellowDE_Object = MibTableColumn
fsp150FrameModificationOutYellowDE = _Fsp150FrameModificationOutYellowDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 18, 13, 1, 7),
    _Fsp150FrameModificationOutYellowDE_Type()
)
fsp150FrameModificationOutYellowDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150FrameModificationOutYellowDE.setStatus("current")
_Fsp150ConfigManagementMIB_ObjectIdentity = ObjectIdentity
fsp150ConfigManagementMIB = _Fsp150ConfigManagementMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19)
)
_Fsp150NodeTable_Object = MibTable
fsp150NodeTable = _Fsp150NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19, 1)
)
if mibBuilder.loadTexts:
    fsp150NodeTable.setStatus("current")
_Fsp150NodeEntry_Object = MibTableRow
fsp150NodeEntry = _Fsp150NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19, 1, 1)
)
fsp150NodeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150NodeEntry.setStatus("current")
_Fsp150NodeCmd_Type = Fsp150ConfigMgmtCommandType
_Fsp150NodeCmd_Object = MibTableColumn
fsp150NodeCmd = _Fsp150NodeCmd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19, 1, 1, 1),
    _Fsp150NodeCmd_Type()
)
fsp150NodeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150NodeCmd.setStatus("current")
_Fsp150NodeActStatus_Type = Fsp150ConfigMgmtFileStatusType
_Fsp150NodeActStatus_Object = MibTableColumn
fsp150NodeActStatus = _Fsp150NodeActStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19, 1, 1, 2),
    _Fsp150NodeActStatus_Type()
)
fsp150NodeActStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150NodeActStatus.setStatus("current")
_Fsp150NodeBakStatus_Type = Fsp150ConfigMgmtFileStatusType
_Fsp150NodeBakStatus_Object = MibTableColumn
fsp150NodeBakStatus = _Fsp150NodeBakStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 19, 1, 1, 3),
    _Fsp150NodeBakStatus_Type()
)
fsp150NodeBakStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150NodeBakStatus.setStatus("current")
_Fsp150NetworkPortMulticastConfigTable_Object = MibTable
fsp150NetworkPortMulticastConfigTable = _Fsp150NetworkPortMulticastConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 20)
)
if mibBuilder.loadTexts:
    fsp150NetworkPortMulticastConfigTable.setStatus("current")
_Fsp150NetworkPortMulticastConfigEntry_Object = MibTableRow
fsp150NetworkPortMulticastConfigEntry = _Fsp150NetworkPortMulticastConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 20, 1)
)
fsp150NetworkPortMulticastConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150NetworkPortMulticastConfigEntry.setStatus("current")
_Fsp150NetworkPortMulticastConfigMulticastIGMPConfig_Type = Fsp150MulticastIGMPConfig
_Fsp150NetworkPortMulticastConfigMulticastIGMPConfig_Object = MibTableColumn
fsp150NetworkPortMulticastConfigMulticastIGMPConfig = _Fsp150NetworkPortMulticastConfigMulticastIGMPConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 20, 1, 1),
    _Fsp150NetworkPortMulticastConfigMulticastIGMPConfig_Type()
)
fsp150NetworkPortMulticastConfigMulticastIGMPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150NetworkPortMulticastConfigMulticastIGMPConfig.setStatus("current")
_Fsp150AccessPortMulticastConfigTable_Object = MibTable
fsp150AccessPortMulticastConfigTable = _Fsp150AccessPortMulticastConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 21)
)
if mibBuilder.loadTexts:
    fsp150AccessPortMulticastConfigTable.setStatus("current")
_Fsp150AccessPortMulticastConfigEntry_Object = MibTableRow
fsp150AccessPortMulticastConfigEntry = _Fsp150AccessPortMulticastConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 21, 1)
)
fsp150AccessPortMulticastConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150AccessPortMulticastConfigEntry.setStatus("current")
_Fsp150AccessPortMulticastConfigMulticastEnable_Type = TruthValue
_Fsp150AccessPortMulticastConfigMulticastEnable_Object = MibTableColumn
fsp150AccessPortMulticastConfigMulticastEnable = _Fsp150AccessPortMulticastConfigMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 3, 21, 1, 1),
    _Fsp150AccessPortMulticastConfigMulticastEnable_Type()
)
fsp150AccessPortMulticastConfigMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150AccessPortMulticastConfigMulticastEnable.setStatus("current")
_Fsp150PerformanceMIB_ObjectIdentity = ObjectIdentity
fsp150PerformanceMIB = _Fsp150PerformanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4)
)
_Fsp150IfPerfTable_Object = MibTable
fsp150IfPerfTable = _Fsp150IfPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsp150IfPerfTable.setStatus("current")
_Fsp150IfPerfEntry_Object = MibTableRow
fsp150IfPerfEntry = _Fsp150IfPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1)
)
fsp150IfPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfPerfEntry.setStatus("current")
_Fsp150IfPerfOutFrames_Type = Counter32
_Fsp150IfPerfOutFrames_Object = MibTableColumn
fsp150IfPerfOutFrames = _Fsp150IfPerfOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 1),
    _Fsp150IfPerfOutFrames_Type()
)
fsp150IfPerfOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfOutFrames.setStatus("current")
_Fsp150IfPerfOutOctets_Type = Counter32
_Fsp150IfPerfOutOctets_Object = MibTableColumn
fsp150IfPerfOutOctets = _Fsp150IfPerfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 2),
    _Fsp150IfPerfOutOctets_Type()
)
fsp150IfPerfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfOutOctets.setStatus("current")
_Fsp150IfPerfSingleCollisionFrames_Type = Counter32
_Fsp150IfPerfSingleCollisionFrames_Object = MibTableColumn
fsp150IfPerfSingleCollisionFrames = _Fsp150IfPerfSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 3),
    _Fsp150IfPerfSingleCollisionFrames_Type()
)
fsp150IfPerfSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfSingleCollisionFrames.setStatus("current")
_Fsp150IfPerfMultipleCollisionFrames_Type = Counter32
_Fsp150IfPerfMultipleCollisionFrames_Object = MibTableColumn
fsp150IfPerfMultipleCollisionFrames = _Fsp150IfPerfMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 4),
    _Fsp150IfPerfMultipleCollisionFrames_Type()
)
fsp150IfPerfMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfMultipleCollisionFrames.setStatus("current")
_Fsp150IfPerfInGoodFrames_Type = Counter32
_Fsp150IfPerfInGoodFrames_Object = MibTableColumn
fsp150IfPerfInGoodFrames = _Fsp150IfPerfInGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 5),
    _Fsp150IfPerfInGoodFrames_Type()
)
fsp150IfPerfInGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfInGoodFrames.setStatus("current")
_Fsp150IfPerfInOctets_Type = Counter32
_Fsp150IfPerfInOctets_Object = MibTableColumn
fsp150IfPerfInOctets = _Fsp150IfPerfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 6),
    _Fsp150IfPerfInOctets_Type()
)
fsp150IfPerfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfInOctets.setStatus("current")
_Fsp150IfPerfAlignmentErrors_Type = Counter32
_Fsp150IfPerfAlignmentErrors_Object = MibTableColumn
fsp150IfPerfAlignmentErrors = _Fsp150IfPerfAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 7),
    _Fsp150IfPerfAlignmentErrors_Type()
)
fsp150IfPerfAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfAlignmentErrors.setStatus("deprecated")
_Fsp150IfPerfFCSErrors_Type = Counter32
_Fsp150IfPerfFCSErrors_Object = MibTableColumn
fsp150IfPerfFCSErrors = _Fsp150IfPerfFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 8),
    _Fsp150IfPerfFCSErrors_Type()
)
fsp150IfPerfFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfFCSErrors.setStatus("current")
_Fsp150IfPerfFramesTooLong_Type = Counter32
_Fsp150IfPerfFramesTooLong_Object = MibTableColumn
fsp150IfPerfFramesTooLong = _Fsp150IfPerfFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 9),
    _Fsp150IfPerfFramesTooLong_Type()
)
fsp150IfPerfFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfFramesTooLong.setStatus("current")
_Fsp150IfPerfSymbolErrors_Type = Counter32
_Fsp150IfPerfSymbolErrors_Object = MibTableColumn
fsp150IfPerfSymbolErrors = _Fsp150IfPerfSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 10),
    _Fsp150IfPerfSymbolErrors_Type()
)
fsp150IfPerfSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfSymbolErrors.setStatus("deprecated")
_Fsp150IfPerfOutTestFrames_Type = Counter32
_Fsp150IfPerfOutTestFrames_Object = MibTableColumn
fsp150IfPerfOutTestFrames = _Fsp150IfPerfOutTestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 11),
    _Fsp150IfPerfOutTestFrames_Type()
)
fsp150IfPerfOutTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfOutTestFrames.setStatus("current")
_Fsp150IfPerfInTestFrames_Type = Counter32
_Fsp150IfPerfInTestFrames_Object = MibTableColumn
fsp150IfPerfInTestFrames = _Fsp150IfPerfInTestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 12),
    _Fsp150IfPerfInTestFrames_Type()
)
fsp150IfPerfInTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfInTestFrames.setStatus("current")
_Fsp150IfPerfRFCSErrors_Type = Counter32
_Fsp150IfPerfRFCSErrors_Object = MibTableColumn
fsp150IfPerfRFCSErrors = _Fsp150IfPerfRFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 13),
    _Fsp150IfPerfRFCSErrors_Type()
)
fsp150IfPerfRFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRFCSErrors.setStatus("current")
_Fsp150IfPerfROutTestFrames_Type = Counter32
_Fsp150IfPerfROutTestFrames_Object = MibTableColumn
fsp150IfPerfROutTestFrames = _Fsp150IfPerfROutTestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 14),
    _Fsp150IfPerfROutTestFrames_Type()
)
fsp150IfPerfROutTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfROutTestFrames.setStatus("current")
_Fsp150IfPerfRInTestFrames_Type = Counter32
_Fsp150IfPerfRInTestFrames_Object = MibTableColumn
fsp150IfPerfRInTestFrames = _Fsp150IfPerfRInTestFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 15),
    _Fsp150IfPerfRInTestFrames_Type()
)
fsp150IfPerfRInTestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRInTestFrames.setStatus("current")
_Fsp150IfPerfRInGoodFrames_Type = Counter32
_Fsp150IfPerfRInGoodFrames_Object = MibTableColumn
fsp150IfPerfRInGoodFrames = _Fsp150IfPerfRInGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 16),
    _Fsp150IfPerfRInGoodFrames_Type()
)
fsp150IfPerfRInGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRInGoodFrames.setStatus("current")
_Fsp150IfPerfROutFrames_Type = Counter32
_Fsp150IfPerfROutFrames_Object = MibTableColumn
fsp150IfPerfROutFrames = _Fsp150IfPerfROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 17),
    _Fsp150IfPerfROutFrames_Type()
)
fsp150IfPerfROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfROutFrames.setStatus("current")
_Fsp150IfPerfROutOctets_Type = Counter32
_Fsp150IfPerfROutOctets_Object = MibTableColumn
fsp150IfPerfROutOctets = _Fsp150IfPerfROutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 18),
    _Fsp150IfPerfROutOctets_Type()
)
fsp150IfPerfROutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfROutOctets.setStatus("current")
_Fsp150IfPerfRInOctets_Type = Counter32
_Fsp150IfPerfRInOctets_Object = MibTableColumn
fsp150IfPerfRInOctets = _Fsp150IfPerfRInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 19),
    _Fsp150IfPerfRInOctets_Type()
)
fsp150IfPerfRInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRInOctets.setStatus("current")
_Fsp150IfPerfRFramesTooLong_Type = Counter32
_Fsp150IfPerfRFramesTooLong_Object = MibTableColumn
fsp150IfPerfRFramesTooLong = _Fsp150IfPerfRFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 20),
    _Fsp150IfPerfRFramesTooLong_Type()
)
fsp150IfPerfRFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRFramesTooLong.setStatus("current")
_Fsp150IfPerfRTestFCSErrors_Type = Counter32
_Fsp150IfPerfRTestFCSErrors_Object = MibTableColumn
fsp150IfPerfRTestFCSErrors = _Fsp150IfPerfRTestFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 21),
    _Fsp150IfPerfRTestFCSErrors_Type()
)
fsp150IfPerfRTestFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRTestFCSErrors.setStatus("current")
_Fsp150IfPerfRSingleCollisionFrames_Type = Counter32
_Fsp150IfPerfRSingleCollisionFrames_Object = MibTableColumn
fsp150IfPerfRSingleCollisionFrames = _Fsp150IfPerfRSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 22),
    _Fsp150IfPerfRSingleCollisionFrames_Type()
)
fsp150IfPerfRSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRSingleCollisionFrames.setStatus("current")
_Fsp150IfPerfRMultipleCollisionFrames_Type = Counter32
_Fsp150IfPerfRMultipleCollisionFrames_Object = MibTableColumn
fsp150IfPerfRMultipleCollisionFrames = _Fsp150IfPerfRMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 1, 1, 23),
    _Fsp150IfPerfRMultipleCollisionFrames_Type()
)
fsp150IfPerfRMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerfRMultipleCollisionFrames.setStatus("current")
_Fsp150IfOAMStatsTable_Object = MibTable
fsp150IfOAMStatsTable = _Fsp150IfOAMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fsp150IfOAMStatsTable.setStatus("current")
_Fsp150IfOAMStatsEntry_Object = MibTableRow
fsp150IfOAMStatsEntry = _Fsp150IfOAMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1)
)
fsp150IfOAMStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfOAMStatsEntry.setStatus("current")
_Fsp150IfOAMStatsPduTx_Type = Counter32
_Fsp150IfOAMStatsPduTx_Object = MibTableColumn
fsp150IfOAMStatsPduTx = _Fsp150IfOAMStatsPduTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 1),
    _Fsp150IfOAMStatsPduTx_Type()
)
fsp150IfOAMStatsPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsPduTx.setStatus("current")
_Fsp150IfOAMStatsPduRx_Type = Counter32
_Fsp150IfOAMStatsPduRx_Object = MibTableColumn
fsp150IfOAMStatsPduRx = _Fsp150IfOAMStatsPduRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 2),
    _Fsp150IfOAMStatsPduRx_Type()
)
fsp150IfOAMStatsPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsPduRx.setStatus("current")
_Fsp150IfOAMStatsInformationTx_Type = Counter32
_Fsp150IfOAMStatsInformationTx_Object = MibTableColumn
fsp150IfOAMStatsInformationTx = _Fsp150IfOAMStatsInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 3),
    _Fsp150IfOAMStatsInformationTx_Type()
)
fsp150IfOAMStatsInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsInformationTx.setStatus("current")
_Fsp150IfOAMStatsInformationRx_Type = Counter32
_Fsp150IfOAMStatsInformationRx_Object = MibTableColumn
fsp150IfOAMStatsInformationRx = _Fsp150IfOAMStatsInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 4),
    _Fsp150IfOAMStatsInformationRx_Type()
)
fsp150IfOAMStatsInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsInformationRx.setStatus("current")
_Fsp150IfOAMStatsUniqueEventNotificationTx_Type = Counter32
_Fsp150IfOAMStatsUniqueEventNotificationTx_Object = MibTableColumn
fsp150IfOAMStatsUniqueEventNotificationTx = _Fsp150IfOAMStatsUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 5),
    _Fsp150IfOAMStatsUniqueEventNotificationTx_Type()
)
fsp150IfOAMStatsUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsUniqueEventNotificationTx.setStatus("current")
_Fsp150IfOAMStatsUniqueEventNotificationRx_Type = Counter32
_Fsp150IfOAMStatsUniqueEventNotificationRx_Object = MibTableColumn
fsp150IfOAMStatsUniqueEventNotificationRx = _Fsp150IfOAMStatsUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 6),
    _Fsp150IfOAMStatsUniqueEventNotificationRx_Type()
)
fsp150IfOAMStatsUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsUniqueEventNotificationRx.setStatus("current")
_Fsp150IfOAMStatsDuplicateEventNotificationRx_Type = Counter32
_Fsp150IfOAMStatsDuplicateEventNotificationRx_Object = MibTableColumn
fsp150IfOAMStatsDuplicateEventNotificationRx = _Fsp150IfOAMStatsDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 7),
    _Fsp150IfOAMStatsDuplicateEventNotificationRx_Type()
)
fsp150IfOAMStatsDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsDuplicateEventNotificationRx.setStatus("current")
_Fsp150IfOAMStatsLoopbackControlTx_Type = Counter32
_Fsp150IfOAMStatsLoopbackControlTx_Object = MibTableColumn
fsp150IfOAMStatsLoopbackControlTx = _Fsp150IfOAMStatsLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 8),
    _Fsp150IfOAMStatsLoopbackControlTx_Type()
)
fsp150IfOAMStatsLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsLoopbackControlTx.setStatus("current")
_Fsp150IfOAMStatsLoopbackControlRx_Type = Counter32
_Fsp150IfOAMStatsLoopbackControlRx_Object = MibTableColumn
fsp150IfOAMStatsLoopbackControlRx = _Fsp150IfOAMStatsLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 9),
    _Fsp150IfOAMStatsLoopbackControlRx_Type()
)
fsp150IfOAMStatsLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsLoopbackControlRx.setStatus("current")
_Fsp150IfOAMStatsVariableRequestTx_Type = Counter32
_Fsp150IfOAMStatsVariableRequestTx_Object = MibTableColumn
fsp150IfOAMStatsVariableRequestTx = _Fsp150IfOAMStatsVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 10),
    _Fsp150IfOAMStatsVariableRequestTx_Type()
)
fsp150IfOAMStatsVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsVariableRequestTx.setStatus("current")
_Fsp150IfOAMStatsVariableRequestRx_Type = Counter32
_Fsp150IfOAMStatsVariableRequestRx_Object = MibTableColumn
fsp150IfOAMStatsVariableRequestRx = _Fsp150IfOAMStatsVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 11),
    _Fsp150IfOAMStatsVariableRequestRx_Type()
)
fsp150IfOAMStatsVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsVariableRequestRx.setStatus("current")
_Fsp150IfOAMStatsVariableResponseTx_Type = Counter32
_Fsp150IfOAMStatsVariableResponseTx_Object = MibTableColumn
fsp150IfOAMStatsVariableResponseTx = _Fsp150IfOAMStatsVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 12),
    _Fsp150IfOAMStatsVariableResponseTx_Type()
)
fsp150IfOAMStatsVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsVariableResponseTx.setStatus("current")
_Fsp150IfOAMStatsVariableResponseRx_Type = Counter32
_Fsp150IfOAMStatsVariableResponseRx_Object = MibTableColumn
fsp150IfOAMStatsVariableResponseRx = _Fsp150IfOAMStatsVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 13),
    _Fsp150IfOAMStatsVariableResponseRx_Type()
)
fsp150IfOAMStatsVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsVariableResponseRx.setStatus("current")
_Fsp150IfOAMStatsOrgSpecificTx_Type = Counter32
_Fsp150IfOAMStatsOrgSpecificTx_Object = MibTableColumn
fsp150IfOAMStatsOrgSpecificTx = _Fsp150IfOAMStatsOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 14),
    _Fsp150IfOAMStatsOrgSpecificTx_Type()
)
fsp150IfOAMStatsOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsOrgSpecificTx.setStatus("current")
_Fsp150IfOAMStatsOrgSpecificRx_Type = Counter32
_Fsp150IfOAMStatsOrgSpecificRx_Object = MibTableColumn
fsp150IfOAMStatsOrgSpecificRx = _Fsp150IfOAMStatsOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 15),
    _Fsp150IfOAMStatsOrgSpecificRx_Type()
)
fsp150IfOAMStatsOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsOrgSpecificRx.setStatus("current")
_Fsp150IfOAMStatsUnsupportedCodesRx_Type = Counter32
_Fsp150IfOAMStatsUnsupportedCodesRx_Object = MibTableColumn
fsp150IfOAMStatsUnsupportedCodesRx = _Fsp150IfOAMStatsUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 16),
    _Fsp150IfOAMStatsUnsupportedCodesRx_Type()
)
fsp150IfOAMStatsUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsUnsupportedCodesRx.setStatus("current")
_Fsp150IfOAMStatsDuplicateEventNotificationTx_Type = Counter32
_Fsp150IfOAMStatsDuplicateEventNotificationTx_Object = MibTableColumn
fsp150IfOAMStatsDuplicateEventNotificationTx = _Fsp150IfOAMStatsDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 17),
    _Fsp150IfOAMStatsDuplicateEventNotificationTx_Type()
)
fsp150IfOAMStatsDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsDuplicateEventNotificationTx.setStatus("current")
_Fsp150IfOAMStatsUnsupportedCodesTx_Type = Counter32
_Fsp150IfOAMStatsUnsupportedCodesTx_Object = MibTableColumn
fsp150IfOAMStatsUnsupportedCodesTx = _Fsp150IfOAMStatsUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 18),
    _Fsp150IfOAMStatsUnsupportedCodesTx_Type()
)
fsp150IfOAMStatsUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsUnsupportedCodesTx.setStatus("current")
_Fsp150IfOAMStatsFramesLostDueToOam_Type = Counter32
_Fsp150IfOAMStatsFramesLostDueToOam_Object = MibTableColumn
fsp150IfOAMStatsFramesLostDueToOam = _Fsp150IfOAMStatsFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 2, 1, 19),
    _Fsp150IfOAMStatsFramesLostDueToOam_Type()
)
fsp150IfOAMStatsFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfOAMStatsFramesLostDueToOam.setStatus("current")
_Fsp150SystemStatsTable_Object = MibTable
fsp150SystemStatsTable = _Fsp150SystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3)
)
if mibBuilder.loadTexts:
    fsp150SystemStatsTable.setStatus("current")
_Fsp150SystemStatsEntry_Object = MibTableRow
fsp150SystemStatsEntry = _Fsp150SystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1)
)
fsp150SystemStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150SystemStatsEntry.setStatus("current")
_Fsp150SystemStatsEgressArrivalPathChanges_Type = Counter32
_Fsp150SystemStatsEgressArrivalPathChanges_Object = MibTableColumn
fsp150SystemStatsEgressArrivalPathChanges = _Fsp150SystemStatsEgressArrivalPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 1),
    _Fsp150SystemStatsEgressArrivalPathChanges_Type()
)
fsp150SystemStatsEgressArrivalPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsEgressArrivalPathChanges.setStatus("current")
_Fsp150SystemStatsEgressBufferOverflowLow_Type = Counter64String
_Fsp150SystemStatsEgressBufferOverflowLow_Object = MibTableColumn
fsp150SystemStatsEgressBufferOverflowLow = _Fsp150SystemStatsEgressBufferOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 2),
    _Fsp150SystemStatsEgressBufferOverflowLow_Type()
)
fsp150SystemStatsEgressBufferOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsEgressBufferOverflowLow.setStatus("current")
_Fsp150SystemStatsEgressBufferOverflowMed_Type = Counter64String
_Fsp150SystemStatsEgressBufferOverflowMed_Object = MibTableColumn
fsp150SystemStatsEgressBufferOverflowMed = _Fsp150SystemStatsEgressBufferOverflowMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 3),
    _Fsp150SystemStatsEgressBufferOverflowMed_Type()
)
fsp150SystemStatsEgressBufferOverflowMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsEgressBufferOverflowMed.setStatus("current")
_Fsp150SystemStatsEgressBufferOverflowHigh_Type = Counter64String
_Fsp150SystemStatsEgressBufferOverflowHigh_Object = MibTableColumn
fsp150SystemStatsEgressBufferOverflowHigh = _Fsp150SystemStatsEgressBufferOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 4),
    _Fsp150SystemStatsEgressBufferOverflowHigh_Type()
)
fsp150SystemStatsEgressBufferOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsEgressBufferOverflowHigh.setStatus("current")
_Fsp150SystemStatsIngressBufferOverflowLow_Type = Counter64String
_Fsp150SystemStatsIngressBufferOverflowLow_Object = MibTableColumn
fsp150SystemStatsIngressBufferOverflowLow = _Fsp150SystemStatsIngressBufferOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 5),
    _Fsp150SystemStatsIngressBufferOverflowLow_Type()
)
fsp150SystemStatsIngressBufferOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsIngressBufferOverflowLow.setStatus("current")
_Fsp150SystemStatsIngressBufferOverflowMed_Type = Counter64String
_Fsp150SystemStatsIngressBufferOverflowMed_Object = MibTableColumn
fsp150SystemStatsIngressBufferOverflowMed = _Fsp150SystemStatsIngressBufferOverflowMed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 6),
    _Fsp150SystemStatsIngressBufferOverflowMed_Type()
)
fsp150SystemStatsIngressBufferOverflowMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsIngressBufferOverflowMed.setStatus("current")
_Fsp150SystemStatsIngressBufferOverflowHigh_Type = Counter64String
_Fsp150SystemStatsIngressBufferOverflowHigh_Object = MibTableColumn
fsp150SystemStatsIngressBufferOverflowHigh = _Fsp150SystemStatsIngressBufferOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 7),
    _Fsp150SystemStatsIngressBufferOverflowHigh_Type()
)
fsp150SystemStatsIngressBufferOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsIngressBufferOverflowHigh.setStatus("current")
_Fsp150SystemStatsEgressMulticastRegOverflow_Type = Counter64String
_Fsp150SystemStatsEgressMulticastRegOverflow_Object = MibTableColumn
fsp150SystemStatsEgressMulticastRegOverflow = _Fsp150SystemStatsEgressMulticastRegOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 3, 1, 8),
    _Fsp150SystemStatsEgressMulticastRegOverflow_Type()
)
fsp150SystemStatsEgressMulticastRegOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SystemStatsEgressMulticastRegOverflow.setStatus("current")
_Fsp150IfPerf64Table_Object = MibTable
fsp150IfPerf64Table = _Fsp150IfPerf64Table_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4)
)
if mibBuilder.loadTexts:
    fsp150IfPerf64Table.setStatus("current")
_Fsp150IfPerf64Entry_Object = MibTableRow
fsp150IfPerf64Entry = _Fsp150IfPerf64Entry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1)
)
fsp150IfPerf64Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsp150IfPerf64Entry.setStatus("current")
_Fsp150IfPerf64OutOctets64_Type = Counter64String
_Fsp150IfPerf64OutOctets64_Object = MibTableColumn
fsp150IfPerf64OutOctets64 = _Fsp150IfPerf64OutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 2),
    _Fsp150IfPerf64OutOctets64_Type()
)
fsp150IfPerf64OutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64OutOctets64.setStatus("current")
_Fsp150IfPerf64InOctets64_Type = Counter64String
_Fsp150IfPerf64InOctets64_Object = MibTableColumn
fsp150IfPerf64InOctets64 = _Fsp150IfPerf64InOctets64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 6),
    _Fsp150IfPerf64InOctets64_Type()
)
fsp150IfPerf64InOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64InOctets64.setStatus("current")
_Fsp150IfPerf64SymbolErrors64_Type = Counter64String
_Fsp150IfPerf64SymbolErrors64_Object = MibTableColumn
fsp150IfPerf64SymbolErrors64 = _Fsp150IfPerf64SymbolErrors64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 10),
    _Fsp150IfPerf64SymbolErrors64_Type()
)
fsp150IfPerf64SymbolErrors64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64SymbolErrors64.setStatus("deprecated")
_Fsp150IfPerf64MulticastFramesRx64_Type = Counter64String
_Fsp150IfPerf64MulticastFramesRx64_Object = MibTableColumn
fsp150IfPerf64MulticastFramesRx64 = _Fsp150IfPerf64MulticastFramesRx64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 11),
    _Fsp150IfPerf64MulticastFramesRx64_Type()
)
fsp150IfPerf64MulticastFramesRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64MulticastFramesRx64.setStatus("current")
_Fsp150IfPerf64MulticastFramesTx64_Type = Counter64String
_Fsp150IfPerf64MulticastFramesTx64_Object = MibTableColumn
fsp150IfPerf64MulticastFramesTx64 = _Fsp150IfPerf64MulticastFramesTx64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 12),
    _Fsp150IfPerf64MulticastFramesTx64_Type()
)
fsp150IfPerf64MulticastFramesTx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64MulticastFramesTx64.setStatus("current")
_Fsp150IfPerf64MulticastOctetsRx64_Type = Counter64String
_Fsp150IfPerf64MulticastOctetsRx64_Object = MibTableColumn
fsp150IfPerf64MulticastOctetsRx64 = _Fsp150IfPerf64MulticastOctetsRx64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 13),
    _Fsp150IfPerf64MulticastOctetsRx64_Type()
)
fsp150IfPerf64MulticastOctetsRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64MulticastOctetsRx64.setStatus("current")
_Fsp150IfPerf64MulticastOctetsTx64_Type = Counter64String
_Fsp150IfPerf64MulticastOctetsTx64_Object = MibTableColumn
fsp150IfPerf64MulticastOctetsTx64 = _Fsp150IfPerf64MulticastOctetsTx64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 4, 4, 1, 14),
    _Fsp150IfPerf64MulticastOctetsTx64_Type()
)
fsp150IfPerf64MulticastOctetsTx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IfPerf64MulticastOctetsTx64.setStatus("current")
_Fsp150TrapMIB_ObjectIdentity = ObjectIdentity
fsp150TrapMIB = _Fsp150TrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0)
)
_Fsp150VendorTypes_ObjectIdentity = ObjectIdentity
fsp150VendorTypes = _Fsp150VendorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6)
)
_Fsp150Chassis_ObjectIdentity = ObjectIdentity
fsp150Chassis = _Fsp150Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3)
)
_Fsp150ChassisUnknown_ObjectIdentity = ObjectIdentity
fsp150ChassisUnknown = _Fsp150ChassisUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 1)
)
_Fsp150ChassisFsp150CP10100_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150CP10100 = _Fsp150ChassisFsp150CP10100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 2)
)
_Fsp150ChassisFsp150CPGigabit_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150CPGigabit = _Fsp150ChassisFsp150CPGigabit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 3)
)
_Fsp150ChassisFsp150MO_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150MO = _Fsp150ChassisFsp150MO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 5)
)
_Fsp150ChassisFsp150ME_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150ME = _Fsp150ChassisFsp150ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 6)
)
_Fsp150ChassisFsp150CPGigabitRev2_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150CPGigabitRev2 = _Fsp150ChassisFsp150CPGigabitRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 7)
)
_Fsp150ChassisFsp150MG_ObjectIdentity = ObjectIdentity
fsp150ChassisFsp150MG = _Fsp150ChassisFsp150MG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 3, 8)
)
_Fsp150PowerSupplies_ObjectIdentity = ObjectIdentity
fsp150PowerSupplies = _Fsp150PowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 6)
)
_Fsp150PowerSupplyUnknown_ObjectIdentity = ObjectIdentity
fsp150PowerSupplyUnknown = _Fsp150PowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 6, 1)
)
_Fsp150PowerSupplyAC_ObjectIdentity = ObjectIdentity
fsp150PowerSupplyAC = _Fsp150PowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 6, 2)
)
_Fsp150PowerSupplyDC_ObjectIdentity = ObjectIdentity
fsp150PowerSupplyDC = _Fsp150PowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 6, 3)
)
_Fsp150Ports_ObjectIdentity = ObjectIdentity
fsp150Ports = _Fsp150Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10)
)
_Fsp150PortUnknown_ObjectIdentity = ObjectIdentity
fsp150PortUnknown = _Fsp150PortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 1)
)
_Fsp150PortNetwork_ObjectIdentity = ObjectIdentity
fsp150PortNetwork = _Fsp150PortNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 2200)
)
_Fsp150PortOpticalAccess_ObjectIdentity = ObjectIdentity
fsp150PortOpticalAccess = _Fsp150PortOpticalAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 2201)
)
_Fsp150PortElectricalAccess_ObjectIdentity = ObjectIdentity
fsp150PortElectricalAccess = _Fsp150PortElectricalAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 2202)
)
_Fsp150PortAccess_ObjectIdentity = ObjectIdentity
fsp150PortAccess = _Fsp150PortAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 2203)
)
_Fsp150PortElectricalNetwork_ObjectIdentity = ObjectIdentity
fsp150PortElectricalNetwork = _Fsp150PortElectricalNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 6, 10, 2204)
)
_Fsp150PidTranslation_ObjectIdentity = ObjectIdentity
fsp150PidTranslation = _Fsp150PidTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7)
)
_Fsp150PidToSvidTable_Object = MibTable
fsp150PidToSvidTable = _Fsp150PidToSvidTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 1)
)
if mibBuilder.loadTexts:
    fsp150PidToSvidTable.setStatus("current")
_Fsp150PidToSvidEntry_Object = MibTableRow
fsp150PidToSvidEntry = _Fsp150PidToSvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 1, 1)
)
fsp150PidToSvidEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150PidToSvidPid"),
)
if mibBuilder.loadTexts:
    fsp150PidToSvidEntry.setStatus("current")
_Fsp150PidToSvidPid_Type = Unsigned32
_Fsp150PidToSvidPid_Object = MibTableColumn
fsp150PidToSvidPid = _Fsp150PidToSvidPid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 1, 1, 1),
    _Fsp150PidToSvidPid_Type()
)
fsp150PidToSvidPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150PidToSvidPid.setStatus("current")


class _Fsp150PidToSvidSvid_Type(Integer32):
    """Custom type fsp150PidToSvidSvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150PidToSvidSvid_Type.__name__ = "Integer32"
_Fsp150PidToSvidSvid_Object = MibTableColumn
fsp150PidToSvidSvid = _Fsp150PidToSvidSvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 1, 1, 2),
    _Fsp150PidToSvidSvid_Type()
)
fsp150PidToSvidSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150PidToSvidSvid.setStatus("current")
_Fsp150SvidToPidTable_Object = MibTable
fsp150SvidToPidTable = _Fsp150SvidToPidTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 2)
)
if mibBuilder.loadTexts:
    fsp150SvidToPidTable.setStatus("current")
_Fsp150SvidToPidEntry_Object = MibTableRow
fsp150SvidToPidEntry = _Fsp150SvidToPidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 2, 1)
)
fsp150SvidToPidEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP150-MIB", "fsp150SvidToPidSvid"),
)
if mibBuilder.loadTexts:
    fsp150SvidToPidEntry.setStatus("current")
_Fsp150SvidToPidSvid_Type = Unsigned32
_Fsp150SvidToPidSvid_Object = MibTableColumn
fsp150SvidToPidSvid = _Fsp150SvidToPidSvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 2, 1, 1),
    _Fsp150SvidToPidSvid_Type()
)
fsp150SvidToPidSvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsp150SvidToPidSvid.setStatus("current")


class _Fsp150SvidToPidPid_Type(Integer32):
    """Custom type fsp150SvidToPidPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Fsp150SvidToPidPid_Type.__name__ = "Integer32"
_Fsp150SvidToPidPid_Object = MibTableColumn
fsp150SvidToPidPid = _Fsp150SvidToPidPid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 7, 2, 1, 2),
    _Fsp150SvidToPidPid_Type()
)
fsp150SvidToPidPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150SvidToPidPid.setStatus("current")
_Fsp150TrafficTestMIB_ObjectIdentity = ObjectIdentity
fsp150TrafficTestMIB = _Fsp150TrafficTestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8)
)
_Fsp150IngressGeneratorConfigTable_Object = MibTable
fsp150IngressGeneratorConfigTable = _Fsp150IngressGeneratorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1)
)
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigTable.setStatus("current")
_Fsp150IngressGeneratorConfigEntry_Object = MibTableRow
fsp150IngressGeneratorConfigEntry = _Fsp150IngressGeneratorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1)
)
fsp150IngressGeneratorConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigEntry.setStatus("current")
_Fsp150IngressGeneratorConfigPortIndex_Type = InterfaceIndex
_Fsp150IngressGeneratorConfigPortIndex_Object = MibTableColumn
fsp150IngressGeneratorConfigPortIndex = _Fsp150IngressGeneratorConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 1),
    _Fsp150IngressGeneratorConfigPortIndex_Type()
)
fsp150IngressGeneratorConfigPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigPortIndex.setStatus("current")


class _Fsp150IngressGeneratorConfigFrameSize_Type(Integer32):
    """Custom type fsp150IngressGeneratorConfigFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IngressGeneratorConfigFrameSize_Type.__name__ = "Integer32"
_Fsp150IngressGeneratorConfigFrameSize_Object = MibTableColumn
fsp150IngressGeneratorConfigFrameSize = _Fsp150IngressGeneratorConfigFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 2),
    _Fsp150IngressGeneratorConfigFrameSize_Type()
)
fsp150IngressGeneratorConfigFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigFrameSize.setStatus("current")
_Fsp150IngressGeneratorConfigFrameCount_Type = Unsigned32
_Fsp150IngressGeneratorConfigFrameCount_Object = MibTableColumn
fsp150IngressGeneratorConfigFrameCount = _Fsp150IngressGeneratorConfigFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 3),
    _Fsp150IngressGeneratorConfigFrameCount_Type()
)
fsp150IngressGeneratorConfigFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigFrameCount.setStatus("current")


class _Fsp150IngressGeneratorConfigSignature_Type(DisplayString):
    """Custom type fsp150IngressGeneratorConfigSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150IngressGeneratorConfigSignature_Type.__name__ = "DisplayString"
_Fsp150IngressGeneratorConfigSignature_Object = MibTableColumn
fsp150IngressGeneratorConfigSignature = _Fsp150IngressGeneratorConfigSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 4),
    _Fsp150IngressGeneratorConfigSignature_Type()
)
fsp150IngressGeneratorConfigSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigSignature.setStatus("current")
_Fsp150IngressGeneratorConfigPayload_Type = Fsp150TTPayloadType
_Fsp150IngressGeneratorConfigPayload_Object = MibTableColumn
fsp150IngressGeneratorConfigPayload = _Fsp150IngressGeneratorConfigPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 5),
    _Fsp150IngressGeneratorConfigPayload_Type()
)
fsp150IngressGeneratorConfigPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigPayload.setStatus("current")
_Fsp150IngressGeneratorConfigCir_Type = Unsigned32
_Fsp150IngressGeneratorConfigCir_Object = MibTableColumn
fsp150IngressGeneratorConfigCir = _Fsp150IngressGeneratorConfigCir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 6),
    _Fsp150IngressGeneratorConfigCir_Type()
)
fsp150IngressGeneratorConfigCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigCir.setStatus("current")
_Fsp150IngressGeneratorConfigCbs_Type = Unsigned32
_Fsp150IngressGeneratorConfigCbs_Object = MibTableColumn
fsp150IngressGeneratorConfigCbs = _Fsp150IngressGeneratorConfigCbs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 7),
    _Fsp150IngressGeneratorConfigCbs_Type()
)
fsp150IngressGeneratorConfigCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigCbs.setStatus("current")
_Fsp150IngressGeneratorConfigSVlanEnable_Type = TruthValue
_Fsp150IngressGeneratorConfigSVlanEnable_Object = MibTableColumn
fsp150IngressGeneratorConfigSVlanEnable = _Fsp150IngressGeneratorConfigSVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 8),
    _Fsp150IngressGeneratorConfigSVlanEnable_Type()
)
fsp150IngressGeneratorConfigSVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigSVlanEnable.setStatus("current")


class _Fsp150IngressGeneratorConfigSVlanVid_Type(Integer32):
    """Custom type fsp150IngressGeneratorConfigSVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IngressGeneratorConfigSVlanVid_Type.__name__ = "Integer32"
_Fsp150IngressGeneratorConfigSVlanVid_Object = MibTableColumn
fsp150IngressGeneratorConfigSVlanVid = _Fsp150IngressGeneratorConfigSVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 9),
    _Fsp150IngressGeneratorConfigSVlanVid_Type()
)
fsp150IngressGeneratorConfigSVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigSVlanVid.setStatus("current")


class _Fsp150IngressGeneratorConfigSVlanPriority_Type(Integer32):
    """Custom type fsp150IngressGeneratorConfigSVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IngressGeneratorConfigSVlanPriority_Type.__name__ = "Integer32"
_Fsp150IngressGeneratorConfigSVlanPriority_Object = MibTableColumn
fsp150IngressGeneratorConfigSVlanPriority = _Fsp150IngressGeneratorConfigSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 10),
    _Fsp150IngressGeneratorConfigSVlanPriority_Type()
)
fsp150IngressGeneratorConfigSVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigSVlanPriority.setStatus("current")
_Fsp150IngressGeneratorConfigCVlanEnable_Type = TruthValue
_Fsp150IngressGeneratorConfigCVlanEnable_Object = MibTableColumn
fsp150IngressGeneratorConfigCVlanEnable = _Fsp150IngressGeneratorConfigCVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 11),
    _Fsp150IngressGeneratorConfigCVlanEnable_Type()
)
fsp150IngressGeneratorConfigCVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigCVlanEnable.setStatus("current")


class _Fsp150IngressGeneratorConfigCVlanVid_Type(Integer32):
    """Custom type fsp150IngressGeneratorConfigCVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IngressGeneratorConfigCVlanVid_Type.__name__ = "Integer32"
_Fsp150IngressGeneratorConfigCVlanVid_Object = MibTableColumn
fsp150IngressGeneratorConfigCVlanVid = _Fsp150IngressGeneratorConfigCVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 12),
    _Fsp150IngressGeneratorConfigCVlanVid_Type()
)
fsp150IngressGeneratorConfigCVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigCVlanVid.setStatus("current")


class _Fsp150IngressGeneratorConfigCVlanPriority_Type(Integer32):
    """Custom type fsp150IngressGeneratorConfigCVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150IngressGeneratorConfigCVlanPriority_Type.__name__ = "Integer32"
_Fsp150IngressGeneratorConfigCVlanPriority_Object = MibTableColumn
fsp150IngressGeneratorConfigCVlanPriority = _Fsp150IngressGeneratorConfigCVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 13),
    _Fsp150IngressGeneratorConfigCVlanPriority_Type()
)
fsp150IngressGeneratorConfigCVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigCVlanPriority.setStatus("current")
_Fsp150IngressGeneratorConfigState_Type = Fsp150TTStateType
_Fsp150IngressGeneratorConfigState_Object = MibTableColumn
fsp150IngressGeneratorConfigState = _Fsp150IngressGeneratorConfigState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 1, 1, 14),
    _Fsp150IngressGeneratorConfigState_Type()
)
fsp150IngressGeneratorConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorConfigState.setStatus("current")
_Fsp150IngressGeneratorStatusTable_Object = MibTable
fsp150IngressGeneratorStatusTable = _Fsp150IngressGeneratorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 2)
)
if mibBuilder.loadTexts:
    fsp150IngressGeneratorStatusTable.setStatus("current")
_Fsp150IngressGeneratorStatusEntry_Object = MibTableRow
fsp150IngressGeneratorStatusEntry = _Fsp150IngressGeneratorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 2, 1)
)
fsp150IngressGeneratorStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150IngressGeneratorStatusEntry.setStatus("current")
_Fsp150IngressGeneratorStatusState_Type = Fsp150TTStateType
_Fsp150IngressGeneratorStatusState_Object = MibTableColumn
fsp150IngressGeneratorStatusState = _Fsp150IngressGeneratorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 2, 1, 1),
    _Fsp150IngressGeneratorStatusState_Type()
)
fsp150IngressGeneratorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorStatusState.setStatus("current")
_Fsp150IngressGeneratorStatusRateGenerated_Type = Unsigned32
_Fsp150IngressGeneratorStatusRateGenerated_Object = MibTableColumn
fsp150IngressGeneratorStatusRateGenerated = _Fsp150IngressGeneratorStatusRateGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 2, 1, 2),
    _Fsp150IngressGeneratorStatusRateGenerated_Type()
)
fsp150IngressGeneratorStatusRateGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorStatusRateGenerated.setStatus("current")


class _Fsp150IngressGeneratorStatusFramesGenerated_Type(OctetString):
    """Custom type fsp150IngressGeneratorStatusFramesGenerated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Fsp150IngressGeneratorStatusFramesGenerated_Type.__name__ = "OctetString"
_Fsp150IngressGeneratorStatusFramesGenerated_Object = MibTableColumn
fsp150IngressGeneratorStatusFramesGenerated = _Fsp150IngressGeneratorStatusFramesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 2, 1, 3),
    _Fsp150IngressGeneratorStatusFramesGenerated_Type()
)
fsp150IngressGeneratorStatusFramesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressGeneratorStatusFramesGenerated.setStatus("current")
_Fsp150EgressGeneratorConfigTable_Object = MibTable
fsp150EgressGeneratorConfigTable = _Fsp150EgressGeneratorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3)
)
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigTable.setStatus("current")
_Fsp150EgressGeneratorConfigEntry_Object = MibTableRow
fsp150EgressGeneratorConfigEntry = _Fsp150EgressGeneratorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1)
)
fsp150EgressGeneratorConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigEntry.setStatus("current")
_Fsp150EgressGeneratorConfigPortIndex_Type = InterfaceIndex
_Fsp150EgressGeneratorConfigPortIndex_Object = MibTableColumn
fsp150EgressGeneratorConfigPortIndex = _Fsp150EgressGeneratorConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 1),
    _Fsp150EgressGeneratorConfigPortIndex_Type()
)
fsp150EgressGeneratorConfigPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigPortIndex.setStatus("current")


class _Fsp150EgressGeneratorConfigFrameSize_Type(Integer32):
    """Custom type fsp150EgressGeneratorConfigFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150EgressGeneratorConfigFrameSize_Type.__name__ = "Integer32"
_Fsp150EgressGeneratorConfigFrameSize_Object = MibTableColumn
fsp150EgressGeneratorConfigFrameSize = _Fsp150EgressGeneratorConfigFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 2),
    _Fsp150EgressGeneratorConfigFrameSize_Type()
)
fsp150EgressGeneratorConfigFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigFrameSize.setStatus("current")
_Fsp150EgressGeneratorConfigFrameCount_Type = Unsigned32
_Fsp150EgressGeneratorConfigFrameCount_Object = MibTableColumn
fsp150EgressGeneratorConfigFrameCount = _Fsp150EgressGeneratorConfigFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 3),
    _Fsp150EgressGeneratorConfigFrameCount_Type()
)
fsp150EgressGeneratorConfigFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigFrameCount.setStatus("current")


class _Fsp150EgressGeneratorConfigSignature_Type(DisplayString):
    """Custom type fsp150EgressGeneratorConfigSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150EgressGeneratorConfigSignature_Type.__name__ = "DisplayString"
_Fsp150EgressGeneratorConfigSignature_Object = MibTableColumn
fsp150EgressGeneratorConfigSignature = _Fsp150EgressGeneratorConfigSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 4),
    _Fsp150EgressGeneratorConfigSignature_Type()
)
fsp150EgressGeneratorConfigSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigSignature.setStatus("current")
_Fsp150EgressGeneratorConfigPayload_Type = Fsp150TTPayloadType
_Fsp150EgressGeneratorConfigPayload_Object = MibTableColumn
fsp150EgressGeneratorConfigPayload = _Fsp150EgressGeneratorConfigPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 5),
    _Fsp150EgressGeneratorConfigPayload_Type()
)
fsp150EgressGeneratorConfigPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigPayload.setStatus("current")
_Fsp150EgressGeneratorConfigCir_Type = Unsigned32
_Fsp150EgressGeneratorConfigCir_Object = MibTableColumn
fsp150EgressGeneratorConfigCir = _Fsp150EgressGeneratorConfigCir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 6),
    _Fsp150EgressGeneratorConfigCir_Type()
)
fsp150EgressGeneratorConfigCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigCir.setStatus("current")
_Fsp150EgressGeneratorConfigCbs_Type = Unsigned32
_Fsp150EgressGeneratorConfigCbs_Object = MibTableColumn
fsp150EgressGeneratorConfigCbs = _Fsp150EgressGeneratorConfigCbs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 7),
    _Fsp150EgressGeneratorConfigCbs_Type()
)
fsp150EgressGeneratorConfigCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigCbs.setStatus("current")


class _Fsp150EgressGeneratorConfigSVlanVid_Type(Integer32):
    """Custom type fsp150EgressGeneratorConfigSVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150EgressGeneratorConfigSVlanVid_Type.__name__ = "Integer32"
_Fsp150EgressGeneratorConfigSVlanVid_Object = MibTableColumn
fsp150EgressGeneratorConfigSVlanVid = _Fsp150EgressGeneratorConfigSVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 8),
    _Fsp150EgressGeneratorConfigSVlanVid_Type()
)
fsp150EgressGeneratorConfigSVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigSVlanVid.setStatus("current")


class _Fsp150EgressGeneratorConfigSVlanPriority_Type(Integer32):
    """Custom type fsp150EgressGeneratorConfigSVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150EgressGeneratorConfigSVlanPriority_Type.__name__ = "Integer32"
_Fsp150EgressGeneratorConfigSVlanPriority_Object = MibTableColumn
fsp150EgressGeneratorConfigSVlanPriority = _Fsp150EgressGeneratorConfigSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 9),
    _Fsp150EgressGeneratorConfigSVlanPriority_Type()
)
fsp150EgressGeneratorConfigSVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigSVlanPriority.setStatus("current")
_Fsp150EgressGeneratorConfigCVlanEnable_Type = TruthValue
_Fsp150EgressGeneratorConfigCVlanEnable_Object = MibTableColumn
fsp150EgressGeneratorConfigCVlanEnable = _Fsp150EgressGeneratorConfigCVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 10),
    _Fsp150EgressGeneratorConfigCVlanEnable_Type()
)
fsp150EgressGeneratorConfigCVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigCVlanEnable.setStatus("current")


class _Fsp150EgressGeneratorConfigCVlanVid_Type(Integer32):
    """Custom type fsp150EgressGeneratorConfigCVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150EgressGeneratorConfigCVlanVid_Type.__name__ = "Integer32"
_Fsp150EgressGeneratorConfigCVlanVid_Object = MibTableColumn
fsp150EgressGeneratorConfigCVlanVid = _Fsp150EgressGeneratorConfigCVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 11),
    _Fsp150EgressGeneratorConfigCVlanVid_Type()
)
fsp150EgressGeneratorConfigCVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigCVlanVid.setStatus("current")


class _Fsp150EgressGeneratorConfigCVlanPriority_Type(Integer32):
    """Custom type fsp150EgressGeneratorConfigCVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsp150EgressGeneratorConfigCVlanPriority_Type.__name__ = "Integer32"
_Fsp150EgressGeneratorConfigCVlanPriority_Object = MibTableColumn
fsp150EgressGeneratorConfigCVlanPriority = _Fsp150EgressGeneratorConfigCVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 12),
    _Fsp150EgressGeneratorConfigCVlanPriority_Type()
)
fsp150EgressGeneratorConfigCVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigCVlanPriority.setStatus("current")
_Fsp150EgressGeneratorConfigState_Type = Fsp150TTStateType
_Fsp150EgressGeneratorConfigState_Object = MibTableColumn
fsp150EgressGeneratorConfigState = _Fsp150EgressGeneratorConfigState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 3, 1, 13),
    _Fsp150EgressGeneratorConfigState_Type()
)
fsp150EgressGeneratorConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorConfigState.setStatus("current")
_Fsp150EgressGeneratorStatusTable_Object = MibTable
fsp150EgressGeneratorStatusTable = _Fsp150EgressGeneratorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 4)
)
if mibBuilder.loadTexts:
    fsp150EgressGeneratorStatusTable.setStatus("current")
_Fsp150EgressGeneratorStatusEntry_Object = MibTableRow
fsp150EgressGeneratorStatusEntry = _Fsp150EgressGeneratorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 4, 1)
)
fsp150EgressGeneratorStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150EgressGeneratorStatusEntry.setStatus("current")
_Fsp150EgressGeneratorStatusState_Type = Fsp150TTStateType
_Fsp150EgressGeneratorStatusState_Object = MibTableColumn
fsp150EgressGeneratorStatusState = _Fsp150EgressGeneratorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 4, 1, 1),
    _Fsp150EgressGeneratorStatusState_Type()
)
fsp150EgressGeneratorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorStatusState.setStatus("current")
_Fsp150EgressGeneratorStatusRateGenerated_Type = Unsigned32
_Fsp150EgressGeneratorStatusRateGenerated_Object = MibTableColumn
fsp150EgressGeneratorStatusRateGenerated = _Fsp150EgressGeneratorStatusRateGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 4, 1, 2),
    _Fsp150EgressGeneratorStatusRateGenerated_Type()
)
fsp150EgressGeneratorStatusRateGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorStatusRateGenerated.setStatus("current")


class _Fsp150EgressGeneratorStatusFramesGenerated_Type(OctetString):
    """Custom type fsp150EgressGeneratorStatusFramesGenerated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Fsp150EgressGeneratorStatusFramesGenerated_Type.__name__ = "OctetString"
_Fsp150EgressGeneratorStatusFramesGenerated_Object = MibTableColumn
fsp150EgressGeneratorStatusFramesGenerated = _Fsp150EgressGeneratorStatusFramesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 4, 1, 3),
    _Fsp150EgressGeneratorStatusFramesGenerated_Type()
)
fsp150EgressGeneratorStatusFramesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressGeneratorStatusFramesGenerated.setStatus("current")
_Fsp150IngressFilterConfigTable_Object = MibTable
fsp150IngressFilterConfigTable = _Fsp150IngressFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5)
)
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigTable.setStatus("current")
_Fsp150IngressFilterConfigEntry_Object = MibTableRow
fsp150IngressFilterConfigEntry = _Fsp150IngressFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5, 1)
)
fsp150IngressFilterConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigEntry.setStatus("current")
_Fsp150IngressFilterConfigEnable_Type = TruthValue
_Fsp150IngressFilterConfigEnable_Object = MibTableColumn
fsp150IngressFilterConfigEnable = _Fsp150IngressFilterConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5, 1, 1),
    _Fsp150IngressFilterConfigEnable_Type()
)
fsp150IngressFilterConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigEnable.setStatus("current")
_Fsp150IngressFilterConfigPortIndex_Type = InterfaceIndex
_Fsp150IngressFilterConfigPortIndex_Object = MibTableColumn
fsp150IngressFilterConfigPortIndex = _Fsp150IngressFilterConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5, 1, 2),
    _Fsp150IngressFilterConfigPortIndex_Type()
)
fsp150IngressFilterConfigPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigPortIndex.setStatus("current")


class _Fsp150IngressFilterConfigSignature_Type(DisplayString):
    """Custom type fsp150IngressFilterConfigSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150IngressFilterConfigSignature_Type.__name__ = "DisplayString"
_Fsp150IngressFilterConfigSignature_Object = MibTableColumn
fsp150IngressFilterConfigSignature = _Fsp150IngressFilterConfigSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5, 1, 3),
    _Fsp150IngressFilterConfigSignature_Type()
)
fsp150IngressFilterConfigSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigSignature.setStatus("current")
_Fsp150IngressFilterConfigAction_Type = Fsp150TTActionType
_Fsp150IngressFilterConfigAction_Object = MibTableColumn
fsp150IngressFilterConfigAction = _Fsp150IngressFilterConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 5, 1, 4),
    _Fsp150IngressFilterConfigAction_Type()
)
fsp150IngressFilterConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150IngressFilterConfigAction.setStatus("current")
_Fsp150EgressFilterConfigTable_Object = MibTable
fsp150EgressFilterConfigTable = _Fsp150EgressFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6)
)
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigTable.setStatus("current")
_Fsp150EgressFilterConfigEntry_Object = MibTableRow
fsp150EgressFilterConfigEntry = _Fsp150EgressFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6, 1)
)
fsp150EgressFilterConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigEntry.setStatus("current")
_Fsp150EgressFilterConfigEnable_Type = TruthValue
_Fsp150EgressFilterConfigEnable_Object = MibTableColumn
fsp150EgressFilterConfigEnable = _Fsp150EgressFilterConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6, 1, 1),
    _Fsp150EgressFilterConfigEnable_Type()
)
fsp150EgressFilterConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigEnable.setStatus("current")
_Fsp150EgressFilterConfigPortIndex_Type = InterfaceIndex
_Fsp150EgressFilterConfigPortIndex_Object = MibTableColumn
fsp150EgressFilterConfigPortIndex = _Fsp150EgressFilterConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6, 1, 2),
    _Fsp150EgressFilterConfigPortIndex_Type()
)
fsp150EgressFilterConfigPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigPortIndex.setStatus("current")


class _Fsp150EgressFilterConfigSignature_Type(DisplayString):
    """Custom type fsp150EgressFilterConfigSignature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150EgressFilterConfigSignature_Type.__name__ = "DisplayString"
_Fsp150EgressFilterConfigSignature_Object = MibTableColumn
fsp150EgressFilterConfigSignature = _Fsp150EgressFilterConfigSignature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6, 1, 3),
    _Fsp150EgressFilterConfigSignature_Type()
)
fsp150EgressFilterConfigSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigSignature.setStatus("current")
_Fsp150EgressFilterConfigAction_Type = Fsp150TTActionType
_Fsp150EgressFilterConfigAction_Object = MibTableColumn
fsp150EgressFilterConfigAction = _Fsp150EgressFilterConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 6, 1, 4),
    _Fsp150EgressFilterConfigAction_Type()
)
fsp150EgressFilterConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150EgressFilterConfigAction.setStatus("current")
_Fsp150IngressFilterStatusTable_Object = MibTable
fsp150IngressFilterStatusTable = _Fsp150IngressFilterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7)
)
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusTable.setStatus("current")
_Fsp150IngressFilterStatusEntry_Object = MibTableRow
fsp150IngressFilterStatusEntry = _Fsp150IngressFilterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1)
)
fsp150IngressFilterStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusEntry.setStatus("current")
_Fsp150IngressFilterStatusFramesReceivedOneAccess_Type = Counter64String
_Fsp150IngressFilterStatusFramesReceivedOneAccess_Object = MibTableColumn
fsp150IngressFilterStatusFramesReceivedOneAccess = _Fsp150IngressFilterStatusFramesReceivedOneAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 1),
    _Fsp150IngressFilterStatusFramesReceivedOneAccess_Type()
)
fsp150IngressFilterStatusFramesReceivedOneAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusFramesReceivedOneAccess.setStatus("current")
_Fsp150IngressFilterStatusBytesReceivedOneAccess_Type = Counter64String
_Fsp150IngressFilterStatusBytesReceivedOneAccess_Object = MibTableColumn
fsp150IngressFilterStatusBytesReceivedOneAccess = _Fsp150IngressFilterStatusBytesReceivedOneAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 2),
    _Fsp150IngressFilterStatusBytesReceivedOneAccess_Type()
)
fsp150IngressFilterStatusBytesReceivedOneAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusBytesReceivedOneAccess.setStatus("current")
_Fsp150IngressFilterStatusFramesReceivedAllAccess_Type = Counter64String
_Fsp150IngressFilterStatusFramesReceivedAllAccess_Object = MibTableColumn
fsp150IngressFilterStatusFramesReceivedAllAccess = _Fsp150IngressFilterStatusFramesReceivedAllAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 3),
    _Fsp150IngressFilterStatusFramesReceivedAllAccess_Type()
)
fsp150IngressFilterStatusFramesReceivedAllAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusFramesReceivedAllAccess.setStatus("current")
_Fsp150IngressFilterStatusBytesReceivedAllAccess_Type = Counter64String
_Fsp150IngressFilterStatusBytesReceivedAllAccess_Object = MibTableColumn
fsp150IngressFilterStatusBytesReceivedAllAccess = _Fsp150IngressFilterStatusBytesReceivedAllAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 4),
    _Fsp150IngressFilterStatusBytesReceivedAllAccess_Type()
)
fsp150IngressFilterStatusBytesReceivedAllAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusBytesReceivedAllAccess.setStatus("current")
_Fsp150IngressFilterStatusFramesSentNetwork1_Type = Counter64String
_Fsp150IngressFilterStatusFramesSentNetwork1_Object = MibTableColumn
fsp150IngressFilterStatusFramesSentNetwork1 = _Fsp150IngressFilterStatusFramesSentNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 5),
    _Fsp150IngressFilterStatusFramesSentNetwork1_Type()
)
fsp150IngressFilterStatusFramesSentNetwork1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusFramesSentNetwork1.setStatus("current")
_Fsp150IngressFilterStatusBytesSentNetwork1_Type = Counter64String
_Fsp150IngressFilterStatusBytesSentNetwork1_Object = MibTableColumn
fsp150IngressFilterStatusBytesSentNetwork1 = _Fsp150IngressFilterStatusBytesSentNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 6),
    _Fsp150IngressFilterStatusBytesSentNetwork1_Type()
)
fsp150IngressFilterStatusBytesSentNetwork1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusBytesSentNetwork1.setStatus("current")
_Fsp150IngressFilterStatusFramesSentNetwork2_Type = Counter64String
_Fsp150IngressFilterStatusFramesSentNetwork2_Object = MibTableColumn
fsp150IngressFilterStatusFramesSentNetwork2 = _Fsp150IngressFilterStatusFramesSentNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 7),
    _Fsp150IngressFilterStatusFramesSentNetwork2_Type()
)
fsp150IngressFilterStatusFramesSentNetwork2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusFramesSentNetwork2.setStatus("current")
_Fsp150IngressFilterStatusBytesSentNetwork2_Type = Counter64String
_Fsp150IngressFilterStatusBytesSentNetwork2_Object = MibTableColumn
fsp150IngressFilterStatusBytesSentNetwork2 = _Fsp150IngressFilterStatusBytesSentNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 8),
    _Fsp150IngressFilterStatusBytesSentNetwork2_Type()
)
fsp150IngressFilterStatusBytesSentNetwork2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusBytesSentNetwork2.setStatus("current")
_Fsp150IngressFilterStatusFramesActionDropped_Type = Counter64String
_Fsp150IngressFilterStatusFramesActionDropped_Object = MibTableColumn
fsp150IngressFilterStatusFramesActionDropped = _Fsp150IngressFilterStatusFramesActionDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 9),
    _Fsp150IngressFilterStatusFramesActionDropped_Type()
)
fsp150IngressFilterStatusFramesActionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusFramesActionDropped.setStatus("current")
_Fsp150IngressFilterStatusRegulatorOverflowDropped_Type = Counter64String
_Fsp150IngressFilterStatusRegulatorOverflowDropped_Object = MibTableColumn
fsp150IngressFilterStatusRegulatorOverflowDropped = _Fsp150IngressFilterStatusRegulatorOverflowDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 10),
    _Fsp150IngressFilterStatusRegulatorOverflowDropped_Type()
)
fsp150IngressFilterStatusRegulatorOverflowDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusRegulatorOverflowDropped.setStatus("current")
_Fsp150IngressFilterStatusBufferOverflowDropped_Type = Counter64String
_Fsp150IngressFilterStatusBufferOverflowDropped_Object = MibTableColumn
fsp150IngressFilterStatusBufferOverflowDropped = _Fsp150IngressFilterStatusBufferOverflowDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 11),
    _Fsp150IngressFilterStatusBufferOverflowDropped_Type()
)
fsp150IngressFilterStatusBufferOverflowDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusBufferOverflowDropped.setStatus("current")
_Fsp150IngressFilterStatusOtherReasonDropped_Type = Counter64String
_Fsp150IngressFilterStatusOtherReasonDropped_Object = MibTableColumn
fsp150IngressFilterStatusOtherReasonDropped = _Fsp150IngressFilterStatusOtherReasonDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 7, 1, 12),
    _Fsp150IngressFilterStatusOtherReasonDropped_Type()
)
fsp150IngressFilterStatusOtherReasonDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150IngressFilterStatusOtherReasonDropped.setStatus("current")
_Fsp150EgressFilterStatusTable_Object = MibTable
fsp150EgressFilterStatusTable = _Fsp150EgressFilterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8)
)
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusTable.setStatus("current")
_Fsp150EgressFilterStatusEntry_Object = MibTableRow
fsp150EgressFilterStatusEntry = _Fsp150EgressFilterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1)
)
fsp150EgressFilterStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusEntry.setStatus("current")
_Fsp150EgressFilterStatusFramesReceivedNetwork1_Type = Counter64String
_Fsp150EgressFilterStatusFramesReceivedNetwork1_Object = MibTableColumn
fsp150EgressFilterStatusFramesReceivedNetwork1 = _Fsp150EgressFilterStatusFramesReceivedNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 1),
    _Fsp150EgressFilterStatusFramesReceivedNetwork1_Type()
)
fsp150EgressFilterStatusFramesReceivedNetwork1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusFramesReceivedNetwork1.setStatus("current")
_Fsp150EgressFilterStatusBytesReceivedNetwork1_Type = Counter64String
_Fsp150EgressFilterStatusBytesReceivedNetwork1_Object = MibTableColumn
fsp150EgressFilterStatusBytesReceivedNetwork1 = _Fsp150EgressFilterStatusBytesReceivedNetwork1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 2),
    _Fsp150EgressFilterStatusBytesReceivedNetwork1_Type()
)
fsp150EgressFilterStatusBytesReceivedNetwork1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusBytesReceivedNetwork1.setStatus("current")
_Fsp150EgressFilterStatusFramesReceivedNetwork2_Type = Counter64String
_Fsp150EgressFilterStatusFramesReceivedNetwork2_Object = MibTableColumn
fsp150EgressFilterStatusFramesReceivedNetwork2 = _Fsp150EgressFilterStatusFramesReceivedNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 3),
    _Fsp150EgressFilterStatusFramesReceivedNetwork2_Type()
)
fsp150EgressFilterStatusFramesReceivedNetwork2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusFramesReceivedNetwork2.setStatus("current")
_Fsp150EgressFilterStatusBytesReceivedNetwork2_Type = Counter64String
_Fsp150EgressFilterStatusBytesReceivedNetwork2_Object = MibTableColumn
fsp150EgressFilterStatusBytesReceivedNetwork2 = _Fsp150EgressFilterStatusBytesReceivedNetwork2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 4),
    _Fsp150EgressFilterStatusBytesReceivedNetwork2_Type()
)
fsp150EgressFilterStatusBytesReceivedNetwork2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusBytesReceivedNetwork2.setStatus("current")
_Fsp150EgressFilterStatusFramesSentOneAccess_Type = Counter64String
_Fsp150EgressFilterStatusFramesSentOneAccess_Object = MibTableColumn
fsp150EgressFilterStatusFramesSentOneAccess = _Fsp150EgressFilterStatusFramesSentOneAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 5),
    _Fsp150EgressFilterStatusFramesSentOneAccess_Type()
)
fsp150EgressFilterStatusFramesSentOneAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusFramesSentOneAccess.setStatus("current")
_Fsp150EgressFilterStatusBytesSentOneAccess_Type = Counter64String
_Fsp150EgressFilterStatusBytesSentOneAccess_Object = MibTableColumn
fsp150EgressFilterStatusBytesSentOneAccess = _Fsp150EgressFilterStatusBytesSentOneAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 6),
    _Fsp150EgressFilterStatusBytesSentOneAccess_Type()
)
fsp150EgressFilterStatusBytesSentOneAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusBytesSentOneAccess.setStatus("current")
_Fsp150EgressFilterStatusFramesSentAllAccess_Type = Counter64String
_Fsp150EgressFilterStatusFramesSentAllAccess_Object = MibTableColumn
fsp150EgressFilterStatusFramesSentAllAccess = _Fsp150EgressFilterStatusFramesSentAllAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 7),
    _Fsp150EgressFilterStatusFramesSentAllAccess_Type()
)
fsp150EgressFilterStatusFramesSentAllAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusFramesSentAllAccess.setStatus("current")
_Fsp150EgressFilterStatusBytesSentAllAccess_Type = Counter64String
_Fsp150EgressFilterStatusBytesSentAllAccess_Object = MibTableColumn
fsp150EgressFilterStatusBytesSentAllAccess = _Fsp150EgressFilterStatusBytesSentAllAccess_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 8),
    _Fsp150EgressFilterStatusBytesSentAllAccess_Type()
)
fsp150EgressFilterStatusBytesSentAllAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusBytesSentAllAccess.setStatus("current")
_Fsp150EgressFilterStatusFramesActionDropped_Type = Counter64String
_Fsp150EgressFilterStatusFramesActionDropped_Object = MibTableColumn
fsp150EgressFilterStatusFramesActionDropped = _Fsp150EgressFilterStatusFramesActionDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 9),
    _Fsp150EgressFilterStatusFramesActionDropped_Type()
)
fsp150EgressFilterStatusFramesActionDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusFramesActionDropped.setStatus("current")
_Fsp150EgressFilterStatusRegulatorOverflowDropped_Type = Counter64String
_Fsp150EgressFilterStatusRegulatorOverflowDropped_Object = MibTableColumn
fsp150EgressFilterStatusRegulatorOverflowDropped = _Fsp150EgressFilterStatusRegulatorOverflowDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 10),
    _Fsp150EgressFilterStatusRegulatorOverflowDropped_Type()
)
fsp150EgressFilterStatusRegulatorOverflowDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusRegulatorOverflowDropped.setStatus("current")
_Fsp150EgressFilterStatusBufferOverflowDropped_Type = Counter64String
_Fsp150EgressFilterStatusBufferOverflowDropped_Object = MibTableColumn
fsp150EgressFilterStatusBufferOverflowDropped = _Fsp150EgressFilterStatusBufferOverflowDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 11),
    _Fsp150EgressFilterStatusBufferOverflowDropped_Type()
)
fsp150EgressFilterStatusBufferOverflowDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusBufferOverflowDropped.setStatus("current")
_Fsp150EgressFilterStatusOtherReasonDropped_Type = Counter64String
_Fsp150EgressFilterStatusOtherReasonDropped_Object = MibTableColumn
fsp150EgressFilterStatusOtherReasonDropped = _Fsp150EgressFilterStatusOtherReasonDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 8, 8, 1, 12),
    _Fsp150EgressFilterStatusOtherReasonDropped_Type()
)
fsp150EgressFilterStatusOtherReasonDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150EgressFilterStatusOtherReasonDropped.setStatus("current")
_Fsp150UpgradeMIB_ObjectIdentity = ObjectIdentity
fsp150UpgradeMIB = _Fsp150UpgradeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9)
)
_Fsp150UpgradeFwStatusTable_Object = MibTable
fsp150UpgradeFwStatusTable = _Fsp150UpgradeFwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1)
)
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusTable.setStatus("current")
_Fsp150UpgradeFwStatusEntry_Object = MibTableRow
fsp150UpgradeFwStatusEntry = _Fsp150UpgradeFwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1, 1)
)
fsp150UpgradeFwStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusEntry.setStatus("current")
_Fsp150UpgradeFwStatusState_Type = Fsp150UpgradeState
_Fsp150UpgradeFwStatusState_Object = MibTableColumn
fsp150UpgradeFwStatusState = _Fsp150UpgradeFwStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1, 1, 1),
    _Fsp150UpgradeFwStatusState_Type()
)
fsp150UpgradeFwStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusState.setStatus("current")


class _Fsp150UpgradeFwStatusProgress_Type(Integer32):
    """Custom type fsp150UpgradeFwStatusProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_Fsp150UpgradeFwStatusProgress_Type.__name__ = "Integer32"
_Fsp150UpgradeFwStatusProgress_Object = MibTableColumn
fsp150UpgradeFwStatusProgress = _Fsp150UpgradeFwStatusProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1, 1, 2),
    _Fsp150UpgradeFwStatusProgress_Type()
)
fsp150UpgradeFwStatusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusProgress.setStatus("current")


class _Fsp150UpgradeFwStatusDetailedMsg_Type(DisplayString):
    """Custom type fsp150UpgradeFwStatusDetailedMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150UpgradeFwStatusDetailedMsg_Type.__name__ = "DisplayString"
_Fsp150UpgradeFwStatusDetailedMsg_Object = MibTableColumn
fsp150UpgradeFwStatusDetailedMsg = _Fsp150UpgradeFwStatusDetailedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1, 1, 3),
    _Fsp150UpgradeFwStatusDetailedMsg_Type()
)
fsp150UpgradeFwStatusDetailedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusDetailedMsg.setStatus("current")
_Fsp150UpgradeFwStatusProgressAvailable_Type = TruthValue
_Fsp150UpgradeFwStatusProgressAvailable_Object = MibTableColumn
fsp150UpgradeFwStatusProgressAvailable = _Fsp150UpgradeFwStatusProgressAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 1, 1, 4),
    _Fsp150UpgradeFwStatusProgressAvailable_Type()
)
fsp150UpgradeFwStatusProgressAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsp150UpgradeFwStatusProgressAvailable.setStatus("current")
_Fsp150UpgradeFwRequestTable_Object = MibTable
fsp150UpgradeFwRequestTable = _Fsp150UpgradeFwRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 2)
)
if mibBuilder.loadTexts:
    fsp150UpgradeFwRequestTable.setStatus("current")
_Fsp150UpgradeFwRequestEntry_Object = MibTableRow
fsp150UpgradeFwRequestEntry = _Fsp150UpgradeFwRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 2, 1)
)
fsp150UpgradeFwRequestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fsp150UpgradeFwRequestEntry.setStatus("current")


class _Fsp150UpgradeFwRequestUrl_Type(DisplayString):
    """Custom type fsp150UpgradeFwRequestUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsp150UpgradeFwRequestUrl_Type.__name__ = "DisplayString"
_Fsp150UpgradeFwRequestUrl_Object = MibTableColumn
fsp150UpgradeFwRequestUrl = _Fsp150UpgradeFwRequestUrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 2, 1, 1),
    _Fsp150UpgradeFwRequestUrl_Type()
)
fsp150UpgradeFwRequestUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150UpgradeFwRequestUrl.setStatus("current")
_Fsp150UpgradeFwRequestRequest_Type = Fsp150UpgradeRequestCmd
_Fsp150UpgradeFwRequestRequest_Object = MibTableColumn
fsp150UpgradeFwRequestRequest = _Fsp150UpgradeFwRequestRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 9, 2, 1, 2),
    _Fsp150UpgradeFwRequestRequest_Type()
)
fsp150UpgradeFwRequestRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsp150UpgradeFwRequestRequest.setStatus("current")

# Managed Objects groups


# Notification objects

fsp150TrapsinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 51)
)
fsp150TrapsinkChange.setObjects(
    ("ADVA-MIB", "neEventLogTimeStamp")
)
if mibBuilder.loadTexts:
    fsp150TrapsinkChange.setStatus(
        "current"
    )

fsp150NeAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 52)
)
fsp150NeAttributeValueChange.setObjects(
    ("ADVA-MIB", "neEventLogTimeStamp")
)
if mibBuilder.loadTexts:
    fsp150NeAttributeValueChange.setStatus(
        "current"
    )

fsp150TopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 53)
)
fsp150TopologyChange.setObjects(
    ("ADVA-MIB", "neEventLogTimeStamp")
)
if mibBuilder.loadTexts:
    fsp150TopologyChange.setStatus(
        "current"
    )

fsp150InterfaceAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 54)
)
fsp150InterfaceAttributeValueChange.setObjects(
      *(("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    fsp150InterfaceAttributeValueChange.setStatus(
        "current"
    )

fsp150EquipmentAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 55)
)
fsp150EquipmentAttributeValueChange.setObjects(
      *(("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    fsp150EquipmentAttributeValueChange.setStatus(
        "current"
    )

fsp150ProtectionSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 56)
)
fsp150ProtectionSwitch.setObjects(
      *(("FSP150-MIB", "fsp150ChassisStatusActiveNetwork"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    fsp150ProtectionSwitch.setStatus(
        "current"
    )

fsp150InterfaceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 57)
)
fsp150InterfaceStatusChange.setObjects(
      *(("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    fsp150InterfaceStatusChange.setStatus(
        "current"
    )

fsp150DyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 58)
)
fsp150DyingGasp.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    fsp150DyingGasp.setStatus(
        "current"
    )

fsp150TempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 100)
)
fsp150TempTooHigh.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150TempTooHigh.setStatus(
        "current"
    )

fsp150NoTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 101)
)
fsp150NoTempTooHigh.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoTempTooHigh.setStatus(
        "current"
    )

fsp150PSUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 102)
)
fsp150PSUFailure.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150PSUFailure.setStatus(
        "current"
    )

fsp150NoPSUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 103)
)
fsp150NoPSUFailure.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoPSUFailure.setStatus(
        "current"
    )

fsp150FanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 104)
)
fsp150FanFailure.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150FanFailure.setStatus(
        "current"
    )

fsp150NoFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 105)
)
fsp150NoFanFailure.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoFanFailure.setStatus(
        "current"
    )

fsp150VoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 106)
)
fsp150VoltageTooLow.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150VoltageTooLow.setStatus(
        "current"
    )

fsp150NoVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 107)
)
fsp150NoVoltageTooLow.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoVoltageTooLow.setStatus(
        "current"
    )

fsp150VoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 108)
)
fsp150VoltageTooHigh.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150VoltageTooHigh.setStatus(
        "current"
    )

fsp150NoVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 109)
)
fsp150NoVoltageTooHigh.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoVoltageTooHigh.setStatus(
        "current"
    )

fsp150LocalChassisMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 110)
)
fsp150LocalChassisMissing.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150LocalChassisMissing.setStatus(
        "current"
    )

fsp150NoLocalChassisMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 111)
)
fsp150NoLocalChassisMissing.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLocalChassisMissing.setStatus(
        "current"
    )

fsp150LocalChassisMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 112)
)
fsp150LocalChassisMismatch.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150LocalChassisMismatch.setStatus(
        "current"
    )

fsp150NoLocalChassisMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 113)
)
fsp150NoLocalChassisMismatch.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLocalChassisMismatch.setStatus(
        "current"
    )

fsp150Configuring = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 114)
)
fsp150Configuring.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150Configuring.setStatus(
        "current"
    )

fsp150NoConfiguring = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 115)
)
fsp150NoConfiguring.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoConfiguring.setStatus(
        "current"
    )

fsp150ConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 116)
)
fsp150ConfigFailed.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150ConfigFailed.setStatus(
        "current"
    )

fsp150NoConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 117)
)
fsp150NoConfigFailed.setObjects(
      *(("FSP150-MIB", "fsp150EquipmentCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150EquipmentCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoConfigFailed.setStatus(
        "current"
    )

fsp150LossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 200)
)
fsp150LossOfSignal.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150LossOfSignal.setStatus(
        "current"
    )

fsp150NoLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 201)
)
fsp150NoLossOfSignal.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLossOfSignal.setStatus(
        "current"
    )

fsp150EqMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 202)
)
fsp150EqMismatch.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150EqMismatch.setStatus(
        "current"
    )

fsp150NoEqMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 203)
)
fsp150NoEqMismatch.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoEqMismatch.setStatus(
        "current"
    )

fsp150LowOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 204)
)
fsp150LowOIP.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150LowOIP.setStatus(
        "current"
    )

fsp150NoLowOIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 205)
)
fsp150NoLowOIP.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLowOIP.setStatus(
        "current"
    )

fsp150TxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 206)
)
fsp150TxFailure.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150TxFailure.setStatus(
        "current"
    )

fsp150NoTxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 207)
)
fsp150NoTxFailure.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoTxFailure.setStatus(
        "current"
    )

fsp150LossOfLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 208)
)
fsp150LossOfLink.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150LossOfLink.setStatus(
        "current"
    )

fsp150NoLossOfLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 209)
)
fsp150NoLossOfLink.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLossOfLink.setStatus(
        "current"
    )

fsp150RemoteChassisMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 210)
)
fsp150RemoteChassisMissing.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150RemoteChassisMissing.setStatus(
        "current"
    )

fsp150NoRemoteChassisMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 211)
)
fsp150NoRemoteChassisMissing.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoRemoteChassisMissing.setStatus(
        "current"
    )

fsp150RemoteChassisMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 212)
)
fsp150RemoteChassisMismatch.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150RemoteChassisMismatch.setStatus(
        "current"
    )

fsp150NoRemoteChassisMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 213)
)
fsp150NoRemoteChassisMismatch.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoRemoteChassisMismatch.setStatus(
        "current"
    )

fsp150Loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 214)
)
fsp150Loopback.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150Loopback.setStatus(
        "current"
    )

fsp150NoLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 215)
)
fsp150NoLoopback.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoLoopback.setStatus(
        "current"
    )

fsp150SFPMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 216)
)
fsp150SFPMissing.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150SFPMissing.setStatus(
        "current"
    )

fsp150NoSFPMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 10, 2, 5, 0, 217)
)
fsp150NoSFPMissing.setObjects(
      *(("FSP150-MIB", "fsp150InterfaceCurrentAlarmSeverity"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"),
        ("FSP150-MIB", "fsp150InterfaceCurrentAlarmImpairment"))
)
if mibBuilder.loadTexts:
    fsp150NoSFPMissing.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP150-MIB",
    **{"Fsp150ProvAssignmentType": Fsp150ProvAssignmentType,
       "Fsp150ProvEquipmentType": Fsp150ProvEquipmentType,
       "Fsp150ProvRequestType": Fsp150ProvRequestType,
       "Fsp150ChassisType": Fsp150ChassisType,
       "Fsp150AlarmType": Fsp150AlarmType,
       "Fsp150ProtectionType": Fsp150ProtectionType,
       "Fsp150IngressDepartureConfig": Fsp150IngressDepartureConfig,
       "Fsp150EgressArrivalConfig": Fsp150EgressArrivalConfig,
       "Fsp150AddressFilter": Fsp150AddressFilter,
       "Fsp150PreferredNetwork": Fsp150PreferredNetwork,
       "Fsp150MulticastProtectionType": Fsp150MulticastProtectionType,
       "Fsp150NEMIModeType": Fsp150NEMIModeType,
       "Fsp150IngressDepartureStatus": Fsp150IngressDepartureStatus,
       "Fsp150EgressArrivalStatus": Fsp150EgressArrivalStatus,
       "Fsp150AdminStatusType": Fsp150AdminStatusType,
       "Fsp150TechnologyAbility": Fsp150TechnologyAbility,
       "Fsp150AutoNegStatus": Fsp150AutoNegStatus,
       "Fsp150FanStatus": Fsp150FanStatus,
       "Fsp150PSUStatus": Fsp150PSUStatus,
       "Fsp150OAMLoopbackCommandType": Fsp150OAMLoopbackCommandType,
       "Fsp150OAMLoopbackStatusType": Fsp150OAMLoopbackStatusType,
       "Fsp150AccessPortForwardMode": Fsp150AccessPortForwardMode,
       "Fsp150AccessPortTagMode": Fsp150AccessPortTagMode,
       "Fsp150PriorityType": Fsp150PriorityType,
       "Fsp150DataRates": Fsp150DataRates,
       "Fsp150TxModes": Fsp150TxModes,
       "Fsp150AutoNegSupp": Fsp150AutoNegSupp,
       "Fsp150MulticastIGMPConfig": Fsp150MulticastIGMPConfig,
       "Fsp150TMPort": Fsp150TMPort,
       "Fsp150VID": Fsp150VID,
       "Fsp150VIDctrl": Fsp150VIDctrl,
       "Fsp150VLANfilter": Fsp150VLANfilter,
       "Fsp150TMPortMap": Fsp150TMPortMap,
       "Fsp150TrafficClassIndex": Fsp150TrafficClassIndex,
       "Fsp150TMColour": Fsp150TMColour,
       "Fsp150ColourMode": Fsp150ColourMode,
       "Fsp150ConfigMgmtCommandType": Fsp150ConfigMgmtCommandType,
       "Fsp150ConfigMgmtFileStatusType": Fsp150ConfigMgmtFileStatusType,
       "Fsp150TTPayloadType": Fsp150TTPayloadType,
       "Fsp150TTStateType": Fsp150TTStateType,
       "Fsp150TTActionType": Fsp150TTActionType,
       "Fsp150UpgradeState": Fsp150UpgradeState,
       "Fsp150UpgradeRequestCmd": Fsp150UpgradeRequestCmd,
       "fsp150Products": fsp150Products,
       "fsp150CP": fsp150CP,
       "fsp150Mx": fsp150Mx,
       "fsp150MIB": fsp150MIB,
       "fsp150TopologyMIB": fsp150TopologyMIB,
       "fsp150LocalChassisTable": fsp150LocalChassisTable,
       "fsp150LocalChassisEntry": fsp150LocalChassisEntry,
       "fsp150LocalChassisProvAssignmentState": fsp150LocalChassisProvAssignmentState,
       "fsp150LocalChassisProvEquipmentState": fsp150LocalChassisProvEquipmentState,
       "fsp150LocalChassisProvRequest": fsp150LocalChassisProvRequest,
       "fsp150LocalChassisAgentAddr": fsp150LocalChassisAgentAddr,
       "fsp150LocalChassisAgentPort": fsp150LocalChassisAgentPort,
       "fsp150PortIDTranslationTable": fsp150PortIDTranslationTable,
       "fsp150PortIDTranslationEntry": fsp150PortIDTranslationEntry,
       "fsp150PortIDTranslationDevID": fsp150PortIDTranslationDevID,
       "fsp150PortIDTranslationPortNum": fsp150PortIDTranslationPortNum,
       "fsp150PortIDTranslationIndex": fsp150PortIDTranslationIndex,
       "fsp150ChassisIDTranslationTable": fsp150ChassisIDTranslationTable,
       "fsp150ChassisIDTranslationEntry": fsp150ChassisIDTranslationEntry,
       "fsp150ChassisIDTranslationDevID": fsp150ChassisIDTranslationDevID,
       "fsp150ChassisIDTranslationIndex": fsp150ChassisIDTranslationIndex,
       "fsp150TopologyTable": fsp150TopologyTable,
       "fsp150TopologyEntry": fsp150TopologyEntry,
       "fsp150TopologyProvAssignmentState": fsp150TopologyProvAssignmentState,
       "fsp150TopologyProvEquipmentState": fsp150TopologyProvEquipmentState,
       "fsp150TopologyProvRequest": fsp150TopologyProvRequest,
       "fsp150TopologyRemAgentAddr": fsp150TopologyRemAgentAddr,
       "fsp150TopologyRemAgentPort": fsp150TopologyRemAgentPort,
       "fsp150TopologyRemChassisType": fsp150TopologyRemChassisType,
       "fsp150TopologyRemDevID": fsp150TopologyRemDevID,
       "fsp150TopologyRemPortNum": fsp150TopologyRemPortNum,
       "fsp150TopologyRemChassisIndex": fsp150TopologyRemChassisIndex,
       "fsp150TopologyRemPortIndex": fsp150TopologyRemPortIndex,
       "fsp150TopologyPhysRemChassisType": fsp150TopologyPhysRemChassisType,
       "fsp150TopologyPhysRemDevID": fsp150TopologyPhysRemDevID,
       "fsp150TopologyPhysRemPortNum": fsp150TopologyPhysRemPortNum,
       "fsp150AlarmMIB": fsp150AlarmMIB,
       "fsp150AlarmFilters": fsp150AlarmFilters,
       "fsp150EquipmentAlarmReportControlTable": fsp150EquipmentAlarmReportControlTable,
       "fsp150EquipmentAlarmReportControlEntry": fsp150EquipmentAlarmReportControlEntry,
       "fsp150EquipmentAlarmReportControlState": fsp150EquipmentAlarmReportControlState,
       "fsp150InterfaceAlarmReportControlTable": fsp150InterfaceAlarmReportControlTable,
       "fsp150InterfaceAlarmReportControlEntry": fsp150InterfaceAlarmReportControlEntry,
       "fsp150InterfaceAlarmReportControlState": fsp150InterfaceAlarmReportControlState,
       "fsp150AlarmSeverityTable": fsp150AlarmSeverityTable,
       "fsp150AlarmSeverityEntry": fsp150AlarmSeverityEntry,
       "fsp150AlarmSeverityType": fsp150AlarmSeverityType,
       "fsp150AlarmSeverityValue": fsp150AlarmSeverityValue,
       "fsp150CurrentAlarms": fsp150CurrentAlarms,
       "fsp150EquipmentCurrentAlarmTable": fsp150EquipmentCurrentAlarmTable,
       "fsp150EquipmentCurrentAlarmEntry": fsp150EquipmentCurrentAlarmEntry,
       "fsp150EquipmentCurrentAlarmType": fsp150EquipmentCurrentAlarmType,
       "fsp150EquipmentCurrentAlarmSeverity": fsp150EquipmentCurrentAlarmSeverity,
       "fsp150EquipmentCurrentAlarmImpairment": fsp150EquipmentCurrentAlarmImpairment,
       "fsp150InterfaceCurrentAlarmTable": fsp150InterfaceCurrentAlarmTable,
       "fsp150InterfaceCurrentAlarmEntry": fsp150InterfaceCurrentAlarmEntry,
       "fsp150InterfaceCurrentAlarmType": fsp150InterfaceCurrentAlarmType,
       "fsp150InterfaceCurrentAlarmSeverity": fsp150InterfaceCurrentAlarmSeverity,
       "fsp150InterfaceCurrentAlarmImpairment": fsp150InterfaceCurrentAlarmImpairment,
       "fsp150AlarmDelayRaise": fsp150AlarmDelayRaise,
       "fsp150AlarmDelayClear": fsp150AlarmDelayClear,
       "fsp150ConfigAndStatus": fsp150ConfigAndStatus,
       "fsp150ChassisConfigTable": fsp150ChassisConfigTable,
       "fsp150ChassisConfigEntry": fsp150ChassisConfigEntry,
       "fsp150ChassisConfigNetAIndex": fsp150ChassisConfigNetAIndex,
       "fsp150ChassisConfigNetBIndex": fsp150ChassisConfigNetBIndex,
       "fsp150ChassisConfigProtType": fsp150ChassisConfigProtType,
       "fsp150ChassisConfigUserString1": fsp150ChassisConfigUserString1,
       "fsp150ChassisConfigUserString2": fsp150ChassisConfigUserString2,
       "fsp150ChassisConfigUserString3": fsp150ChassisConfigUserString3,
       "fsp150ChassisConfigLowVoltageThreshold": fsp150ChassisConfigLowVoltageThreshold,
       "fsp150ChassisConfigHighVoltageThreshold": fsp150ChassisConfigHighVoltageThreshold,
       "fsp150ChassisConfigHighTempThreshold": fsp150ChassisConfigHighTempThreshold,
       "fsp150ChassisConfigForwardHSRP": fsp150ChassisConfigForwardHSRP,
       "fsp150ChassisConfigForwardVRRP": fsp150ChassisConfigForwardVRRP,
       "fsp150ChassisConfigBPDUInflation": fsp150ChassisConfigBPDUInflation,
       "fsp150ChassisConfigIngressDepartureConfig": fsp150ChassisConfigIngressDepartureConfig,
       "fsp150ChassisConfigEgressArrivalConfig": fsp150ChassisConfigEgressArrivalConfig,
       "fsp150ChassisConfigLinkLossFwd": fsp150ChassisConfigLinkLossFwd,
       "fsp150ChassisConfigPointToPointMode": fsp150ChassisConfigPointToPointMode,
       "fsp150ChassisConfigTagProtocolId": fsp150ChassisConfigTagProtocolId,
       "fsp150ChassisConfigTrafficMgmtClassification": fsp150ChassisConfigTrafficMgmtClassification,
       "fsp150ChassisConfigJumboFrame": fsp150ChassisConfigJumboFrame,
       "fsp150ChassisConfigTandemMode": fsp150ChassisConfigTandemMode,
       "fsp150ChassisConfigRingId": fsp150ChassisConfigRingId,
       "fsp150ChassisConfigPauseEnable": fsp150ChassisConfigPauseEnable,
       "fsp150ChassisConfigBpduFilter": fsp150ChassisConfigBpduFilter,
       "fsp150ChassisConfigTmSupp": fsp150ChassisConfigTmSupp,
       "fsp150ChassisConfigPreferredNet": fsp150ChassisConfigPreferredNet,
       "fsp150ChassisConfigSwSyncRequest": fsp150ChassisConfigSwSyncRequest,
       "fsp150ChassisConfigMACAddressLearning": fsp150ChassisConfigMACAddressLearning,
       "fsp150ChassisConfigUnitEgressMulticastCIR": fsp150ChassisConfigUnitEgressMulticastCIR,
       "fsp150ChassisConfigUnitEgressMulticastCBS": fsp150ChassisConfigUnitEgressMulticastCBS,
       "fsp150ChassisConfigMulticastProtType": fsp150ChassisConfigMulticastProtType,
       "fsp150ChassisStatusTable": fsp150ChassisStatusTable,
       "fsp150ChassisStatusEntry": fsp150ChassisStatusEntry,
       "fsp150ChassisStatusProtState": fsp150ChassisStatusProtState,
       "fsp150ChassisStatusTemperature": fsp150ChassisStatusTemperature,
       "fsp150ChassisStatusRailVoltage": fsp150ChassisStatusRailVoltage,
       "fsp150ChassisStatusNEMIMode": fsp150ChassisStatusNEMIMode,
       "fsp150ChassisStatusActiveNetwork": fsp150ChassisStatusActiveNetwork,
       "fsp150ChassisStatusBootTimer": fsp150ChassisStatusBootTimer,
       "fsp150ChassisStatusIngressDepartureStatus": fsp150ChassisStatusIngressDepartureStatus,
       "fsp150ChassisStatusEgressArrivalStatus": fsp150ChassisStatusEgressArrivalStatus,
       "fsp150ChassisStatusPreferredNet": fsp150ChassisStatusPreferredNet,
       "fsp150ChassisStatusMulticastActiveNetwork": fsp150ChassisStatusMulticastActiveNetwork,
       "fsp150IfConfigTable": fsp150IfConfigTable,
       "fsp150IfConfigEntry": fsp150IfConfigEntry,
       "fsp150IfConfigUserString": fsp150IfConfigUserString,
       "fsp150IfConfigLinkLossFwd": fsp150IfConfigLinkLossFwd,
       "fsp150IfConfigAutoNeg": fsp150IfConfigAutoNeg,
       "fsp150IfConfigDataRate": fsp150IfConfigDataRate,
       "fsp150IfConfigAdminStatus": fsp150IfConfigAdminStatus,
       "fsp150IfConfigRingController": fsp150IfConfigRingController,
       "fsp150IfConfigDasaSwapping": fsp150IfConfigDasaSwapping,
       "fsp150IfConfigTerminalLoopback": fsp150IfConfigTerminalLoopback,
       "fsp150IfTable": fsp150IfTable,
       "fsp150IfEntry": fsp150IfEntry,
       "fsp150IfConnectorType": fsp150IfConnectorType,
       "fsp150IfLinkLossFwdActive": fsp150IfLinkLossFwdActive,
       "fsp150IfDataRate": fsp150IfDataRate,
       "fsp150OpticalIfConfigTable": fsp150OpticalIfConfigTable,
       "fsp150OpticalIfConfigEntry": fsp150OpticalIfConfigEntry,
       "fsp150OpticalIfConfigLowOIPThreshold": fsp150OpticalIfConfigLowOIPThreshold,
       "fsp150OpticalIfTable": fsp150OpticalIfTable,
       "fsp150OpticalIfEntry": fsp150OpticalIfEntry,
       "fsp150OpticalIfLinkLength9um": fsp150OpticalIfLinkLength9um,
       "fsp150OpticalIfLinkLength50um": fsp150OpticalIfLinkLength50um,
       "fsp150OpticalIfLinkLength62d5um": fsp150OpticalIfLinkLength62d5um,
       "fsp150OpticalIfLinkLengthCopper": fsp150OpticalIfLinkLengthCopper,
       "fsp150OpticalIfWavelength": fsp150OpticalIfWavelength,
       "fsp150OpticalIfStatusTable": fsp150OpticalIfStatusTable,
       "fsp150OpticalIfStatusEntry": fsp150OpticalIfStatusEntry,
       "fsp150OpticalIfStatusLaserBias": fsp150OpticalIfStatusLaserBias,
       "fsp150OpticalIfStatusTxPower": fsp150OpticalIfStatusTxPower,
       "fsp150OpticalIfStatusRxPower": fsp150OpticalIfStatusRxPower,
       "fsp150OpticalIfStatusLaserTemp": fsp150OpticalIfStatusLaserTemp,
       "fsp150ElectricalIfConfigTable": fsp150ElectricalIfConfigTable,
       "fsp150ElectricalIfConfigEntry": fsp150ElectricalIfConfigEntry,
       "fsp150ElectricalIfConfigFullDuplex": fsp150ElectricalIfConfigFullDuplex,
       "fsp150IfAutoNegConfigTable": fsp150IfAutoNegConfigTable,
       "fsp150IfAutoNegConfigEntry": fsp150IfAutoNegConfigEntry,
       "fsp150IfAutoNegConfigAdvertisedTechnologyAbility": fsp150IfAutoNegConfigAdvertisedTechnologyAbility,
       "fsp150IfAutoNegStatusTable": fsp150IfAutoNegStatusTable,
       "fsp150IfAutoNegStatusEntry": fsp150IfAutoNegStatusEntry,
       "fsp150IfAutoNegStatusRemSignallingDetected": fsp150IfAutoNegStatusRemSignallingDetected,
       "fsp150IfAutoNegStatusStatus": fsp150IfAutoNegStatusStatus,
       "fsp150IfAutoNegStatusLocalTechnologyAbility": fsp150IfAutoNegStatusLocalTechnologyAbility,
       "fsp150IfAutoNegStatusReceivedTechnologyAbility": fsp150IfAutoNegStatusReceivedTechnologyAbility,
       "fsp150FanTable": fsp150FanTable,
       "fsp150FanEntry": fsp150FanEntry,
       "fsp150FanStatus": fsp150FanStatus,
       "fsp150PSUTable": fsp150PSUTable,
       "fsp150PSUEntry": fsp150PSUEntry,
       "fsp150PSUType": fsp150PSUType,
       "fsp150PSUStatus": fsp150PSUStatus,
       "fsp150PSUVoltage": fsp150PSUVoltage,
       "fsp150IfOAMConfigTable": fsp150IfOAMConfigTable,
       "fsp150IfOAMConfigEntry": fsp150IfOAMConfigEntry,
       "fsp150IfOAMConfigOAMEnable": fsp150IfOAMConfigOAMEnable,
       "fsp150IfOAMConfigLoopbackCommand": fsp150IfOAMConfigLoopbackCommand,
       "fsp150IfOAMConfigLoopbackStatus": fsp150IfOAMConfigLoopbackStatus,
       "fsp150IfOAMConfigOAMActive": fsp150IfOAMConfigOAMActive,
       "fsp150IfOAMConfigOAMInfoEnable": fsp150IfOAMConfigOAMInfoEnable,
       "fsp150IfOAMConfigLoopbacktimer": fsp150IfOAMConfigLoopbacktimer,
       "fsp150IfOAMConfigTestTrafficEnable": fsp150IfOAMConfigTestTrafficEnable,
       "fsp150IfOAMConfigResetCounters": fsp150IfOAMConfigResetCounters,
       "fsp150IfOAMConfigDaSaSwapping": fsp150IfOAMConfigDaSaSwapping,
       "fsp150AccessIfConfigTable": fsp150AccessIfConfigTable,
       "fsp150AccessIfConfigEntry": fsp150AccessIfConfigEntry,
       "fsp150AccessIfConfigForwardMode": fsp150AccessIfConfigForwardMode,
       "fsp150AccessIfConfigTagMode": fsp150AccessIfConfigTagMode,
       "fsp150AccessIfConfigEgressCirLow": fsp150AccessIfConfigEgressCirLow,
       "fsp150AccessIfConfigEgressCbsLow": fsp150AccessIfConfigEgressCbsLow,
       "fsp150AccessIfConfigEgressCirMed": fsp150AccessIfConfigEgressCirMed,
       "fsp150AccessIfConfigEgressCbsMed": fsp150AccessIfConfigEgressCbsMed,
       "fsp150AccessIfConfigEgressCirHigh": fsp150AccessIfConfigEgressCirHigh,
       "fsp150AccessIfConfigEgressCbsHigh": fsp150AccessIfConfigEgressCbsHigh,
       "fsp150AccessIfConfigIngressCirLow": fsp150AccessIfConfigIngressCirLow,
       "fsp150AccessIfConfigIngressCbsLow": fsp150AccessIfConfigIngressCbsLow,
       "fsp150AccessIfConfigIngressCirMed": fsp150AccessIfConfigIngressCirMed,
       "fsp150AccessIfConfigIngressCbsMed": fsp150AccessIfConfigIngressCbsMed,
       "fsp150AccessIfConfigIngressCirHigh": fsp150AccessIfConfigIngressCirHigh,
       "fsp150AccessIfConfigIngressCbsHigh": fsp150AccessIfConfigIngressCbsHigh,
       "fsp150AccessIfConfigPriorityType": fsp150AccessIfConfigPriorityType,
       "fsp150AccessIfConfigPriorityValue": fsp150AccessIfConfigPriorityValue,
       "fsp150AccessIfStatusTable": fsp150AccessIfStatusTable,
       "fsp150AccessIfStatusEntry": fsp150AccessIfStatusEntry,
       "fsp150AccessIfStatusForwardMode": fsp150AccessIfStatusForwardMode,
       "fsp150AccessIfStatusEgressRegulatorOverflowLow": fsp150AccessIfStatusEgressRegulatorOverflowLow,
       "fsp150AccessIfStatusEgressRegulatorOverflowMed": fsp150AccessIfStatusEgressRegulatorOverflowMed,
       "fsp150AccessIfStatusEgressRegulatorOverflowHigh": fsp150AccessIfStatusEgressRegulatorOverflowHigh,
       "fsp150AccessIfStatusIngressRegulatorOverflowLow": fsp150AccessIfStatusIngressRegulatorOverflowLow,
       "fsp150AccessIfStatusIngressRegulatorOverflowMed": fsp150AccessIfStatusIngressRegulatorOverflowMed,
       "fsp150AccessIfStatusIngressRegulatorOverflowHigh": fsp150AccessIfStatusIngressRegulatorOverflowHigh,
       "fsp150IfCapsTable": fsp150IfCapsTable,
       "fsp150IfCapsEntry": fsp150IfCapsEntry,
       "fsp150IfCapsSuppRates": fsp150IfCapsSuppRates,
       "fsp150IfCapsSuppTxModes": fsp150IfCapsSuppTxModes,
       "fsp150IfCapsSuppAutoNeg": fsp150IfCapsSuppAutoNeg,
       "fsp150NetworkIfConfigTable": fsp150NetworkIfConfigTable,
       "fsp150NetworkIfConfigEntry": fsp150NetworkIfConfigEntry,
       "fsp150NetworkIfConfigTransmitAc": fsp150NetworkIfConfigTransmitAc,
       "fsp150NetworkIfConfigTransmitAbs": fsp150NetworkIfConfigTransmitAbs,
       "fsp150NetworkIfConfigTranslation": fsp150NetworkIfConfigTranslation,
       "fsp150TrafficManagementMIB": fsp150TrafficManagementMIB,
       "fsp150TMBaseTable": fsp150TMBaseTable,
       "fsp150TMBaseEntry": fsp150TMBaseEntry,
       "fsp150TMBaseMaxClassRules": fsp150TMBaseMaxClassRules,
       "fsp150TMBaseMaxClasses": fsp150TMBaseMaxClasses,
       "fsp150TMBaseMaxMeters": fsp150TMBaseMaxMeters,
       "fsp150TMBaseMaxQueues": fsp150TMBaseMaxQueues,
       "fsp150TMBaseLastChangeTime": fsp150TMBaseLastChangeTime,
       "fsp150TMPortTable": fsp150TMPortTable,
       "fsp150TMPortEntry": fsp150TMPortEntry,
       "fsp150TMPortPortNo": fsp150TMPortPortNo,
       "fsp150TMPortConfigTable": fsp150TMPortConfigTable,
       "fsp150TMPortConfigEntry": fsp150TMPortConfigEntry,
       "fsp150TMPortConfigPortNo": fsp150TMPortConfigPortNo,
       "fsp150TMPortConfigPVID": fsp150TMPortConfigPVID,
       "fsp150TMPortConfigPVIDctrl": fsp150TMPortConfigPVIDctrl,
       "fsp150TMPortConfigTPID": fsp150TMPortConfigTPID,
       "fsp150TMPortConfigVLANfilter": fsp150TMPortConfigVLANfilter,
       "fsp150VIDtranslationTable": fsp150VIDtranslationTable,
       "fsp150VIDtranslationEntry": fsp150VIDtranslationEntry,
       "fsp150VIDtranslationPortNo": fsp150VIDtranslationPortNo,
       "fsp150VIDtranslationInternal": fsp150VIDtranslationInternal,
       "fsp150VIDtranslationExternal": fsp150VIDtranslationExternal,
       "fsp150VIDtranslationRowStatus": fsp150VIDtranslationRowStatus,
       "fsp150FilteringTable": fsp150FilteringTable,
       "fsp150FilteringEntry": fsp150FilteringEntry,
       "fsp150FilteringVlanId": fsp150FilteringVlanId,
       "fsp150FilteringMembers": fsp150FilteringMembers,
       "fsp150FilteringTrunkMode": fsp150FilteringTrunkMode,
       "fsp150FilteringRowStatus": fsp150FilteringRowStatus,
       "fsp150ClassificationTable": fsp150ClassificationTable,
       "fsp150ClassificationEntry": fsp150ClassificationEntry,
       "fsp150ClassificationPriority": fsp150ClassificationPriority,
       "fsp150ClassificationArrivalPortMask": fsp150ClassificationArrivalPortMask,
       "fsp150ClassificationInVID": fsp150ClassificationInVID,
       "fsp150ClassificationInPCP": fsp150ClassificationInPCP,
       "fsp150ClassificationInDE": fsp150ClassificationInDE,
       "fsp150ClassificationInDSCP": fsp150ClassificationInDSCP,
       "fsp150ClassificationOutTrafficClass": fsp150ClassificationOutTrafficClass,
       "fsp150ClassificationOutColour": fsp150ClassificationOutColour,
       "fsp150ClassificationRowStatus": fsp150ClassificationRowStatus,
       "fsp150ClassificationStatisticsTable": fsp150ClassificationStatisticsTable,
       "fsp150ClassificationStatisticsEntry": fsp150ClassificationStatisticsEntry,
       "fsp150ClassificationStatisticsPriority": fsp150ClassificationStatisticsPriority,
       "fsp150ClassificationStatisticsClassified": fsp150ClassificationStatisticsClassified,
       "fsp150MeterAllocationTable": fsp150MeterAllocationTable,
       "fsp150MeterAllocationEntry": fsp150MeterAllocationEntry,
       "fsp150MeterAllocationTrafficClass": fsp150MeterAllocationTrafficClass,
       "fsp150MeterAllocationMeterIndex": fsp150MeterAllocationMeterIndex,
       "fsp150MeterAllocationRowStatus": fsp150MeterAllocationRowStatus,
       "fsp150MeterTable": fsp150MeterTable,
       "fsp150MeterEntry": fsp150MeterEntry,
       "fsp150MeterMeterIndex": fsp150MeterMeterIndex,
       "fsp150MeterCIR": fsp150MeterCIR,
       "fsp150MeterCBS": fsp150MeterCBS,
       "fsp150MeterEIR": fsp150MeterEIR,
       "fsp150MeterEBS": fsp150MeterEBS,
       "fsp150MeterCM": fsp150MeterCM,
       "fsp150MeterCF": fsp150MeterCF,
       "fsp150MeterStatisticsTable": fsp150MeterStatisticsTable,
       "fsp150MeterStatisticsEntry": fsp150MeterStatisticsEntry,
       "fsp150MeterStatisticsMeterIndex": fsp150MeterStatisticsMeterIndex,
       "fsp150MeterStatisticsUnchanged": fsp150MeterStatisticsUnchanged,
       "fsp150MeterStatisticsReMarked": fsp150MeterStatisticsReMarked,
       "fsp150MeterStatisticsDropped": fsp150MeterStatisticsDropped,
       "fsp150QueueMappingTable": fsp150QueueMappingTable,
       "fsp150QueueMappingEntry": fsp150QueueMappingEntry,
       "fsp150QueueMappingPortNo": fsp150QueueMappingPortNo,
       "fsp150QueueMappingTrafficClass": fsp150QueueMappingTrafficClass,
       "fsp150QueueMappingOutQueueIndex": fsp150QueueMappingOutQueueIndex,
       "fsp150QueueMappingRowStatus": fsp150QueueMappingRowStatus,
       "fsp150ShaperTable": fsp150ShaperTable,
       "fsp150ShaperEntry": fsp150ShaperEntry,
       "fsp150ShaperPortNo": fsp150ShaperPortNo,
       "fsp150ShaperQueueIndex": fsp150ShaperQueueIndex,
       "fsp150ShaperAC": fsp150ShaperAC,
       "fsp150ShaperABS": fsp150ShaperABS,
       "fsp150FrameModificationTable": fsp150FrameModificationTable,
       "fsp150FrameModificationEntry": fsp150FrameModificationEntry,
       "fsp150FrameModificationDeparturePort": fsp150FrameModificationDeparturePort,
       "fsp150FrameModificationTrafficClass": fsp150FrameModificationTrafficClass,
       "fsp150FrameModificationOutGreenPCP": fsp150FrameModificationOutGreenPCP,
       "fsp150FrameModificationOutGreenDE": fsp150FrameModificationOutGreenDE,
       "fsp150FrameModificationOutYellowPCP": fsp150FrameModificationOutYellowPCP,
       "fsp150FrameModificationOutYellowDE": fsp150FrameModificationOutYellowDE,
       "fsp150ConfigManagementMIB": fsp150ConfigManagementMIB,
       "fsp150NodeTable": fsp150NodeTable,
       "fsp150NodeEntry": fsp150NodeEntry,
       "fsp150NodeCmd": fsp150NodeCmd,
       "fsp150NodeActStatus": fsp150NodeActStatus,
       "fsp150NodeBakStatus": fsp150NodeBakStatus,
       "fsp150NetworkPortMulticastConfigTable": fsp150NetworkPortMulticastConfigTable,
       "fsp150NetworkPortMulticastConfigEntry": fsp150NetworkPortMulticastConfigEntry,
       "fsp150NetworkPortMulticastConfigMulticastIGMPConfig": fsp150NetworkPortMulticastConfigMulticastIGMPConfig,
       "fsp150AccessPortMulticastConfigTable": fsp150AccessPortMulticastConfigTable,
       "fsp150AccessPortMulticastConfigEntry": fsp150AccessPortMulticastConfigEntry,
       "fsp150AccessPortMulticastConfigMulticastEnable": fsp150AccessPortMulticastConfigMulticastEnable,
       "fsp150PerformanceMIB": fsp150PerformanceMIB,
       "fsp150IfPerfTable": fsp150IfPerfTable,
       "fsp150IfPerfEntry": fsp150IfPerfEntry,
       "fsp150IfPerfOutFrames": fsp150IfPerfOutFrames,
       "fsp150IfPerfOutOctets": fsp150IfPerfOutOctets,
       "fsp150IfPerfSingleCollisionFrames": fsp150IfPerfSingleCollisionFrames,
       "fsp150IfPerfMultipleCollisionFrames": fsp150IfPerfMultipleCollisionFrames,
       "fsp150IfPerfInGoodFrames": fsp150IfPerfInGoodFrames,
       "fsp150IfPerfInOctets": fsp150IfPerfInOctets,
       "fsp150IfPerfAlignmentErrors": fsp150IfPerfAlignmentErrors,
       "fsp150IfPerfFCSErrors": fsp150IfPerfFCSErrors,
       "fsp150IfPerfFramesTooLong": fsp150IfPerfFramesTooLong,
       "fsp150IfPerfSymbolErrors": fsp150IfPerfSymbolErrors,
       "fsp150IfPerfOutTestFrames": fsp150IfPerfOutTestFrames,
       "fsp150IfPerfInTestFrames": fsp150IfPerfInTestFrames,
       "fsp150IfPerfRFCSErrors": fsp150IfPerfRFCSErrors,
       "fsp150IfPerfROutTestFrames": fsp150IfPerfROutTestFrames,
       "fsp150IfPerfRInTestFrames": fsp150IfPerfRInTestFrames,
       "fsp150IfPerfRInGoodFrames": fsp150IfPerfRInGoodFrames,
       "fsp150IfPerfROutFrames": fsp150IfPerfROutFrames,
       "fsp150IfPerfROutOctets": fsp150IfPerfROutOctets,
       "fsp150IfPerfRInOctets": fsp150IfPerfRInOctets,
       "fsp150IfPerfRFramesTooLong": fsp150IfPerfRFramesTooLong,
       "fsp150IfPerfRTestFCSErrors": fsp150IfPerfRTestFCSErrors,
       "fsp150IfPerfRSingleCollisionFrames": fsp150IfPerfRSingleCollisionFrames,
       "fsp150IfPerfRMultipleCollisionFrames": fsp150IfPerfRMultipleCollisionFrames,
       "fsp150IfOAMStatsTable": fsp150IfOAMStatsTable,
       "fsp150IfOAMStatsEntry": fsp150IfOAMStatsEntry,
       "fsp150IfOAMStatsPduTx": fsp150IfOAMStatsPduTx,
       "fsp150IfOAMStatsPduRx": fsp150IfOAMStatsPduRx,
       "fsp150IfOAMStatsInformationTx": fsp150IfOAMStatsInformationTx,
       "fsp150IfOAMStatsInformationRx": fsp150IfOAMStatsInformationRx,
       "fsp150IfOAMStatsUniqueEventNotificationTx": fsp150IfOAMStatsUniqueEventNotificationTx,
       "fsp150IfOAMStatsUniqueEventNotificationRx": fsp150IfOAMStatsUniqueEventNotificationRx,
       "fsp150IfOAMStatsDuplicateEventNotificationRx": fsp150IfOAMStatsDuplicateEventNotificationRx,
       "fsp150IfOAMStatsLoopbackControlTx": fsp150IfOAMStatsLoopbackControlTx,
       "fsp150IfOAMStatsLoopbackControlRx": fsp150IfOAMStatsLoopbackControlRx,
       "fsp150IfOAMStatsVariableRequestTx": fsp150IfOAMStatsVariableRequestTx,
       "fsp150IfOAMStatsVariableRequestRx": fsp150IfOAMStatsVariableRequestRx,
       "fsp150IfOAMStatsVariableResponseTx": fsp150IfOAMStatsVariableResponseTx,
       "fsp150IfOAMStatsVariableResponseRx": fsp150IfOAMStatsVariableResponseRx,
       "fsp150IfOAMStatsOrgSpecificTx": fsp150IfOAMStatsOrgSpecificTx,
       "fsp150IfOAMStatsOrgSpecificRx": fsp150IfOAMStatsOrgSpecificRx,
       "fsp150IfOAMStatsUnsupportedCodesRx": fsp150IfOAMStatsUnsupportedCodesRx,
       "fsp150IfOAMStatsDuplicateEventNotificationTx": fsp150IfOAMStatsDuplicateEventNotificationTx,
       "fsp150IfOAMStatsUnsupportedCodesTx": fsp150IfOAMStatsUnsupportedCodesTx,
       "fsp150IfOAMStatsFramesLostDueToOam": fsp150IfOAMStatsFramesLostDueToOam,
       "fsp150SystemStatsTable": fsp150SystemStatsTable,
       "fsp150SystemStatsEntry": fsp150SystemStatsEntry,
       "fsp150SystemStatsEgressArrivalPathChanges": fsp150SystemStatsEgressArrivalPathChanges,
       "fsp150SystemStatsEgressBufferOverflowLow": fsp150SystemStatsEgressBufferOverflowLow,
       "fsp150SystemStatsEgressBufferOverflowMed": fsp150SystemStatsEgressBufferOverflowMed,
       "fsp150SystemStatsEgressBufferOverflowHigh": fsp150SystemStatsEgressBufferOverflowHigh,
       "fsp150SystemStatsIngressBufferOverflowLow": fsp150SystemStatsIngressBufferOverflowLow,
       "fsp150SystemStatsIngressBufferOverflowMed": fsp150SystemStatsIngressBufferOverflowMed,
       "fsp150SystemStatsIngressBufferOverflowHigh": fsp150SystemStatsIngressBufferOverflowHigh,
       "fsp150SystemStatsEgressMulticastRegOverflow": fsp150SystemStatsEgressMulticastRegOverflow,
       "fsp150IfPerf64Table": fsp150IfPerf64Table,
       "fsp150IfPerf64Entry": fsp150IfPerf64Entry,
       "fsp150IfPerf64OutOctets64": fsp150IfPerf64OutOctets64,
       "fsp150IfPerf64InOctets64": fsp150IfPerf64InOctets64,
       "fsp150IfPerf64SymbolErrors64": fsp150IfPerf64SymbolErrors64,
       "fsp150IfPerf64MulticastFramesRx64": fsp150IfPerf64MulticastFramesRx64,
       "fsp150IfPerf64MulticastFramesTx64": fsp150IfPerf64MulticastFramesTx64,
       "fsp150IfPerf64MulticastOctetsRx64": fsp150IfPerf64MulticastOctetsRx64,
       "fsp150IfPerf64MulticastOctetsTx64": fsp150IfPerf64MulticastOctetsTx64,
       "fsp150TrapMIB": fsp150TrapMIB,
       "fsp150TrapsinkChange": fsp150TrapsinkChange,
       "fsp150NeAttributeValueChange": fsp150NeAttributeValueChange,
       "fsp150TopologyChange": fsp150TopologyChange,
       "fsp150InterfaceAttributeValueChange": fsp150InterfaceAttributeValueChange,
       "fsp150EquipmentAttributeValueChange": fsp150EquipmentAttributeValueChange,
       "fsp150ProtectionSwitch": fsp150ProtectionSwitch,
       "fsp150InterfaceStatusChange": fsp150InterfaceStatusChange,
       "fsp150DyingGasp": fsp150DyingGasp,
       "fsp150TempTooHigh": fsp150TempTooHigh,
       "fsp150NoTempTooHigh": fsp150NoTempTooHigh,
       "fsp150PSUFailure": fsp150PSUFailure,
       "fsp150NoPSUFailure": fsp150NoPSUFailure,
       "fsp150FanFailure": fsp150FanFailure,
       "fsp150NoFanFailure": fsp150NoFanFailure,
       "fsp150VoltageTooLow": fsp150VoltageTooLow,
       "fsp150NoVoltageTooLow": fsp150NoVoltageTooLow,
       "fsp150VoltageTooHigh": fsp150VoltageTooHigh,
       "fsp150NoVoltageTooHigh": fsp150NoVoltageTooHigh,
       "fsp150LocalChassisMissing": fsp150LocalChassisMissing,
       "fsp150NoLocalChassisMissing": fsp150NoLocalChassisMissing,
       "fsp150LocalChassisMismatch": fsp150LocalChassisMismatch,
       "fsp150NoLocalChassisMismatch": fsp150NoLocalChassisMismatch,
       "fsp150Configuring": fsp150Configuring,
       "fsp150NoConfiguring": fsp150NoConfiguring,
       "fsp150ConfigFailed": fsp150ConfigFailed,
       "fsp150NoConfigFailed": fsp150NoConfigFailed,
       "fsp150LossOfSignal": fsp150LossOfSignal,
       "fsp150NoLossOfSignal": fsp150NoLossOfSignal,
       "fsp150EqMismatch": fsp150EqMismatch,
       "fsp150NoEqMismatch": fsp150NoEqMismatch,
       "fsp150LowOIP": fsp150LowOIP,
       "fsp150NoLowOIP": fsp150NoLowOIP,
       "fsp150TxFailure": fsp150TxFailure,
       "fsp150NoTxFailure": fsp150NoTxFailure,
       "fsp150LossOfLink": fsp150LossOfLink,
       "fsp150NoLossOfLink": fsp150NoLossOfLink,
       "fsp150RemoteChassisMissing": fsp150RemoteChassisMissing,
       "fsp150NoRemoteChassisMissing": fsp150NoRemoteChassisMissing,
       "fsp150RemoteChassisMismatch": fsp150RemoteChassisMismatch,
       "fsp150NoRemoteChassisMismatch": fsp150NoRemoteChassisMismatch,
       "fsp150Loopback": fsp150Loopback,
       "fsp150NoLoopback": fsp150NoLoopback,
       "fsp150SFPMissing": fsp150SFPMissing,
       "fsp150NoSFPMissing": fsp150NoSFPMissing,
       "fsp150VendorTypes": fsp150VendorTypes,
       "fsp150Chassis": fsp150Chassis,
       "fsp150ChassisUnknown": fsp150ChassisUnknown,
       "fsp150ChassisFsp150CP10100": fsp150ChassisFsp150CP10100,
       "fsp150ChassisFsp150CPGigabit": fsp150ChassisFsp150CPGigabit,
       "fsp150ChassisFsp150MO": fsp150ChassisFsp150MO,
       "fsp150ChassisFsp150ME": fsp150ChassisFsp150ME,
       "fsp150ChassisFsp150CPGigabitRev2": fsp150ChassisFsp150CPGigabitRev2,
       "fsp150ChassisFsp150MG": fsp150ChassisFsp150MG,
       "fsp150PowerSupplies": fsp150PowerSupplies,
       "fsp150PowerSupplyUnknown": fsp150PowerSupplyUnknown,
       "fsp150PowerSupplyAC": fsp150PowerSupplyAC,
       "fsp150PowerSupplyDC": fsp150PowerSupplyDC,
       "fsp150Ports": fsp150Ports,
       "fsp150PortUnknown": fsp150PortUnknown,
       "fsp150PortNetwork": fsp150PortNetwork,
       "fsp150PortOpticalAccess": fsp150PortOpticalAccess,
       "fsp150PortElectricalAccess": fsp150PortElectricalAccess,
       "fsp150PortAccess": fsp150PortAccess,
       "fsp150PortElectricalNetwork": fsp150PortElectricalNetwork,
       "fsp150PidTranslation": fsp150PidTranslation,
       "fsp150PidToSvidTable": fsp150PidToSvidTable,
       "fsp150PidToSvidEntry": fsp150PidToSvidEntry,
       "fsp150PidToSvidPid": fsp150PidToSvidPid,
       "fsp150PidToSvidSvid": fsp150PidToSvidSvid,
       "fsp150SvidToPidTable": fsp150SvidToPidTable,
       "fsp150SvidToPidEntry": fsp150SvidToPidEntry,
       "fsp150SvidToPidSvid": fsp150SvidToPidSvid,
       "fsp150SvidToPidPid": fsp150SvidToPidPid,
       "fsp150TrafficTestMIB": fsp150TrafficTestMIB,
       "fsp150IngressGeneratorConfigTable": fsp150IngressGeneratorConfigTable,
       "fsp150IngressGeneratorConfigEntry": fsp150IngressGeneratorConfigEntry,
       "fsp150IngressGeneratorConfigPortIndex": fsp150IngressGeneratorConfigPortIndex,
       "fsp150IngressGeneratorConfigFrameSize": fsp150IngressGeneratorConfigFrameSize,
       "fsp150IngressGeneratorConfigFrameCount": fsp150IngressGeneratorConfigFrameCount,
       "fsp150IngressGeneratorConfigSignature": fsp150IngressGeneratorConfigSignature,
       "fsp150IngressGeneratorConfigPayload": fsp150IngressGeneratorConfigPayload,
       "fsp150IngressGeneratorConfigCir": fsp150IngressGeneratorConfigCir,
       "fsp150IngressGeneratorConfigCbs": fsp150IngressGeneratorConfigCbs,
       "fsp150IngressGeneratorConfigSVlanEnable": fsp150IngressGeneratorConfigSVlanEnable,
       "fsp150IngressGeneratorConfigSVlanVid": fsp150IngressGeneratorConfigSVlanVid,
       "fsp150IngressGeneratorConfigSVlanPriority": fsp150IngressGeneratorConfigSVlanPriority,
       "fsp150IngressGeneratorConfigCVlanEnable": fsp150IngressGeneratorConfigCVlanEnable,
       "fsp150IngressGeneratorConfigCVlanVid": fsp150IngressGeneratorConfigCVlanVid,
       "fsp150IngressGeneratorConfigCVlanPriority": fsp150IngressGeneratorConfigCVlanPriority,
       "fsp150IngressGeneratorConfigState": fsp150IngressGeneratorConfigState,
       "fsp150IngressGeneratorStatusTable": fsp150IngressGeneratorStatusTable,
       "fsp150IngressGeneratorStatusEntry": fsp150IngressGeneratorStatusEntry,
       "fsp150IngressGeneratorStatusState": fsp150IngressGeneratorStatusState,
       "fsp150IngressGeneratorStatusRateGenerated": fsp150IngressGeneratorStatusRateGenerated,
       "fsp150IngressGeneratorStatusFramesGenerated": fsp150IngressGeneratorStatusFramesGenerated,
       "fsp150EgressGeneratorConfigTable": fsp150EgressGeneratorConfigTable,
       "fsp150EgressGeneratorConfigEntry": fsp150EgressGeneratorConfigEntry,
       "fsp150EgressGeneratorConfigPortIndex": fsp150EgressGeneratorConfigPortIndex,
       "fsp150EgressGeneratorConfigFrameSize": fsp150EgressGeneratorConfigFrameSize,
       "fsp150EgressGeneratorConfigFrameCount": fsp150EgressGeneratorConfigFrameCount,
       "fsp150EgressGeneratorConfigSignature": fsp150EgressGeneratorConfigSignature,
       "fsp150EgressGeneratorConfigPayload": fsp150EgressGeneratorConfigPayload,
       "fsp150EgressGeneratorConfigCir": fsp150EgressGeneratorConfigCir,
       "fsp150EgressGeneratorConfigCbs": fsp150EgressGeneratorConfigCbs,
       "fsp150EgressGeneratorConfigSVlanVid": fsp150EgressGeneratorConfigSVlanVid,
       "fsp150EgressGeneratorConfigSVlanPriority": fsp150EgressGeneratorConfigSVlanPriority,
       "fsp150EgressGeneratorConfigCVlanEnable": fsp150EgressGeneratorConfigCVlanEnable,
       "fsp150EgressGeneratorConfigCVlanVid": fsp150EgressGeneratorConfigCVlanVid,
       "fsp150EgressGeneratorConfigCVlanPriority": fsp150EgressGeneratorConfigCVlanPriority,
       "fsp150EgressGeneratorConfigState": fsp150EgressGeneratorConfigState,
       "fsp150EgressGeneratorStatusTable": fsp150EgressGeneratorStatusTable,
       "fsp150EgressGeneratorStatusEntry": fsp150EgressGeneratorStatusEntry,
       "fsp150EgressGeneratorStatusState": fsp150EgressGeneratorStatusState,
       "fsp150EgressGeneratorStatusRateGenerated": fsp150EgressGeneratorStatusRateGenerated,
       "fsp150EgressGeneratorStatusFramesGenerated": fsp150EgressGeneratorStatusFramesGenerated,
       "fsp150IngressFilterConfigTable": fsp150IngressFilterConfigTable,
       "fsp150IngressFilterConfigEntry": fsp150IngressFilterConfigEntry,
       "fsp150IngressFilterConfigEnable": fsp150IngressFilterConfigEnable,
       "fsp150IngressFilterConfigPortIndex": fsp150IngressFilterConfigPortIndex,
       "fsp150IngressFilterConfigSignature": fsp150IngressFilterConfigSignature,
       "fsp150IngressFilterConfigAction": fsp150IngressFilterConfigAction,
       "fsp150EgressFilterConfigTable": fsp150EgressFilterConfigTable,
       "fsp150EgressFilterConfigEntry": fsp150EgressFilterConfigEntry,
       "fsp150EgressFilterConfigEnable": fsp150EgressFilterConfigEnable,
       "fsp150EgressFilterConfigPortIndex": fsp150EgressFilterConfigPortIndex,
       "fsp150EgressFilterConfigSignature": fsp150EgressFilterConfigSignature,
       "fsp150EgressFilterConfigAction": fsp150EgressFilterConfigAction,
       "fsp150IngressFilterStatusTable": fsp150IngressFilterStatusTable,
       "fsp150IngressFilterStatusEntry": fsp150IngressFilterStatusEntry,
       "fsp150IngressFilterStatusFramesReceivedOneAccess": fsp150IngressFilterStatusFramesReceivedOneAccess,
       "fsp150IngressFilterStatusBytesReceivedOneAccess": fsp150IngressFilterStatusBytesReceivedOneAccess,
       "fsp150IngressFilterStatusFramesReceivedAllAccess": fsp150IngressFilterStatusFramesReceivedAllAccess,
       "fsp150IngressFilterStatusBytesReceivedAllAccess": fsp150IngressFilterStatusBytesReceivedAllAccess,
       "fsp150IngressFilterStatusFramesSentNetwork1": fsp150IngressFilterStatusFramesSentNetwork1,
       "fsp150IngressFilterStatusBytesSentNetwork1": fsp150IngressFilterStatusBytesSentNetwork1,
       "fsp150IngressFilterStatusFramesSentNetwork2": fsp150IngressFilterStatusFramesSentNetwork2,
       "fsp150IngressFilterStatusBytesSentNetwork2": fsp150IngressFilterStatusBytesSentNetwork2,
       "fsp150IngressFilterStatusFramesActionDropped": fsp150IngressFilterStatusFramesActionDropped,
       "fsp150IngressFilterStatusRegulatorOverflowDropped": fsp150IngressFilterStatusRegulatorOverflowDropped,
       "fsp150IngressFilterStatusBufferOverflowDropped": fsp150IngressFilterStatusBufferOverflowDropped,
       "fsp150IngressFilterStatusOtherReasonDropped": fsp150IngressFilterStatusOtherReasonDropped,
       "fsp150EgressFilterStatusTable": fsp150EgressFilterStatusTable,
       "fsp150EgressFilterStatusEntry": fsp150EgressFilterStatusEntry,
       "fsp150EgressFilterStatusFramesReceivedNetwork1": fsp150EgressFilterStatusFramesReceivedNetwork1,
       "fsp150EgressFilterStatusBytesReceivedNetwork1": fsp150EgressFilterStatusBytesReceivedNetwork1,
       "fsp150EgressFilterStatusFramesReceivedNetwork2": fsp150EgressFilterStatusFramesReceivedNetwork2,
       "fsp150EgressFilterStatusBytesReceivedNetwork2": fsp150EgressFilterStatusBytesReceivedNetwork2,
       "fsp150EgressFilterStatusFramesSentOneAccess": fsp150EgressFilterStatusFramesSentOneAccess,
       "fsp150EgressFilterStatusBytesSentOneAccess": fsp150EgressFilterStatusBytesSentOneAccess,
       "fsp150EgressFilterStatusFramesSentAllAccess": fsp150EgressFilterStatusFramesSentAllAccess,
       "fsp150EgressFilterStatusBytesSentAllAccess": fsp150EgressFilterStatusBytesSentAllAccess,
       "fsp150EgressFilterStatusFramesActionDropped": fsp150EgressFilterStatusFramesActionDropped,
       "fsp150EgressFilterStatusRegulatorOverflowDropped": fsp150EgressFilterStatusRegulatorOverflowDropped,
       "fsp150EgressFilterStatusBufferOverflowDropped": fsp150EgressFilterStatusBufferOverflowDropped,
       "fsp150EgressFilterStatusOtherReasonDropped": fsp150EgressFilterStatusOtherReasonDropped,
       "fsp150UpgradeMIB": fsp150UpgradeMIB,
       "fsp150UpgradeFwStatusTable": fsp150UpgradeFwStatusTable,
       "fsp150UpgradeFwStatusEntry": fsp150UpgradeFwStatusEntry,
       "fsp150UpgradeFwStatusState": fsp150UpgradeFwStatusState,
       "fsp150UpgradeFwStatusProgress": fsp150UpgradeFwStatusProgress,
       "fsp150UpgradeFwStatusDetailedMsg": fsp150UpgradeFwStatusDetailedMsg,
       "fsp150UpgradeFwStatusProgressAvailable": fsp150UpgradeFwStatusProgressAvailable,
       "fsp150UpgradeFwRequestTable": fsp150UpgradeFwRequestTable,
       "fsp150UpgradeFwRequestEntry": fsp150UpgradeFwRequestEntry,
       "fsp150UpgradeFwRequestUrl": fsp150UpgradeFwRequestUrl,
       "fsp150UpgradeFwRequestRequest": fsp150UpgradeFwRequestRequest}
)
