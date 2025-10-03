# SNMP MIB module (NETSCREEN-SET-GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-SET-GEN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:46 2025
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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

netscreenSetGenMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 1)
)
if mibBuilder.loadTexts:
    netscreenSetGenMibModule.setRevisions(
        ("2005-08-12 00:00",
         "2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetGeneral_ObjectIdentity = ObjectIdentity
nsSetGeneral = _NsSetGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1)
)
_NsSetGenSysIp_Type = IpAddress
_NsSetGenSysIp_Object = MibScalar
nsSetGenSysIp = _NsSetGenSysIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 1),
    _NsSetGenSysIp_Type()
)
nsSetGenSysIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenSysIp.setStatus("obsolete")


class _NsSetGenHostName_Type(DisplayString):
    """Custom type nsSetGenHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetGenHostName_Type.__name__ = "DisplayString"
_NsSetGenHostName_Object = MibScalar
nsSetGenHostName = _NsSetGenHostName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 2),
    _NsSetGenHostName_Type()
)
nsSetGenHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenHostName.setStatus("current")


class _NsSetGenDomain_Type(DisplayString):
    """Custom type nsSetGenDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetGenDomain_Type.__name__ = "DisplayString"
_NsSetGenDomain_Object = MibScalar
nsSetGenDomain = _NsSetGenDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 3),
    _NsSetGenDomain_Type()
)
nsSetGenDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenDomain.setStatus("current")


class _NsSetGenOpMode_Type(DisplayString):
    """Custom type nsSetGenOpMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetGenOpMode_Type.__name__ = "DisplayString"
_NsSetGenOpMode_Object = MibScalar
nsSetGenOpMode = _NsSetGenOpMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 4),
    _NsSetGenOpMode_Type()
)
nsSetGenOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenOpMode.setStatus("current")


class _NsSetGenSwVer_Type(DisplayString):
    """Custom type nsSetGenSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NsSetGenSwVer_Type.__name__ = "DisplayString"
_NsSetGenSwVer_Object = MibScalar
nsSetGenSwVer = _NsSetGenSwVer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 5),
    _NsSetGenSwVer_Type()
)
nsSetGenSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenSwVer.setStatus("current")


class _NsSetGenLicInfo_Type(DisplayString):
    """Custom type nsSetGenLicInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsSetGenLicInfo_Type.__name__ = "DisplayString"
_NsSetGenLicInfo_Object = MibScalar
nsSetGenLicInfo = _NsSetGenLicInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 6),
    _NsSetGenLicInfo_Type()
)
nsSetGenLicInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenLicInfo.setStatus("current")


class _NsSetGenSCSAdminEnable_Type(Integer32):
    """Custom type nsSetGenSCSAdminEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGenSCSAdminEnable_Type.__name__ = "Integer32"
_NsSetGenSCSAdminEnable_Object = MibScalar
nsSetGenSCSAdminEnable = _NsSetGenSCSAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 7),
    _NsSetGenSCSAdminEnable_Type()
)
nsSetGenSCSAdminEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenSCSAdminEnable.setStatus("current")


class _NsSetGenDropSelfLogPac_Type(Integer32):
    """Custom type nsSetGenDropSelfLogPac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGenDropSelfLogPac_Type.__name__ = "Integer32"
_NsSetGenDropSelfLogPac_Object = MibScalar
nsSetGenDropSelfLogPac = _NsSetGenDropSelfLogPac_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 1, 8),
    _NsSetGenDropSelfLogPac_Type()
)
nsSetGenDropSelfLogPac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGenDropSelfLogPac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-GEN-MIB",
    **{"netscreenSetGenMibModule": netscreenSetGenMibModule,
       "nsSetGeneral": nsSetGeneral,
       "nsSetGenSysIp": nsSetGenSysIp,
       "nsSetGenHostName": nsSetGenHostName,
       "nsSetGenDomain": nsSetGenDomain,
       "nsSetGenOpMode": nsSetGenOpMode,
       "nsSetGenSwVer": nsSetGenSwVer,
       "nsSetGenLicInfo": nsSetGenLicInfo,
       "nsSetGenSCSAdminEnable": nsSetGenSCSAdminEnable,
       "nsSetGenDropSelfLogPac": nsSetGenDropSelfLogPac}
)
