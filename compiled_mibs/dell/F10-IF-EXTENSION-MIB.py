# SNMP MIB module (F10-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\F10-IF-EXTENSION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:04 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

f10IfExtensionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11)
)
if mibBuilder.loadTexts:
    f10IfExtensionMib.setRevisions(
        ("2008-04-07 12:00",
         "2007-10-03 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10IfExtensionMibObject_ObjectIdentity = ObjectIdentity
f10IfExtensionMibObject = _F10IfExtensionMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1)
)
_F10IfExtensionParams_ObjectIdentity = ObjectIdentity
f10IfExtensionParams = _F10IfExtensionParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1)
)
_F10IfTable_Object = MibTable
f10IfTable = _F10IfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f10IfTable.setStatus("current")
_F10IfEntry_Object = MibTableRow
f10IfEntry = _F10IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1)
)
f10IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    f10IfEntry.setStatus("current")
_F10IfIpMtu_Type = Unsigned32
_F10IfIpMtu_Object = MibTableColumn
f10IfIpMtu = _F10IfIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 1),
    _F10IfIpMtu_Type()
)
f10IfIpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfIpMtu.setStatus("current")


class _F10IfDuplexMode_Type(Integer32):
    """Custom type f10IfDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2),
          ("auto", 3))
    )


_F10IfDuplexMode_Type.__name__ = "Integer32"
_F10IfDuplexMode_Object = MibTableColumn
f10IfDuplexMode = _F10IfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 2),
    _F10IfDuplexMode_Type()
)
f10IfDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfDuplexMode.setStatus("current")


class _F10IfQueueingStrategy_Type(DisplayString):
    """Custom type f10IfQueueingStrategy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_F10IfQueueingStrategy_Type.__name__ = "DisplayString"
_F10IfQueueingStrategy_Object = MibTableColumn
f10IfQueueingStrategy = _F10IfQueueingStrategy_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 3),
    _F10IfQueueingStrategy_Type()
)
f10IfQueueingStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfQueueingStrategy.setStatus("current")
_F10IfRxFlowCtrl_Type = TruthValue
_F10IfRxFlowCtrl_Object = MibTableColumn
f10IfRxFlowCtrl = _F10IfRxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 4),
    _F10IfRxFlowCtrl_Type()
)
f10IfRxFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfRxFlowCtrl.setStatus("current")
_F10IfTxFlowCtrl_Type = TruthValue
_F10IfTxFlowCtrl_Object = MibTableColumn
f10IfTxFlowCtrl = _F10IfTxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 5),
    _F10IfTxFlowCtrl_Type()
)
f10IfTxFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfTxFlowCtrl.setStatus("current")
_F10IfExtensionStats_ObjectIdentity = ObjectIdentity
f10IfExtensionStats = _F10IfExtensionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2)
)
_F10IfStaticsTable_Object = MibTable
f10IfStaticsTable = _F10IfStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f10IfStaticsTable.setStatus("current")
_F10IfStaticsEntry_Object = MibTableRow
f10IfStaticsEntry = _F10IfStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1)
)
f10IfStaticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    f10IfStaticsEntry.setStatus("current")
_F10IfInVlanPkts_Type = Counter64
_F10IfInVlanPkts_Object = MibTableColumn
f10IfInVlanPkts = _F10IfInVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 1),
    _F10IfInVlanPkts_Type()
)
f10IfInVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInVlanPkts.setStatus("current")
_F10IfIn64BytePkts_Type = Counter64
_F10IfIn64BytePkts_Object = MibTableColumn
f10IfIn64BytePkts = _F10IfIn64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 2),
    _F10IfIn64BytePkts_Type()
)
f10IfIn64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfIn64BytePkts.setStatus("current")
_F10ifIn65To127BytePkts_Type = Counter64
_F10ifIn65To127BytePkts_Object = MibTableColumn
f10ifIn65To127BytePkts = _F10ifIn65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 3),
    _F10ifIn65To127BytePkts_Type()
)
f10ifIn65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10ifIn65To127BytePkts.setStatus("current")
_F10IfIn128To255BytePkts_Type = Counter64
_F10IfIn128To255BytePkts_Object = MibTableColumn
f10IfIn128To255BytePkts = _F10IfIn128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 4),
    _F10IfIn128To255BytePkts_Type()
)
f10IfIn128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfIn128To255BytePkts.setStatus("current")
_F10IfIn256To511BytePkts_Type = Counter64
_F10IfIn256To511BytePkts_Object = MibTableColumn
f10IfIn256To511BytePkts = _F10IfIn256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 5),
    _F10IfIn256To511BytePkts_Type()
)
f10IfIn256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfIn256To511BytePkts.setStatus("current")
_F10IfIn512To1023BytePkts_Type = Counter64
_F10IfIn512To1023BytePkts_Object = MibTableColumn
f10IfIn512To1023BytePkts = _F10IfIn512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 6),
    _F10IfIn512To1023BytePkts_Type()
)
f10IfIn512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfIn512To1023BytePkts.setStatus("current")
_F10IfInOver1023BytePkts_Type = Counter64
_F10IfInOver1023BytePkts_Object = MibTableColumn
f10IfInOver1023BytePkts = _F10IfInOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 7),
    _F10IfInOver1023BytePkts_Type()
)
f10IfInOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInOver1023BytePkts.setStatus("current")
_F10IfInThrottles_Type = Counter64
_F10IfInThrottles_Object = MibTableColumn
f10IfInThrottles = _F10IfInThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 8),
    _F10IfInThrottles_Type()
)
f10IfInThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInThrottles.setStatus("current")
_F10IfInRunts_Type = Counter64
_F10IfInRunts_Object = MibTableColumn
f10IfInRunts = _F10IfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 9),
    _F10IfInRunts_Type()
)
f10IfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInRunts.setStatus("current")
_F10IfInGiants_Type = Counter64
_F10IfInGiants_Object = MibTableColumn
f10IfInGiants = _F10IfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 10),
    _F10IfInGiants_Type()
)
f10IfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInGiants.setStatus("current")
_F10IfInCRC_Type = Counter64
_F10IfInCRC_Object = MibTableColumn
f10IfInCRC = _F10IfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 11),
    _F10IfInCRC_Type()
)
f10IfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInCRC.setStatus("current")
_F10IfInOverruns_Type = Counter64
_F10IfInOverruns_Object = MibTableColumn
f10IfInOverruns = _F10IfInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 12),
    _F10IfInOverruns_Type()
)
f10IfInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfInOverruns.setStatus("current")
_F10IfOutVlanPkts_Type = Counter64
_F10IfOutVlanPkts_Object = MibTableColumn
f10IfOutVlanPkts = _F10IfOutVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 13),
    _F10IfOutVlanPkts_Type()
)
f10IfOutVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutVlanPkts.setStatus("current")
_F10IfOutUnderruns_Type = Counter64
_F10IfOutUnderruns_Object = MibTableColumn
f10IfOutUnderruns = _F10IfOutUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 14),
    _F10IfOutUnderruns_Type()
)
f10IfOutUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutUnderruns.setStatus("current")
_F10IfOutUnicasts_Type = Counter64
_F10IfOutUnicasts_Object = MibTableColumn
f10IfOutUnicasts = _F10IfOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 15),
    _F10IfOutUnicasts_Type()
)
f10IfOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutUnicasts.setStatus("current")
_F10IfOutCollisions_Type = Counter64
_F10IfOutCollisions_Object = MibTableColumn
f10IfOutCollisions = _F10IfOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 16),
    _F10IfOutCollisions_Type()
)
f10IfOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutCollisions.setStatus("current")
_F10IfOutWredDrops_Type = Counter64
_F10IfOutWredDrops_Object = MibTableColumn
f10IfOutWredDrops = _F10IfOutWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 17),
    _F10IfOutWredDrops_Type()
)
f10IfOutWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutWredDrops.setStatus("current")
_F10IfOut64BytePkts_Type = Counter64
_F10IfOut64BytePkts_Object = MibTableColumn
f10IfOut64BytePkts = _F10IfOut64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 18),
    _F10IfOut64BytePkts_Type()
)
f10IfOut64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOut64BytePkts.setStatus("current")
_F10IfOut65To127BytePkts_Type = Counter64
_F10IfOut65To127BytePkts_Object = MibTableColumn
f10IfOut65To127BytePkts = _F10IfOut65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 19),
    _F10IfOut65To127BytePkts_Type()
)
f10IfOut65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOut65To127BytePkts.setStatus("current")
_F10IfOut128To255BytePkts_Type = Counter64
_F10IfOut128To255BytePkts_Object = MibTableColumn
f10IfOut128To255BytePkts = _F10IfOut128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 20),
    _F10IfOut128To255BytePkts_Type()
)
f10IfOut128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOut128To255BytePkts.setStatus("current")
_F10IfOut256To511BytePkts_Type = Counter64
_F10IfOut256To511BytePkts_Object = MibTableColumn
f10IfOut256To511BytePkts = _F10IfOut256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 21),
    _F10IfOut256To511BytePkts_Type()
)
f10IfOut256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOut256To511BytePkts.setStatus("current")
_F10IfOut512To1023BytePkts_Type = Counter64
_F10IfOut512To1023BytePkts_Object = MibTableColumn
f10IfOut512To1023BytePkts = _F10IfOut512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 22),
    _F10IfOut512To1023BytePkts_Type()
)
f10IfOut512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOut512To1023BytePkts.setStatus("current")
_F10IfOutOver1023BytePkts_Type = Counter64
_F10IfOutOver1023BytePkts_Object = MibTableColumn
f10IfOutOver1023BytePkts = _F10IfOutOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 23),
    _F10IfOutOver1023BytePkts_Type()
)
f10IfOutOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutOver1023BytePkts.setStatus("current")
_F10IfOutThrottles_Type = Counter64
_F10IfOutThrottles_Object = MibTableColumn
f10IfOutThrottles = _F10IfOutThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 24),
    _F10IfOutThrottles_Type()
)
f10IfOutThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfOutThrottles.setStatus("current")
_F10IfLastDiscontinuityTime_Type = TimeStamp
_F10IfLastDiscontinuityTime_Object = MibTableColumn
f10IfLastDiscontinuityTime = _F10IfLastDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 25),
    _F10IfLastDiscontinuityTime_Type()
)
f10IfLastDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IfLastDiscontinuityTime.setStatus("current")
_F10IfExtensionMibConformance_ObjectIdentity = ObjectIdentity
f10IfExtensionMibConformance = _F10IfExtensionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2)
)
_F10IfExtensionMibCompliances_ObjectIdentity = ObjectIdentity
f10IfExtensionMibCompliances = _F10IfExtensionMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1)
)
_F10IfExtensionMibGroups_ObjectIdentity = ObjectIdentity
f10IfExtensionMibGroups = _F10IfExtensionMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2)
)

# Managed Objects groups

f10IfParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 1)
)
f10IfParamsGroup.setObjects(
      *(("F10-IF-EXTENSION-MIB", "f10IfIpMtu"),
        ("F10-IF-EXTENSION-MIB", "f10IfDuplexMode"),
        ("F10-IF-EXTENSION-MIB", "f10IfQueueingStrategy"),
        ("F10-IF-EXTENSION-MIB", "f10IfRxFlowCtrl"),
        ("F10-IF-EXTENSION-MIB", "f10IfTxFlowCtrl"))
)
if mibBuilder.loadTexts:
    f10IfParamsGroup.setStatus("current")

f10IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 2)
)
f10IfStatsGroup.setObjects(
      *(("F10-IF-EXTENSION-MIB", "f10IfInVlanPkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfIn64BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10ifIn65To127BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfIn128To255BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfIn256To511BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfIn512To1023BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfInOver1023BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfInThrottles"),
        ("F10-IF-EXTENSION-MIB", "f10IfInRunts"),
        ("F10-IF-EXTENSION-MIB", "f10IfInGiants"),
        ("F10-IF-EXTENSION-MIB", "f10IfInCRC"),
        ("F10-IF-EXTENSION-MIB", "f10IfInOverruns"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutVlanPkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutUnderruns"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutUnicasts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutCollisions"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutWredDrops"),
        ("F10-IF-EXTENSION-MIB", "f10IfOut64BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOut65To127BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOut128To255BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOut256To511BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOut512To1023BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutOver1023BytePkts"),
        ("F10-IF-EXTENSION-MIB", "f10IfOutThrottles"),
        ("F10-IF-EXTENSION-MIB", "f10IfLastDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    f10IfStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10IfExtensionMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1, 1)
)
f10IfExtensionMibCompliance.setObjects(
      *(("F10-IF-EXTENSION-MIB", "f10IfParamsGroup"),
        ("F10-IF-EXTENSION-MIB", "f10IfStatsGroup"))
)
if mibBuilder.loadTexts:
    f10IfExtensionMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-IF-EXTENSION-MIB",
    **{"f10IfExtensionMib": f10IfExtensionMib,
       "f10IfExtensionMibObject": f10IfExtensionMibObject,
       "f10IfExtensionParams": f10IfExtensionParams,
       "f10IfTable": f10IfTable,
       "f10IfEntry": f10IfEntry,
       "f10IfIpMtu": f10IfIpMtu,
       "f10IfDuplexMode": f10IfDuplexMode,
       "f10IfQueueingStrategy": f10IfQueueingStrategy,
       "f10IfRxFlowCtrl": f10IfRxFlowCtrl,
       "f10IfTxFlowCtrl": f10IfTxFlowCtrl,
       "f10IfExtensionStats": f10IfExtensionStats,
       "f10IfStaticsTable": f10IfStaticsTable,
       "f10IfStaticsEntry": f10IfStaticsEntry,
       "f10IfInVlanPkts": f10IfInVlanPkts,
       "f10IfIn64BytePkts": f10IfIn64BytePkts,
       "f10ifIn65To127BytePkts": f10ifIn65To127BytePkts,
       "f10IfIn128To255BytePkts": f10IfIn128To255BytePkts,
       "f10IfIn256To511BytePkts": f10IfIn256To511BytePkts,
       "f10IfIn512To1023BytePkts": f10IfIn512To1023BytePkts,
       "f10IfInOver1023BytePkts": f10IfInOver1023BytePkts,
       "f10IfInThrottles": f10IfInThrottles,
       "f10IfInRunts": f10IfInRunts,
       "f10IfInGiants": f10IfInGiants,
       "f10IfInCRC": f10IfInCRC,
       "f10IfInOverruns": f10IfInOverruns,
       "f10IfOutVlanPkts": f10IfOutVlanPkts,
       "f10IfOutUnderruns": f10IfOutUnderruns,
       "f10IfOutUnicasts": f10IfOutUnicasts,
       "f10IfOutCollisions": f10IfOutCollisions,
       "f10IfOutWredDrops": f10IfOutWredDrops,
       "f10IfOut64BytePkts": f10IfOut64BytePkts,
       "f10IfOut65To127BytePkts": f10IfOut65To127BytePkts,
       "f10IfOut128To255BytePkts": f10IfOut128To255BytePkts,
       "f10IfOut256To511BytePkts": f10IfOut256To511BytePkts,
       "f10IfOut512To1023BytePkts": f10IfOut512To1023BytePkts,
       "f10IfOutOver1023BytePkts": f10IfOutOver1023BytePkts,
       "f10IfOutThrottles": f10IfOutThrottles,
       "f10IfLastDiscontinuityTime": f10IfLastDiscontinuityTime,
       "f10IfExtensionMibConformance": f10IfExtensionMibConformance,
       "f10IfExtensionMibCompliances": f10IfExtensionMibCompliances,
       "f10IfExtensionMibCompliance": f10IfExtensionMibCompliance,
       "f10IfExtensionMibGroups": f10IfExtensionMibGroups,
       "f10IfParamsGroup": f10IfParamsGroup,
       "f10IfStatsGroup": f10IfStatsGroup}
)
