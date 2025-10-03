# SNMP MIB module (NETSCREEN-SET-EMAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-SET-EMAIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:45 2025
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

netscreenSetEmailMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 7)
)
if mibBuilder.loadTexts:
    netscreenSetEmailMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetEmail_ObjectIdentity = ObjectIdentity
nsSetEmail = _NsSetEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7)
)


class _NsSetEmailEnable_Type(Integer32):
    """Custom type nsSetEmailEnable based on Integer32"""
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


_NsSetEmailEnable_Type.__name__ = "Integer32"
_NsSetEmailEnable_Object = MibScalar
nsSetEmailEnable = _NsSetEmailEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7, 1),
    _NsSetEmailEnable_Type()
)
nsSetEmailEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetEmailEnable.setStatus("current")


class _NsSetEmailSMTP_Type(DisplayString):
    """Custom type nsSetEmailSMTP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetEmailSMTP_Type.__name__ = "DisplayString"
_NsSetEmailSMTP_Object = MibScalar
nsSetEmailSMTP = _NsSetEmailSMTP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7, 2),
    _NsSetEmailSMTP_Type()
)
nsSetEmailSMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetEmailSMTP.setStatus("current")


class _NsSetEmailLog_Type(Integer32):
    """Custom type nsSetEmailLog based on Integer32"""
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


_NsSetEmailLog_Type.__name__ = "Integer32"
_NsSetEmailLog_Object = MibScalar
nsSetEmailLog = _NsSetEmailLog_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7, 3),
    _NsSetEmailLog_Type()
)
nsSetEmailLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetEmailLog.setStatus("current")


class _NsSetEmailAddr1_Type(DisplayString):
    """Custom type nsSetEmailAddr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsSetEmailAddr1_Type.__name__ = "DisplayString"
_NsSetEmailAddr1_Object = MibScalar
nsSetEmailAddr1 = _NsSetEmailAddr1_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7, 4),
    _NsSetEmailAddr1_Type()
)
nsSetEmailAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetEmailAddr1.setStatus("current")


class _NsSetEmailAddr2_Type(DisplayString):
    """Custom type nsSetEmailAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsSetEmailAddr2_Type.__name__ = "DisplayString"
_NsSetEmailAddr2_Object = MibScalar
nsSetEmailAddr2 = _NsSetEmailAddr2_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 7, 5),
    _NsSetEmailAddr2_Type()
)
nsSetEmailAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetEmailAddr2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-EMAIL-MIB",
    **{"netscreenSetEmailMibModule": netscreenSetEmailMibModule,
       "nsSetEmail": nsSetEmail,
       "nsSetEmailEnable": nsSetEmailEnable,
       "nsSetEmailSMTP": nsSetEmailSMTP,
       "nsSetEmailLog": nsSetEmailLog,
       "nsSetEmailAddr1": nsSetEmailAddr1,
       "nsSetEmailAddr2": nsSetEmailAddr2}
)
