# SNMP MIB module (TN-DEV-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-AGGREGATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:53 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevAggregation_ObjectIdentity = ObjectIdentity
tnDevAggregation = _TnDevAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38)
)
_TnDevAggrModeCfgTable_Object = MibTable
tnDevAggrModeCfgTable = _TnDevAggrModeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    tnDevAggrModeCfgTable.setStatus("current")
_TnDevAggrModeCfgEntry_Object = MibTableRow
tnDevAggrModeCfgEntry = _TnDevAggrModeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1, 1)
)
tnDevAggrModeCfgEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevAggrModeCfgEntry.setStatus("current")


class _TnDevAggrModeSmac_Type(Integer32):
    """Custom type tnDevAggrModeSmac based on Integer32"""
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


_TnDevAggrModeSmac_Type.__name__ = "Integer32"
_TnDevAggrModeSmac_Object = MibTableColumn
tnDevAggrModeSmac = _TnDevAggrModeSmac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1, 1, 1),
    _TnDevAggrModeSmac_Type()
)
tnDevAggrModeSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevAggrModeSmac.setStatus("current")


class _TnDevAggrModeDmac_Type(Integer32):
    """Custom type tnDevAggrModeDmac based on Integer32"""
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


_TnDevAggrModeDmac_Type.__name__ = "Integer32"
_TnDevAggrModeDmac_Object = MibTableColumn
tnDevAggrModeDmac = _TnDevAggrModeDmac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1, 1, 2),
    _TnDevAggrModeDmac_Type()
)
tnDevAggrModeDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevAggrModeDmac.setStatus("current")


class _TnDevAggrModeSipDip_Type(Integer32):
    """Custom type tnDevAggrModeSipDip based on Integer32"""
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


_TnDevAggrModeSipDip_Type.__name__ = "Integer32"
_TnDevAggrModeSipDip_Object = MibTableColumn
tnDevAggrModeSipDip = _TnDevAggrModeSipDip_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1, 1, 3),
    _TnDevAggrModeSipDip_Type()
)
tnDevAggrModeSipDip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevAggrModeSipDip.setStatus("current")


class _TnDevAggrModeSportDport_Type(Integer32):
    """Custom type tnDevAggrModeSportDport based on Integer32"""
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


_TnDevAggrModeSportDport_Type.__name__ = "Integer32"
_TnDevAggrModeSportDport_Object = MibTableColumn
tnDevAggrModeSportDport = _TnDevAggrModeSportDport_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 1, 1, 4),
    _TnDevAggrModeSportDport_Type()
)
tnDevAggrModeSportDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevAggrModeSportDport.setStatus("current")
_TnDevAggrGroupCfgTable_Object = MibTable
tnDevAggrGroupCfgTable = _TnDevAggrGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 2)
)
if mibBuilder.loadTexts:
    tnDevAggrGroupCfgTable.setStatus("current")
_TnDevAggrGroupCfgEntry_Object = MibTableRow
tnDevAggrGroupCfgEntry = _TnDevAggrGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 2, 1)
)
tnDevAggrGroupCfgEntry.setIndexNames(
    (0, "TN-DEV-AGGREGATION-MIB", "tnDevAggrGroupId"),
)
if mibBuilder.loadTexts:
    tnDevAggrGroupCfgEntry.setStatus("current")
_TnDevAggrGroupId_Type = Unsigned32
_TnDevAggrGroupId_Object = MibTableColumn
tnDevAggrGroupId = _TnDevAggrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 2, 1, 1),
    _TnDevAggrGroupId_Type()
)
tnDevAggrGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDevAggrGroupId.setStatus("current")
_TnDevAggrGroupPortMember_Type = PortList
_TnDevAggrGroupPortMember_Object = MibTableColumn
tnDevAggrGroupPortMember = _TnDevAggrGroupPortMember_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 2, 1, 2),
    _TnDevAggrGroupPortMember_Type()
)
tnDevAggrGroupPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevAggrGroupPortMember.setStatus("current")
_TnDevAggrGroupRowStatus_Type = RowStatus
_TnDevAggrGroupRowStatus_Object = MibTableColumn
tnDevAggrGroupRowStatus = _TnDevAggrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 38, 2, 1, 3),
    _TnDevAggrGroupRowStatus_Type()
)
tnDevAggrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDevAggrGroupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-AGGREGATION-MIB",
    **{"tnDevAggregation": tnDevAggregation,
       "tnDevAggrModeCfgTable": tnDevAggrModeCfgTable,
       "tnDevAggrModeCfgEntry": tnDevAggrModeCfgEntry,
       "tnDevAggrModeSmac": tnDevAggrModeSmac,
       "tnDevAggrModeDmac": tnDevAggrModeDmac,
       "tnDevAggrModeSipDip": tnDevAggrModeSipDip,
       "tnDevAggrModeSportDport": tnDevAggrModeSportDport,
       "tnDevAggrGroupCfgTable": tnDevAggrGroupCfgTable,
       "tnDevAggrGroupCfgEntry": tnDevAggrGroupCfgEntry,
       "tnDevAggrGroupId": tnDevAggrGroupId,
       "tnDevAggrGroupPortMember": tnDevAggrGroupPortMember,
       "tnDevAggrGroupRowStatus": tnDevAggrGroupRowStatus}
)
