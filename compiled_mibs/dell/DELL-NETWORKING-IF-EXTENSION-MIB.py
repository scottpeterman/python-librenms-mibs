# SNMP MIB module (DELL-NETWORKING-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-NETWORKING-IF-EXTENSION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:42 2025
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetIfExtensionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11)
)
if mibBuilder.loadTexts:
    dellNetIfExtensionMib.setRevisions(
        ("2014-08-12 12:00",
         "2012-03-06 12:00",
         "2010-08-11 12:00",
         "2010-08-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetIfExtensionMibObject_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibObject = _DellNetIfExtensionMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1)
)
_DellNetIfExtensionParams_ObjectIdentity = ObjectIdentity
dellNetIfExtensionParams = _DellNetIfExtensionParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1)
)
_DellNetIfTable_Object = MibTable
dellNetIfTable = _DellNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetIfTable.setStatus("current")
_DellNetIfEntry_Object = MibTableRow
dellNetIfEntry = _DellNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1)
)
dellNetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetIfEntry.setStatus("current")


class _DellNetIfIpMtu_Type(Unsigned32):
    """Custom type dellNetIfIpMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(594, 9252),
    )


_DellNetIfIpMtu_Type.__name__ = "Unsigned32"
_DellNetIfIpMtu_Object = MibTableColumn
dellNetIfIpMtu = _DellNetIfIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 1),
    _DellNetIfIpMtu_Type()
)
dellNetIfIpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfIpMtu.setStatus("current")


class _DellNetIfDuplexMode_Type(Integer32):
    """Custom type dellNetIfDuplexMode based on Integer32"""
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


_DellNetIfDuplexMode_Type.__name__ = "Integer32"
_DellNetIfDuplexMode_Object = MibTableColumn
dellNetIfDuplexMode = _DellNetIfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 2),
    _DellNetIfDuplexMode_Type()
)
dellNetIfDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfDuplexMode.setStatus("current")


class _DellNetIfQueueingStrategy_Type(DisplayString):
    """Custom type dellNetIfQueueingStrategy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetIfQueueingStrategy_Type.__name__ = "DisplayString"
_DellNetIfQueueingStrategy_Object = MibTableColumn
dellNetIfQueueingStrategy = _DellNetIfQueueingStrategy_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 3),
    _DellNetIfQueueingStrategy_Type()
)
dellNetIfQueueingStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfQueueingStrategy.setStatus("current")
_DellNetIfRxFlowCtrl_Type = TruthValue
_DellNetIfRxFlowCtrl_Object = MibTableColumn
dellNetIfRxFlowCtrl = _DellNetIfRxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 4),
    _DellNetIfRxFlowCtrl_Type()
)
dellNetIfRxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfRxFlowCtrl.setStatus("current")
_DellNetIfTxFlowCtrl_Type = TruthValue
_DellNetIfTxFlowCtrl_Object = MibTableColumn
dellNetIfTxFlowCtrl = _DellNetIfTxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 5),
    _DellNetIfTxFlowCtrl_Type()
)
dellNetIfTxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfTxFlowCtrl.setStatus("current")


class _DellNetIfDescr_Type(OctetString):
    """Custom type dellNetIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfDescr_Type.__name__ = "OctetString"
_DellNetIfDescr_Object = MibTableColumn
dellNetIfDescr = _DellNetIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 6),
    _DellNetIfDescr_Type()
)
dellNetIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfDescr.setStatus("current")


class _DellNetIfAdminStatus_Type(Integer32):
    """Custom type dellNetIfAdminStatus based on Integer32"""
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


_DellNetIfAdminStatus_Type.__name__ = "Integer32"
_DellNetIfAdminStatus_Object = MibTableColumn
dellNetIfAdminStatus = _DellNetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 7),
    _DellNetIfAdminStatus_Type()
)
dellNetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfAdminStatus.setStatus("current")


class _DellNetIfRateInterval_Type(Unsigned32):
    """Custom type dellNetIfRateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 299),
    )


_DellNetIfRateInterval_Type.__name__ = "Unsigned32"
_DellNetIfRateInterval_Object = MibTableColumn
dellNetIfRateInterval = _DellNetIfRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 8),
    _DellNetIfRateInterval_Type()
)
dellNetIfRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfRateInterval.setStatus("current")


class _DellNetIfSpeed_Type(Integer32):
    """Custom type dellNetIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("tenMbps", 10),
          ("hundredMbps", 100),
          ("thousandMbps", 1000))
    )


_DellNetIfSpeed_Type.__name__ = "Integer32"
_DellNetIfSpeed_Object = MibTableColumn
dellNetIfSpeed = _DellNetIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 9),
    _DellNetIfSpeed_Type()
)
dellNetIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfSpeed.setStatus("current")
_DellNetIfPortListBitPos_Type = Integer32
_DellNetIfPortListBitPos_Object = MibTableColumn
dellNetIfPortListBitPos = _DellNetIfPortListBitPos_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 10),
    _DellNetIfPortListBitPos_Type()
)
dellNetIfPortListBitPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfPortListBitPos.setStatus("current")
_DellNetIfExtensionStats_ObjectIdentity = ObjectIdentity
dellNetIfExtensionStats = _DellNetIfExtensionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2)
)
_DellNetIfStaticsTable_Object = MibTable
dellNetIfStaticsTable = _DellNetIfStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetIfStaticsTable.setStatus("current")
_DellNetIfStaticsEntry_Object = MibTableRow
dellNetIfStaticsEntry = _DellNetIfStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1)
)
dellNetIfStaticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetIfStaticsEntry.setStatus("current")
_DellNetIfInVlanPkts_Type = Counter64
_DellNetIfInVlanPkts_Object = MibTableColumn
dellNetIfInVlanPkts = _DellNetIfInVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 1),
    _DellNetIfInVlanPkts_Type()
)
dellNetIfInVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInVlanPkts.setStatus("current")
_DellNetIfIn64BytePkts_Type = Counter64
_DellNetIfIn64BytePkts_Object = MibTableColumn
dellNetIfIn64BytePkts = _DellNetIfIn64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 2),
    _DellNetIfIn64BytePkts_Type()
)
dellNetIfIn64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn64BytePkts.setStatus("current")
_DellNetIfIn65To127BytePkts_Type = Counter64
_DellNetIfIn65To127BytePkts_Object = MibTableColumn
dellNetIfIn65To127BytePkts = _DellNetIfIn65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 3),
    _DellNetIfIn65To127BytePkts_Type()
)
dellNetIfIn65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn65To127BytePkts.setStatus("current")
_DellNetIfIn128To255BytePkts_Type = Counter64
_DellNetIfIn128To255BytePkts_Object = MibTableColumn
dellNetIfIn128To255BytePkts = _DellNetIfIn128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 4),
    _DellNetIfIn128To255BytePkts_Type()
)
dellNetIfIn128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn128To255BytePkts.setStatus("current")
_DellNetIfIn256To511BytePkts_Type = Counter64
_DellNetIfIn256To511BytePkts_Object = MibTableColumn
dellNetIfIn256To511BytePkts = _DellNetIfIn256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 5),
    _DellNetIfIn256To511BytePkts_Type()
)
dellNetIfIn256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn256To511BytePkts.setStatus("current")
_DellNetIfIn512To1023BytePkts_Type = Counter64
_DellNetIfIn512To1023BytePkts_Object = MibTableColumn
dellNetIfIn512To1023BytePkts = _DellNetIfIn512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 6),
    _DellNetIfIn512To1023BytePkts_Type()
)
dellNetIfIn512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn512To1023BytePkts.setStatus("current")
_DellNetIfInOver1023BytePkts_Type = Counter64
_DellNetIfInOver1023BytePkts_Object = MibTableColumn
dellNetIfInOver1023BytePkts = _DellNetIfInOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 7),
    _DellNetIfInOver1023BytePkts_Type()
)
dellNetIfInOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInOver1023BytePkts.setStatus("current")
_DellNetIfInThrottles_Type = Counter64
_DellNetIfInThrottles_Object = MibTableColumn
dellNetIfInThrottles = _DellNetIfInThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 8),
    _DellNetIfInThrottles_Type()
)
dellNetIfInThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInThrottles.setStatus("current")
_DellNetIfInRunts_Type = Counter64
_DellNetIfInRunts_Object = MibTableColumn
dellNetIfInRunts = _DellNetIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 9),
    _DellNetIfInRunts_Type()
)
dellNetIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInRunts.setStatus("current")
_DellNetIfInGiants_Type = Counter64
_DellNetIfInGiants_Object = MibTableColumn
dellNetIfInGiants = _DellNetIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 10),
    _DellNetIfInGiants_Type()
)
dellNetIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInGiants.setStatus("current")
_DellNetIfInCRC_Type = Counter64
_DellNetIfInCRC_Object = MibTableColumn
dellNetIfInCRC = _DellNetIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 11),
    _DellNetIfInCRC_Type()
)
dellNetIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInCRC.setStatus("current")
_DellNetIfInOverruns_Type = Counter64
_DellNetIfInOverruns_Object = MibTableColumn
dellNetIfInOverruns = _DellNetIfInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 12),
    _DellNetIfInOverruns_Type()
)
dellNetIfInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInOverruns.setStatus("current")
_DellNetIfOutVlanPkts_Type = Counter64
_DellNetIfOutVlanPkts_Object = MibTableColumn
dellNetIfOutVlanPkts = _DellNetIfOutVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 13),
    _DellNetIfOutVlanPkts_Type()
)
dellNetIfOutVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutVlanPkts.setStatus("current")
_DellNetIfOutUnderruns_Type = Counter64
_DellNetIfOutUnderruns_Object = MibTableColumn
dellNetIfOutUnderruns = _DellNetIfOutUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 14),
    _DellNetIfOutUnderruns_Type()
)
dellNetIfOutUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutUnderruns.setStatus("current")
_DellNetIfOutUnicasts_Type = Counter64
_DellNetIfOutUnicasts_Object = MibTableColumn
dellNetIfOutUnicasts = _DellNetIfOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 15),
    _DellNetIfOutUnicasts_Type()
)
dellNetIfOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutUnicasts.setStatus("current")
_DellNetIfOutCollisions_Type = Counter64
_DellNetIfOutCollisions_Object = MibTableColumn
dellNetIfOutCollisions = _DellNetIfOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 16),
    _DellNetIfOutCollisions_Type()
)
dellNetIfOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutCollisions.setStatus("current")
_DellNetIfOutWredDrops_Type = Counter64
_DellNetIfOutWredDrops_Object = MibTableColumn
dellNetIfOutWredDrops = _DellNetIfOutWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 17),
    _DellNetIfOutWredDrops_Type()
)
dellNetIfOutWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutWredDrops.setStatus("current")
_DellNetIfOut64BytePkts_Type = Counter64
_DellNetIfOut64BytePkts_Object = MibTableColumn
dellNetIfOut64BytePkts = _DellNetIfOut64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 18),
    _DellNetIfOut64BytePkts_Type()
)
dellNetIfOut64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut64BytePkts.setStatus("current")
_DellNetIfOut65To127BytePkts_Type = Counter64
_DellNetIfOut65To127BytePkts_Object = MibTableColumn
dellNetIfOut65To127BytePkts = _DellNetIfOut65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 19),
    _DellNetIfOut65To127BytePkts_Type()
)
dellNetIfOut65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut65To127BytePkts.setStatus("current")
_DellNetIfOut128To255BytePkts_Type = Counter64
_DellNetIfOut128To255BytePkts_Object = MibTableColumn
dellNetIfOut128To255BytePkts = _DellNetIfOut128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 20),
    _DellNetIfOut128To255BytePkts_Type()
)
dellNetIfOut128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut128To255BytePkts.setStatus("current")
_DellNetIfOut256To511BytePkts_Type = Counter64
_DellNetIfOut256To511BytePkts_Object = MibTableColumn
dellNetIfOut256To511BytePkts = _DellNetIfOut256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 21),
    _DellNetIfOut256To511BytePkts_Type()
)
dellNetIfOut256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut256To511BytePkts.setStatus("current")
_DellNetIfOut512To1023BytePkts_Type = Counter64
_DellNetIfOut512To1023BytePkts_Object = MibTableColumn
dellNetIfOut512To1023BytePkts = _DellNetIfOut512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 22),
    _DellNetIfOut512To1023BytePkts_Type()
)
dellNetIfOut512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut512To1023BytePkts.setStatus("current")
_DellNetIfOutOver1023BytePkts_Type = Counter64
_DellNetIfOutOver1023BytePkts_Object = MibTableColumn
dellNetIfOutOver1023BytePkts = _DellNetIfOutOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 23),
    _DellNetIfOutOver1023BytePkts_Type()
)
dellNetIfOutOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutOver1023BytePkts.setStatus("current")
_DellNetIfOutThrottles_Type = Counter64
_DellNetIfOutThrottles_Object = MibTableColumn
dellNetIfOutThrottles = _DellNetIfOutThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 24),
    _DellNetIfOutThrottles_Type()
)
dellNetIfOutThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutThrottles.setStatus("current")
_DellNetIfLastDiscontinuityTime_Type = TimeStamp
_DellNetIfLastDiscontinuityTime_Object = MibTableColumn
dellNetIfLastDiscontinuityTime = _DellNetIfLastDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 25),
    _DellNetIfLastDiscontinuityTime_Type()
)
dellNetIfLastDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfLastDiscontinuityTime.setStatus("current")


class _DellNetIfInCentRate_Type(Integer32):
    """Custom type dellNetIfInCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetIfInCentRate_Type.__name__ = "Integer32"
_DellNetIfInCentRate_Object = MibTableColumn
dellNetIfInCentRate = _DellNetIfInCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 26),
    _DellNetIfInCentRate_Type()
)
dellNetIfInCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInCentRate.setStatus("current")


class _DellNetIfOutCentRate_Type(Integer32):
    """Custom type dellNetIfOutCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetIfOutCentRate_Type.__name__ = "Integer32"
_DellNetIfOutCentRate_Object = MibTableColumn
dellNetIfOutCentRate = _DellNetIfOutCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 27),
    _DellNetIfOutCentRate_Type()
)
dellNetIfOutCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutCentRate.setStatus("current")
_DellNetIfTransceiverData_ObjectIdentity = ObjectIdentity
dellNetIfTransceiverData = _DellNetIfTransceiverData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3)
)
_DellNetIfTransceiverDataTable_Object = MibTable
dellNetIfTransceiverDataTable = _DellNetIfTransceiverDataTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetIfTransceiverDataTable.setStatus("current")
_DellNetIfTransceiverDataEntry_Object = MibTableRow
dellNetIfTransceiverDataEntry = _DellNetIfTransceiverDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1)
)
dellNetIfTransceiverDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetIfTransceiverDataEntry.setStatus("current")


class _DellNetIfTransDeviceName_Type(OctetString):
    """Custom type dellNetIfTransDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransDeviceName_Type.__name__ = "OctetString"
_DellNetIfTransDeviceName_Object = MibTableColumn
dellNetIfTransDeviceName = _DellNetIfTransDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 1),
    _DellNetIfTransDeviceName_Type()
)
dellNetIfTransDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransDeviceName.setStatus("current")


class _DellNetIfTransPort_Type(OctetString):
    """Custom type dellNetIfTransPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransPort_Type.__name__ = "OctetString"
_DellNetIfTransPort_Object = MibTableColumn
dellNetIfTransPort = _DellNetIfTransPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 2),
    _DellNetIfTransPort_Type()
)
dellNetIfTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransPort.setStatus("current")
_DellNetIfTransOpticsPresent_Type = TruthValue
_DellNetIfTransOpticsPresent_Object = MibTableColumn
dellNetIfTransOpticsPresent = _DellNetIfTransOpticsPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 3),
    _DellNetIfTransOpticsPresent_Type()
)
dellNetIfTransOpticsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransOpticsPresent.setStatus("current")


class _DellNetIfTransOpticsType_Type(OctetString):
    """Custom type dellNetIfTransOpticsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransOpticsType_Type.__name__ = "OctetString"
_DellNetIfTransOpticsType_Object = MibTableColumn
dellNetIfTransOpticsType = _DellNetIfTransOpticsType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 4),
    _DellNetIfTransOpticsType_Type()
)
dellNetIfTransOpticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransOpticsType.setStatus("current")


class _DellNetIfTransVendorName_Type(OctetString):
    """Custom type dellNetIfTransVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransVendorName_Type.__name__ = "OctetString"
_DellNetIfTransVendorName_Object = MibTableColumn
dellNetIfTransVendorName = _DellNetIfTransVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 5),
    _DellNetIfTransVendorName_Type()
)
dellNetIfTransVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransVendorName.setStatus("current")


class _DellNetIfTransPartNumber_Type(OctetString):
    """Custom type dellNetIfTransPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransPartNumber_Type.__name__ = "OctetString"
_DellNetIfTransPartNumber_Object = MibTableColumn
dellNetIfTransPartNumber = _DellNetIfTransPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 6),
    _DellNetIfTransPartNumber_Type()
)
dellNetIfTransPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransPartNumber.setStatus("current")


class _DellNetIfTransSerialNumber_Type(OctetString):
    """Custom type dellNetIfTransSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransSerialNumber_Type.__name__ = "OctetString"
_DellNetIfTransSerialNumber_Object = MibTableColumn
dellNetIfTransSerialNumber = _DellNetIfTransSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 7),
    _DellNetIfTransSerialNumber_Type()
)
dellNetIfTransSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransSerialNumber.setStatus("current")


class _DellNetIfTransTransmitPowerLane1_Type(OctetString):
    """Custom type dellNetIfTransTransmitPowerLane1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitPowerLane1_Type.__name__ = "OctetString"
_DellNetIfTransTransmitPowerLane1_Object = MibTableColumn
dellNetIfTransTransmitPowerLane1 = _DellNetIfTransTransmitPowerLane1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 8),
    _DellNetIfTransTransmitPowerLane1_Type()
)
dellNetIfTransTransmitPowerLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane1.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane1.setUnits("dBm")


class _DellNetIfTransTransmitPowerLane2_Type(OctetString):
    """Custom type dellNetIfTransTransmitPowerLane2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitPowerLane2_Type.__name__ = "OctetString"
_DellNetIfTransTransmitPowerLane2_Object = MibTableColumn
dellNetIfTransTransmitPowerLane2 = _DellNetIfTransTransmitPowerLane2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 9),
    _DellNetIfTransTransmitPowerLane2_Type()
)
dellNetIfTransTransmitPowerLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane2.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane2.setUnits("dBm")


class _DellNetIfTransTransmitPowerLane3_Type(OctetString):
    """Custom type dellNetIfTransTransmitPowerLane3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitPowerLane3_Type.__name__ = "OctetString"
_DellNetIfTransTransmitPowerLane3_Object = MibTableColumn
dellNetIfTransTransmitPowerLane3 = _DellNetIfTransTransmitPowerLane3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 10),
    _DellNetIfTransTransmitPowerLane3_Type()
)
dellNetIfTransTransmitPowerLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane3.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane3.setUnits("dBm")


class _DellNetIfTransTransmitPowerLane4_Type(OctetString):
    """Custom type dellNetIfTransTransmitPowerLane4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitPowerLane4_Type.__name__ = "OctetString"
_DellNetIfTransTransmitPowerLane4_Object = MibTableColumn
dellNetIfTransTransmitPowerLane4 = _DellNetIfTransTransmitPowerLane4_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 11),
    _DellNetIfTransTransmitPowerLane4_Type()
)
dellNetIfTransTransmitPowerLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane4.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitPowerLane4.setUnits("dBm")


class _DellNetIfTransReceivePowerLane1_Type(OctetString):
    """Custom type dellNetIfTransReceivePowerLane1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransReceivePowerLane1_Type.__name__ = "OctetString"
_DellNetIfTransReceivePowerLane1_Object = MibTableColumn
dellNetIfTransReceivePowerLane1 = _DellNetIfTransReceivePowerLane1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 12),
    _DellNetIfTransReceivePowerLane1_Type()
)
dellNetIfTransReceivePowerLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane1.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane1.setUnits("dBm")


class _DellNetIfTransReceivePowerLane2_Type(OctetString):
    """Custom type dellNetIfTransReceivePowerLane2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransReceivePowerLane2_Type.__name__ = "OctetString"
_DellNetIfTransReceivePowerLane2_Object = MibTableColumn
dellNetIfTransReceivePowerLane2 = _DellNetIfTransReceivePowerLane2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 13),
    _DellNetIfTransReceivePowerLane2_Type()
)
dellNetIfTransReceivePowerLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane2.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane2.setUnits("dBm")


class _DellNetIfTransReceivePowerLane3_Type(OctetString):
    """Custom type dellNetIfTransReceivePowerLane3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransReceivePowerLane3_Type.__name__ = "OctetString"
_DellNetIfTransReceivePowerLane3_Object = MibTableColumn
dellNetIfTransReceivePowerLane3 = _DellNetIfTransReceivePowerLane3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 14),
    _DellNetIfTransReceivePowerLane3_Type()
)
dellNetIfTransReceivePowerLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane3.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane3.setUnits("dBm")


class _DellNetIfTransReceivePowerLane4_Type(OctetString):
    """Custom type dellNetIfTransReceivePowerLane4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransReceivePowerLane4_Type.__name__ = "OctetString"
_DellNetIfTransReceivePowerLane4_Object = MibTableColumn
dellNetIfTransReceivePowerLane4 = _DellNetIfTransReceivePowerLane4_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 15),
    _DellNetIfTransReceivePowerLane4_Type()
)
dellNetIfTransReceivePowerLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane4.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransReceivePowerLane4.setUnits("dBm")


class _DellNetIfTransTemperature_Type(OctetString):
    """Custom type dellNetIfTransTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTemperature_Type.__name__ = "OctetString"
_DellNetIfTransTemperature_Object = MibTableColumn
dellNetIfTransTemperature = _DellNetIfTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 16),
    _DellNetIfTransTemperature_Type()
)
dellNetIfTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTemperature.setUnits("degree Celsius")


class _DellNetIfTransVoltage_Type(OctetString):
    """Custom type dellNetIfTransVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransVoltage_Type.__name__ = "OctetString"
_DellNetIfTransVoltage_Object = MibTableColumn
dellNetIfTransVoltage = _DellNetIfTransVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 17),
    _DellNetIfTransVoltage_Type()
)
dellNetIfTransVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransVoltage.setUnits("volts")


class _DellNetIfTransTransmitBiasCurrentLane1_Type(OctetString):
    """Custom type dellNetIfTransTransmitBiasCurrentLane1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitBiasCurrentLane1_Type.__name__ = "OctetString"
_DellNetIfTransTransmitBiasCurrentLane1_Object = MibTableColumn
dellNetIfTransTransmitBiasCurrentLane1 = _DellNetIfTransTransmitBiasCurrentLane1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 18),
    _DellNetIfTransTransmitBiasCurrentLane1_Type()
)
dellNetIfTransTransmitBiasCurrentLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane1.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane1.setUnits("mA")


class _DellNetIfTransTransmitBiasCurrentLane2_Type(OctetString):
    """Custom type dellNetIfTransTransmitBiasCurrentLane2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitBiasCurrentLane2_Type.__name__ = "OctetString"
_DellNetIfTransTransmitBiasCurrentLane2_Object = MibTableColumn
dellNetIfTransTransmitBiasCurrentLane2 = _DellNetIfTransTransmitBiasCurrentLane2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 19),
    _DellNetIfTransTransmitBiasCurrentLane2_Type()
)
dellNetIfTransTransmitBiasCurrentLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane2.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane2.setUnits("mA")


class _DellNetIfTransTransmitBiasCurrentLane3_Type(OctetString):
    """Custom type dellNetIfTransTransmitBiasCurrentLane3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitBiasCurrentLane3_Type.__name__ = "OctetString"
_DellNetIfTransTransmitBiasCurrentLane3_Object = MibTableColumn
dellNetIfTransTransmitBiasCurrentLane3 = _DellNetIfTransTransmitBiasCurrentLane3_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 20),
    _DellNetIfTransTransmitBiasCurrentLane3_Type()
)
dellNetIfTransTransmitBiasCurrentLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane3.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane3.setUnits("mA")


class _DellNetIfTransTransmitBiasCurrentLane4_Type(OctetString):
    """Custom type dellNetIfTransTransmitBiasCurrentLane4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfTransTransmitBiasCurrentLane4_Type.__name__ = "OctetString"
_DellNetIfTransTransmitBiasCurrentLane4_Object = MibTableColumn
dellNetIfTransTransmitBiasCurrentLane4 = _DellNetIfTransTransmitBiasCurrentLane4_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 3, 1, 1, 21),
    _DellNetIfTransTransmitBiasCurrentLane4_Type()
)
dellNetIfTransTransmitBiasCurrentLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane4.setStatus("current")
if mibBuilder.loadTexts:
    dellNetIfTransTransmitBiasCurrentLane4.setUnits("mA")
_DellNetIfAlarmObjects_ObjectIdentity = ObjectIdentity
dellNetIfAlarmObjects = _DellNetIfAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 4)
)
_DellNetIfAlarmMibNotifications_ObjectIdentity = ObjectIdentity
dellNetIfAlarmMibNotifications = _DellNetIfAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 4, 1)
)
_DellNetIfExtensionMibConformance_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibConformance = _DellNetIfExtensionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2)
)
_DellNetIfExtensionMibCompliances_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibCompliances = _DellNetIfExtensionMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1)
)
_DellNetIfExtensionMibGroups_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibGroups = _DellNetIfExtensionMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2)
)

# Managed Objects groups

dellNetIfParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 1)
)
dellNetIfParamsGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIpMtu"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDuplexMode"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfQueueingStrategy"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRxFlowCtrl"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTxFlowCtrl"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDescr"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAdminStatus"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRateInterval"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfSpeed"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfPortListBitPos"))
)
if mibBuilder.loadTexts:
    dellNetIfParamsGroup.setStatus("current")

dellNetIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 2)
)
dellNetIfStatsGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInVlanPkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn64BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn65To127BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn128To255BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn256To511BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn512To1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOver1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInThrottles"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInRunts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInGiants"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCRC"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOverruns"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutVlanPkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnderruns"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnicasts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCollisions"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutWredDrops"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut64BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut65To127BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut128To255BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut256To511BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut512To1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutOver1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutThrottles"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfLastDiscontinuityTime"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCentRate"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCentRate"))
)
if mibBuilder.loadTexts:
    dellNetIfStatsGroup.setStatus("current")

dellNetIfTransceiverDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 3)
)
dellNetIfTransceiverDataGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransDeviceName"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransPort"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransOpticsPresent"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransOpticsType"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransVendorName"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransPartNumber"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransSerialNumber"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitPowerLane1"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitPowerLane2"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitPowerLane3"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitPowerLane4"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransReceivePowerLane1"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransReceivePowerLane2"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransReceivePowerLane3"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransReceivePowerLane4"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTemperature"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransVoltage"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitBiasCurrentLane1"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitBiasCurrentLane2"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitBiasCurrentLane3"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransTransmitBiasCurrentLane4"))
)
if mibBuilder.loadTexts:
    dellNetIfTransceiverDataGroup.setStatus("current")


# Notification objects

dellNetIfAlarmHighBer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 4, 1, 1)
)
dellNetIfAlarmHighBer.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dellNetIfAlarmHighBer.setStatus(
        "current"
    )

dellNetIfAlarmHighBerClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 4, 1, 2)
)
dellNetIfAlarmHighBerClr.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dellNetIfAlarmHighBerClr.setStatus(
        "current"
    )

dellNetIfAlarmFastRetrain = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 4, 1, 3)
)
dellNetIfAlarmFastRetrain.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dellNetIfAlarmFastRetrain.setStatus(
        "current"
    )


# Notifications groups

dellNetIfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 4)
)
dellNetIfNotificationGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAlarmHighBer"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAlarmHighBerClr"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAlarmFastRetrain"))
)
if mibBuilder.loadTexts:
    dellNetIfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetIfExtensionMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1, 1)
)
dellNetIfExtensionMibCompliance.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfParamsGroup"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfStatsGroup"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTransceiverDataGroup"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfNotificationGroup"))
)
if mibBuilder.loadTexts:
    dellNetIfExtensionMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-IF-EXTENSION-MIB",
    **{"dellNetIfExtensionMib": dellNetIfExtensionMib,
       "dellNetIfExtensionMibObject": dellNetIfExtensionMibObject,
       "dellNetIfExtensionParams": dellNetIfExtensionParams,
       "dellNetIfTable": dellNetIfTable,
       "dellNetIfEntry": dellNetIfEntry,
       "dellNetIfIpMtu": dellNetIfIpMtu,
       "dellNetIfDuplexMode": dellNetIfDuplexMode,
       "dellNetIfQueueingStrategy": dellNetIfQueueingStrategy,
       "dellNetIfRxFlowCtrl": dellNetIfRxFlowCtrl,
       "dellNetIfTxFlowCtrl": dellNetIfTxFlowCtrl,
       "dellNetIfDescr": dellNetIfDescr,
       "dellNetIfAdminStatus": dellNetIfAdminStatus,
       "dellNetIfRateInterval": dellNetIfRateInterval,
       "dellNetIfSpeed": dellNetIfSpeed,
       "dellNetIfPortListBitPos": dellNetIfPortListBitPos,
       "dellNetIfExtensionStats": dellNetIfExtensionStats,
       "dellNetIfStaticsTable": dellNetIfStaticsTable,
       "dellNetIfStaticsEntry": dellNetIfStaticsEntry,
       "dellNetIfInVlanPkts": dellNetIfInVlanPkts,
       "dellNetIfIn64BytePkts": dellNetIfIn64BytePkts,
       "dellNetIfIn65To127BytePkts": dellNetIfIn65To127BytePkts,
       "dellNetIfIn128To255BytePkts": dellNetIfIn128To255BytePkts,
       "dellNetIfIn256To511BytePkts": dellNetIfIn256To511BytePkts,
       "dellNetIfIn512To1023BytePkts": dellNetIfIn512To1023BytePkts,
       "dellNetIfInOver1023BytePkts": dellNetIfInOver1023BytePkts,
       "dellNetIfInThrottles": dellNetIfInThrottles,
       "dellNetIfInRunts": dellNetIfInRunts,
       "dellNetIfInGiants": dellNetIfInGiants,
       "dellNetIfInCRC": dellNetIfInCRC,
       "dellNetIfInOverruns": dellNetIfInOverruns,
       "dellNetIfOutVlanPkts": dellNetIfOutVlanPkts,
       "dellNetIfOutUnderruns": dellNetIfOutUnderruns,
       "dellNetIfOutUnicasts": dellNetIfOutUnicasts,
       "dellNetIfOutCollisions": dellNetIfOutCollisions,
       "dellNetIfOutWredDrops": dellNetIfOutWredDrops,
       "dellNetIfOut64BytePkts": dellNetIfOut64BytePkts,
       "dellNetIfOut65To127BytePkts": dellNetIfOut65To127BytePkts,
       "dellNetIfOut128To255BytePkts": dellNetIfOut128To255BytePkts,
       "dellNetIfOut256To511BytePkts": dellNetIfOut256To511BytePkts,
       "dellNetIfOut512To1023BytePkts": dellNetIfOut512To1023BytePkts,
       "dellNetIfOutOver1023BytePkts": dellNetIfOutOver1023BytePkts,
       "dellNetIfOutThrottles": dellNetIfOutThrottles,
       "dellNetIfLastDiscontinuityTime": dellNetIfLastDiscontinuityTime,
       "dellNetIfInCentRate": dellNetIfInCentRate,
       "dellNetIfOutCentRate": dellNetIfOutCentRate,
       "dellNetIfTransceiverData": dellNetIfTransceiverData,
       "dellNetIfTransceiverDataTable": dellNetIfTransceiverDataTable,
       "dellNetIfTransceiverDataEntry": dellNetIfTransceiverDataEntry,
       "dellNetIfTransDeviceName": dellNetIfTransDeviceName,
       "dellNetIfTransPort": dellNetIfTransPort,
       "dellNetIfTransOpticsPresent": dellNetIfTransOpticsPresent,
       "dellNetIfTransOpticsType": dellNetIfTransOpticsType,
       "dellNetIfTransVendorName": dellNetIfTransVendorName,
       "dellNetIfTransPartNumber": dellNetIfTransPartNumber,
       "dellNetIfTransSerialNumber": dellNetIfTransSerialNumber,
       "dellNetIfTransTransmitPowerLane1": dellNetIfTransTransmitPowerLane1,
       "dellNetIfTransTransmitPowerLane2": dellNetIfTransTransmitPowerLane2,
       "dellNetIfTransTransmitPowerLane3": dellNetIfTransTransmitPowerLane3,
       "dellNetIfTransTransmitPowerLane4": dellNetIfTransTransmitPowerLane4,
       "dellNetIfTransReceivePowerLane1": dellNetIfTransReceivePowerLane1,
       "dellNetIfTransReceivePowerLane2": dellNetIfTransReceivePowerLane2,
       "dellNetIfTransReceivePowerLane3": dellNetIfTransReceivePowerLane3,
       "dellNetIfTransReceivePowerLane4": dellNetIfTransReceivePowerLane4,
       "dellNetIfTransTemperature": dellNetIfTransTemperature,
       "dellNetIfTransVoltage": dellNetIfTransVoltage,
       "dellNetIfTransTransmitBiasCurrentLane1": dellNetIfTransTransmitBiasCurrentLane1,
       "dellNetIfTransTransmitBiasCurrentLane2": dellNetIfTransTransmitBiasCurrentLane2,
       "dellNetIfTransTransmitBiasCurrentLane3": dellNetIfTransTransmitBiasCurrentLane3,
       "dellNetIfTransTransmitBiasCurrentLane4": dellNetIfTransTransmitBiasCurrentLane4,
       "dellNetIfAlarmObjects": dellNetIfAlarmObjects,
       "dellNetIfAlarmMibNotifications": dellNetIfAlarmMibNotifications,
       "dellNetIfAlarmHighBer": dellNetIfAlarmHighBer,
       "dellNetIfAlarmHighBerClr": dellNetIfAlarmHighBerClr,
       "dellNetIfAlarmFastRetrain": dellNetIfAlarmFastRetrain,
       "dellNetIfExtensionMibConformance": dellNetIfExtensionMibConformance,
       "dellNetIfExtensionMibCompliances": dellNetIfExtensionMibCompliances,
       "dellNetIfExtensionMibCompliance": dellNetIfExtensionMibCompliance,
       "dellNetIfExtensionMibGroups": dellNetIfExtensionMibGroups,
       "dellNetIfParamsGroup": dellNetIfParamsGroup,
       "dellNetIfStatsGroup": dellNetIfStatsGroup,
       "dellNetIfTransceiverDataGroup": dellNetIfTransceiverDataGroup,
       "dellNetIfNotificationGroup": dellNetIfNotificationGroup}
)
