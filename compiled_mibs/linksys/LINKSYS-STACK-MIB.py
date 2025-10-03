# SNMP MIB module (LINKSYS-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-STACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:01 2025
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107)
)
if mibBuilder.loadTexts:
    rlStack.setRevisions(
        ("2005-04-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStackActiveUnitIdTable_Object = MibTable
rlStackActiveUnitIdTable = _RlStackActiveUnitIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 1)
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdTable.setStatus("current")
_RlStackActiveUnitIdEntry_Object = MibTableRow
rlStackActiveUnitIdEntry = _RlStackActiveUnitIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 1, 1)
)
rlStackActiveUnitIdEntry.setIndexNames(
    (0, "LINKSYS-STACK-MIB", "rlStackCurrentUnitId"),
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdEntry.setStatus("current")
_RlStackCurrentUnitId_Type = Integer32
_RlStackCurrentUnitId_Object = MibTableColumn
rlStackCurrentUnitId = _RlStackCurrentUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 1, 1, 1),
    _RlStackCurrentUnitId_Type()
)
rlStackCurrentUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlStackCurrentUnitId.setStatus("current")


class _RlStackActiveUnitIdAfterReset_Type(Integer32):
    """Custom type rlStackActiveUnitIdAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlStackActiveUnitIdAfterReset_Type.__name__ = "Integer32"
_RlStackActiveUnitIdAfterReset_Object = MibTableColumn
rlStackActiveUnitIdAfterReset = _RlStackActiveUnitIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 1, 1, 2),
    _RlStackActiveUnitIdAfterReset_Type()
)
rlStackActiveUnitIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackActiveUnitIdAfterReset.setStatus("current")


class _RlStackUnitModeAfterReset_Type(Integer32):
    """Custom type rlStackUnitModeAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("stack", 2))
    )


_RlStackUnitModeAfterReset_Type.__name__ = "Integer32"
_RlStackUnitModeAfterReset_Object = MibScalar
rlStackUnitModeAfterReset = _RlStackUnitModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 2),
    _RlStackUnitModeAfterReset_Type()
)
rlStackUnitModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitModeAfterReset.setStatus("current")


class _RlStackUnitMode_Type(Integer32):
    """Custom type rlStackUnitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("stack", 2))
    )


_RlStackUnitMode_Type.__name__ = "Integer32"
_RlStackUnitMode_Object = MibScalar
rlStackUnitMode = _RlStackUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 3),
    _RlStackUnitMode_Type()
)
rlStackUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackUnitMode.setStatus("current")
_RlStackUnitMacAddressAfterReset_Type = MacAddress
_RlStackUnitMacAddressAfterReset_Object = MibScalar
rlStackUnitMacAddressAfterReset = _RlStackUnitMacAddressAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 107, 4),
    _RlStackUnitMacAddressAfterReset_Type()
)
rlStackUnitMacAddressAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitMacAddressAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-STACK-MIB",
    **{"rlStack": rlStack,
       "rlStackActiveUnitIdTable": rlStackActiveUnitIdTable,
       "rlStackActiveUnitIdEntry": rlStackActiveUnitIdEntry,
       "rlStackCurrentUnitId": rlStackCurrentUnitId,
       "rlStackActiveUnitIdAfterReset": rlStackActiveUnitIdAfterReset,
       "rlStackUnitModeAfterReset": rlStackUnitModeAfterReset,
       "rlStackUnitMode": rlStackUnitMode,
       "rlStackUnitMacAddressAfterReset": rlStackUnitMacAddressAfterReset}
)
