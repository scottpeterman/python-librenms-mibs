# SNMP MIB module (WATCHGUARD-INFO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\watchguard\WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:50 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
if mibBuilder.loadTexts:
    wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgInfoSystem_ObjectIdentity = ObjectIdentity
wgInfoSystem = _WgInfoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1)
)
if mibBuilder.loadTexts:
    wgInfoSystem.setStatus("current")
_WgInfoSystemCurrentTime_Type = DateAndTime
_WgInfoSystemCurrentTime_Object = MibScalar
wgInfoSystemCurrentTime = _WgInfoSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 1),
    _WgInfoSystemCurrentTime_Type()
)
wgInfoSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoSystemCurrentTime.setStatus("current")


class _WgInfoGavService_Type(OctetString):
    """Custom type wgInfoGavService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgInfoGavService_Type.__name__ = "OctetString"
_WgInfoGavService_Object = MibScalar
wgInfoGavService = _WgInfoGavService_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 3),
    _WgInfoGavService_Type()
)
wgInfoGavService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoGavService.setStatus("current")


class _WgInfoIpsService_Type(OctetString):
    """Custom type wgInfoIpsService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgInfoIpsService_Type.__name__ = "OctetString"
_WgInfoIpsService_Object = MibScalar
wgInfoIpsService = _WgInfoIpsService_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 4),
    _WgInfoIpsService_Type()
)
wgInfoIpsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgInfoIpsService.setStatus("current")
_WgFeaureKeyExpirationInfo_Type = DateAndTime
_WgFeaureKeyExpirationInfo_Object = MibScalar
wgFeaureKeyExpirationInfo = _WgFeaureKeyExpirationInfo_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 1, 5),
    _WgFeaureKeyExpirationInfo_Type()
)
wgFeaureKeyExpirationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgFeaureKeyExpirationInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-INFO-SYSTEM-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgInfoSystem": wgInfoSystem,
       "wgInfoSystemCurrentTime": wgInfoSystemCurrentTime,
       "wgInfoGavService": wgInfoGavService,
       "wgInfoIpsService": wgInfoIpsService,
       "wgFeaureKeyExpirationInfo": wgFeaureKeyExpirationInfo}
)
