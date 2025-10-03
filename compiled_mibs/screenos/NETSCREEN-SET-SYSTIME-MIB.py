# SNMP MIB module (NETSCREEN-SET-SYSTIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-SET-SYSTIME-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:51 2025
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

netscreenSetSystimeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 6)
)
if mibBuilder.loadTexts:
    netscreenSetSystimeMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-12 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetSysTime_ObjectIdentity = ObjectIdentity
nsSetSysTime = _NsSetSysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6)
)
_NsSetSysTimeGmtOffset_Type = Integer32
_NsSetSysTimeGmtOffset_Object = MibScalar
nsSetSysTimeGmtOffset = _NsSetSysTimeGmtOffset_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 1),
    _NsSetSysTimeGmtOffset_Type()
)
nsSetSysTimeGmtOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSysTimeGmtOffset.setStatus("current")


class _NsSetSysTimeDaySaving_Type(Integer32):
    """Custom type nsSetSysTimeDaySaving based on Integer32"""
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


_NsSetSysTimeDaySaving_Type.__name__ = "Integer32"
_NsSetSysTimeDaySaving_Object = MibScalar
nsSetSysTimeDaySaving = _NsSetSysTimeDaySaving_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 2),
    _NsSetSysTimeDaySaving_Type()
)
nsSetSysTimeDaySaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetSysTimeDaySaving.setStatus("current")
_NsSetSysTimeNTP_ObjectIdentity = ObjectIdentity
nsSetSysTimeNTP = _NsSetSysTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 3)
)


class _NsSetNtpEnable_Type(Integer32):
    """Custom type nsSetNtpEnable based on Integer32"""
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


_NsSetNtpEnable_Type.__name__ = "Integer32"
_NsSetNtpEnable_Object = MibScalar
nsSetNtpEnable = _NsSetNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 1),
    _NsSetNtpEnable_Type()
)
nsSetNtpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetNtpEnable.setStatus("current")
_NsSetNtpServer_Type = IpAddress
_NsSetNtpServer_Object = MibScalar
nsSetNtpServer = _NsSetNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 2),
    _NsSetNtpServer_Type()
)
nsSetNtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetNtpServer.setStatus("current")
_NsSetNtpUpdateInterval_Type = Integer32
_NsSetNtpUpdateInterval_Object = MibScalar
nsSetNtpUpdateInterval = _NsSetNtpUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 3),
    _NsSetNtpUpdateInterval_Type()
)
nsSetNtpUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetNtpUpdateInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-SYSTIME-MIB",
    **{"netscreenSetSystimeMibModule": netscreenSetSystimeMibModule,
       "nsSetSysTime": nsSetSysTime,
       "nsSetSysTimeGmtOffset": nsSetSysTimeGmtOffset,
       "nsSetSysTimeDaySaving": nsSetSysTimeDaySaving,
       "nsSetSysTimeNTP": nsSetSysTimeNTP,
       "nsSetNtpEnable": nsSetNtpEnable,
       "nsSetNtpServer": nsSetNtpServer,
       "nsSetNtpUpdateInterval": nsSetNtpUpdateInterval}
)
