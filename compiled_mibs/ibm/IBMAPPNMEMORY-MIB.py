# SNMP MIB module (IBMAPPNMEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBMAPPNMEMORY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:54 2025
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
 enterprises,
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
    "enterprises",
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_Ibmappn_ObjectIdentity = ObjectIdentity
ibmappn = _Ibmappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13)
)
_IbmappnNode_ObjectIdentity = ObjectIdentity
ibmappnNode = _IbmappnNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1)
)
_IbmappnMemoryUse_ObjectIdentity = ObjectIdentity
ibmappnMemoryUse = _IbmappnMemoryUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7)
)


class _IbmappnMemorySize_Type(Integer32):
    """Custom type ibmappnMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnMemorySize_Type.__name__ = "Integer32"
_IbmappnMemorySize_Object = MibScalar
ibmappnMemorySize = _IbmappnMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 1),
    _IbmappnMemorySize_Type()
)
ibmappnMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemorySize.setStatus("mandatory")


class _IbmappnMemoryUsed_Type(Integer32):
    """Custom type ibmappnMemoryUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnMemoryUsed_Type.__name__ = "Integer32"
_IbmappnMemoryUsed_Object = MibScalar
ibmappnMemoryUsed = _IbmappnMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 2),
    _IbmappnMemoryUsed_Type()
)
ibmappnMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryUsed.setStatus("mandatory")


class _IbmappnMemoryWarnThresh_Type(Integer32):
    """Custom type ibmappnMemoryWarnThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnMemoryWarnThresh_Type.__name__ = "Integer32"
_IbmappnMemoryWarnThresh_Object = MibScalar
ibmappnMemoryWarnThresh = _IbmappnMemoryWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 3),
    _IbmappnMemoryWarnThresh_Type()
)
ibmappnMemoryWarnThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryWarnThresh.setStatus("mandatory")


class _IbmappnMemoryCritThresh_Type(Integer32):
    """Custom type ibmappnMemoryCritThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnMemoryCritThresh_Type.__name__ = "Integer32"
_IbmappnMemoryCritThresh_Object = MibScalar
ibmappnMemoryCritThresh = _IbmappnMemoryCritThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 4),
    _IbmappnMemoryCritThresh_Type()
)
ibmappnMemoryCritThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryCritThresh.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMAPPNMEMORY-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmappn": ibmappn,
       "ibmappnNode": ibmappnNode,
       "ibmappnMemoryUse": ibmappnMemoryUse,
       "ibmappnMemorySize": ibmappnMemorySize,
       "ibmappnMemoryUsed": ibmappnMemoryUsed,
       "ibmappnMemoryWarnThresh": ibmappnMemoryWarnThresh,
       "ibmappnMemoryCritThresh": ibmappnMemoryCritThresh}
)
