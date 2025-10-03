# SNMP MIB module (NETELASTIC-FLEXBNG-SYSINFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netelastic\NETELASTIC-FLEXBNG-SYSINFO
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:46 2025
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

(flexbng,) = mibBuilder.importSymbols(
    "NETELASTIC-FLEXBNG-MIB",
    "flexbng")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sysInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 8)
)
if mibBuilder.loadTexts:
    sysInfoMib.setRevisions(
        ("2016-01-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_SysInfoMibInfo_ObjectIdentity = ObjectIdentity
sysInfoMibInfo = _SysInfoMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 8, 1)
)


class _CpuUsage_Type(Unsigned32):
    """Custom type cpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUsage_Type.__name__ = "Unsigned32"
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 8, 1, 1),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")


class _MemUsage_Type(Unsigned32):
    """Custom type memUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemUsage_Type.__name__ = "Unsigned32"
_MemUsage_Object = MibScalar
memUsage = _MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 8, 1, 2),
    _MemUsage_Type()
)
memUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETELASTIC-FLEXBNG-SYSINFO",
    **{"ConfdString": ConfdString,
       "String": String,
       "sysInfoMib": sysInfoMib,
       "sysInfoMibInfo": sysInfoMibInfo,
       "cpuUsage": cpuUsage,
       "memUsage": memUsage}
)
