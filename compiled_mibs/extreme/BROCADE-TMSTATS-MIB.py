# SNMP MIB module (BROCADE-TMSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-TMSTATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:17 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bcsiTMStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15)
)
if mibBuilder.loadTexts:
    bcsiTMStats.setRevisions(
        ("2018-05-29 12:00",
         "2016-10-21 13:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiTMStatsNotification_ObjectIdentity = ObjectIdentity
bcsiTMStatsNotification = _BcsiTMStatsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 0)
)
_BcsiTMStatsObjects_ObjectIdentity = ObjectIdentity
bcsiTMStatsObjects = _BcsiTMStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1)
)
_BcsiTMStatsGlobals_ObjectIdentity = ObjectIdentity
bcsiTMStatsGlobals = _BcsiTMStatsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 1)
)
_BcsiTMStatsInfoGroup_ObjectIdentity = ObjectIdentity
bcsiTMStatsInfoGroup = _BcsiTMStatsInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2)
)
_BcsiTMStatsInfoGroupGlobals_ObjectIdentity = ObjectIdentity
bcsiTMStatsInfoGroupGlobals = _BcsiTMStatsInfoGroupGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 1)
)
_BcsiTMStatsTable_Object = MibTable
bcsiTMStatsTable = _BcsiTMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bcsiTMStatsTable.setStatus("current")
_BcsiTMStatsEntry_Object = MibTableRow
bcsiTMStatsEntry = _BcsiTMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1)
)
bcsiTMStatsEntry.setIndexNames(
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMStatsSlot"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMStatsTower"),
)
if mibBuilder.loadTexts:
    bcsiTMStatsEntry.setStatus("current")
_BcsiTMStatsSlot_Type = Unsigned32
_BcsiTMStatsSlot_Object = MibTableColumn
bcsiTMStatsSlot = _BcsiTMStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 1),
    _BcsiTMStatsSlot_Type()
)
bcsiTMStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMStatsSlot.setStatus("current")
_BcsiTMStatsTower_Type = Unsigned32
_BcsiTMStatsTower_Object = MibTableColumn
bcsiTMStatsTower = _BcsiTMStatsTower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 2),
    _BcsiTMStatsTower_Type()
)
bcsiTMStatsTower.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMStatsTower.setStatus("current")
_BcsiTMStatsDescription_Type = DisplayString
_BcsiTMStatsDescription_Object = MibTableColumn
bcsiTMStatsDescription = _BcsiTMStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 3),
    _BcsiTMStatsDescription_Type()
)
bcsiTMStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsDescription.setStatus("current")
_BcsiTMStatsTotalIngressPkts_Type = Counter64
_BcsiTMStatsTotalIngressPkts_Object = MibTableColumn
bcsiTMStatsTotalIngressPkts = _BcsiTMStatsTotalIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 4),
    _BcsiTMStatsTotalIngressPkts_Type()
)
bcsiTMStatsTotalIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsTotalIngressPkts.setStatus("current")
_BcsiTMStatsIngressCPUPkts_Type = Counter64
_BcsiTMStatsIngressCPUPkts_Object = MibTableColumn
bcsiTMStatsIngressCPUPkts = _BcsiTMStatsIngressCPUPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 5),
    _BcsiTMStatsIngressCPUPkts_Type()
)
bcsiTMStatsIngressCPUPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressCPUPkts.setStatus("current")
_BcsiTMStatsIngressEnquePkts_Type = Counter64
_BcsiTMStatsIngressEnquePkts_Object = MibTableColumn
bcsiTMStatsIngressEnquePkts = _BcsiTMStatsIngressEnquePkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 6),
    _BcsiTMStatsIngressEnquePkts_Type()
)
bcsiTMStatsIngressEnquePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressEnquePkts.setStatus("current")
_BcsiTMStatsIngressDequePkts_Type = Counter64
_BcsiTMStatsIngressDequePkts_Object = MibTableColumn
bcsiTMStatsIngressDequePkts = _BcsiTMStatsIngressDequePkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 7),
    _BcsiTMStatsIngressDequePkts_Type()
)
bcsiTMStatsIngressDequePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressDequePkts.setStatus("current")
_BcsiTMStatsIngressTotalDiscardPkts_Type = Counter64
_BcsiTMStatsIngressTotalDiscardPkts_Object = MibTableColumn
bcsiTMStatsIngressTotalDiscardPkts = _BcsiTMStatsIngressTotalDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 8),
    _BcsiTMStatsIngressTotalDiscardPkts_Type()
)
bcsiTMStatsIngressTotalDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressTotalDiscardPkts.setStatus("current")
_BcsiTMStatsIngressOldestDiscardPkts_Type = Counter64
_BcsiTMStatsIngressOldestDiscardPkts_Object = MibTableColumn
bcsiTMStatsIngressOldestDiscardPkts = _BcsiTMStatsIngressOldestDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 9),
    _BcsiTMStatsIngressOldestDiscardPkts_Type()
)
bcsiTMStatsIngressOldestDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressOldestDiscardPkts.setStatus("current")
_BcsiTMStatsIngressResolvedToBeDropped_Type = Counter64
_BcsiTMStatsIngressResolvedToBeDropped_Object = MibTableColumn
bcsiTMStatsIngressResolvedToBeDropped = _BcsiTMStatsIngressResolvedToBeDropped_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 10),
    _BcsiTMStatsIngressResolvedToBeDropped_Type()
)
bcsiTMStatsIngressResolvedToBeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressResolvedToBeDropped.setStatus("current")
_BcsiTMStatsIngressCRCErrorCount_Type = Counter64
_BcsiTMStatsIngressCRCErrorCount_Object = MibTableColumn
bcsiTMStatsIngressCRCErrorCount = _BcsiTMStatsIngressCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 11),
    _BcsiTMStatsIngressCRCErrorCount_Type()
)
bcsiTMStatsIngressCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsIngressCRCErrorCount.setStatus("current")
_BcsiTMStatsEgressREDiscardPkts_Type = Counter64
_BcsiTMStatsEgressREDiscardPkts_Object = MibTableColumn
bcsiTMStatsEgressREDiscardPkts = _BcsiTMStatsEgressREDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 12),
    _BcsiTMStatsEgressREDiscardPkts_Type()
)
bcsiTMStatsEgressREDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressREDiscardPkts.setStatus("current")
_BcsiTMStatsEgressFilterDiscardPkts_Type = Counter64
_BcsiTMStatsEgressFilterDiscardPkts_Object = MibTableColumn
bcsiTMStatsEgressFilterDiscardPkts = _BcsiTMStatsEgressFilterDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 13),
    _BcsiTMStatsEgressFilterDiscardPkts_Type()
)
bcsiTMStatsEgressFilterDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressFilterDiscardPkts.setStatus("current")
_BcsiTMStatsEgressDiscardUCPkts_Type = Counter64
_BcsiTMStatsEgressDiscardUCPkts_Object = MibTableColumn
bcsiTMStatsEgressDiscardUCPkts = _BcsiTMStatsEgressDiscardUCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 14),
    _BcsiTMStatsEgressDiscardUCPkts_Type()
)
bcsiTMStatsEgressDiscardUCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressDiscardUCPkts.setStatus("current")
_BcsiTMStatsEgressDiscardMCPkts_Type = Counter64
_BcsiTMStatsEgressDiscardMCPkts_Object = MibTableColumn
bcsiTMStatsEgressDiscardMCPkts = _BcsiTMStatsEgressDiscardMCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 15),
    _BcsiTMStatsEgressDiscardMCPkts_Type()
)
bcsiTMStatsEgressDiscardMCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressDiscardMCPkts.setStatus("current")
_BcsiTMStatsEgressUnicastPkts_Type = Counter64
_BcsiTMStatsEgressUnicastPkts_Object = MibTableColumn
bcsiTMStatsEgressUnicastPkts = _BcsiTMStatsEgressUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 16),
    _BcsiTMStatsEgressUnicastPkts_Type()
)
bcsiTMStatsEgressUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressUnicastPkts.setStatus("current")
_BcsiTMStatsEgressMulticastPkts_Type = Counter64
_BcsiTMStatsEgressMulticastPkts_Object = MibTableColumn
bcsiTMStatsEgressMulticastPkts = _BcsiTMStatsEgressMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 17),
    _BcsiTMStatsEgressMulticastPkts_Type()
)
bcsiTMStatsEgressMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressMulticastPkts.setStatus("current")
_BcsiTMStatsEgressFQPPkts_Type = Counter64
_BcsiTMStatsEgressFQPPkts_Object = MibTableColumn
bcsiTMStatsEgressFQPPkts = _BcsiTMStatsEgressFQPPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 2, 2, 1, 18),
    _BcsiTMStatsEgressFQPPkts_Type()
)
bcsiTMStatsEgressFQPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMStatsEgressFQPPkts.setStatus("current")
_BcsiTMVOQStatsInfoGroup_ObjectIdentity = ObjectIdentity
bcsiTMVOQStatsInfoGroup = _BcsiTMVOQStatsInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3)
)
_BcsiTMVOQStatsInfoGroupGlobals_ObjectIdentity = ObjectIdentity
bcsiTMVOQStatsInfoGroupGlobals = _BcsiTMVOQStatsInfoGroupGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 1)
)
_BcsiTMVOQCPUGroupStatsTable_Object = MibTable
bcsiTMVOQCPUGroupStatsTable = _BcsiTMVOQCPUGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsTable.setStatus("current")
_BcsiTMVOQCPUGroupStatsEntry_Object = MibTableRow
bcsiTMVOQCPUGroupStatsEntry = _BcsiTMVOQCPUGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1)
)
bcsiTMVOQCPUGroupStatsEntry.setIndexNames(
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQCPUGroupStatsSlot"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQCPUGroupStatsGroup"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQCPUGroupStatsPriority"),
)
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsEntry.setStatus("current")
_BcsiTMVOQCPUGroupStatsSlot_Type = Unsigned32
_BcsiTMVOQCPUGroupStatsSlot_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsSlot = _BcsiTMVOQCPUGroupStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 1),
    _BcsiTMVOQCPUGroupStatsSlot_Type()
)
bcsiTMVOQCPUGroupStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsSlot.setStatus("current")
_BcsiTMVOQCPUGroupStatsGroup_Type = Unsigned32
_BcsiTMVOQCPUGroupStatsGroup_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsGroup = _BcsiTMVOQCPUGroupStatsGroup_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 2),
    _BcsiTMVOQCPUGroupStatsGroup_Type()
)
bcsiTMVOQCPUGroupStatsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsGroup.setStatus("current")
_BcsiTMVOQCPUGroupStatsPriority_Type = Unsigned32
_BcsiTMVOQCPUGroupStatsPriority_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsPriority = _BcsiTMVOQCPUGroupStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 3),
    _BcsiTMVOQCPUGroupStatsPriority_Type()
)
bcsiTMVOQCPUGroupStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsPriority.setStatus("current")
_BcsiTMVOQCPUGroupStatsDescription_Type = DisplayString
_BcsiTMVOQCPUGroupStatsDescription_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsDescription = _BcsiTMVOQCPUGroupStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 4),
    _BcsiTMVOQCPUGroupStatsDescription_Type()
)
bcsiTMVOQCPUGroupStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsDescription.setStatus("current")
_BcsiTMVOQCPUGroupStatsEnQPkts_Type = Counter64
_BcsiTMVOQCPUGroupStatsEnQPkts_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsEnQPkts = _BcsiTMVOQCPUGroupStatsEnQPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 5),
    _BcsiTMVOQCPUGroupStatsEnQPkts_Type()
)
bcsiTMVOQCPUGroupStatsEnQPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsEnQPkts.setStatus("current")
_BcsiTMVOQCPUGroupStatsEnQBytes_Type = Counter64
_BcsiTMVOQCPUGroupStatsEnQBytes_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsEnQBytes = _BcsiTMVOQCPUGroupStatsEnQBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 6),
    _BcsiTMVOQCPUGroupStatsEnQBytes_Type()
)
bcsiTMVOQCPUGroupStatsEnQBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsEnQBytes.setStatus("current")
_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Type = Counter64
_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsTotalDiscardPkts = _BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 7),
    _BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Type()
)
bcsiTMVOQCPUGroupStatsTotalDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsTotalDiscardPkts.setStatus("current")
_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Type = Counter64
_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsTotalDiscardBytes = _BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 8),
    _BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Type()
)
bcsiTMVOQCPUGroupStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsTotalDiscardBytes.setStatus("current")
_BcsiTMVOQCPUGroupStatsCurrQDepth_Type = Counter64
_BcsiTMVOQCPUGroupStatsCurrQDepth_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsCurrQDepth = _BcsiTMVOQCPUGroupStatsCurrQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 9),
    _BcsiTMVOQCPUGroupStatsCurrQDepth_Type()
)
bcsiTMVOQCPUGroupStatsCurrQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsCurrQDepth.setStatus("current")
_BcsiTMVOQCPUGroupStatsMaxQDepth_Type = Counter64
_BcsiTMVOQCPUGroupStatsMaxQDepth_Object = MibTableColumn
bcsiTMVOQCPUGroupStatsMaxQDepth = _BcsiTMVOQCPUGroupStatsMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 2, 1, 10),
    _BcsiTMVOQCPUGroupStatsMaxQDepth_Type()
)
bcsiTMVOQCPUGroupStatsMaxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQCPUGroupStatsMaxQDepth.setStatus("current")
_BcsiTMVOQIngressStatsTable_Object = MibTable
bcsiTMVOQIngressStatsTable = _BcsiTMVOQIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3)
)
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsTable.setStatus("current")
_BcsiTMVOQIngressStatsEntry_Object = MibTableRow
bcsiTMVOQIngressStatsEntry = _BcsiTMVOQIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1)
)
bcsiTMVOQIngressStatsEntry.setIndexNames(
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQIngressStatsSlot"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQIngressStatsTower"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQIngressStatsEgressPort"),
    (0, "BROCADE-TMSTATS-MIB", "bcsiTMVOQIngressStatsPriority"),
)
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsEntry.setStatus("current")
_BcsiTMVOQIngressStatsSlot_Type = Unsigned32
_BcsiTMVOQIngressStatsSlot_Object = MibTableColumn
bcsiTMVOQIngressStatsSlot = _BcsiTMVOQIngressStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 1),
    _BcsiTMVOQIngressStatsSlot_Type()
)
bcsiTMVOQIngressStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsSlot.setStatus("current")
_BcsiTMVOQIngressStatsTower_Type = Unsigned32
_BcsiTMVOQIngressStatsTower_Object = MibTableColumn
bcsiTMVOQIngressStatsTower = _BcsiTMVOQIngressStatsTower_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 2),
    _BcsiTMVOQIngressStatsTower_Type()
)
bcsiTMVOQIngressStatsTower.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsTower.setStatus("current")
_BcsiTMVOQIngressStatsEgressPort_Type = InterfaceIndex
_BcsiTMVOQIngressStatsEgressPort_Object = MibTableColumn
bcsiTMVOQIngressStatsEgressPort = _BcsiTMVOQIngressStatsEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 3),
    _BcsiTMVOQIngressStatsEgressPort_Type()
)
bcsiTMVOQIngressStatsEgressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsEgressPort.setStatus("current")
_BcsiTMVOQIngressStatsPriority_Type = Unsigned32
_BcsiTMVOQIngressStatsPriority_Object = MibTableColumn
bcsiTMVOQIngressStatsPriority = _BcsiTMVOQIngressStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 4),
    _BcsiTMVOQIngressStatsPriority_Type()
)
bcsiTMVOQIngressStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsPriority.setStatus("current")
_BcsiTMVOQIngressStatsDescription_Type = DisplayString
_BcsiTMVOQIngressStatsDescription_Object = MibTableColumn
bcsiTMVOQIngressStatsDescription = _BcsiTMVOQIngressStatsDescription_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 5),
    _BcsiTMVOQIngressStatsDescription_Type()
)
bcsiTMVOQIngressStatsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsDescription.setStatus("current")
_BcsiTMVOQIngressStatsEnQPkts_Type = Counter64
_BcsiTMVOQIngressStatsEnQPkts_Object = MibTableColumn
bcsiTMVOQIngressStatsEnQPkts = _BcsiTMVOQIngressStatsEnQPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 6),
    _BcsiTMVOQIngressStatsEnQPkts_Type()
)
bcsiTMVOQIngressStatsEnQPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsEnQPkts.setStatus("current")
_BcsiTMVOQIngressStatsEnQBytes_Type = Counter64
_BcsiTMVOQIngressStatsEnQBytes_Object = MibTableColumn
bcsiTMVOQIngressStatsEnQBytes = _BcsiTMVOQIngressStatsEnQBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 7),
    _BcsiTMVOQIngressStatsEnQBytes_Type()
)
bcsiTMVOQIngressStatsEnQBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsEnQBytes.setStatus("current")
_BcsiTMVOQIngressStatsTotalDiscardPkts_Type = Counter64
_BcsiTMVOQIngressStatsTotalDiscardPkts_Object = MibTableColumn
bcsiTMVOQIngressStatsTotalDiscardPkts = _BcsiTMVOQIngressStatsTotalDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 8),
    _BcsiTMVOQIngressStatsTotalDiscardPkts_Type()
)
bcsiTMVOQIngressStatsTotalDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsTotalDiscardPkts.setStatus("current")
_BcsiTMVOQIngressStatsTotalDiscardBytes_Type = Counter64
_BcsiTMVOQIngressStatsTotalDiscardBytes_Object = MibTableColumn
bcsiTMVOQIngressStatsTotalDiscardBytes = _BcsiTMVOQIngressStatsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 9),
    _BcsiTMVOQIngressStatsTotalDiscardBytes_Type()
)
bcsiTMVOQIngressStatsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsTotalDiscardBytes.setStatus("current")
_BcsiTMVOQIngressStatsCurrQDepth_Type = Counter64
_BcsiTMVOQIngressStatsCurrQDepth_Object = MibTableColumn
bcsiTMVOQIngressStatsCurrQDepth = _BcsiTMVOQIngressStatsCurrQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 10),
    _BcsiTMVOQIngressStatsCurrQDepth_Type()
)
bcsiTMVOQIngressStatsCurrQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsCurrQDepth.setStatus("current")
_BcsiTMVOQIngressStatsMaxQDepth_Type = Counter64
_BcsiTMVOQIngressStatsMaxQDepth_Object = MibTableColumn
bcsiTMVOQIngressStatsMaxQDepth = _BcsiTMVOQIngressStatsMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 15, 1, 3, 3, 1, 11),
    _BcsiTMVOQIngressStatsMaxQDepth_Type()
)
bcsiTMVOQIngressStatsMaxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiTMVOQIngressStatsMaxQDepth.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-TMSTATS-MIB",
    **{"bcsiTMStats": bcsiTMStats,
       "bcsiTMStatsNotification": bcsiTMStatsNotification,
       "bcsiTMStatsObjects": bcsiTMStatsObjects,
       "bcsiTMStatsGlobals": bcsiTMStatsGlobals,
       "bcsiTMStatsInfoGroup": bcsiTMStatsInfoGroup,
       "bcsiTMStatsInfoGroupGlobals": bcsiTMStatsInfoGroupGlobals,
       "bcsiTMStatsTable": bcsiTMStatsTable,
       "bcsiTMStatsEntry": bcsiTMStatsEntry,
       "bcsiTMStatsSlot": bcsiTMStatsSlot,
       "bcsiTMStatsTower": bcsiTMStatsTower,
       "bcsiTMStatsDescription": bcsiTMStatsDescription,
       "bcsiTMStatsTotalIngressPkts": bcsiTMStatsTotalIngressPkts,
       "bcsiTMStatsIngressCPUPkts": bcsiTMStatsIngressCPUPkts,
       "bcsiTMStatsIngressEnquePkts": bcsiTMStatsIngressEnquePkts,
       "bcsiTMStatsIngressDequePkts": bcsiTMStatsIngressDequePkts,
       "bcsiTMStatsIngressTotalDiscardPkts": bcsiTMStatsIngressTotalDiscardPkts,
       "bcsiTMStatsIngressOldestDiscardPkts": bcsiTMStatsIngressOldestDiscardPkts,
       "bcsiTMStatsIngressResolvedToBeDropped": bcsiTMStatsIngressResolvedToBeDropped,
       "bcsiTMStatsIngressCRCErrorCount": bcsiTMStatsIngressCRCErrorCount,
       "bcsiTMStatsEgressREDiscardPkts": bcsiTMStatsEgressREDiscardPkts,
       "bcsiTMStatsEgressFilterDiscardPkts": bcsiTMStatsEgressFilterDiscardPkts,
       "bcsiTMStatsEgressDiscardUCPkts": bcsiTMStatsEgressDiscardUCPkts,
       "bcsiTMStatsEgressDiscardMCPkts": bcsiTMStatsEgressDiscardMCPkts,
       "bcsiTMStatsEgressUnicastPkts": bcsiTMStatsEgressUnicastPkts,
       "bcsiTMStatsEgressMulticastPkts": bcsiTMStatsEgressMulticastPkts,
       "bcsiTMStatsEgressFQPPkts": bcsiTMStatsEgressFQPPkts,
       "bcsiTMVOQStatsInfoGroup": bcsiTMVOQStatsInfoGroup,
       "bcsiTMVOQStatsInfoGroupGlobals": bcsiTMVOQStatsInfoGroupGlobals,
       "bcsiTMVOQCPUGroupStatsTable": bcsiTMVOQCPUGroupStatsTable,
       "bcsiTMVOQCPUGroupStatsEntry": bcsiTMVOQCPUGroupStatsEntry,
       "bcsiTMVOQCPUGroupStatsSlot": bcsiTMVOQCPUGroupStatsSlot,
       "bcsiTMVOQCPUGroupStatsGroup": bcsiTMVOQCPUGroupStatsGroup,
       "bcsiTMVOQCPUGroupStatsPriority": bcsiTMVOQCPUGroupStatsPriority,
       "bcsiTMVOQCPUGroupStatsDescription": bcsiTMVOQCPUGroupStatsDescription,
       "bcsiTMVOQCPUGroupStatsEnQPkts": bcsiTMVOQCPUGroupStatsEnQPkts,
       "bcsiTMVOQCPUGroupStatsEnQBytes": bcsiTMVOQCPUGroupStatsEnQBytes,
       "bcsiTMVOQCPUGroupStatsTotalDiscardPkts": bcsiTMVOQCPUGroupStatsTotalDiscardPkts,
       "bcsiTMVOQCPUGroupStatsTotalDiscardBytes": bcsiTMVOQCPUGroupStatsTotalDiscardBytes,
       "bcsiTMVOQCPUGroupStatsCurrQDepth": bcsiTMVOQCPUGroupStatsCurrQDepth,
       "bcsiTMVOQCPUGroupStatsMaxQDepth": bcsiTMVOQCPUGroupStatsMaxQDepth,
       "bcsiTMVOQIngressStatsTable": bcsiTMVOQIngressStatsTable,
       "bcsiTMVOQIngressStatsEntry": bcsiTMVOQIngressStatsEntry,
       "bcsiTMVOQIngressStatsSlot": bcsiTMVOQIngressStatsSlot,
       "bcsiTMVOQIngressStatsTower": bcsiTMVOQIngressStatsTower,
       "bcsiTMVOQIngressStatsEgressPort": bcsiTMVOQIngressStatsEgressPort,
       "bcsiTMVOQIngressStatsPriority": bcsiTMVOQIngressStatsPriority,
       "bcsiTMVOQIngressStatsDescription": bcsiTMVOQIngressStatsDescription,
       "bcsiTMVOQIngressStatsEnQPkts": bcsiTMVOQIngressStatsEnQPkts,
       "bcsiTMVOQIngressStatsEnQBytes": bcsiTMVOQIngressStatsEnQBytes,
       "bcsiTMVOQIngressStatsTotalDiscardPkts": bcsiTMVOQIngressStatsTotalDiscardPkts,
       "bcsiTMVOQIngressStatsTotalDiscardBytes": bcsiTMVOQIngressStatsTotalDiscardBytes,
       "bcsiTMVOQIngressStatsCurrQDepth": bcsiTMVOQIngressStatsCurrQDepth,
       "bcsiTMVOQIngressStatsMaxQDepth": bcsiTMVOQIngressStatsMaxQDepth}
)
