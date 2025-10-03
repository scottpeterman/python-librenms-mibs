# SNMP MIB module (NPT-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ribbon\NPT-ROOT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:18 2025
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

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Eci_ObjectIdentity = ObjectIdentity
eci = _Eci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286)
)
_ENpti_ObjectIdentity = ObjectIdentity
eNpti = _ENpti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5)
)
_ENptiProducts_ObjectIdentity = ObjectIdentity
eNptiProducts = _ENptiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1)
)
_EciNpti_ObjectIdentity = ObjectIdentity
eciNpti = _EciNpti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1)
)
_NptSystem_ObjectIdentity = ObjectIdentity
nptSystem = _NptSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 2)
)
_NptPerformance_ObjectIdentity = ObjectIdentity
nptPerformance = _NptPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 3)
)
_NptStatistics_ObjectIdentity = ObjectIdentity
nptStatistics = _NptStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 4)
)
_NptAlarm_ObjectIdentity = ObjectIdentity
nptAlarm = _NptAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 5)
)
_NptTrap_ObjectIdentity = ObjectIdentity
nptTrap = _NptTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 6)
)
_NptBGP_ObjectIdentity = ObjectIdentity
nptBGP = _NptBGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 7)
)
_NptOSPF_ObjectIdentity = ObjectIdentity
nptOSPF = _NptOSPF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 8)
)
_NptOSPFv3_ObjectIdentity = ObjectIdentity
nptOSPFv3 = _NptOSPFv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 9)
)
_NptVRF_ObjectIdentity = ObjectIdentity
nptVRF = _NptVRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 10)
)
_NptRSVP_ObjectIdentity = ObjectIdentity
nptRSVP = _NptRSVP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 11)
)
_NptIP_ObjectIdentity = ObjectIdentity
nptIP = _NptIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 12)
)
_NptMsdp_ObjectIdentity = ObjectIdentity
nptMsdp = _NptMsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1286, 5, 1, 1, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NPT-ROOT-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "eci": eci,
       "eNpti": eNpti,
       "eNptiProducts": eNptiProducts,
       "eciNpti": eciNpti,
       "nptSystem": nptSystem,
       "nptPerformance": nptPerformance,
       "nptStatistics": nptStatistics,
       "nptAlarm": nptAlarm,
       "nptTrap": nptTrap,
       "nptBGP": nptBGP,
       "nptOSPF": nptOSPF,
       "nptOSPFv3": nptOSPFv3,
       "nptVRF": nptVRF,
       "nptRSVP": nptRSVP,
       "nptIP": nptIP,
       "nptMsdp": nptMsdp}
)
