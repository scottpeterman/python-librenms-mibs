# SNMP MIB module (DLINKSW-IF-COUNTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IF-COUNTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:10 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwIfCounterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66)
)
if mibBuilder.loadTexts:
    dlinkSwIfCounterMIB.setRevisions(
        ("2013-02-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIfCounterNotifications_ObjectIdentity = ObjectIdentity
dIfCounterNotifications = _DIfCounterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 0)
)
_DIfCounterObjects_ObjectIdentity = ObjectIdentity
dIfCounterObjects = _DIfCounterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1)
)
_DIfCounterGernal_ObjectIdentity = ObjectIdentity
dIfCounterGernal = _DIfCounterGernal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1)
)
_DIfCounterIfLinkChangeTable_Object = MibTable
dIfCounterIfLinkChangeTable = _DIfCounterIfLinkChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dIfCounterIfLinkChangeTable.setStatus("current")
_DIfCounterIfLinkChangeEntry_Object = MibTableRow
dIfCounterIfLinkChangeEntry = _DIfCounterIfLinkChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 1, 1)
)
dIfCounterIfLinkChangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfCounterIfLinkChangeEntry.setStatus("current")
_DIfCounterIfLinkChange_Type = Counter64
_DIfCounterIfLinkChange_Object = MibTableColumn
dIfCounterIfLinkChange = _DIfCounterIfLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 1, 1, 1),
    _DIfCounterIfLinkChange_Type()
)
dIfCounterIfLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterIfLinkChange.setStatus("current")
_DIfCounterIfUtilizationTable_Object = MibTable
dIfCounterIfUtilizationTable = _DIfCounterIfUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationTable.setStatus("current")
_DIfCounterIfUtilizationEntry_Object = MibTableRow
dIfCounterIfUtilizationEntry = _DIfCounterIfUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 2, 1)
)
dIfCounterIfUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationEntry.setStatus("current")
_DIfCounterIfUtilizationRx_Type = Unsigned32
_DIfCounterIfUtilizationRx_Object = MibTableColumn
dIfCounterIfUtilizationRx = _DIfCounterIfUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 2, 1, 1),
    _DIfCounterIfUtilizationRx_Type()
)
dIfCounterIfUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationRx.setStatus("current")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationRx.setUnits("packets per second")
_DIfCounterIfUtilizationTx_Type = Unsigned32
_DIfCounterIfUtilizationTx_Object = MibTableColumn
dIfCounterIfUtilizationTx = _DIfCounterIfUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 2, 1, 2),
    _DIfCounterIfUtilizationTx_Type()
)
dIfCounterIfUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationTx.setStatus("current")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationTx.setUnits("packets per second")


class _DIfCounterIfUtilizationUtil_Type(Unsigned32):
    """Custom type dIfCounterIfUtilizationUtil based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DIfCounterIfUtilizationUtil_Type.__name__ = "Unsigned32"
_DIfCounterIfUtilizationUtil_Object = MibTableColumn
dIfCounterIfUtilizationUtil = _DIfCounterIfUtilizationUtil_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 1, 2, 1, 3),
    _DIfCounterIfUtilizationUtil_Type()
)
dIfCounterIfUtilizationUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationUtil.setStatus("current")
if mibBuilder.loadTexts:
    dIfCounterIfUtilizationUtil.setUnits("percentage")
_DIfCounterClearCtrl_ObjectIdentity = ObjectIdentity
dIfCounterClearCtrl = _DIfCounterClearCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 2)
)


class _DIfCounterClearAll_Type(Integer32):
    """Custom type dIfCounterClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DIfCounterClearAll_Type.__name__ = "Integer32"
_DIfCounterClearAll_Object = MibScalar
dIfCounterClearAll = _DIfCounterClearAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 2, 1),
    _DIfCounterClearAll_Type()
)
dIfCounterClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIfCounterClearAll.setStatus("current")
_DIfCounterClearIf_Type = InterfaceIndexOrZero
_DIfCounterClearIf_Object = MibScalar
dIfCounterClearIf = _DIfCounterClearIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 2, 2),
    _DIfCounterClearIf_Type()
)
dIfCounterClearIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIfCounterClearIf.setStatus("current")
_DIfCounterRxStatistics_ObjectIdentity = ObjectIdentity
dIfCounterRxStatistics = _DIfCounterRxStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3)
)
_DIfRxStatsTable_Object = MibTable
dIfRxStatsTable = _DIfRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dIfRxStatsTable.setStatus("current")
_DIfRxStatsEntry_Object = MibTableRow
dIfRxStatsEntry = _DIfRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1)
)
dIfRxStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfRxStatsEntry.setStatus("current")
_DIfRxStatsHCPkts_Type = Counter64
_DIfRxStatsHCPkts_Object = MibTableColumn
dIfRxStatsHCPkts = _DIfRxStatsHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 1),
    _DIfRxStatsHCPkts_Type()
)
dIfRxStatsHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts.setStatus("current")
_DIfRxStatsHCPkts64Octets_Type = Counter64
_DIfRxStatsHCPkts64Octets_Object = MibTableColumn
dIfRxStatsHCPkts64Octets = _DIfRxStatsHCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 2),
    _DIfRxStatsHCPkts64Octets_Type()
)
dIfRxStatsHCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts64Octets.setStatus("current")
_DIfRxStatsHCPkts65to127Octets_Type = Counter64
_DIfRxStatsHCPkts65to127Octets_Object = MibTableColumn
dIfRxStatsHCPkts65to127Octets = _DIfRxStatsHCPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 3),
    _DIfRxStatsHCPkts65to127Octets_Type()
)
dIfRxStatsHCPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts65to127Octets.setStatus("current")
_DIfRxStatsHCPkts128to255Octets_Type = Counter64
_DIfRxStatsHCPkts128to255Octets_Object = MibTableColumn
dIfRxStatsHCPkts128to255Octets = _DIfRxStatsHCPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 4),
    _DIfRxStatsHCPkts128to255Octets_Type()
)
dIfRxStatsHCPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts128to255Octets.setStatus("current")
_DIfRxStatsHCPkts256to511Octets_Type = Counter64
_DIfRxStatsHCPkts256to511Octets_Object = MibTableColumn
dIfRxStatsHCPkts256to511Octets = _DIfRxStatsHCPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 5),
    _DIfRxStatsHCPkts256to511Octets_Type()
)
dIfRxStatsHCPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts256to511Octets.setStatus("current")
_DIfRxStatsHCPkts512to1023Octets_Type = Counter64
_DIfRxStatsHCPkts512to1023Octets_Object = MibTableColumn
dIfRxStatsHCPkts512to1023Octets = _DIfRxStatsHCPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 6),
    _DIfRxStatsHCPkts512to1023Octets_Type()
)
dIfRxStatsHCPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts512to1023Octets.setStatus("current")
_DIfRxStatsHCPkts1024to1518Octets_Type = Counter64
_DIfRxStatsHCPkts1024to1518Octets_Object = MibTableColumn
dIfRxStatsHCPkts1024to1518Octets = _DIfRxStatsHCPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 7),
    _DIfRxStatsHCPkts1024to1518Octets_Type()
)
dIfRxStatsHCPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts1024to1518Octets.setStatus("current")
_DIfRxStatsHCPkts1519to1522Octets_Type = Counter64
_DIfRxStatsHCPkts1519to1522Octets_Object = MibTableColumn
dIfRxStatsHCPkts1519to1522Octets = _DIfRxStatsHCPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 8),
    _DIfRxStatsHCPkts1519to1522Octets_Type()
)
dIfRxStatsHCPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts1519to1522Octets.setStatus("current")
_DIfRxStatsHCPkts1519to2047Octets_Type = Counter64
_DIfRxStatsHCPkts1519to2047Octets_Object = MibTableColumn
dIfRxStatsHCPkts1519to2047Octets = _DIfRxStatsHCPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 9),
    _DIfRxStatsHCPkts1519to2047Octets_Type()
)
dIfRxStatsHCPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts1519to2047Octets.setStatus("current")
_DIfRxStatsHCPkts2048to4095Octets_Type = Counter64
_DIfRxStatsHCPkts2048to4095Octets_Object = MibTableColumn
dIfRxStatsHCPkts2048to4095Octets = _DIfRxStatsHCPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 10),
    _DIfRxStatsHCPkts2048to4095Octets_Type()
)
dIfRxStatsHCPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts2048to4095Octets.setStatus("current")
_DIfRxStatsHCPkts4096to9216Octets_Type = Counter64
_DIfRxStatsHCPkts4096to9216Octets_Object = MibTableColumn
dIfRxStatsHCPkts4096to9216Octets = _DIfRxStatsHCPkts4096to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 1, 1, 11),
    _DIfRxStatsHCPkts4096to9216Octets_Type()
)
dIfRxStatsHCPkts4096to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfRxStatsHCPkts4096to9216Octets.setStatus("current")
_DIfCounterRxDropTable_Object = MibTable
dIfCounterRxDropTable = _DIfCounterRxDropTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dIfCounterRxDropTable.setStatus("current")
_DIfCounterRxDropEntry_Object = MibTableRow
dIfCounterRxDropEntry = _DIfCounterRxDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1)
)
dIfCounterRxDropEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfCounterRxDropEntry.setStatus("current")
_DIfCounterRxBufferFullDrops_Type = Counter64
_DIfCounterRxBufferFullDrops_Object = MibTableColumn
dIfCounterRxBufferFullDrops = _DIfCounterRxBufferFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 1),
    _DIfCounterRxBufferFullDrops_Type()
)
dIfCounterRxBufferFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxBufferFullDrops.setStatus("current")
_DIfCounterRxACLDrops_Type = Counter64
_DIfCounterRxACLDrops_Object = MibTableColumn
dIfCounterRxACLDrops = _DIfCounterRxACLDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 2),
    _DIfCounterRxACLDrops_Type()
)
dIfCounterRxACLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxACLDrops.setStatus("current")
_DIfCounterRxMulticastDrops_Type = Counter64
_DIfCounterRxMulticastDrops_Object = MibTableColumn
dIfCounterRxMulticastDrops = _DIfCounterRxMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 3),
    _DIfCounterRxMulticastDrops_Type()
)
dIfCounterRxMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxMulticastDrops.setStatus("current")
_DIfCounterRxVLANIngressDrops_Type = Counter64
_DIfCounterRxVLANIngressDrops_Object = MibTableColumn
dIfCounterRxVLANIngressDrops = _DIfCounterRxVLANIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 4),
    _DIfCounterRxVLANIngressDrops_Type()
)
dIfCounterRxVLANIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxVLANIngressDrops.setStatus("current")
_DIfCounterRxIPv6Drops_Type = Counter64
_DIfCounterRxIPv6Drops_Object = MibTableColumn
dIfCounterRxIPv6Drops = _DIfCounterRxIPv6Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 5),
    _DIfCounterRxIPv6Drops_Type()
)
dIfCounterRxIPv6Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxIPv6Drops.setStatus("current")
_DIfCounterRxSTPDrops_Type = Counter64
_DIfCounterRxSTPDrops_Object = MibTableColumn
dIfCounterRxSTPDrops = _DIfCounterRxSTPDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 6),
    _DIfCounterRxSTPDrops_Type()
)
dIfCounterRxSTPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxSTPDrops.setStatus("current")
_DIfCounterRxStormAndTableDiscard_Type = Counter64
_DIfCounterRxStormAndTableDiscard_Object = MibTableColumn
dIfCounterRxStormAndTableDiscard = _DIfCounterRxStormAndTableDiscard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 7),
    _DIfCounterRxStormAndTableDiscard_Type()
)
dIfCounterRxStormAndTableDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxStormAndTableDiscard.setStatus("current")
_DIfCounterRxMTUDrops_Type = Counter64
_DIfCounterRxMTUDrops_Object = MibTableColumn
dIfCounterRxMTUDrops = _DIfCounterRxMTUDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 8),
    _DIfCounterRxMTUDrops_Type()
)
dIfCounterRxMTUDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxMTUDrops.setStatus("current")
_DIfCounterRxInvalidDestPort_Type = Counter64
_DIfCounterRxInvalidDestPort_Object = MibTableColumn
dIfCounterRxInvalidDestPort = _DIfCounterRxInvalidDestPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 9),
    _DIfCounterRxInvalidDestPort_Type()
)
dIfCounterRxInvalidDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxInvalidDestPort.setStatus("current")
_DIfCounterRxBandwidthCtrlDrops_Type = Counter64
_DIfCounterRxBandwidthCtrlDrops_Object = MibTableColumn
dIfCounterRxBandwidthCtrlDrops = _DIfCounterRxBandwidthCtrlDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 3, 2, 1, 10),
    _DIfCounterRxBandwidthCtrlDrops_Type()
)
dIfCounterRxBandwidthCtrlDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterRxBandwidthCtrlDrops.setStatus("current")
_DIfCounterTxStatistics_ObjectIdentity = ObjectIdentity
dIfCounterTxStatistics = _DIfCounterTxStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4)
)
_DIfTxStatsTable_Object = MibTable
dIfTxStatsTable = _DIfTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dIfTxStatsTable.setStatus("current")
_DIfTxStatsEntry_Object = MibTableRow
dIfTxStatsEntry = _DIfTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1)
)
dIfTxStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfTxStatsEntry.setStatus("current")
_DIfTxStatsHCPkts_Type = Counter64
_DIfTxStatsHCPkts_Object = MibTableColumn
dIfTxStatsHCPkts = _DIfTxStatsHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 1),
    _DIfTxStatsHCPkts_Type()
)
dIfTxStatsHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts.setStatus("current")
_DIfTxStatsHCPkts64Octets_Type = Counter64
_DIfTxStatsHCPkts64Octets_Object = MibTableColumn
dIfTxStatsHCPkts64Octets = _DIfTxStatsHCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 2),
    _DIfTxStatsHCPkts64Octets_Type()
)
dIfTxStatsHCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts64Octets.setStatus("current")
_DIfTxStatsHCPkts65to127Octets_Type = Counter64
_DIfTxStatsHCPkts65to127Octets_Object = MibTableColumn
dIfTxStatsHCPkts65to127Octets = _DIfTxStatsHCPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 3),
    _DIfTxStatsHCPkts65to127Octets_Type()
)
dIfTxStatsHCPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts65to127Octets.setStatus("current")
_DIfTxStatsHCPkts128to255Octets_Type = Counter64
_DIfTxStatsHCPkts128to255Octets_Object = MibTableColumn
dIfTxStatsHCPkts128to255Octets = _DIfTxStatsHCPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 4),
    _DIfTxStatsHCPkts128to255Octets_Type()
)
dIfTxStatsHCPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts128to255Octets.setStatus("current")
_DIfTxStatsHCPkts256to511Octets_Type = Counter64
_DIfTxStatsHCPkts256to511Octets_Object = MibTableColumn
dIfTxStatsHCPkts256to511Octets = _DIfTxStatsHCPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 5),
    _DIfTxStatsHCPkts256to511Octets_Type()
)
dIfTxStatsHCPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts256to511Octets.setStatus("current")
_DIfTxStatsHCPkts512to1023Octets_Type = Counter64
_DIfTxStatsHCPkts512to1023Octets_Object = MibTableColumn
dIfTxStatsHCPkts512to1023Octets = _DIfTxStatsHCPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 6),
    _DIfTxStatsHCPkts512to1023Octets_Type()
)
dIfTxStatsHCPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts512to1023Octets.setStatus("current")
_DIfTxStatsHCPkts1024to1518Octets_Type = Counter64
_DIfTxStatsHCPkts1024to1518Octets_Object = MibTableColumn
dIfTxStatsHCPkts1024to1518Octets = _DIfTxStatsHCPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 7),
    _DIfTxStatsHCPkts1024to1518Octets_Type()
)
dIfTxStatsHCPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts1024to1518Octets.setStatus("current")
_DIfTxStatsHCPkts1519to1522Octets_Type = Counter64
_DIfTxStatsHCPkts1519to1522Octets_Object = MibTableColumn
dIfTxStatsHCPkts1519to1522Octets = _DIfTxStatsHCPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 8),
    _DIfTxStatsHCPkts1519to1522Octets_Type()
)
dIfTxStatsHCPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts1519to1522Octets.setStatus("current")
_DIfTxStatsHCPkts1519to2047Octets_Type = Counter64
_DIfTxStatsHCPkts1519to2047Octets_Object = MibTableColumn
dIfTxStatsHCPkts1519to2047Octets = _DIfTxStatsHCPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 9),
    _DIfTxStatsHCPkts1519to2047Octets_Type()
)
dIfTxStatsHCPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts1519to2047Octets.setStatus("current")
_DIfTxStatsHCPkts2048to4095Octets_Type = Counter64
_DIfTxStatsHCPkts2048to4095Octets_Object = MibTableColumn
dIfTxStatsHCPkts2048to4095Octets = _DIfTxStatsHCPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 10),
    _DIfTxStatsHCPkts2048to4095Octets_Type()
)
dIfTxStatsHCPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts2048to4095Octets.setStatus("current")
_DIfTxStatsHCPkts4096to9216Octets_Type = Counter64
_DIfTxStatsHCPkts4096to9216Octets_Object = MibTableColumn
dIfTxStatsHCPkts4096to9216Octets = _DIfTxStatsHCPkts4096to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 11),
    _DIfTxStatsHCPkts4096to9216Octets_Type()
)
dIfTxStatsHCPkts4096to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsHCPkts4096to9216Octets.setStatus("current")
_DIfTxStatsFCSErrors_Type = Counter64
_DIfTxStatsFCSErrors_Object = MibTableColumn
dIfTxStatsFCSErrors = _DIfTxStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 1, 1, 12),
    _DIfTxStatsFCSErrors_Type()
)
dIfTxStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfTxStatsFCSErrors.setStatus("current")
_DIfCounterTxDropTable_Object = MibTable
dIfCounterTxDropTable = _DIfCounterTxDropTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dIfCounterTxDropTable.setStatus("current")
_DIfCounterTxDropEntry_Object = MibTableRow
dIfCounterTxDropEntry = _DIfCounterTxDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1)
)
dIfCounterTxDropEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIfCounterTxDropEntry.setStatus("current")
_DIfCounterTxSTPDrops_Type = Counter64
_DIfCounterTxSTPDrops_Object = MibTableColumn
dIfCounterTxSTPDrops = _DIfCounterTxSTPDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 1),
    _DIfCounterTxSTPDrops_Type()
)
dIfCounterTxSTPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxSTPDrops.setStatus("current")
_DIfCounterTxHOLDrops_Type = Counter64
_DIfCounterTxHOLDrops_Object = MibTableColumn
dIfCounterTxHOLDrops = _DIfCounterTxHOLDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 2),
    _DIfCounterTxHOLDrops_Type()
)
dIfCounterTxHOLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxHOLDrops.setStatus("current")
_DIfCounterTxCOS0Drops_Type = Counter64
_DIfCounterTxCOS0Drops_Object = MibTableColumn
dIfCounterTxCOS0Drops = _DIfCounterTxCOS0Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 3),
    _DIfCounterTxCOS0Drops_Type()
)
dIfCounterTxCOS0Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS0Drops.setStatus("current")
_DIfCounterTxCOS1Drops_Type = Counter64
_DIfCounterTxCOS1Drops_Object = MibTableColumn
dIfCounterTxCOS1Drops = _DIfCounterTxCOS1Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 4),
    _DIfCounterTxCOS1Drops_Type()
)
dIfCounterTxCOS1Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS1Drops.setStatus("current")
_DIfCounterTxCOS2Drops_Type = Counter64
_DIfCounterTxCOS2Drops_Object = MibTableColumn
dIfCounterTxCOS2Drops = _DIfCounterTxCOS2Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 5),
    _DIfCounterTxCOS2Drops_Type()
)
dIfCounterTxCOS2Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS2Drops.setStatus("current")
_DIfCounterTxCOS3Drops_Type = Counter64
_DIfCounterTxCOS3Drops_Object = MibTableColumn
dIfCounterTxCOS3Drops = _DIfCounterTxCOS3Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 6),
    _DIfCounterTxCOS3Drops_Type()
)
dIfCounterTxCOS3Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS3Drops.setStatus("current")
_DIfCounterTxCOS4Drops_Type = Counter64
_DIfCounterTxCOS4Drops_Object = MibTableColumn
dIfCounterTxCOS4Drops = _DIfCounterTxCOS4Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 7),
    _DIfCounterTxCOS4Drops_Type()
)
dIfCounterTxCOS4Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS4Drops.setStatus("current")
_DIfCounterTxCOS5Drops_Type = Counter64
_DIfCounterTxCOS5Drops_Object = MibTableColumn
dIfCounterTxCOS5Drops = _DIfCounterTxCOS5Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 8),
    _DIfCounterTxCOS5Drops_Type()
)
dIfCounterTxCOS5Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS5Drops.setStatus("current")
_DIfCounterTxCOS6Drops_Type = Counter64
_DIfCounterTxCOS6Drops_Object = MibTableColumn
dIfCounterTxCOS6Drops = _DIfCounterTxCOS6Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 9),
    _DIfCounterTxCOS6Drops_Type()
)
dIfCounterTxCOS6Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS6Drops.setStatus("current")
_DIfCounterTxCOS7Drops_Type = Counter64
_DIfCounterTxCOS7Drops_Object = MibTableColumn
dIfCounterTxCOS7Drops = _DIfCounterTxCOS7Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 1, 4, 2, 1, 10),
    _DIfCounterTxCOS7Drops_Type()
)
dIfCounterTxCOS7Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIfCounterTxCOS7Drops.setStatus("current")
_DIfCounterConformance_ObjectIdentity = ObjectIdentity
dIfCounterConformance = _DIfCounterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2)
)
_DIfCounterCompliances_ObjectIdentity = ObjectIdentity
dIfCounterCompliances = _DIfCounterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 1)
)
_DIfCounterGroups_ObjectIdentity = ObjectIdentity
dIfCounterGroups = _DIfCounterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2)
)

# Managed Objects groups

dIfCounterIfLinkChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2, 1)
)
dIfCounterIfLinkChangeGroup.setObjects(
    ("DLINKSW-IF-COUNTER-MIB", "dIfCounterIfLinkChange")
)
if mibBuilder.loadTexts:
    dIfCounterIfLinkChangeGroup.setStatus("current")

dIfCounterUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2, 2)
)
dIfCounterUtilizationGroup.setObjects(
      *(("DLINKSW-IF-COUNTER-MIB", "dIfCounterIfUtilizationRx"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterIfUtilizationTx"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterIfUtilizationUtil"))
)
if mibBuilder.loadTexts:
    dIfCounterUtilizationGroup.setStatus("current")

dIfCounterClearCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2, 3)
)
dIfCounterClearCtrlGroup.setObjects(
      *(("DLINKSW-IF-COUNTER-MIB", "dIfCounterClearAll"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterClearIf"))
)
if mibBuilder.loadTexts:
    dIfCounterClearCtrlGroup.setStatus("current")

dIfCounterHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2, 4)
)
dIfCounterHCStatsGroup.setObjects(
      *(("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts64Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts65to127Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts128to255Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts256to511Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts512to1023Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts1024to1518Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts1519to1522Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts1519to2047Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts2048to4095Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfRxStatsHCPkts4096to9216Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts64Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts65to127Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts128to255Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts256to511Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts512to1023Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts1024to1518Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts1519to1522Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts1519to2047Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts2048to4095Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsHCPkts4096to9216Octets"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfTxStatsFCSErrors"))
)
if mibBuilder.loadTexts:
    dIfCounterHCStatsGroup.setStatus("current")

dIfCounterDropStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 2, 5)
)
dIfCounterDropStatsGroup.setObjects(
      *(("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxBufferFullDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxACLDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxMulticastDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxVLANIngressDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxIPv6Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxSTPDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxStormAndTableDiscard"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxMTUDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxInvalidDestPort"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterRxBandwidthCtrlDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxSTPDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxHOLDrops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS0Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS1Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS2Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS3Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS4Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS5Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS6Drops"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterTxCOS7Drops"))
)
if mibBuilder.loadTexts:
    dIfCounterDropStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIfCounterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 66, 2, 1, 1)
)
dIfCounterCompliance.setObjects(
      *(("DLINKSW-IF-COUNTER-MIB", "dIfCounterUtilizationGroup"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterClearCtrlGroup"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterHCStatsGroup"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterIfLinkChangeGroup"),
        ("DLINKSW-IF-COUNTER-MIB", "dIfCounterDropStatsGroup"))
)
if mibBuilder.loadTexts:
    dIfCounterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IF-COUNTER-MIB",
    **{"dlinkSwIfCounterMIB": dlinkSwIfCounterMIB,
       "dIfCounterNotifications": dIfCounterNotifications,
       "dIfCounterObjects": dIfCounterObjects,
       "dIfCounterGernal": dIfCounterGernal,
       "dIfCounterIfLinkChangeTable": dIfCounterIfLinkChangeTable,
       "dIfCounterIfLinkChangeEntry": dIfCounterIfLinkChangeEntry,
       "dIfCounterIfLinkChange": dIfCounterIfLinkChange,
       "dIfCounterIfUtilizationTable": dIfCounterIfUtilizationTable,
       "dIfCounterIfUtilizationEntry": dIfCounterIfUtilizationEntry,
       "dIfCounterIfUtilizationRx": dIfCounterIfUtilizationRx,
       "dIfCounterIfUtilizationTx": dIfCounterIfUtilizationTx,
       "dIfCounterIfUtilizationUtil": dIfCounterIfUtilizationUtil,
       "dIfCounterClearCtrl": dIfCounterClearCtrl,
       "dIfCounterClearAll": dIfCounterClearAll,
       "dIfCounterClearIf": dIfCounterClearIf,
       "dIfCounterRxStatistics": dIfCounterRxStatistics,
       "dIfRxStatsTable": dIfRxStatsTable,
       "dIfRxStatsEntry": dIfRxStatsEntry,
       "dIfRxStatsHCPkts": dIfRxStatsHCPkts,
       "dIfRxStatsHCPkts64Octets": dIfRxStatsHCPkts64Octets,
       "dIfRxStatsHCPkts65to127Octets": dIfRxStatsHCPkts65to127Octets,
       "dIfRxStatsHCPkts128to255Octets": dIfRxStatsHCPkts128to255Octets,
       "dIfRxStatsHCPkts256to511Octets": dIfRxStatsHCPkts256to511Octets,
       "dIfRxStatsHCPkts512to1023Octets": dIfRxStatsHCPkts512to1023Octets,
       "dIfRxStatsHCPkts1024to1518Octets": dIfRxStatsHCPkts1024to1518Octets,
       "dIfRxStatsHCPkts1519to1522Octets": dIfRxStatsHCPkts1519to1522Octets,
       "dIfRxStatsHCPkts1519to2047Octets": dIfRxStatsHCPkts1519to2047Octets,
       "dIfRxStatsHCPkts2048to4095Octets": dIfRxStatsHCPkts2048to4095Octets,
       "dIfRxStatsHCPkts4096to9216Octets": dIfRxStatsHCPkts4096to9216Octets,
       "dIfCounterRxDropTable": dIfCounterRxDropTable,
       "dIfCounterRxDropEntry": dIfCounterRxDropEntry,
       "dIfCounterRxBufferFullDrops": dIfCounterRxBufferFullDrops,
       "dIfCounterRxACLDrops": dIfCounterRxACLDrops,
       "dIfCounterRxMulticastDrops": dIfCounterRxMulticastDrops,
       "dIfCounterRxVLANIngressDrops": dIfCounterRxVLANIngressDrops,
       "dIfCounterRxIPv6Drops": dIfCounterRxIPv6Drops,
       "dIfCounterRxSTPDrops": dIfCounterRxSTPDrops,
       "dIfCounterRxStormAndTableDiscard": dIfCounterRxStormAndTableDiscard,
       "dIfCounterRxMTUDrops": dIfCounterRxMTUDrops,
       "dIfCounterRxInvalidDestPort": dIfCounterRxInvalidDestPort,
       "dIfCounterRxBandwidthCtrlDrops": dIfCounterRxBandwidthCtrlDrops,
       "dIfCounterTxStatistics": dIfCounterTxStatistics,
       "dIfTxStatsTable": dIfTxStatsTable,
       "dIfTxStatsEntry": dIfTxStatsEntry,
       "dIfTxStatsHCPkts": dIfTxStatsHCPkts,
       "dIfTxStatsHCPkts64Octets": dIfTxStatsHCPkts64Octets,
       "dIfTxStatsHCPkts65to127Octets": dIfTxStatsHCPkts65to127Octets,
       "dIfTxStatsHCPkts128to255Octets": dIfTxStatsHCPkts128to255Octets,
       "dIfTxStatsHCPkts256to511Octets": dIfTxStatsHCPkts256to511Octets,
       "dIfTxStatsHCPkts512to1023Octets": dIfTxStatsHCPkts512to1023Octets,
       "dIfTxStatsHCPkts1024to1518Octets": dIfTxStatsHCPkts1024to1518Octets,
       "dIfTxStatsHCPkts1519to1522Octets": dIfTxStatsHCPkts1519to1522Octets,
       "dIfTxStatsHCPkts1519to2047Octets": dIfTxStatsHCPkts1519to2047Octets,
       "dIfTxStatsHCPkts2048to4095Octets": dIfTxStatsHCPkts2048to4095Octets,
       "dIfTxStatsHCPkts4096to9216Octets": dIfTxStatsHCPkts4096to9216Octets,
       "dIfTxStatsFCSErrors": dIfTxStatsFCSErrors,
       "dIfCounterTxDropTable": dIfCounterTxDropTable,
       "dIfCounterTxDropEntry": dIfCounterTxDropEntry,
       "dIfCounterTxSTPDrops": dIfCounterTxSTPDrops,
       "dIfCounterTxHOLDrops": dIfCounterTxHOLDrops,
       "dIfCounterTxCOS0Drops": dIfCounterTxCOS0Drops,
       "dIfCounterTxCOS1Drops": dIfCounterTxCOS1Drops,
       "dIfCounterTxCOS2Drops": dIfCounterTxCOS2Drops,
       "dIfCounterTxCOS3Drops": dIfCounterTxCOS3Drops,
       "dIfCounterTxCOS4Drops": dIfCounterTxCOS4Drops,
       "dIfCounterTxCOS5Drops": dIfCounterTxCOS5Drops,
       "dIfCounterTxCOS6Drops": dIfCounterTxCOS6Drops,
       "dIfCounterTxCOS7Drops": dIfCounterTxCOS7Drops,
       "dIfCounterConformance": dIfCounterConformance,
       "dIfCounterCompliances": dIfCounterCompliances,
       "dIfCounterCompliance": dIfCounterCompliance,
       "dIfCounterGroups": dIfCounterGroups,
       "dIfCounterIfLinkChangeGroup": dIfCounterIfLinkChangeGroup,
       "dIfCounterUtilizationGroup": dIfCounterUtilizationGroup,
       "dIfCounterClearCtrlGroup": dIfCounterClearCtrlGroup,
       "dIfCounterHCStatsGroup": dIfCounterHCStatsGroup,
       "dIfCounterDropStatsGroup": dIfCounterDropStatsGroup}
)
