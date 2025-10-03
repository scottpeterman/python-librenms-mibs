# SNMP MIB module (F3-JDSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-JDSU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:15 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 OperationalState,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "OperationalState",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetTrafficPortEntry,
 cmEthernetTrafficPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetTrafficPortEntry",
    "cmEthernetTrafficPortIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3JdsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31)
)
if mibBuilder.loadTexts:
    f3JdsuMIB.setRevisions(
        ("2014-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GeneratorStatus(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("initial", 2),
          ("helloIngress", 3),
          ("helloCompleted", 4),
          ("helloFailed", 5),
          ("lookupIngress", 6),
          ("lookupCompleted", 7),
          ("lookupFailed", 8),
          ("lookdownIngress", 9),
          ("lookdownCompleted", 10),
          ("lookdownFailed", 11))
    )



class ItemOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("save", 2))
    )



class UpdateReachStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("update", 2))
    )



class JdsuGeneratorFrameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("frameType8023", 2))
    )



class JdsuGeneratorPayloadType(TextualConvention, Integer32):
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
          ("fixed", 2),
          ("random", 3))
    )



class GeneratorAction(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("loopUp", 2),
          ("loopDown", 3))
    )



class DiscoveryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("discover", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3JdsuObjects_ObjectIdentity = ObjectIdentity
f3JdsuObjects = _F3JdsuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1)
)
_F3JdsuGeneratorPort_Type = VariablePointer
_F3JdsuGeneratorPort_Object = MibScalar
f3JdsuGeneratorPort = _F3JdsuGeneratorPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 1),
    _F3JdsuGeneratorPort_Type()
)
f3JdsuGeneratorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorPort.setStatus("current")
_F3JdsuGeneratorOuterVlanEnabled_Type = TruthValue
_F3JdsuGeneratorOuterVlanEnabled_Object = MibScalar
f3JdsuGeneratorOuterVlanEnabled = _F3JdsuGeneratorOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 2),
    _F3JdsuGeneratorOuterVlanEnabled_Type()
)
f3JdsuGeneratorOuterVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorOuterVlanEnabled.setStatus("current")
_F3JdsuGeneratorOuterVlanId_Type = VlanId
_F3JdsuGeneratorOuterVlanId_Object = MibScalar
f3JdsuGeneratorOuterVlanId = _F3JdsuGeneratorOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 3),
    _F3JdsuGeneratorOuterVlanId_Type()
)
f3JdsuGeneratorOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorOuterVlanId.setStatus("current")
_F3JdsuGeneratorOuterVlanPri_Type = VlanPriority
_F3JdsuGeneratorOuterVlanPri_Object = MibScalar
f3JdsuGeneratorOuterVlanPri = _F3JdsuGeneratorOuterVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 4),
    _F3JdsuGeneratorOuterVlanPri_Type()
)
f3JdsuGeneratorOuterVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorOuterVlanPri.setStatus("current")
_F3JdsuGeneratorOuterVlanEtherType_Type = Unsigned32
_F3JdsuGeneratorOuterVlanEtherType_Object = MibScalar
f3JdsuGeneratorOuterVlanEtherType = _F3JdsuGeneratorOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 5),
    _F3JdsuGeneratorOuterVlanEtherType_Type()
)
f3JdsuGeneratorOuterVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorOuterVlanEtherType.setStatus("current")
_F3JdsuGeneratorInnerVlan1Enabled_Type = TruthValue
_F3JdsuGeneratorInnerVlan1Enabled_Object = MibScalar
f3JdsuGeneratorInnerVlan1Enabled = _F3JdsuGeneratorInnerVlan1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 6),
    _F3JdsuGeneratorInnerVlan1Enabled_Type()
)
f3JdsuGeneratorInnerVlan1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan1Enabled.setStatus("current")
_F3JdsuGeneratorInnerVlan1Id_Type = VlanId
_F3JdsuGeneratorInnerVlan1Id_Object = MibScalar
f3JdsuGeneratorInnerVlan1Id = _F3JdsuGeneratorInnerVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 7),
    _F3JdsuGeneratorInnerVlan1Id_Type()
)
f3JdsuGeneratorInnerVlan1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan1Id.setStatus("current")
_F3JdsuGeneratorInnerVlan1Pri_Type = VlanPriority
_F3JdsuGeneratorInnerVlan1Pri_Object = MibScalar
f3JdsuGeneratorInnerVlan1Pri = _F3JdsuGeneratorInnerVlan1Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 8),
    _F3JdsuGeneratorInnerVlan1Pri_Type()
)
f3JdsuGeneratorInnerVlan1Pri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan1Pri.setStatus("current")
_F3JdsuGeneratorInnerVlan1EtherType_Type = Unsigned32
_F3JdsuGeneratorInnerVlan1EtherType_Object = MibScalar
f3JdsuGeneratorInnerVlan1EtherType = _F3JdsuGeneratorInnerVlan1EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 9),
    _F3JdsuGeneratorInnerVlan1EtherType_Type()
)
f3JdsuGeneratorInnerVlan1EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan1EtherType.setStatus("current")
_F3JdsuGeneratorInnerVlan2Enabled_Type = TruthValue
_F3JdsuGeneratorInnerVlan2Enabled_Object = MibScalar
f3JdsuGeneratorInnerVlan2Enabled = _F3JdsuGeneratorInnerVlan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 10),
    _F3JdsuGeneratorInnerVlan2Enabled_Type()
)
f3JdsuGeneratorInnerVlan2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan2Enabled.setStatus("current")
_F3JdsuGeneratorInnerVlan2Id_Type = VlanId
_F3JdsuGeneratorInnerVlan2Id_Object = MibScalar
f3JdsuGeneratorInnerVlan2Id = _F3JdsuGeneratorInnerVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 11),
    _F3JdsuGeneratorInnerVlan2Id_Type()
)
f3JdsuGeneratorInnerVlan2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan2Id.setStatus("current")
_F3JdsuGeneratorInnerVlan2Pri_Type = VlanPriority
_F3JdsuGeneratorInnerVlan2Pri_Object = MibScalar
f3JdsuGeneratorInnerVlan2Pri = _F3JdsuGeneratorInnerVlan2Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 12),
    _F3JdsuGeneratorInnerVlan2Pri_Type()
)
f3JdsuGeneratorInnerVlan2Pri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan2Pri.setStatus("current")
_F3JdsuGeneratorInnerVlan2EtherType_Type = Unsigned32
_F3JdsuGeneratorInnerVlan2EtherType_Object = MibScalar
f3JdsuGeneratorInnerVlan2EtherType = _F3JdsuGeneratorInnerVlan2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 13),
    _F3JdsuGeneratorInnerVlan2EtherType_Type()
)
f3JdsuGeneratorInnerVlan2EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorInnerVlan2EtherType.setStatus("current")
_F3JdsuGeneratorFrameType_Type = JdsuGeneratorFrameType
_F3JdsuGeneratorFrameType_Object = MibScalar
f3JdsuGeneratorFrameType = _F3JdsuGeneratorFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 14),
    _F3JdsuGeneratorFrameType_Type()
)
f3JdsuGeneratorFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorFrameType.setStatus("current")
_F3JdsuGeneratorPayloadType_Type = JdsuGeneratorPayloadType
_F3JdsuGeneratorPayloadType_Object = MibScalar
f3JdsuGeneratorPayloadType = _F3JdsuGeneratorPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 15),
    _F3JdsuGeneratorPayloadType_Type()
)
f3JdsuGeneratorPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorPayloadType.setStatus("current")
_F3JdsuGeneratorFrameLength_Type = Integer32
_F3JdsuGeneratorFrameLength_Object = MibScalar
f3JdsuGeneratorFrameLength = _F3JdsuGeneratorFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 16),
    _F3JdsuGeneratorFrameLength_Type()
)
f3JdsuGeneratorFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorFrameLength.setStatus("current")
_F3JdsuGeneratorDiscoveryAction_Type = DiscoveryAction
_F3JdsuGeneratorDiscoveryAction_Object = MibScalar
f3JdsuGeneratorDiscoveryAction = _F3JdsuGeneratorDiscoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 17),
    _F3JdsuGeneratorDiscoveryAction_Type()
)
f3JdsuGeneratorDiscoveryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoveryAction.setStatus("current")
_F3JdsuGeneratorDiscoverTable_Object = MibTable
f3JdsuGeneratorDiscoverTable = _F3JdsuGeneratorDiscoverTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18)
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverTable.setStatus("current")
_F3JdsuGeneratorDiscoverEntry_Object = MibTableRow
f3JdsuGeneratorDiscoverEntry = _F3JdsuGeneratorDiscoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1)
)
f3JdsuGeneratorDiscoverEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-JDSU-MIB", "f3JdsuGeneratorDiscoverDestMacAddr"),
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverEntry.setStatus("current")
_F3JdsuGeneratorDiscoverDestMacAddr_Type = MacAddress
_F3JdsuGeneratorDiscoverDestMacAddr_Object = MibTableColumn
f3JdsuGeneratorDiscoverDestMacAddr = _F3JdsuGeneratorDiscoverDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 1),
    _F3JdsuGeneratorDiscoverDestMacAddr_Type()
)
f3JdsuGeneratorDiscoverDestMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverDestMacAddr.setStatus("current")
_F3JdsuGeneratorDiscoverOuterVlanEnabled_Type = TruthValue
_F3JdsuGeneratorDiscoverOuterVlanEnabled_Object = MibTableColumn
f3JdsuGeneratorDiscoverOuterVlanEnabled = _F3JdsuGeneratorDiscoverOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 2),
    _F3JdsuGeneratorDiscoverOuterVlanEnabled_Type()
)
f3JdsuGeneratorDiscoverOuterVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverOuterVlanEnabled.setStatus("current")
_F3JdsuGeneratorDiscoverOuterVlanId_Type = VlanId
_F3JdsuGeneratorDiscoverOuterVlanId_Object = MibTableColumn
f3JdsuGeneratorDiscoverOuterVlanId = _F3JdsuGeneratorDiscoverOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 3),
    _F3JdsuGeneratorDiscoverOuterVlanId_Type()
)
f3JdsuGeneratorDiscoverOuterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverOuterVlanId.setStatus("current")
_F3JdsuGeneratorDiscoverOuterVlanPri_Type = VlanPriority
_F3JdsuGeneratorDiscoverOuterVlanPri_Object = MibTableColumn
f3JdsuGeneratorDiscoverOuterVlanPri = _F3JdsuGeneratorDiscoverOuterVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 4),
    _F3JdsuGeneratorDiscoverOuterVlanPri_Type()
)
f3JdsuGeneratorDiscoverOuterVlanPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverOuterVlanPri.setStatus("current")
_F3JdsuGeneratorDiscoverOuterVlanEtherType_Type = Integer32
_F3JdsuGeneratorDiscoverOuterVlanEtherType_Object = MibTableColumn
f3JdsuGeneratorDiscoverOuterVlanEtherType = _F3JdsuGeneratorDiscoverOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 5),
    _F3JdsuGeneratorDiscoverOuterVlanEtherType_Type()
)
f3JdsuGeneratorDiscoverOuterVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverOuterVlanEtherType.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan1Enabled_Type = TruthValue
_F3JdsuGeneratorDiscoverInnerVlan1Enabled_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan1Enabled = _F3JdsuGeneratorDiscoverInnerVlan1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 6),
    _F3JdsuGeneratorDiscoverInnerVlan1Enabled_Type()
)
f3JdsuGeneratorDiscoverInnerVlan1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan1Enabled.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan1Id_Type = VlanId
_F3JdsuGeneratorDiscoverInnerVlan1Id_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan1Id = _F3JdsuGeneratorDiscoverInnerVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 7),
    _F3JdsuGeneratorDiscoverInnerVlan1Id_Type()
)
f3JdsuGeneratorDiscoverInnerVlan1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan1Id.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan1Pri_Type = VlanPriority
_F3JdsuGeneratorDiscoverInnerVlan1Pri_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan1Pri = _F3JdsuGeneratorDiscoverInnerVlan1Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 8),
    _F3JdsuGeneratorDiscoverInnerVlan1Pri_Type()
)
f3JdsuGeneratorDiscoverInnerVlan1Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan1Pri.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan1EtherType_Type = Integer32
_F3JdsuGeneratorDiscoverInnerVlan1EtherType_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan1EtherType = _F3JdsuGeneratorDiscoverInnerVlan1EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 9),
    _F3JdsuGeneratorDiscoverInnerVlan1EtherType_Type()
)
f3JdsuGeneratorDiscoverInnerVlan1EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan1EtherType.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan2Enabled_Type = TruthValue
_F3JdsuGeneratorDiscoverInnerVlan2Enabled_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan2Enabled = _F3JdsuGeneratorDiscoverInnerVlan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 10),
    _F3JdsuGeneratorDiscoverInnerVlan2Enabled_Type()
)
f3JdsuGeneratorDiscoverInnerVlan2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan2Enabled.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan2Id_Type = VlanId
_F3JdsuGeneratorDiscoverInnerVlan2Id_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan2Id = _F3JdsuGeneratorDiscoverInnerVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 11),
    _F3JdsuGeneratorDiscoverInnerVlan2Id_Type()
)
f3JdsuGeneratorDiscoverInnerVlan2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan2Id.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan2Pri_Type = VlanPriority
_F3JdsuGeneratorDiscoverInnerVlan2Pri_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan2Pri = _F3JdsuGeneratorDiscoverInnerVlan2Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 12),
    _F3JdsuGeneratorDiscoverInnerVlan2Pri_Type()
)
f3JdsuGeneratorDiscoverInnerVlan2Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan2Pri.setStatus("current")
_F3JdsuGeneratorDiscoverInnerVlan2EtherType_Type = Integer32
_F3JdsuGeneratorDiscoverInnerVlan2EtherType_Object = MibTableColumn
f3JdsuGeneratorDiscoverInnerVlan2EtherType = _F3JdsuGeneratorDiscoverInnerVlan2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 13),
    _F3JdsuGeneratorDiscoverInnerVlan2EtherType_Type()
)
f3JdsuGeneratorDiscoverInnerVlan2EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverInnerVlan2EtherType.setStatus("current")
_F3JdsuGeneratorDiscoverFrameType_Type = JdsuGeneratorFrameType
_F3JdsuGeneratorDiscoverFrameType_Object = MibTableColumn
f3JdsuGeneratorDiscoverFrameType = _F3JdsuGeneratorDiscoverFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 14),
    _F3JdsuGeneratorDiscoverFrameType_Type()
)
f3JdsuGeneratorDiscoverFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverFrameType.setStatus("current")
_F3JdsuGeneratorDiscoverPayloadType_Type = JdsuGeneratorPayloadType
_F3JdsuGeneratorDiscoverPayloadType_Object = MibTableColumn
f3JdsuGeneratorDiscoverPayloadType = _F3JdsuGeneratorDiscoverPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 15),
    _F3JdsuGeneratorDiscoverPayloadType_Type()
)
f3JdsuGeneratorDiscoverPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverPayloadType.setStatus("current")
_F3JdsuGeneratorDiscoverFrameLength_Type = Integer32
_F3JdsuGeneratorDiscoverFrameLength_Object = MibTableColumn
f3JdsuGeneratorDiscoverFrameLength = _F3JdsuGeneratorDiscoverFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 16),
    _F3JdsuGeneratorDiscoverFrameLength_Type()
)
f3JdsuGeneratorDiscoverFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverFrameLength.setStatus("current")
_F3JdsuGeneratorDiscoverUnitTextId_Type = DisplayString
_F3JdsuGeneratorDiscoverUnitTextId_Object = MibTableColumn
f3JdsuGeneratorDiscoverUnitTextId = _F3JdsuGeneratorDiscoverUnitTextId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 17),
    _F3JdsuGeneratorDiscoverUnitTextId_Type()
)
f3JdsuGeneratorDiscoverUnitTextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverUnitTextId.setStatus("current")
_F3JdsuGeneratorDiscoverIfReachable_Type = TruthValue
_F3JdsuGeneratorDiscoverIfReachable_Object = MibTableColumn
f3JdsuGeneratorDiscoverIfReachable = _F3JdsuGeneratorDiscoverIfReachable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 18),
    _F3JdsuGeneratorDiscoverIfReachable_Type()
)
f3JdsuGeneratorDiscoverIfReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverIfReachable.setStatus("current")
_F3JdsuGeneratorDiscoverGeneratorStatus_Type = GeneratorStatus
_F3JdsuGeneratorDiscoverGeneratorStatus_Object = MibTableColumn
f3JdsuGeneratorDiscoverGeneratorStatus = _F3JdsuGeneratorDiscoverGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 19),
    _F3JdsuGeneratorDiscoverGeneratorStatus_Type()
)
f3JdsuGeneratorDiscoverGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverGeneratorStatus.setStatus("current")
_F3JdsuGeneratorDiscoverItemOperation_Type = ItemOperation
_F3JdsuGeneratorDiscoverItemOperation_Object = MibTableColumn
f3JdsuGeneratorDiscoverItemOperation = _F3JdsuGeneratorDiscoverItemOperation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 20),
    _F3JdsuGeneratorDiscoverItemOperation_Type()
)
f3JdsuGeneratorDiscoverItemOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverItemOperation.setStatus("current")
_F3JdsuGeneratorDiscoverItemIfSaved_Type = TruthValue
_F3JdsuGeneratorDiscoverItemIfSaved_Object = MibTableColumn
f3JdsuGeneratorDiscoverItemIfSaved = _F3JdsuGeneratorDiscoverItemIfSaved_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 21),
    _F3JdsuGeneratorDiscoverItemIfSaved_Type()
)
f3JdsuGeneratorDiscoverItemIfSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverItemIfSaved.setStatus("current")
_F3JdsuGeneratorDiscoverGeneratorAction_Type = GeneratorAction
_F3JdsuGeneratorDiscoverGeneratorAction_Object = MibTableColumn
f3JdsuGeneratorDiscoverGeneratorAction = _F3JdsuGeneratorDiscoverGeneratorAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 22),
    _F3JdsuGeneratorDiscoverGeneratorAction_Type()
)
f3JdsuGeneratorDiscoverGeneratorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorDiscoverGeneratorAction.setStatus("current")
_F3JdsuGeneratorConfigureTable_Object = MibTable
f3JdsuGeneratorConfigureTable = _F3JdsuGeneratorConfigureTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19)
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureTable.setStatus("current")
_F3JdsuGeneratorConfigureEntry_Object = MibTableRow
f3JdsuGeneratorConfigureEntry = _F3JdsuGeneratorConfigureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1)
)
f3JdsuGeneratorConfigureEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-JDSU-MIB", "f3JdsuGeneratorConfigureDestMacAddr"),
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureEntry.setStatus("current")
_F3JdsuGeneratorConfigureDestMacAddr_Type = MacAddress
_F3JdsuGeneratorConfigureDestMacAddr_Object = MibTableColumn
f3JdsuGeneratorConfigureDestMacAddr = _F3JdsuGeneratorConfigureDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 1),
    _F3JdsuGeneratorConfigureDestMacAddr_Type()
)
f3JdsuGeneratorConfigureDestMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureDestMacAddr.setStatus("current")
_F3JdsuGeneratorConfigureOuterVlanEnabled_Type = TruthValue
_F3JdsuGeneratorConfigureOuterVlanEnabled_Object = MibTableColumn
f3JdsuGeneratorConfigureOuterVlanEnabled = _F3JdsuGeneratorConfigureOuterVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 2),
    _F3JdsuGeneratorConfigureOuterVlanEnabled_Type()
)
f3JdsuGeneratorConfigureOuterVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureOuterVlanEnabled.setStatus("current")
_F3JdsuGeneratorConfigureOuterVlanId_Type = VlanId
_F3JdsuGeneratorConfigureOuterVlanId_Object = MibTableColumn
f3JdsuGeneratorConfigureOuterVlanId = _F3JdsuGeneratorConfigureOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 3),
    _F3JdsuGeneratorConfigureOuterVlanId_Type()
)
f3JdsuGeneratorConfigureOuterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureOuterVlanId.setStatus("current")
_F3JdsuGeneratorConfigureOuterVlanPri_Type = VlanPriority
_F3JdsuGeneratorConfigureOuterVlanPri_Object = MibTableColumn
f3JdsuGeneratorConfigureOuterVlanPri = _F3JdsuGeneratorConfigureOuterVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 4),
    _F3JdsuGeneratorConfigureOuterVlanPri_Type()
)
f3JdsuGeneratorConfigureOuterVlanPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureOuterVlanPri.setStatus("current")
_F3JdsuGeneratorConfigureOuterVlanEtherType_Type = Integer32
_F3JdsuGeneratorConfigureOuterVlanEtherType_Object = MibTableColumn
f3JdsuGeneratorConfigureOuterVlanEtherType = _F3JdsuGeneratorConfigureOuterVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 5),
    _F3JdsuGeneratorConfigureOuterVlanEtherType_Type()
)
f3JdsuGeneratorConfigureOuterVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureOuterVlanEtherType.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan1Enabled_Type = TruthValue
_F3JdsuGeneratorConfigureInnerVlan1Enabled_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan1Enabled = _F3JdsuGeneratorConfigureInnerVlan1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 6),
    _F3JdsuGeneratorConfigureInnerVlan1Enabled_Type()
)
f3JdsuGeneratorConfigureInnerVlan1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan1Enabled.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan1Id_Type = VlanId
_F3JdsuGeneratorConfigureInnerVlan1Id_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan1Id = _F3JdsuGeneratorConfigureInnerVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 7),
    _F3JdsuGeneratorConfigureInnerVlan1Id_Type()
)
f3JdsuGeneratorConfigureInnerVlan1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan1Id.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan1Pri_Type = VlanPriority
_F3JdsuGeneratorConfigureInnerVlan1Pri_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan1Pri = _F3JdsuGeneratorConfigureInnerVlan1Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 8),
    _F3JdsuGeneratorConfigureInnerVlan1Pri_Type()
)
f3JdsuGeneratorConfigureInnerVlan1Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan1Pri.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan1EtherType_Type = Integer32
_F3JdsuGeneratorConfigureInnerVlan1EtherType_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan1EtherType = _F3JdsuGeneratorConfigureInnerVlan1EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 9),
    _F3JdsuGeneratorConfigureInnerVlan1EtherType_Type()
)
f3JdsuGeneratorConfigureInnerVlan1EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan1EtherType.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan2Enabled_Type = TruthValue
_F3JdsuGeneratorConfigureInnerVlan2Enabled_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan2Enabled = _F3JdsuGeneratorConfigureInnerVlan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 10),
    _F3JdsuGeneratorConfigureInnerVlan2Enabled_Type()
)
f3JdsuGeneratorConfigureInnerVlan2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan2Enabled.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan2Id_Type = VlanId
_F3JdsuGeneratorConfigureInnerVlan2Id_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan2Id = _F3JdsuGeneratorConfigureInnerVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 11),
    _F3JdsuGeneratorConfigureInnerVlan2Id_Type()
)
f3JdsuGeneratorConfigureInnerVlan2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan2Id.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan2Pri_Type = VlanPriority
_F3JdsuGeneratorConfigureInnerVlan2Pri_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan2Pri = _F3JdsuGeneratorConfigureInnerVlan2Pri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 12),
    _F3JdsuGeneratorConfigureInnerVlan2Pri_Type()
)
f3JdsuGeneratorConfigureInnerVlan2Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan2Pri.setStatus("current")
_F3JdsuGeneratorConfigureInnerVlan2EtherType_Type = Integer32
_F3JdsuGeneratorConfigureInnerVlan2EtherType_Object = MibTableColumn
f3JdsuGeneratorConfigureInnerVlan2EtherType = _F3JdsuGeneratorConfigureInnerVlan2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 13),
    _F3JdsuGeneratorConfigureInnerVlan2EtherType_Type()
)
f3JdsuGeneratorConfigureInnerVlan2EtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureInnerVlan2EtherType.setStatus("current")
_F3JdsuGeneratorConfigureFrameType_Type = JdsuGeneratorFrameType
_F3JdsuGeneratorConfigureFrameType_Object = MibTableColumn
f3JdsuGeneratorConfigureFrameType = _F3JdsuGeneratorConfigureFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 14),
    _F3JdsuGeneratorConfigureFrameType_Type()
)
f3JdsuGeneratorConfigureFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureFrameType.setStatus("current")
_F3JdsuGeneratorConfigurePayloadType_Type = JdsuGeneratorPayloadType
_F3JdsuGeneratorConfigurePayloadType_Object = MibTableColumn
f3JdsuGeneratorConfigurePayloadType = _F3JdsuGeneratorConfigurePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 15),
    _F3JdsuGeneratorConfigurePayloadType_Type()
)
f3JdsuGeneratorConfigurePayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigurePayloadType.setStatus("current")
_F3JdsuGeneratorConfigureFrameLength_Type = Integer32
_F3JdsuGeneratorConfigureFrameLength_Object = MibTableColumn
f3JdsuGeneratorConfigureFrameLength = _F3JdsuGeneratorConfigureFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 16),
    _F3JdsuGeneratorConfigureFrameLength_Type()
)
f3JdsuGeneratorConfigureFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureFrameLength.setStatus("current")
_F3JdsuGeneratorConfigureUnitTextId_Type = DisplayString
_F3JdsuGeneratorConfigureUnitTextId_Object = MibTableColumn
f3JdsuGeneratorConfigureUnitTextId = _F3JdsuGeneratorConfigureUnitTextId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 17),
    _F3JdsuGeneratorConfigureUnitTextId_Type()
)
f3JdsuGeneratorConfigureUnitTextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureUnitTextId.setStatus("current")
_F3JdsuGeneratorConfigureIfReachable_Type = TruthValue
_F3JdsuGeneratorConfigureIfReachable_Object = MibTableColumn
f3JdsuGeneratorConfigureIfReachable = _F3JdsuGeneratorConfigureIfReachable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 18),
    _F3JdsuGeneratorConfigureIfReachable_Type()
)
f3JdsuGeneratorConfigureIfReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureIfReachable.setStatus("current")
_F3JdsuGeneratorConfigureReachableUpdate_Type = UpdateReachStatus
_F3JdsuGeneratorConfigureReachableUpdate_Object = MibTableColumn
f3JdsuGeneratorConfigureReachableUpdate = _F3JdsuGeneratorConfigureReachableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 19),
    _F3JdsuGeneratorConfigureReachableUpdate_Type()
)
f3JdsuGeneratorConfigureReachableUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureReachableUpdate.setStatus("current")
_F3JdsuGeneratorConfigureStatus_Type = GeneratorStatus
_F3JdsuGeneratorConfigureStatus_Object = MibTableColumn
f3JdsuGeneratorConfigureStatus = _F3JdsuGeneratorConfigureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 20),
    _F3JdsuGeneratorConfigureStatus_Type()
)
f3JdsuGeneratorConfigureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureStatus.setStatus("current")
_F3JdsuGeneratorConfigureGeneratorAction_Type = GeneratorAction
_F3JdsuGeneratorConfigureGeneratorAction_Object = MibTableColumn
f3JdsuGeneratorConfigureGeneratorAction = _F3JdsuGeneratorConfigureGeneratorAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 21),
    _F3JdsuGeneratorConfigureGeneratorAction_Type()
)
f3JdsuGeneratorConfigureGeneratorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureGeneratorAction.setStatus("current")
_F3JdsuGeneratorConfigureStorageType_Type = StorageType
_F3JdsuGeneratorConfigureStorageType_Object = MibTableColumn
f3JdsuGeneratorConfigureStorageType = _F3JdsuGeneratorConfigureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 22),
    _F3JdsuGeneratorConfigureStorageType_Type()
)
f3JdsuGeneratorConfigureStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureStorageType.setStatus("current")
_F3JdsuGeneratorConfigureRowStatus_Type = RowStatus
_F3JdsuGeneratorConfigureRowStatus_Object = MibTableColumn
f3JdsuGeneratorConfigureRowStatus = _F3JdsuGeneratorConfigureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 23),
    _F3JdsuGeneratorConfigureRowStatus_Type()
)
f3JdsuGeneratorConfigureRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3JdsuGeneratorConfigureRowStatus.setStatus("current")
_F3EthernetTrafficPortJdsuExtTable_Object = MibTable
f3EthernetTrafficPortJdsuExtTable = _F3EthernetTrafficPortJdsuExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20)
)
if mibBuilder.loadTexts:
    f3EthernetTrafficPortJdsuExtTable.setStatus("current")
_F3EthernetTrafficPortJdsuExtEntry_Object = MibTableRow
f3EthernetTrafficPortJdsuExtEntry = _F3EthernetTrafficPortJdsuExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1)
)
if mibBuilder.loadTexts:
    f3EthernetTrafficPortJdsuExtEntry.setStatus("current")
_F3EthernetTrafficPortJdsuLoopbackEnabled_Type = TruthValue
_F3EthernetTrafficPortJdsuLoopbackEnabled_Object = MibTableColumn
f3EthernetTrafficPortJdsuLoopbackEnabled = _F3EthernetTrafficPortJdsuLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 1),
    _F3EthernetTrafficPortJdsuLoopbackEnabled_Type()
)
f3EthernetTrafficPortJdsuLoopbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetTrafficPortJdsuLoopbackEnabled.setStatus("current")
_F3EthernetTrafficPortJdsuGenerationEanbled_Type = TruthValue
_F3EthernetTrafficPortJdsuGenerationEanbled_Object = MibTableColumn
f3EthernetTrafficPortJdsuGenerationEanbled = _F3EthernetTrafficPortJdsuGenerationEanbled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 2),
    _F3EthernetTrafficPortJdsuGenerationEanbled_Type()
)
f3EthernetTrafficPortJdsuGenerationEanbled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetTrafficPortJdsuGenerationEanbled.setStatus("current")
_F3EthernetTrafficPortJdsuLoopbackVlanList_Type = DisplayString
_F3EthernetTrafficPortJdsuLoopbackVlanList_Object = MibTableColumn
f3EthernetTrafficPortJdsuLoopbackVlanList = _F3EthernetTrafficPortJdsuLoopbackVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 3),
    _F3EthernetTrafficPortJdsuLoopbackVlanList_Type()
)
f3EthernetTrafficPortJdsuLoopbackVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetTrafficPortJdsuLoopbackVlanList.setStatus("current")
_F3JdsuNotifications_ObjectIdentity = ObjectIdentity
f3JdsuNotifications = _F3JdsuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 2)
)
_F3JdsuConformance_ObjectIdentity = ObjectIdentity
f3JdsuConformance = _F3JdsuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3)
)
_F3JdsuCompliances_ObjectIdentity = ObjectIdentity
f3JdsuCompliances = _F3JdsuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 1)
)
_F3JdsuGroups_ObjectIdentity = ObjectIdentity
f3JdsuGroups = _F3JdsuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 2)
)
cmEthernetTrafficPortEntry.registerAugmentions(
    ("F3-JDSU-MIB",
     "f3EthernetTrafficPortJdsuExtEntry")
)
f3EthernetTrafficPortJdsuExtEntry.setIndexNames(*cmEthernetTrafficPortEntry.getIndexNames())

# Managed Objects groups

f3JdsuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 2, 1)
)
f3JdsuGroup.setObjects(
      *(("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverDestMacAddr"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanEnabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanId"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanPri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanEtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverFrameType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverPayloadType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverFrameLength"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverUnitTextId"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverIfReachable"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverGeneratorStatus"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverItemOperation"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverItemIfSaved"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverGeneratorAction"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureDestMacAddr"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanEnabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanId"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanPri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanEtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureFrameType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigurePayloadType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureFrameLength"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureUnitTextId"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureIfReachable"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureReachableUpdate"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureStatus"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureGeneratorAction"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureStorageType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureRowStatus"),
        ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuLoopbackEnabled"),
        ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuGenerationEanbled"),
        ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuLoopbackVlanList"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorPort"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanEnabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanId"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanPri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanEtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Enabled"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Id"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Pri"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2EtherType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorFrameType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorPayloadType"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorFrameLength"),
        ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoveryAction"))
)
if mibBuilder.loadTexts:
    f3JdsuGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3JdsuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 1, 1)
)
f3JdsuCompliance.setObjects(
    ("F3-JDSU-MIB", "f3JdsuGroup")
)
if mibBuilder.loadTexts:
    f3JdsuCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-JDSU-MIB",
    **{"GeneratorStatus": GeneratorStatus,
       "ItemOperation": ItemOperation,
       "UpdateReachStatus": UpdateReachStatus,
       "JdsuGeneratorFrameType": JdsuGeneratorFrameType,
       "JdsuGeneratorPayloadType": JdsuGeneratorPayloadType,
       "GeneratorAction": GeneratorAction,
       "DiscoveryAction": DiscoveryAction,
       "f3JdsuMIB": f3JdsuMIB,
       "f3JdsuObjects": f3JdsuObjects,
       "f3JdsuGeneratorPort": f3JdsuGeneratorPort,
       "f3JdsuGeneratorOuterVlanEnabled": f3JdsuGeneratorOuterVlanEnabled,
       "f3JdsuGeneratorOuterVlanId": f3JdsuGeneratorOuterVlanId,
       "f3JdsuGeneratorOuterVlanPri": f3JdsuGeneratorOuterVlanPri,
       "f3JdsuGeneratorOuterVlanEtherType": f3JdsuGeneratorOuterVlanEtherType,
       "f3JdsuGeneratorInnerVlan1Enabled": f3JdsuGeneratorInnerVlan1Enabled,
       "f3JdsuGeneratorInnerVlan1Id": f3JdsuGeneratorInnerVlan1Id,
       "f3JdsuGeneratorInnerVlan1Pri": f3JdsuGeneratorInnerVlan1Pri,
       "f3JdsuGeneratorInnerVlan1EtherType": f3JdsuGeneratorInnerVlan1EtherType,
       "f3JdsuGeneratorInnerVlan2Enabled": f3JdsuGeneratorInnerVlan2Enabled,
       "f3JdsuGeneratorInnerVlan2Id": f3JdsuGeneratorInnerVlan2Id,
       "f3JdsuGeneratorInnerVlan2Pri": f3JdsuGeneratorInnerVlan2Pri,
       "f3JdsuGeneratorInnerVlan2EtherType": f3JdsuGeneratorInnerVlan2EtherType,
       "f3JdsuGeneratorFrameType": f3JdsuGeneratorFrameType,
       "f3JdsuGeneratorPayloadType": f3JdsuGeneratorPayloadType,
       "f3JdsuGeneratorFrameLength": f3JdsuGeneratorFrameLength,
       "f3JdsuGeneratorDiscoveryAction": f3JdsuGeneratorDiscoveryAction,
       "f3JdsuGeneratorDiscoverTable": f3JdsuGeneratorDiscoverTable,
       "f3JdsuGeneratorDiscoverEntry": f3JdsuGeneratorDiscoverEntry,
       "f3JdsuGeneratorDiscoverDestMacAddr": f3JdsuGeneratorDiscoverDestMacAddr,
       "f3JdsuGeneratorDiscoverOuterVlanEnabled": f3JdsuGeneratorDiscoverOuterVlanEnabled,
       "f3JdsuGeneratorDiscoverOuterVlanId": f3JdsuGeneratorDiscoverOuterVlanId,
       "f3JdsuGeneratorDiscoverOuterVlanPri": f3JdsuGeneratorDiscoverOuterVlanPri,
       "f3JdsuGeneratorDiscoverOuterVlanEtherType": f3JdsuGeneratorDiscoverOuterVlanEtherType,
       "f3JdsuGeneratorDiscoverInnerVlan1Enabled": f3JdsuGeneratorDiscoverInnerVlan1Enabled,
       "f3JdsuGeneratorDiscoverInnerVlan1Id": f3JdsuGeneratorDiscoverInnerVlan1Id,
       "f3JdsuGeneratorDiscoverInnerVlan1Pri": f3JdsuGeneratorDiscoverInnerVlan1Pri,
       "f3JdsuGeneratorDiscoverInnerVlan1EtherType": f3JdsuGeneratorDiscoverInnerVlan1EtherType,
       "f3JdsuGeneratorDiscoverInnerVlan2Enabled": f3JdsuGeneratorDiscoverInnerVlan2Enabled,
       "f3JdsuGeneratorDiscoverInnerVlan2Id": f3JdsuGeneratorDiscoverInnerVlan2Id,
       "f3JdsuGeneratorDiscoverInnerVlan2Pri": f3JdsuGeneratorDiscoverInnerVlan2Pri,
       "f3JdsuGeneratorDiscoverInnerVlan2EtherType": f3JdsuGeneratorDiscoverInnerVlan2EtherType,
       "f3JdsuGeneratorDiscoverFrameType": f3JdsuGeneratorDiscoverFrameType,
       "f3JdsuGeneratorDiscoverPayloadType": f3JdsuGeneratorDiscoverPayloadType,
       "f3JdsuGeneratorDiscoverFrameLength": f3JdsuGeneratorDiscoverFrameLength,
       "f3JdsuGeneratorDiscoverUnitTextId": f3JdsuGeneratorDiscoverUnitTextId,
       "f3JdsuGeneratorDiscoverIfReachable": f3JdsuGeneratorDiscoverIfReachable,
       "f3JdsuGeneratorDiscoverGeneratorStatus": f3JdsuGeneratorDiscoverGeneratorStatus,
       "f3JdsuGeneratorDiscoverItemOperation": f3JdsuGeneratorDiscoverItemOperation,
       "f3JdsuGeneratorDiscoverItemIfSaved": f3JdsuGeneratorDiscoverItemIfSaved,
       "f3JdsuGeneratorDiscoverGeneratorAction": f3JdsuGeneratorDiscoverGeneratorAction,
       "f3JdsuGeneratorConfigureTable": f3JdsuGeneratorConfigureTable,
       "f3JdsuGeneratorConfigureEntry": f3JdsuGeneratorConfigureEntry,
       "f3JdsuGeneratorConfigureDestMacAddr": f3JdsuGeneratorConfigureDestMacAddr,
       "f3JdsuGeneratorConfigureOuterVlanEnabled": f3JdsuGeneratorConfigureOuterVlanEnabled,
       "f3JdsuGeneratorConfigureOuterVlanId": f3JdsuGeneratorConfigureOuterVlanId,
       "f3JdsuGeneratorConfigureOuterVlanPri": f3JdsuGeneratorConfigureOuterVlanPri,
       "f3JdsuGeneratorConfigureOuterVlanEtherType": f3JdsuGeneratorConfigureOuterVlanEtherType,
       "f3JdsuGeneratorConfigureInnerVlan1Enabled": f3JdsuGeneratorConfigureInnerVlan1Enabled,
       "f3JdsuGeneratorConfigureInnerVlan1Id": f3JdsuGeneratorConfigureInnerVlan1Id,
       "f3JdsuGeneratorConfigureInnerVlan1Pri": f3JdsuGeneratorConfigureInnerVlan1Pri,
       "f3JdsuGeneratorConfigureInnerVlan1EtherType": f3JdsuGeneratorConfigureInnerVlan1EtherType,
       "f3JdsuGeneratorConfigureInnerVlan2Enabled": f3JdsuGeneratorConfigureInnerVlan2Enabled,
       "f3JdsuGeneratorConfigureInnerVlan2Id": f3JdsuGeneratorConfigureInnerVlan2Id,
       "f3JdsuGeneratorConfigureInnerVlan2Pri": f3JdsuGeneratorConfigureInnerVlan2Pri,
       "f3JdsuGeneratorConfigureInnerVlan2EtherType": f3JdsuGeneratorConfigureInnerVlan2EtherType,
       "f3JdsuGeneratorConfigureFrameType": f3JdsuGeneratorConfigureFrameType,
       "f3JdsuGeneratorConfigurePayloadType": f3JdsuGeneratorConfigurePayloadType,
       "f3JdsuGeneratorConfigureFrameLength": f3JdsuGeneratorConfigureFrameLength,
       "f3JdsuGeneratorConfigureUnitTextId": f3JdsuGeneratorConfigureUnitTextId,
       "f3JdsuGeneratorConfigureIfReachable": f3JdsuGeneratorConfigureIfReachable,
       "f3JdsuGeneratorConfigureReachableUpdate": f3JdsuGeneratorConfigureReachableUpdate,
       "f3JdsuGeneratorConfigureStatus": f3JdsuGeneratorConfigureStatus,
       "f3JdsuGeneratorConfigureGeneratorAction": f3JdsuGeneratorConfigureGeneratorAction,
       "f3JdsuGeneratorConfigureStorageType": f3JdsuGeneratorConfigureStorageType,
       "f3JdsuGeneratorConfigureRowStatus": f3JdsuGeneratorConfigureRowStatus,
       "f3EthernetTrafficPortJdsuExtTable": f3EthernetTrafficPortJdsuExtTable,
       "f3EthernetTrafficPortJdsuExtEntry": f3EthernetTrafficPortJdsuExtEntry,
       "f3EthernetTrafficPortJdsuLoopbackEnabled": f3EthernetTrafficPortJdsuLoopbackEnabled,
       "f3EthernetTrafficPortJdsuGenerationEanbled": f3EthernetTrafficPortJdsuGenerationEanbled,
       "f3EthernetTrafficPortJdsuLoopbackVlanList": f3EthernetTrafficPortJdsuLoopbackVlanList,
       "f3JdsuNotifications": f3JdsuNotifications,
       "f3JdsuConformance": f3JdsuConformance,
       "f3JdsuCompliances": f3JdsuCompliances,
       "f3JdsuCompliance": f3JdsuCompliance,
       "f3JdsuGroups": f3JdsuGroups,
       "f3JdsuGroup": f3JdsuGroup}
)
