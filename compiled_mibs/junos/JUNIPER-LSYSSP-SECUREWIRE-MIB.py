# SNMP MIB module (JUNIPER-LSYSSP-SECUREWIRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-LSYSSP-SECUREWIRE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:56 2025
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

(jnxLsysSpSecurewire,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpSecurewire")

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

jnxLsysSpSecurewireMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpSecurewireObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpSecurewireObjects = _JnxLsysSpSecurewireObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1)
)
_JnxLsysSpSecurewireTable_Object = MibTable
jnxLsysSpSecurewireTable = _JnxLsysSpSecurewireTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireTable.setStatus("current")
_JnxLsysSpSecurewireEntry_Object = MibTableRow
jnxLsysSpSecurewireEntry = _JnxLsysSpSecurewireEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1)
)
jnxLsysSpSecurewireEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-SECUREWIRE-MIB", "jnxLsysSpSecurewireLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireEntry.setStatus("current")


class _JnxLsysSpSecurewireLsysName_Type(DisplayString):
    """Custom type jnxLsysSpSecurewireLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSecurewireLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpSecurewireLsysName_Object = MibTableColumn
jnxLsysSpSecurewireLsysName = _JnxLsysSpSecurewireLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1, 1),
    _JnxLsysSpSecurewireLsysName_Type()
)
jnxLsysSpSecurewireLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireLsysName.setStatus("current")


class _JnxLsysSpSecurewireProfileName_Type(DisplayString):
    """Custom type jnxLsysSpSecurewireProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpSecurewireProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpSecurewireProfileName_Object = MibTableColumn
jnxLsysSpSecurewireProfileName = _JnxLsysSpSecurewireProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1, 2),
    _JnxLsysSpSecurewireProfileName_Type()
)
jnxLsysSpSecurewireProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireProfileName.setStatus("current")
_JnxLsysSpSecurewireUsage_Type = Unsigned32
_JnxLsysSpSecurewireUsage_Object = MibTableColumn
jnxLsysSpSecurewireUsage = _JnxLsysSpSecurewireUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1, 3),
    _JnxLsysSpSecurewireUsage_Type()
)
jnxLsysSpSecurewireUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireUsage.setStatus("current")
_JnxLsysSpSecurewireReserved_Type = Unsigned32
_JnxLsysSpSecurewireReserved_Object = MibTableColumn
jnxLsysSpSecurewireReserved = _JnxLsysSpSecurewireReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1, 4),
    _JnxLsysSpSecurewireReserved_Type()
)
jnxLsysSpSecurewireReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireReserved.setStatus("current")
_JnxLsysSpSecurewireMaximum_Type = Unsigned32
_JnxLsysSpSecurewireMaximum_Object = MibTableColumn
jnxLsysSpSecurewireMaximum = _JnxLsysSpSecurewireMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 1, 1, 1, 5),
    _JnxLsysSpSecurewireMaximum_Type()
)
jnxLsysSpSecurewireMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireMaximum.setStatus("current")
_JnxLsysSpSecurewireSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpSecurewireSummary = _JnxLsysSpSecurewireSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2)
)
_JnxLsysSpSecurewireUsedAmount_Type = Unsigned32
_JnxLsysSpSecurewireUsedAmount_Object = MibScalar
jnxLsysSpSecurewireUsedAmount = _JnxLsysSpSecurewireUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 1),
    _JnxLsysSpSecurewireUsedAmount_Type()
)
jnxLsysSpSecurewireUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireUsedAmount.setStatus("current")
_JnxLsysSpSecurewireMaxQuota_Type = Unsigned32
_JnxLsysSpSecurewireMaxQuota_Object = MibScalar
jnxLsysSpSecurewireMaxQuota = _JnxLsysSpSecurewireMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 2),
    _JnxLsysSpSecurewireMaxQuota_Type()
)
jnxLsysSpSecurewireMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireMaxQuota.setStatus("current")
_JnxLsysSpSecurewireAvailableAmount_Type = Unsigned32
_JnxLsysSpSecurewireAvailableAmount_Object = MibScalar
jnxLsysSpSecurewireAvailableAmount = _JnxLsysSpSecurewireAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 3),
    _JnxLsysSpSecurewireAvailableAmount_Type()
)
jnxLsysSpSecurewireAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireAvailableAmount.setStatus("current")
_JnxLsysSpSecurewireHeaviestUsage_Type = Unsigned32
_JnxLsysSpSecurewireHeaviestUsage_Object = MibScalar
jnxLsysSpSecurewireHeaviestUsage = _JnxLsysSpSecurewireHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 4),
    _JnxLsysSpSecurewireHeaviestUsage_Type()
)
jnxLsysSpSecurewireHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireHeaviestUsage.setStatus("current")


class _JnxLsysSpSecurewireHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpSecurewireHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSecurewireHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSecurewireHeaviestUser_Object = MibScalar
jnxLsysSpSecurewireHeaviestUser = _JnxLsysSpSecurewireHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 5),
    _JnxLsysSpSecurewireHeaviestUser_Type()
)
jnxLsysSpSecurewireHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireHeaviestUser.setStatus("current")
_JnxLsysSpSecurewireLightestUsage_Type = Unsigned32
_JnxLsysSpSecurewireLightestUsage_Object = MibScalar
jnxLsysSpSecurewireLightestUsage = _JnxLsysSpSecurewireLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 6),
    _JnxLsysSpSecurewireLightestUsage_Type()
)
jnxLsysSpSecurewireLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireLightestUsage.setStatus("current")


class _JnxLsysSpSecurewireLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpSecurewireLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpSecurewireLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpSecurewireLightestUser_Object = MibScalar
jnxLsysSpSecurewireLightestUser = _JnxLsysSpSecurewireLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 20, 1, 2, 7),
    _JnxLsysSpSecurewireLightestUser_Type()
)
jnxLsysSpSecurewireLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpSecurewireLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-SECUREWIRE-MIB",
    **{"jnxLsysSpSecurewireMIB": jnxLsysSpSecurewireMIB,
       "jnxLsysSpSecurewireObjects": jnxLsysSpSecurewireObjects,
       "jnxLsysSpSecurewireTable": jnxLsysSpSecurewireTable,
       "jnxLsysSpSecurewireEntry": jnxLsysSpSecurewireEntry,
       "jnxLsysSpSecurewireLsysName": jnxLsysSpSecurewireLsysName,
       "jnxLsysSpSecurewireProfileName": jnxLsysSpSecurewireProfileName,
       "jnxLsysSpSecurewireUsage": jnxLsysSpSecurewireUsage,
       "jnxLsysSpSecurewireReserved": jnxLsysSpSecurewireReserved,
       "jnxLsysSpSecurewireMaximum": jnxLsysSpSecurewireMaximum,
       "jnxLsysSpSecurewireSummary": jnxLsysSpSecurewireSummary,
       "jnxLsysSpSecurewireUsedAmount": jnxLsysSpSecurewireUsedAmount,
       "jnxLsysSpSecurewireMaxQuota": jnxLsysSpSecurewireMaxQuota,
       "jnxLsysSpSecurewireAvailableAmount": jnxLsysSpSecurewireAvailableAmount,
       "jnxLsysSpSecurewireHeaviestUsage": jnxLsysSpSecurewireHeaviestUsage,
       "jnxLsysSpSecurewireHeaviestUser": jnxLsysSpSecurewireHeaviestUser,
       "jnxLsysSpSecurewireLightestUsage": jnxLsysSpSecurewireLightestUsage,
       "jnxLsysSpSecurewireLightestUser": jnxLsysSpSecurewireLightestUser}
)
