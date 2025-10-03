# SNMP MIB module (CTRON-TX-QUEUE-ARBITRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-TX-QUEUE-ARBITRATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:58 2025
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

(ctTxQArb,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTxQArb")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtTxQArbConfig_ObjectIdentity = ObjectIdentity
ctTxQArbConfig = _CtTxQArbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1)
)
_CtTxQPortGroupMapTable_Object = MibTable
ctTxQPortGroupMapTable = _CtTxQPortGroupMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ctTxQPortGroupMapTable.setStatus("mandatory")
_CtTxQPortGroupEntry_Object = MibTableRow
ctTxQPortGroupEntry = _CtTxQPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1)
)
ctTxQPortGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctTxQPortGroupEntry.setStatus("mandatory")
_CtTxQPortGroup_Type = Integer32
_CtTxQPortGroup_Object = MibTableColumn
ctTxQPortGroup = _CtTxQPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1, 1),
    _CtTxQPortGroup_Type()
)
ctTxQPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTxQPortGroup.setStatus("mandatory")
_CtTxQArbTable_Object = MibTable
ctTxQArbTable = _CtTxQArbTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2)
)
if mibBuilder.loadTexts:
    ctTxQArbTable.setStatus("mandatory")
_CtTxQArbEntry_Object = MibTableRow
ctTxQArbEntry = _CtTxQArbEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1)
)
ctTxQArbEntry.setIndexNames(
    (0, "CTRON-TX-QUEUE-ARBITRATION-MIB", "ctTxQPortGroup"),
)
if mibBuilder.loadTexts:
    ctTxQArbEntry.setStatus("mandatory")
_CtTxQArbNumQueues_Type = Integer32
_CtTxQArbNumQueues_Object = MibTableColumn
ctTxQArbNumQueues = _CtTxQArbNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 2),
    _CtTxQArbNumQueues_Type()
)
ctTxQArbNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTxQArbNumQueues.setStatus("mandatory")
_CtTxQArbNumSlices_Type = Integer32
_CtTxQArbNumSlices_Object = MibTableColumn
ctTxQArbNumSlices = _CtTxQArbNumSlices_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 3),
    _CtTxQArbNumSlices_Type()
)
ctTxQArbNumSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTxQArbNumSlices.setStatus("mandatory")
_CtTxQArbSetting_Type = OctetString
_CtTxQArbSetting_Object = MibTableColumn
ctTxQArbSetting = _CtTxQArbSetting_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 4),
    _CtTxQArbSetting_Type()
)
ctTxQArbSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTxQArbSetting.setStatus("mandatory")
_CtTxQBufferConfig_ObjectIdentity = ObjectIdentity
ctTxQBufferConfig = _CtTxQBufferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2)
)


class _CtTxQBufferOptimizeEnable_Type(Integer32):
    """Custom type ctTxQBufferOptimizeEnable based on Integer32"""
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


_CtTxQBufferOptimizeEnable_Type.__name__ = "Integer32"
_CtTxQBufferOptimizeEnable_Object = MibScalar
ctTxQBufferOptimizeEnable = _CtTxQBufferOptimizeEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2, 1),
    _CtTxQBufferOptimizeEnable_Type()
)
ctTxQBufferOptimizeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTxQBufferOptimizeEnable.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-TX-QUEUE-ARBITRATION-MIB",
    **{"ctTxQArbConfig": ctTxQArbConfig,
       "ctTxQPortGroupMapTable": ctTxQPortGroupMapTable,
       "ctTxQPortGroupEntry": ctTxQPortGroupEntry,
       "ctTxQPortGroup": ctTxQPortGroup,
       "ctTxQArbTable": ctTxQArbTable,
       "ctTxQArbEntry": ctTxQArbEntry,
       "ctTxQArbNumQueues": ctTxQArbNumQueues,
       "ctTxQArbNumSlices": ctTxQArbNumSlices,
       "ctTxQArbSetting": ctTxQArbSetting,
       "ctTxQBufferConfig": ctTxQBufferConfig,
       "ctTxQBufferOptimizeEnable": ctTxQBufferOptimizeEnable}
)
